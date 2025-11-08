# 🧪 Tests del Proyecto Mood Keeper

Este directorio contiene tests unitarios para validar las funcionalidades críticas del backend.

## 📋 Tests Disponibles

### test_security.py
Valida funcionalidades de seguridad:
- ✅ Hash de contraseñas (bcrypt)
- ✅ Verificación de contraseñas
- ✅ Generación de tokens JWT
- ✅ Validación de tokens
- ✅ Expiración de tokens

**Tests:** 7

### test_storage_db.py
Valida operaciones de base de datos:
- ✅ Creación de cuentas
- ✅ Búsqueda de cuentas por handle
- ✅ Creación de entries (mood + hábitos)
- ✅ Listado de entries
- ✅ Búsqueda de entries por ID
- ✅ Manejo de registros inexistentes

**Tests:** 8

### test_insights.py
Valida análisis de datos y visualizaciones:
- ✅ Generación de estadísticas descriptivas
- ✅ Cálculo de promedios por usuario
- ✅ Sistema de alertas
- ✅ Generación de gráficos (PNG)
- ✅ Estructura de datos de salida
- ✅ Manejo de datasets vacíos

**Tests:** 10

---

## 🚀 Cómo Ejecutar los Tests

### Ejecutar todos los tests
```bash
cd mood-keeper
pytest tests/ -v
```

### Ejecutar un archivo específico
```bash
pytest tests/test_security.py -v
```

### Ejecutar un test específico
```bash
pytest tests/test_security.py::test_hash_secret -v
```

### Con reporte de cobertura
```bash
pytest tests/ --cov=app --cov-report=html
```

---

## 📊 Salida Esperada

```
tests/test_security.py::test_hash_secret PASSED                 [ 4%]
tests/test_security.py::test_verify_secret PASSED               [ 8%]
tests/test_security.py::test_make_token PASSED                  [12%]
tests/test_security.py::test_read_token PASSED                  [16%]
tests/test_security.py::test_token_expiration PASSED            [20%]
tests/test_storage_db.py::test_create_account PASSED            [24%]
tests/test_storage_db.py::test_find_account_by_handle PASSED    [28%]
tests/test_storage_db.py::test_find_nonexistent_account PASSED  [32%]
tests/test_storage_db.py::test_create_entry PASSED              [36%]
tests/test_storage_db.py::test_create_entry_minimal PASSED      [40%]
tests/test_storage_db.py::test_list_entries PASSED              [44%]
tests/test_storage_db.py::test_get_entry_by_id PASSED           [48%]
tests/test_storage_db.py::test_get_nonexistent_entry PASSED     [52%]
tests/test_insights.py::test_summary_empty PASSED               [56%]
tests/test_insights.py::test_avg_by_empty PASSED                [60%]
tests/test_insights.py::test_alerts_parameters PASSED           [64%]
tests/test_insights.py::test_alerts_with_threshold PASSED       [68%]
tests/test_insights.py::test_plot_png_histogram PASSED          [72%]
tests/test_insights.py::test_plot_png_by_handle PASSED          [76%]
tests/test_insights.py::test_plot_png_timeseries PASSED         [80%]
tests/test_insights.py::test_plot_png_invalid PASSED            [84%]
tests/test_insights.py::test_plot_png_with_types PASSED         [88%]
tests/test_insights.py::test_summary_structure PASSED           [92%]
tests/test_insights.py::test_avg_by_returns_dict PASSED         [96%]
tests/test_insights.py::test_alerts_item_structure PASSED       [100%]

======================== 25 passed in 2.34s ========================
```

---

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError"
```bash
# Asegúrate de que las dependencias estén instaladas
pip install -r requirements.txt
```

### Error: "Database locked"
```bash
# Cierra todas las conexiones activas a la base de datos
# O elimina y recrea la base de datos de test
```

### Tests fallan después de cambios
```bash
# Limpia cache de pytest
pytest --cache-clear tests/ -v
```

---

## 📝 Agregar Nuevos Tests

Para agregar un nuevo test:

1. Crear archivo `test_nombre.py` en este directorio
2. Importar pytest: `import pytest`
3. Definir funciones con prefijo `test_`:
```python
def test_mi_funcionalidad():
    # Arrange
    input_data = "test"
    
    # Act
    result = mi_funcion(input_data)
    
    # Assert
    assert result == "expected"
```

4. Ejecutar: `pytest tests/test_nombre.py -v`

---

## 🎯 Buenas Prácticas

- ✅ Un test por funcionalidad específica
- ✅ Nombres descriptivos: `test_create_account_with_valid_data`
- ✅ Usar fixtures para setup/teardown
- ✅ Independencia entre tests (no depender del orden)
- ✅ Limpiar datos de test después de cada test

---

**Total de tests:** 25  
**Cobertura estimada:** ~70% de funcionalidades críticas
