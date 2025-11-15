#### Requirements

- **Python 3.12.1** (EXACTAMENTE esta versión - el proyecto no funcionará con otras versiones)
- pip (Python package installer)
- virtualenv or venv module

> **⚠️ IMPORTANTE**: Este proyecto requiere Python 3.12.1 exactamente. El proyecto tiene verificaciones automáticas que impedirán la instalación y ejecución de tests con otras versiones de Python.

#### Setup Instructions

1. **Verificar versión de Python:**

```bash
python3 --version
# Debe mostrar: Python 3.12.1
```

2. **Crear y activar un entorno virtual:**

```bash
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. **Instalar dependencias:**

```bash
pip install -r requirements.txt
```

> El archivo `setup.py` verificará automáticamente que estés usando Python 3.12.1. Si usas otra versión, la instalación fallará con un mensaje de error.

4. **Ejecutar la aplicación:**

```bash
python run.py
```

#### Running Tests

El archivo `conftest.py` verifica automáticamente la versión de Python antes de ejecutar los tests.

```bash
# Ejecutar todos los tests
pytest -s tests

# Ejecutar un test específico
pytest -s tests/test_prices_controller.py::test_get_prices
```

Si intentas ejecutar pytest con una versión incorrecta de Python, recibirás un error claro indicando la versión requerida.

#### Archivos de Configuración de Versión

Este proyecto utiliza múltiples métodos para asegurar la versión correcta de Python (similar a `package.json` en Node.js):

- **`pyproject.toml`**: Especifica `requires-python = "==3.12.1"` (estándar moderno de Python)
- **`.python-version`**: Utilizado por pyenv y otras herramientas de gestión de versiones
- **`setup.py`**: Verifica la versión durante la instalación
- **`conftest.py`**: Verifica la versión antes de ejecutar tests con pytest
