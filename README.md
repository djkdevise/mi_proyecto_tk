# Estructura de carpetas para un proyecto básico en Python con Tkinter

mi_proyecto/
├── README.md
├── main.py
├── requirements.txt
├── .gitignore
├── src/
│ ├── init.py
│ ├── gui/
│ │ ├── init.py
│ │ └── main_window.py
│ └── logic/
│ ├── init.py
│ └── calculations.py
└── tests/
├── init.py
└── test_calculations.py


## Descripción de las carpetas y archivos

- **README.md**: Archivo de documentación donde se describe el proyecto, cómo instalarlo, y cómo usarlo.
- **main.py**: Archivo principal donde se inicia la aplicación.
- **requirements.txt**: Archivo que lista las dependencias del proyecto.
- **.gitignore**: Archivo para especificar qué archivos o directorios deben ser ignorados por Git.

### src/
Directorio que contiene todo el código fuente del proyecto.

- **gui/**: Contiene los archivos relacionados con la interfaz gráfica de usuario.
  - **main_window.py**: Archivo que define la ventana principal de la aplicación.

- **logic/**: Contiene la lógica de negocio del proyecto.
  - **calculations.py**: Archivo con funciones y métodos para realizar cálculos o procesos lógicos.

### tests/
Directorio que contiene los archivos de pruebas unitarias.

- **test_calculations.py**: Archivo con pruebas unitarias para las funciones de cálculo.

## Ejemplo de contenido de archivos

### main.py
```python
from src.gui.main_window import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.run()
```

### src/gui/main_window.py
```python
import tkinter as tk

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mi Aplicación Tkinter")

    def run(self):
        self.root.mainloop()
```

### src/logic/calculations.py
```python
def add(a, b):
    return a + b

```

### tests/test_calculations.py
```python
import unittest
from src.logic.calculations import add

class TestCalculations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == "__main__":
    unittest.main()


```

### script .bat que generará la estructura de carpetas y archivos vacíos para el proyecto en Windows:

## Instrucciones para usar el script

1. Abre el Bloc de notas.
2. Copia y pega el contenido siguiente en el Bloc de notas:

    ```bat
    @echo off
    SET PROJECT_DIR=mi_proyecto

    REM Crear las carpetas del proyecto
    mkdir %PROJECT_DIR%
    mkdir %PROJECT_DIR%\src
    mkdir %PROJECT_DIR%\src\gui
    mkdir %PROJECT_DIR%\src\logic
    mkdir %PROJECT_DIR%\tests

    REM Crear los archivos vacíos
    type nul > %PROJECT_DIR%\README.md
    type nul > %PROJECT_DIR%\main.py
    type nul > %PROJECT_DIR%\requirements.txt
    type nul > %PROJECT_DIR%\.gitignore
    type nul > %PROJECT_DIR%\src\__init__.py
    type nul > %PROJECT_DIR%\src\gui\__init__.py
    type nul > %PROJECT_DIR%\src\gui\main_window.py
    type nul > %PROJECT_DIR%\src\logic\__init__.py
    type nul > %PROJECT_DIR%\src\logic\calculations.py
    type nul > %PROJECT_DIR%\tests\__init__.py
    type nul > %PROJECT_DIR%\tests\test_calculations.py

    echo Estructura de proyecto creada con éxito.
    pause
    ```

3. Guarda el archivo con el nombre `crear_proyecto.bat`, asegurándote de seleccionar "Todos los archivos" en el menú desplegable de tipo de archivo.
4. Ejecuta el archivo `.bat` haciendo doble clic sobre él. Esto creará la estructura de carpetas y archivos vacíos en el directorio donde se encuentra el script.

## Instrucciones para ejecutar el proyecto

1. **Usa el Script .bat crear directorios y archivos del proyecto**

    Sigue las indicaciones del apartado Instrucciones para usar el script .bat:

    Luego, navega al directorio del proyecto:

    ```bash
    cd mi_proyecto
    ```

2. **Crea un entorno virtual (opcional pero recomendado)**

    En Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    En macOS/Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instala las dependencias**

    Asegúrate de estar en el directorio del proyecto (`mi_proyecto`) y ejecuta:

    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecuta la aplicación**

    En el mismo directorio del proyecto, ejecuta el siguiente comando:

    ```bash
    python main.py
    ```

    Esto iniciará la aplicación Tkinter.

5. **Estructura del proyecto**

    La estructura del proyecto debería verse de la siguiente manera:

    ```
    mi_proyecto/
    ├── README.md
    ├── main.py
    ├── requirements.txt
    ├── .gitignore
    ├── src/
    │   ├── __init__.py
    │   ├── gui/
    │   │   ├── __init__.py
    │   │   └── main_window.py
    │   └── logic/
    │       ├── __init__.py
    │       └── calculations.py
    └── tests/
        ├── __init__.py
        └── test_calculations.py
    ```

6. **Ejecutar las pruebas**

    Si deseas ejecutar las pruebas unitarias, puedes usar el siguiente comando:

    ```bash
    python -m unittest discover -s tests
    ```

Siguiendo estos pasos, deberías poder configurar, instalar dependencias y ejecutar el proyecto en tu entorno local.


### 
```python


```
### 

