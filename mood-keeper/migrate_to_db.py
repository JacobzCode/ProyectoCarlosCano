"""
Script para migrar datos de CSV a SQLite
Ejecutar una sola vez al actualizar el sistema
"""
import os
import sys

# Agregar el directorio raíz al path
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from app.database import init_db, SessionLocal, Account, Entry
from app.storage import AccountStore, EntryStore


def migrate_csv_to_sqlite():
    """Migra datos existentes de CSV a SQLite"""
    print("🔄 Iniciando migración de CSV a SQLite...")
    
    # Inicializar base de datos
    init_db()
    print("✅ Base de datos SQLite inicializada")
    
    db = SessionLocal()
    
    try:
        # Migrar cuentas
        print("\n📋 Migrando cuentas...")
        csv_accounts = AccountStore()
        account_count = 0
        
        for acc in csv_accounts._iter():
            # Verificar si ya existe
            existing = db.query(Account).filter(Account.handle == acc.handle).first()
            if existing:
                print(f"⏭️  Cuenta '{acc.handle}' ya existe, omitiendo...")
                continue
            
            db_account = Account(
                handle=acc.handle,
                email=acc.email,
                hashed=acc.hashed,
                created=acc.created
            )
            db.add(db_account)
            account_count += 1
            print(f"✅ Migrada cuenta: {acc.handle}")
        
        db.commit()
        print(f"\n✅ {account_count} cuentas migradas exitosamente")
        
        # Migrar entradas
        print("\n📝 Migrando entradas...")
        csv_entries = EntryStore()
        entry_count = 0
        
        for entry in csv_entries.list_all():
            # Verificar si ya existe (por timestamp y handle)
            existing = db.query(Entry).filter(
                Entry.handle == entry.handle,
                Entry.created == entry.created
            ).first()
            
            if existing:
                continue
            
            db_entry = Entry(
                account_id=entry.account_id,
                handle=entry.handle,
                mood=entry.mood,
                comment=entry.comment,
                created=entry.created
            )
            db.add(db_entry)
            entry_count += 1
            
            if entry_count % 10 == 0:
                print(f"⏳ Migradas {entry_count} entradas...")
        
        db.commit()
        print(f"\n✅ {entry_count} entradas migradas exitosamente")
        
        print("\n🎉 Migración completada con éxito!")
        print(f"📊 Total: {account_count} cuentas, {entry_count} entradas")
        
    except Exception as e:
        print(f"\n❌ Error durante la migración: {e}")
        db.rollback()
        raise
    
    finally:
        db.close()


if __name__ == "__main__":
    print("=" * 60)
    print("MIGRACIÓN DE DATOS: CSV → SQLite")
    print("=" * 60)
    
    response = input("\n⚠️  ¿Continuar con la migración? (s/n): ")
    
    if response.lower() in ['s', 'si', 'yes', 'y']:
        migrate_csv_to_sqlite()
    else:
        print("❌ Migración cancelada")
