matraz-babylonjs

# Matraz BabylonJS

> Una aplicación Python Flask con escenas 3D de Babylon.js

Basado en "Cómo estructurar una aplicación Flask grande con Flask Blueprints y Flask-SQLAlchemy" en<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

Basado en "Flask SQLAlchemy" en<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

Basado en el "Patrón de fábrica" ​​en<https://github.com/vanHeemstraSystems/factory-pattern>

Basado en "Diagramas de relación de entidades basados ​​en texto con Mermaid.js" en<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

Basado en "TailwindsCSS Getting Started" en<https://tailwindcss.com/docs/installation>

Basado en "FlowBite" en<https://github.com/themesberg/flowbite>

~ Basado en "Curso intensivo de CSS Flowbite + Tailwind | Aprenda Flowbite para React y Next.js (tutorial completo)" en<https://www.youtube.com/watch?v=FTNBPSPy6P8>~

Basado en "Tailwind CSS Flask - Flowbite" en<https://flowbite.com/docs/getting-started/flask/>

Basado en "Tailwind Flask Starter" en<https://github.com/themesberg/tailwind-flask-starter>

Basado en "DB Browser para SQLite" en<https://sqlitebrowser.org/>, usar<https://dbhub.io/wvanheemstra>

Basado en "Cómo realizar migraciones de Flask-SQLAlchemy usando Flask-Migrate" en<https://www.digitalocean.com/community/tutorials/how-to-perform-flask-sqlalchemy-migrations-using-flask-migrate>

Basado en "pydbhub" en<https://pypi.org/project/pydbhub/>

Abra esta URL con`https://github.dev/`en lugar de`https://github.com/`para utilizar el IDE basado en web de Visual Studio Code.

# Resumen ejecutivo

Ejecute esta aplicación de la siguiente manera:

1) entrar`flask_app`directorio:`$ cd flask_app`2) Si no existe, cree un entorno virtual dentro del`flask_app`directorio:`$ python3 -m venv .venv`(macOS:`$ virtualenv .venv`)

En caso de lo siguiente, siga sus consejos:

El entorno virtual no se creó correctamente porque surepip no está
disponible.

En sistemas Debian/Ubuntu, necesita instalar python3-venv
paquete usando el siguiente comando.

    sudo apt-get update
    sudo apt install python3.10-venv

Es posible que necesites usar sudo con ese comando.  Después de instalar python3-venv
paquete, recrear su entorno virtual.

En macOS ver<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) Inicie el entorno virtual e ingrese:`. .venv/bin/activate`(macOS:`source .venv/bin/activate`)
4) correr`$ pip install -r requirements.txt`
5) Run: `$ cd app`entonces`$ npm install`finalmente`$ cd ..`6) Configure la aplicación Flask en el directorio de aplicaciones:`(.venv) $ export FLASK_APP=app`7) Establezca el entorno Flask en Verdadero para el desarrollo:`(.venv) $ export FLASK_DEBUG=True`8) Configure el URI de la base de datos SQLAlchemy:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, el valor predeterminado es`sqlite:///app.db`9) Establecer modificaciones de seguimiento de SQLAlchemy:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) Establecer clave secreta:`(.venv) $ export SECRET_KEY=********`11) Ejecute la aplicación del matraz: ~`(.venv) $ flask run`~`(.venv) $ python3 run.py`12) Abra la interfaz web cuando se le solicite
13) Uso`CTRL+c`para salir del servidor web.
14) Alternativamente, ejecute la interfaz de línea de comando del matraz:`(.venv) $ flask shell`15) Ejecute cualquier comando de matraz: >>>
16) Uso`exit()`para salir de la interfaz de línea de comando.

En general, puede seguir los siguientes pasos para administrar las migraciones de su base de datos a medida que desarrolla sus aplicaciones Flask:

1) Modificar los modelos de base de datos.

2) If no `migrations`directorio todavía existe en el`flask_app`directorio, ejecutar` (.venv) flask_app $ flask db init`.

3) Generar un script de migración con el`flask db migrate -m "some comment"`dominio. Si no ha habido cambios desde la última migración, se le solicitará`No changes in schema detected.`. De ahí que puedas repetir este comando sin miedo.

4) Revise el script de migración generado y corríjalo si es necesario.

5) Aplicar los cambios a la base de datos con el`flask db upgrade`dominio.

6) Para restaurar una versión anterior de la base de datos, utilice el`flask db downgrade`dominio.

## 100 - Introducción

Ver[README.md](./100/README.md)

## 200 - Requisitos

Ver[README.md](./200/README.md)

## 300 - Construyendo nuestra aplicación

Ver[README.md](./300/README.md)

## 400 - Conclusión

Ver[README.md](./400/README.md)
