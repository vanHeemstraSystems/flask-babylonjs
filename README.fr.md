flask-babylonjs

# Flacon BabylonJS

> A Python Flask application with Babylon.js 3D scenes

Basé sur « Comment structurer une grande application Flask avec des plans Flask et Flask-SQLAlchemy » sur<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

Basé sur "Flask SQLAlchemy" sur<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

Basé sur le « modèle d'usine » à<https://github.com/vanHeemstraSystems/factory-pattern>

Basé sur les « Diagrammes de relations d'entités basés sur du texte avec Mermaid.js » sur<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

Basé sur "TailwindsCSS Getting Started" sur<https://tailwindcss.com/docs/installation>

Basé sur "FlowBite" à<https://github.com/themesberg/flowbite>

~ Basé sur "Cours accéléré CSS Flowbite + Tailwind | Apprenez Flowbite pour React et Next.js (tutoriel complet)" sur<https://www.youtube.com/watch?v=FTNBPSPy6P8>~

Basé sur "Tailwind CSS Flask - Flowbite" sur<https://flowbite.com/docs/getting-started/flask/>

Basé sur "Tailwind Flask Starter" sur<https://github.com/themesberg/tailwind-flask-starter>

Basé sur "DB Browser pour SQLite" sur<https://sqlitebrowser.org/>, utiliser<https://dbhub.io/wvanheemstra>

Basé sur « Comment effectuer des migrations Flask-SQLAlchemy à l'aide de Flask-Migrate » sur<https://www.digitalocean.com/community/tutorials/how-to-perform-flask-sqlalchemy-migrations-using-flask-migrate>

Ouvrez cette URL avec`https://github.dev/`au lieu de`https://github.com/`pour utiliser l'EDI Web Visual Studio Code.

Exécutez cette application comme suit :

1) Entrez`flask_app`annuaire:`$ cd flask_app`2) S'il n'existe pas, créez un environnement virtuel à l'intérieur du`flask_app`annuaire:`$ python3 -m venv .venv`(macOS :`$ virtualenv .venv`)

Dans les cas suivants, suivez ses conseils :

L'environnement virtuel n'a pas été créé correctement car Ensurepip n'est pas
disponible.

On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    sudo apt-get update
    sudo apt install python3.10-venv

Vous devrez peut-être utiliser sudo avec cette commande.  Après avoir installé python3-venv
package, recréez votre environnement virtuel.

Sur macOS, voir<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) Démarrez l'environnement virtuel et entrez :`. .venv/bin/activate`(macOS :`source .venv/bin/activate`)
4) Courir`$ pip install -r requirements.txt`5) Exécutez :`$ cd app`alors`$ npm install`enfin`$ cd ..`6) Définissez l'application Flask dans le répertoire des applications :`(.venv) $ export FLASK_APP=app`7) Définissez l'environnement Flask sur True pour le développement :`(.venv) $ export FLASK_DEBUG=True`8) Définissez l'URI de la base de données SQLAlchemy :`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, la valeur par défaut est`sqlite:///app.db`9) Définir les modifications de la piste SQLAlchemy :`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) Définir la clé secrète :`(.venv) $ export SECRET_KEY=********`11) Exécutez l'application Flask :`(.venv) $ flask run`12) Ouvrez l'interface Web comme vous y êtes invité
13) Utiliser`CTRL+c`pour quitter le serveur Web.
14) Vous pouvez également exécuter l'interface de ligne de commande flask :`(.venv) $ flask shell`15) Exécutez toutes les commandes du flacon : >>>
16) Utiliser`exit()`pour quitter l'interface de ligne de commande.

## 100 - Présentation

Voir[README.md](./100/README.md)

## 200 - Exigences

Voir[README.md](./200/README.md)

## 300 - Construire notre application

Voir[README.md](./300/README.md)

## 400 - Conclusion

Voir[README.md](./400/README.md)
