flacon-babylonjs

# Flacon BabylonJS

> Une application Python Flask avec des scènes 3D Babylon.js

Ouvrez cette URL avec`https://github.dev/`au lieu de`https://github.com/`pour utiliser l'EDI Web Visual Studio Code.

# Résumé exécutif

Exécutez cette application comme suit :

1) Entrez`flask_app`annuaire:`$ cd flask_app`2) S'il n'existe pas, créez un environnement virtuel à l'intérieur du`flask_app`annuaire:`$ python3 -m venv .venv`(macOS :`$ virtualenv .venv`)

Dans les cas suivants, suivez ses conseils :

L'environnement virtuel n'a pas été créé correctement car Ensurepip n'est pas
disponible.

Sur les systèmes Debian/Ubuntu, vous devez installer le python3-venv
package à l’aide de la commande suivante.

    sudo apt-get update
    sudo apt install python3.10-venv

Vous devrez peut-être utiliser sudo avec cette commande.  Après avoir installé python3-venv
package, recréez votre environnement virtuel.

Sur macOS, voir<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) Démarrez l'environnement virtuel et entrez :`. .venv/bin/activate`(macOS :`source .venv/bin/activate`)
4) Courir`$ pip install -r requirements.txt`5) Exécutez :`$ cd app`alors`$ npm install`enfin`$ cd ..`6) Définissez l'application Flask dans le répertoire des applications :`(.venv) $ export FLASK_APP=app`7) Définissez l'environnement Flask sur True pour le développement :`(.venv) $ export FLASK_DEBUG=True`8) Définissez l'URI de la base de données SQLAlchemy :`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, la valeur par défaut est`sqlite:///app.db`9) Définir les modifications de la piste SQLAlchemy :`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) Définir la clé secrète :`(.venv) $ export SECRET_KEY=********`11) Exécutez l'application Flask : ~`(.venv) $ flask run`~`(.venv) $ python3 run.py`12) Ouvrez l'interface Web comme vous y êtes invité
13) Utiliser`CTRL+c`pour quitter le serveur Web.
14) Vous pouvez également exécuter l'interface de ligne de commande flask :`(.venv) $ flask shell`15) Exécutez toutes les commandes du flacon : >>>
16) Utiliser`exit()`pour quitter l'interface de ligne de commande.

En général, vous pouvez suivre les étapes suivantes pour gérer vos migrations de bases de données lorsque vous développez vos applications Flask :

1) Modifier les modèles de base de données.

2) Si non`migrations`répertoire existe encore dans le`flask_app`répertoire, exécutez` (.venv) flask_app $ flask db init`.

3) Générez un script de migration avec le`flask db migrate -m "some comment"`commande. S'il n'y a eu aucun changement depuis la dernière migration, vous serez invité à`No changes in schema detected.`. Par conséquent, vous pouvez répéter cette commande sans crainte.

4) Vérifiez le script de migration généré et corrigez-le si nécessaire.

5) Appliquez les modifications à la base de données avec le`flask db upgrade`commande.

6) Pour restaurer une version précédente de la base de données, utilisez le`flask db downgrade`commande.

## 100 - Introduction

Voir[README.md](./100/README.md)

## 200 - Exigences

See [README.md](./200/README.md)

## 300 - Construire notre application

Voir[README.md](./300/README.md)

## 400 - Conclusion

Voir[README.md](./400/README.md)
