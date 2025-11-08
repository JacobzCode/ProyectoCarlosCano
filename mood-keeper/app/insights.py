import os
from datetime import datetime
from typing import Optional, Dict, Any
import math

_HAS_PANDAS = True
try:
    import pandas as pd
except Exception:
    pd = None
    _HAS_PANDAS = False

from io import BytesIO

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ENTRIES_CSV = os.path.join(ROOT, 'data', 'entries.csv')
DB_PATH = os.path.join(ROOT, 'data', 'mood_keeper.db')


def _load_entries():
    """Load entries from SQLite database or fallback to CSV"""
    if not _HAS_PANDAS:
        return None
    
    # Try loading from SQLite first
    if os.path.exists(DB_PATH):
        try:
            import sqlite3
            conn = sqlite3.connect(DB_PATH)
            df = pd.read_sql_query("SELECT * FROM entries", conn)
            conn.close()
            
            if 'created' in df.columns:
                df['created'] = pd.to_datetime(df['created'], errors='coerce')
            if 'mood' in df.columns:
                df['mood'] = pd.to_numeric(df['mood'], errors='coerce')
            
            return df
        except Exception as e:
            print(f"Warning: Could not load from database: {e}")
            # Fall through to CSV
    
    # Fallback to CSV
    if not os.path.exists(ENTRIES_CSV):
        return pd.DataFrame()
    
    df = pd.read_csv(ENTRIES_CSV)
    if 'created' in df.columns:
        df['created'] = pd.to_datetime(df['created'], errors='coerce')
    if 'mood' in df.columns:
        df['mood'] = pd.to_numeric(df['mood'], errors='coerce')
    
    return df


def summary():
    df = _load_entries()
    if df is None:
        return {'error': 'pandas required'}
    if df.empty:
        return {'count':0}
    s = df['mood'].describe().to_dict()
    mood_stats = {}
    for k, v in s.items():
        try:
            fv = float(v)
            # convert non-finite (nan/inf) to None for JSON safety
            mood_stats[k] = fv if math.isfinite(fv) else None
        except Exception:
            mood_stats[k] = None
    return {'count': int(df.shape[0]), 'mood_stats': mood_stats}


def avg_by(handle_col='handle'):
    df = _load_entries()
    if df is None:
        return {'error': 'pandas required'}
    if df.empty or handle_col not in df.columns:
        return {}
    r = df.groupby(handle_col)['mood'].mean().sort_values(ascending=False)
    out = {}
    for k, v in r.items():
        try:
            fv = float(v)
            out[str(k)] = fv if math.isfinite(fv) else None
        except Exception:
            out[str(k)] = None
    return out


def alerts(threshold=3, days=30):
    """Detecta alertas de riesgo considerando mood y hábitos"""
    df = _load_entries()
    if df is None:
        return {'error': 'pandas required'}
    if df.empty:
        return {'count':0,'items':[]}
    cutoff = pd.Timestamp.now() - pd.Timedelta(days=days)
    recent = df[df['created'] >= cutoff]
    
    # Detectar riesgo por múltiples factores
    risk_conditions = (recent['mood'] <= threshold)
    
    # Añadir condiciones de hábitos si existen
    if 'horas_sueno' in recent.columns:
        # Sueño < 6 horas es factor de riesgo
        risk_conditions = risk_conditions | (recent['horas_sueno'] < 6)
    
    if 'actividad_fisica' in recent.columns:
        # Actividad física muy baja (< 3) es factor de riesgo
        risk_conditions = risk_conditions | (recent['actividad_fisica'] < 3)
    
    if 'calidad_alimentacion' in recent.columns:
        # Alimentación muy mala (< 3) es factor de riesgo
        risk_conditions = risk_conditions | (recent['calidad_alimentacion'] < 3)
    
    a = recent[risk_conditions]
    items = []
    for _, row in a.iterrows():
        # include comment/note so frontend can display the full text
        comment = row.get('comment') if 'comment' in row.index else None
        if isinstance(comment, float) and math.isnan(comment):
            comment = None
        
        # Calcular score de riesgo (0-100)
        risk_score = 0
        if row.get('mood', 5) <= threshold:
            risk_score += 40
        if row.get('horas_sueno', 8) < 6:
            risk_score += 20
        if row.get('actividad_fisica', 5) < 3:
            risk_score += 15
        if row.get('calidad_alimentacion', 5) < 3:
            risk_score += 15
        if row.get('nivel_socializacion', 5) < 3:
            risk_score += 10
        
        items.append({
            'id': int(row.get('id',0)),
            'handle': row.get('handle'),
            'mood': float(row.get('mood')),
            'created': pd.Timestamp(row.get('created')).isoformat(),
            'comment': comment or '',
            'risk_score': min(risk_score, 100),
            'factors': {
                'horas_sueno': row.get('horas_sueno'),
                'actividad_fisica': row.get('actividad_fisica'),
                'calidad_alimentacion': row.get('calidad_alimentacion'),
                'nivel_socializacion': row.get('nivel_socializacion')
            }
        })
    
    # Ordenar por risk_score descendente
    items.sort(key=lambda x: x['risk_score'], reverse=True)
    
    return {'count': int(a.shape[0]), 'items': items}


def plot_png(plot_name: str, plot_type: str = None) -> Optional[bytes]:
    """Generate PNG bytes for supported plots: 'hist', 'by_handle', 'ts'"""
    if not _HAS_PANDAS:
        return None
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import seaborn as sns
    except Exception:
        return None

    df = _load_entries()
    if df is None or df.empty:
        return None

    buf = BytesIO()
    try:
        if plot_name == 'hist':
            # distribution of mood values
            vals = df['mood'].dropna()
            if plot_type and plot_type.lower() in ('pie','doughnut'):
                # pie/doughnut by mood value counts
                counts = vals.astype(int).value_counts().sort_index()
                if counts.empty:
                    return None
                labels = [str(i) for i in counts.index]
                sizes = counts.values
                plt.figure(figsize=(6,6))
                if plot_type.lower() == 'doughnut':
                    # draw a doughnut by setting wedgeprops width
                    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops={'width':0.4})
                    plt.title('Mood distribution (doughnut)')
                else:
                    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                    plt.title('Mood distribution (pie)')
                plt.tight_layout()
                plt.savefig(buf, format='png')
                plt.close()
                buf.seek(0)
                return buf.read()
            if plot_type and plot_type.lower() in ('scatter','points'):
                # scatter of mood over time - fallback to index if created missing
                x = None
                if 'created' in df.columns and not df['created'].isna().all():
                    x = df['created']
                else:
                    x = range(len(df))
                plt.figure(figsize=(10,4))
                plt.scatter(x, df['mood'], alpha=0.6)
                plt.title('Mood scatter over time')
                try:
                    plt.xticks(rotation=45)
                except Exception:
                    pass
                plt.tight_layout()
                plt.savefig(buf, format='png')
                plt.close()
                buf.seek(0)
                return buf.read()
            # default: histogram
            plt.figure(figsize=(8,4))
            sns.histplot(vals, bins=10)
            plt.title('Mood distribution')
            plt.tight_layout()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            return buf.read()

        if plot_name == 'by_handle':
            # Show top handles
            top = df['handle'].value_counts().head(10).index.tolist()
            sub = df[df['handle'].isin(top)]
            if plot_type and plot_type.lower() in ('pie','doughnut'):
                counts = df['handle'].value_counts().head(10)
                plt.figure(figsize=(6,6))
                plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
                plt.title('Entries by handle (top 10)')
                plt.tight_layout()
                plt.savefig(buf, format='png')
                plt.close()
                buf.seek(0)
                return buf.read()
            if plot_type and plot_type.lower() in ('scatter','points'):
                plt.figure(figsize=(10,6))
                # stripplot/jitter to represent points per handle
                sns.stripplot(x='mood', y='handle', data=sub, jitter=True)
                plt.title('Mood points by handle (top 10)')
                plt.tight_layout()
                plt.savefig(buf, format='png')
                plt.close()
                buf.seek(0)
                return buf.read()
            # default: boxplot
            plt.figure(figsize=(10,6))
            sns.boxplot(x='handle', y='mood', data=sub)
            plt.xticks(rotation=45)
            plt.title('Mood by handle (top 10)')
            plt.tight_layout()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            return buf.read()

        if plot_name == 'ts':
            if 'created' not in df.columns:
                return None
            ts = df.set_index('created').resample('D')['mood'].mean().dropna()
            ts = ts.last('90D')
            if plot_type and plot_type.lower() in ('scatter','points'):
                plt.figure(figsize=(10,4))
                plt.scatter(ts.index, ts.values, alpha=0.7)
                plt.title('Average mood per day (points)')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig(buf, format='png')
                plt.close()
                buf.seek(0)
                return buf.read()
            # default line
            plt.figure(figsize=(10,4))
            sns.lineplot(x=ts.index, y=ts.values)
            plt.title('Average mood per day')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            return buf.read()
    except Exception:
        return None

    return None
