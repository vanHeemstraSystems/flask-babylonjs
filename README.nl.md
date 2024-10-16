fles-babylonjs

# Kolf BabylonJS

> Een Python Flask-applicatie met Babylon.js 3D-scènes

Gebaseerd op "Hoe u een grote Flask-toepassing structureert met Flask Blueprints en Flask-SQLAlchemy" op<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

Gebaseerd op "Flask SQLAlchemy" op<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

Gebaseerd op "Fabriekspatroon" op<https://github.com/vanHeemstraSystems/factory-pattern>

Gebaseerd op "Op tekst gebaseerde entiteitsrelatiediagrammen met Mermaid.js" op<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

Based on "TailwindsCSS Getting Started" at <https://tailwindcss.com/docs/installation>

Gebaseerd op "FlowBite" op<https://github.com/themesberg/flowbite>

~Gebaseerd op "Flowbite + Tailwind CSS Crash Course | Leer Flowbite voor React & Next.js (volledige tutorial)" op<https://www.youtube.com/watch?v=FTNBPSPy6P8>~

Gebaseerd op "Tailwind CSS Flask - Flowbite" op<https://flowbite.com/docs/getting-started/flask/>

Gebaseerd op "Tailwind Flask Starter" op<https://github.com/themesberg/tailwind-flask-starter>

Gebaseerd op "DB Browser voor SQLite" op<https://sqlitebrowser.org/>, gebruik<https://dbhub.io/wvanheemstra>

Gebaseerd op "Hoe Flask-SQLAlchemy-migraties uit te voeren met behulp van Flask-Migrate" op<https://www.digitalocean.com/community/tutorials/how-to-perform-flask-sqlalchemy-migrations-using-flask-migrate>

Open deze URL met`https://github.dev/`in plaats van`https://github.com/`om de webgebaseerde IDE van Visual Studio Code te gebruiken.

Voer deze applicatie als volgt uit:

1) Voer in`flask_app`map:`$ cd flask_app`2) Als deze niet bestaat, creëer dan een virtuele omgeving binnen de`flask_app`map:`$ python3 -m venv .venv`(macOS:`$ virtualenv .venv`)

Volg in geval van het volgende het advies:

De virtuele omgeving is niet succesvol gemaakt omdat surepip dat niet is
beschikbaar.

Op Debian/Ubuntu-systemen moet u het bestand python3-venv installeren
pakket met behulp van de volgende opdracht.

    sudo apt-get update
    sudo apt install python3.10-venv

Mogelijk moet u sudo gebruiken met die opdracht.  Na het installeren van het python3-venv
pakket, creëer uw virtuele omgeving opnieuw.

Op macOS zie<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) Start de virtuele omgeving en voer in:`. .venv/bin/activate`(macOS:`source .venv/bin/activate`)
4) Rennen`$ pip install -r requirements.txt`5) Uitvoeren:`$ cd app`Dan`$ npm install`Eindelijk`$ cd ..`6) Stel de Flask-app in op de app-map:`(.venv) $ export FLASK_APP=app`7) Stel de Flask Environment in op True voor ontwikkeling:`(.venv) $ export FLASK_DEBUG=True`8) Stel de SQLAlchemy Database-URI in:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, standaard is`sqlite:///app.db`9) SQLAlchemy-trackwijzigingen instellen:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) Geheime sleutel instellen:`(.venv) $ export SECRET_KEY=********`11) Voer de flask-app uit: ~`(.venv) $ flask run`~`(.venv) $ python3 run.py`12) Open de webinterface zoals gevraagd
13) Gebruik`CTRL+c`om de webserver te verlaten.
14) U kunt ook de flask-opdrachtregelinterface uitvoeren:`(.venv) $ flask shell`15) Voer eventuele flescommando's uit: >>>
16) Gebruik`exit()`om de opdrachtregelinterface te verlaten.

## 100 - Inleiding

Zien[README.md](./100/README.md)

## 200 - Vereisten

Zien[README.md](./200/README.md)

## 300 - Onze applicatie bouwen

Zien[README.md](./300/README.md)

## 400 - Conclusie

Zien[README.md](./400/README.md)
