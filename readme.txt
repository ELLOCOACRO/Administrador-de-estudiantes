Hola :D.

Proyecto final del curso python desde 0: Administrador de estudiantes en consola.

Este proyecto de consola fue construido mayormente con el uso de la libreria rich en su version "15.0.0",
esta libreria nos permite dar estilo a la consola de una forma muy sencilla, manejar espaciados, padding, 
manejar tablas y entre muchas funcionalidades utiles mas.

Bien, el proyecto esta estructurado en 2 modulos principales y un archivo principal. El modulo "DB", el modulo "SRC" y el archivo de conexion "main.py".


main.py:
    Archivo principal del proyecto (se debe ejecutar este para correr el programa), conecta todos los modulos


Modulo DB:

    En el modulo "DB" esta todo lo relacionado con el guardado de datos, todos los datos se guardan en memoria,
    por lo tanto, solo se encuentra un archivo llamado "estudiantes.py" con una lista de estudiantes.

    Si se desea se podria reemplazar esto por una base de datos como sqlite e integrarlo en el programa con algun ORM como sqlAlchemist o incluso
    con algo mas simple como escribir las consultas uno mismo.


Modulo SRC:

    El modulo SRC contiene todos los modulos y todo el codigo fuente del programa, contiene logica de renderizado, modelos de entidades etc...
    El modulo se divide en 2 carpetas principales y un modulo de conexion llamado "console.py"


    console.py:
        Contiene la instancia del objeto console de la libreria rich, se usa en todo el programa para hacer renderizado en la consola para aprovechar sus funcionalidades.


    views:
        en views contenemos dos modulos principales, "menu.py" y "menu_helpers.py"

        menu.py:
            contiene toda la logica del renderizado de todos los menus, incluyendo validaciones etc.

        menu_helpers.py:
            contiene algunas ayudas o utilidades que se usan en la logica del menu


    models:
        models contiene todos los modulos de los modelos de entidades con sus helpers, aunque solo contiene el modelo de estudiantes "estudiante.py" y su helper "models_helpers.py"


        estudiante.py:

            contiene la clase constructora "Estudiante"

        
        models_helpers.py:
            contiene las utilidades del modulo estudiante

Instrucciones de ejecución:

Para ejecutar el proyecto, simplemente sigue estos pasos:

1. Extraer el proyecto (si está comprimido).
2. Crear un entorno virtual: `python -m venv venv`
3. Activar el entorno virtual: `source venv/bin/activate` (en Linux/macOS) o `venv\Scripts\activate` (en Windows).
4. Instalar las dependencias: `pip install -r requirements.txt`
5. Ejecutar el archivo principal: `python main.py`
