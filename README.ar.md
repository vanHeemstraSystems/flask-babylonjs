قارورة-babylonjs

# قارورة BabylonJS

استنادًا إلى "كيفية إنشاء تطبيق قارورة كبيرة باستخدام مخططات قارورة وFlask-SQLAlchemy" في<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

استنادا إلى "Flask SQLAlchemy" في<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

بناءً على "نمط المصنع" في<https://github.com/vanHeemstraSystems/factory-pattern>

Based on "Text-Based Entity Relationship Diagrams with Mermaid.js" at <https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

قم بتشغيل هذا التطبيق على النحو التالي:

1) أدخل`flask_app`دليل:`$ cd flask_app`2) في حالة عدم وجودها، قم بإنشاء بيئة افتراضية داخل`flask_app`دليل:`$ python3 -m venv .venv`(ماك:`$ virtualenv .venv`)

وفي حالة ما يلي، اتبع نصيحتها:

لم يتم إنشاء البيئة الافتراضية بنجاح بسبب عدم إنشاء ميزة التأكد من ذلك
متاح.

على أنظمة Debian/Ubuntu، تحتاج إلى تثبيت python3-venv
الحزمة باستخدام الأمر التالي.

    sudo apt-get update
    sudo apt install python3.10-venv

قد تحتاج إلى استخدام Sudo مع هذا الأمر.  بعد تثبيت python3-venv
الحزمة، أعد إنشاء بيئتك الافتراضية.

على نظام التشغيل MacOS، انظر<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) ابدأ البيئة الافتراضية وأدخل:`. .venv/bin/activate`(ماك:`source .venv/bin/activate`)
4) تشغيل`pip install -r requirements.txt`5) قم بتعيين تطبيق Flask على دليل التطبيق:`(.venv) $ export FLASK_APP=app`6) ضبط بيئة القارورة للتطوير:`(.venv) $ export FLASK_ENV=development`7) قم بتشغيل تطبيق القارورة:`(.venv) $ flask run`8) افتح واجهة الويب كما هو مطلوب
9) الاستخدام`CTRL+c`للخروج من خادم الويب.
10) بدلاً من ذلك، قم بتشغيل واجهة سطر أوامر القارورة:`(.venv) $ flask shell`11) تنفيذ أي أوامر قارورة: >>>
12) الاستخدام`exit()`للخروج من واجهة سطر الأوامر.

## 100- مقدمة

يرى[README.md](./100/README.md)

## 200 - المتطلبات

يرى[README.md](./200/README.md)

## 300 – بناء تطبيقنا

يرى[README.md](./300/README.md)

## 400 - الخاتمة

يرى[README.md](./400/README.md)
