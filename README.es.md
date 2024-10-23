matraz-babylonjs

# Matraz BabylonJS

> Una aplicación Python Flask con escenas 3D de Babylon.js

Abra esta URL con`https://github.dev/`en lugar de`https://github.com/`para utilizar el IDE basado en web de Visual Studio Code.

# Resumen ejecutivo

Ejecute esta aplicación de la siguiente manera:

1) entrar`flask_app`directorio:`$ cd flask_app`2) Si no existe, cree un entorno virtual dentro del`flask_app`directorio:`$ python3 -m venv .venv`(macOS:`$ virtualenv .venv`)

En caso de lo siguiente, siga sus consejos:

El entorno virtual no se creó correctamente porque surepip no está
disponible.

On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    sudo apt-get update
    sudo apt install python3.10-venv

Es posible que necesites usar sudo con ese comando.  Después de instalar python3-venv
paquete, recrear su entorno virtual.

En macOS ver<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) Inicie el entorno virtual e ingrese:`. .venv/bin/activate`(macOS:`source .venv/bin/activate`)
4) correr`$ pip install -r requirements.txt`5) Ejecutar:`$ cd app`entonces`$ npm install`finalmente`$ cd ..`6) Configure la aplicación Flask en el directorio de aplicaciones:`(.venv) $ export FLASK_APP=app`7) Establezca el entorno Flask en Verdadero para el desarrollo:`(.venv) $ export FLASK_DEBUG=True`8) Configure el URI de la base de datos SQLAlchemy:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, el valor predeterminado es`sqlite:///app.db`9) Establecer modificaciones de seguimiento de SQLAlchemy:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) Establecer clave secreta:`(.venv) $ export SECRET_KEY=********`11) Ejecute la aplicación del matraz: ~`(.venv) $ flask run`~`(.venv) $ python3 run.py`12) Abra la interfaz web cuando se le solicite
13) Uso`CTRL+c`para salir del servidor web.
14) Alternativamente, ejecute la interfaz de línea de comando del matraz:`(.venv) $ flask shell`15) Ejecute cualquier comando de matraz: >>>
16) Uso`exit()`para salir de la interfaz de línea de comando.

En general, puede seguir los siguientes pasos para administrar las migraciones de su base de datos a medida que desarrolla sus aplicaciones Flask:

1) Modificar los modelos de base de datos.

2) Si no`migrations`directorio todavía existe en el`flask_app`directorio, ejecutar` (.venv) flask_app $ flask db init`.

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
