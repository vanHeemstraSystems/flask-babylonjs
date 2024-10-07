flask-babylonjs

# Flacon BabylonJS

Basé sur « Comment structurer une grande application Flask avec des plans Flask et Flask-SQLAlchemy » sur<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

Basé sur "Flask SQLAlchemy" sur<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

Basé sur le « modèle d'usine » à<https://github.com/vanHeemstraSystems/factory-pattern>

Basé sur les « Diagrammes de relations d'entités basés sur du texte avec Mermaid.js » sur<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

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
4) Courir`pip install -r requirements.txt`5) Définissez l'application Flask dans le répertoire des applications :`(.venv) $ export FLASK_APP=app`6) Définissez l'environnement Flask sur le développement :`(.venv) $ export FLASK_ENV=development`7) Exécutez l'application Flask :`(.venv) $ flask run`8) Ouvrez l'interface Web comme vous y êtes invité
9) Utiliser`CTRL+c`pour quitter le serveur Web.
10) Vous pouvez également exécuter l'interface de ligne de commande flask :`(.venv) $ flask shell`11) Exécutez toutes les commandes du flacon : >>>
12) Utiliser`exit()`pour quitter l'interface de ligne de commande.

## 100 - Présentation

Voir[README.md](./100/README.md)

## 200 - Exigences

Voir[README.md](./200/README.md)

## 300 - Créer notre application

See [README.md](./300/README.md)

## 400 - Conclusion

Voir[README.md](./400/README.md)
