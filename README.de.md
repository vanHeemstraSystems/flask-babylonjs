Flasche-Babylonjs

# Flasche BabylonJS

> Eine Python-Flask-Anwendung mit Babylon.js 3D-Szenen

Öffnen Sie diese URL mit`https://github.dev/`anstatt`https://github.com/`um die webbasierte Visual Studio Code-IDE zu verwenden.

# Zusammenfassung

Führen Sie diese Anwendung wie folgt aus:

1) Geben Sie ein`flask_app`Verzeichnis:`$ cd flask_app`2) Falls nicht vorhanden, erstellen Sie eine virtuelle Umgebung innerhalb des`flask_app`Verzeichnis:`$ python3 -m venv .venv`(macOS:`$ virtualenv .venv`)

Befolgen Sie im folgenden Fall die Ratschläge:

Die virtuelle Umgebung konnte nicht erfolgreich erstellt werden, da dies bei „surepip“ nicht der Fall ist
verfügbar.

Auf Debian/Ubuntu-Systemen müssen Sie python3-venv installieren
Paket mit dem folgenden Befehl.

    sudo apt-get update
    sudo apt install python3.10-venv

Möglicherweise müssen Sie sudo mit diesem Befehl verwenden.  Nach der Installation von python3-venv
Paket, erstellen Sie Ihre virtuelle Umgebung neu.

Auf macOS siehe<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) Starten Sie die virtuelle Umgebung und geben Sie Folgendes ein:`. .venv/bin/activate`(macOS:`source .venv/bin/activate`)
4) Laufen`$ pip install -r requirements.txt`5) Ausführen:`$ cd app`Dann`$ npm install`Endlich`$ cd ..`6) Stellen Sie die Flask-App auf das App-Verzeichnis ein:`(.venv) $ export FLASK_APP=app`7) Setzen Sie die Flask-Umgebung für die Entwicklung auf True:`(.venv) $ export FLASK_DEBUG=True`8) Legen Sie den SQLAlchemy-Datenbank-URI fest:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, Standard ist`sqlite:///app.db`9) Legen Sie die SQLAlchemy-Track-Änderungen fest:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) Geheimen Schlüssel festlegen:`(.venv) $ export SECRET_KEY=********`11) Führen Sie die Flask-App aus: ~`(.venv) $ flask run`~`(.venv) $ python3 run.py`12) Öffnen Sie nach Aufforderung die Weboberfläche
13) Verwendung`CTRL+c`um den Webserver zu verlassen.
14) Alternativ führen Sie die Befehlszeilenschnittstelle von flask aus:`(.venv) $ flask shell`15) Führen Sie alle Flaschenbefehle aus: >>>
16) Verwendung`exit()`um die Befehlszeilenschnittstelle zu verlassen.

Im Allgemeinen können Sie die folgenden Schritte ausführen, um Ihre Datenbankmigrationen zu verwalten, während Sie Ihre Flask-Anwendungen entwickeln:

1) Ändern Sie die Datenbankmodelle.

2) Wenn nein`migrations`Verzeichnis existiert noch in der`flask_app`Verzeichnis, ausführen` (.venv) flask_app $ flask db init`.

3) Generieren Sie ein Migrationsskript mit`flask db migrate -m "some comment"`Befehl. Wenn seit der letzten Migration keine Änderungen vorgenommen wurden, werden Sie dazu aufgefordert`No changes in schema detected.`. Daher können Sie diesen Befehl ohne Angst wiederholen.

4) Überprüfen Sie das generierte Migrationsskript und korrigieren Sie es gegebenenfalls.

5) Übernehmen Sie die Änderungen mit dem auf die Datenbank`flask db upgrade`Befehl.

6) Um eine frühere Datenbankversion wiederherzustellen, verwenden Sie die`flask db downgrade`Befehl.

## 100 - Einführung

Sehen[README.md](./100/README.md)

## 200 – Anforderungen

Sehen[README.md](./200/README.md)

## 300 – Erstellen unserer Anwendung

Sehen[README.md](./300/README.md)

## 400 – Fazit

Sehen[README.md](./400/README.md)
