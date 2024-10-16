قارورة-babylonjs

# قارورة BabylonJS

> تطبيق Python Flask مع مشاهد Babylon.js ثلاثية الأبعاد

استنادًا إلى "كيفية إنشاء تطبيق قارورة كبيرة باستخدام مخططات قارورة وFlask-SQLAlchemy" في<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

استنادا إلى "قارورة SQLAlchemy" في<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

بناءً على "نمط المصنع" في<https://github.com/vanHeemstraSystems/factory-pattern>

استنادًا إلى "الرسوم التخطيطية لعلاقة الكيانات المستندة إلى النص مع Mermaid.js" في<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

استنادًا إلى "بدء تشغيل TailwindsCSS" على الموقع<https://tailwindcss.com/docs/installation>

بناء على "FlowBite" في<https://github.com/themesberg/flowbite>

~استنادًا إلى "الدورة التدريبية المكثفة لـ Flowbite + Tailwind CSS | تعلم Flowbite لـ React وNext.js (البرنامج التعليمي الكامل)" في<https://www.youtube.com/watch?v=FTNBPSPy6P8>~

استنادًا إلى "Tailwind CSS Flask - Flowbite" في<https://flowbite.com/docs/getting-started/flask/>

استنادًا إلى "Tailwind Flask Starter" في<https://github.com/themesberg/tailwind-flask-starter>

استنادًا إلى "متصفح DB لـ SQLite" في<https://sqlitebrowser.org/>، يستخدم<https://dbhub.io/wvanheemstra>

استنادًا إلى "كيفية إجراء عمليات ترحيل Flask-SQLAlchemy باستخدام Flask-Migrate" في<https://www.digitalocean.com/community/tutorials/how-to-perform-flask-sqlalchemy-migrations-using-flask-migrate>

استنادا إلى "pydbhub" في<https://pypi.org/project/pydbhub/>

افتح عنوان URL هذا باستخدام`https://github.dev/`بدلاً من`https://github.com/`لاستخدام IDE المستند إلى الويب لـ Visual Studio Code.

# ملخص تنفيذي

قم بتشغيل هذا التطبيق على النحو التالي:

1) أدخل`flask_app`دليل:`$ cd flask_app`2) في حالة عدم وجودها، قم بإنشاء بيئة افتراضية داخل`flask_app`دليل:`$ python3 -m venv .venv`(ماك:`$ virtualenv .venv`)

وفي حالة ما يلي، اتبع نصيحتها:

لم يتم إنشاء البيئة الظاهرية بنجاح نظرًا لعدم إنشاء متأكد
متاح.

على أنظمة Debian/Ubuntu، تحتاج إلى تثبيت python3-venv
الحزمة باستخدام الأمر التالي.

    sudo apt-get update
    sudo apt install python3.10-venv

قد تحتاج إلى استخدام sudo مع هذا الأمر.  بعد تثبيت python3-venv
الحزمة، أعد إنشاء بيئتك الافتراضية.

على نظام التشغيل MacOS، انظر<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) ابدأ البيئة الافتراضية وأدخل:`. .venv/bin/activate`(ماك:`source .venv/bin/activate`)
4) تشغيل`$ pip install -r requirements.txt`5) تشغيل:`$ cd app`ثم`$ npm install`أخيراً`$ cd ..`6) قم بتعيين تطبيق Flask على دليل التطبيق:`(.venv) $ export FLASK_APP=app`7) اضبط بيئة Flask على True من أجل التطوير:`(.venv) $ export FLASK_DEBUG=True`8) قم بتعيين URI لقاعدة بيانات SQLAlchemy:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`، الافتراضي هو`sqlite:///app.db`9) تعيين تعديلات مسار SQLAlchemy:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) تعيين المفتاح السري:`(.venv) $ export SECRET_KEY=********`11) قم بتشغيل تطبيق القارورة: ~`(.venv) $ flask run`~`(.venv) $ python3 run.py`12) افتح واجهة الويب كما هو مطلوب
13) الاستخدام`CTRL+c` to exit the web server.
14) Alternatively run the flask command line interface: `(.venv) $ flask shell`15) تنفيذ أي أوامر قارورة: >>>
16) الاستخدام`exit()`للخروج من واجهة سطر الأوامر.

بشكل عام، يمكنك اتخاذ الخطوات التالية لإدارة عمليات ترحيل قاعدة البيانات الخاصة بك أثناء تطوير تطبيقات Flask الخاصة بك:

1) تعديل نماذج قاعدة البيانات.

2) إذا لا`migrations`الدليل موجود حتى الآن في`flask_app`الدليل، تشغيل` (.venv) flask_app $ flask db init`.

3) قم بإنشاء برنامج نصي للترحيل باستخدام ملف`flask db migrate -m "some comment"`يأمر. إذا لم تكن هناك أي تغييرات منذ آخر عملية ترحيل، فستتم مطالبتك بذلك`No changes in schema detected.`. ومن ثم، يمكنك تكرار هذا الأمر دون خوف.

4) قم بمراجعة البرنامج النصي للترحيل الذي تم إنشاؤه وقم بتصحيحه إذا لزم الأمر.

5) قم بتطبيق التغييرات على قاعدة البيانات باستخدام الملف`flask db upgrade`يأمر.

6) لاستعادة إصدار سابق من قاعدة البيانات، استخدم الأمر`flask db downgrade`يأمر.

## 100- مقدمة

يرى[README.md](./100/README.md)

## 200 - المتطلبات

يرى[README.md](./200/README.md)

## 300 – بناء تطبيقنا

يرى[README.md](./300/README.md)

## 400 - الخاتمة

يرى[README.md](./400/README.md)
