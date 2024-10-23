قارورة-babylonjs

# قارورة BabylonJS

> تطبيق Python Flask مع مشاهد Babylon.js ثلاثية الأبعاد

افتح عنوان URL هذا باستخدام`https://github.dev/`بدلاً من`https://github.com/`لاستخدام IDE المستند إلى الويب لـ Visual Studio Code.

# ملخص تنفيذي

قم بتشغيل هذا التطبيق على النحو التالي:

1) أدخل`flask_app`دليل:`$ cd flask_app`2) في حالة عدم وجودها، قم بإنشاء بيئة افتراضية داخل`flask_app`دليل:`$ python3 -m venv .venv`(ماك:`$ virtualenv .venv`)

وفي حالة ما يلي، اتبع نصيحتها:

لم يتم إنشاء البيئة الافتراضية بنجاح بسبب عدم إنشاء متأكد
متاح.

على أنظمة Debian/Ubuntu، تحتاج إلى تثبيت python3-venv
الحزمة باستخدام الأمر التالي.

    sudo apt-get update
    sudo apt install python3.10-venv

قد تحتاج إلى استخدام Sudo مع هذا الأمر.  بعد تثبيت python3-venv
الحزمة، أعد إنشاء بيئتك الافتراضية.

على نظام التشغيل MacOS، انظر<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) ابدأ البيئة الافتراضية وأدخل:`. .venv/bin/activate`(ماك:`source .venv/bin/activate`)
4) تشغيل`$ pip install -r requirements.txt`5) تشغيل:`$ cd app`ثم`$ npm install`أخيراً`$ cd ..`6) قم بتعيين تطبيق Flask على دليل التطبيق:`(.venv) $ export FLASK_APP=app`7) اضبط بيئة Flask على True من أجل التطوير:`(.venv) $ export FLASK_DEBUG=True`8) قم بتعيين URI لقاعدة بيانات SQLAlchemy:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`، الافتراضي هو`sqlite:///app.db`9) تعيين تعديلات مسار SQLAlchemy:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) تعيين المفتاح السري:`(.venv) $ export SECRET_KEY=********`11) قم بتشغيل تطبيق القارورة: ~`(.venv) $ flask run`~`(.venv) $ python3 run.py`12) افتح واجهة الويب كما هو مطلوب
13) الاستخدام`CTRL+c`للخروج من خادم الويب.
14) بدلاً من ذلك، قم بتشغيل واجهة سطر أوامر القارورة:`(.venv) $ flask shell`15) تنفيذ أي أوامر قارورة: >>>
16) الاستخدام`exit()`للخروج من واجهة سطر الأوامر.

بشكل عام، يمكنك اتخاذ الخطوات التالية لإدارة عمليات ترحيل قاعدة البيانات الخاصة بك أثناء تطوير تطبيقات Flask الخاصة بك:

1) تعديل نماذج قاعدة البيانات.

2) إذا لا`migrations`الدليل موجود حتى الآن في`flask_app`الدليل، تشغيل` (.venv) flask_app $ flask db init`.

3) قم بإنشاء برنامج نصي للترحيل باستخدام ملف`flask db migrate -m "some comment"`يأمر. إذا لم تكن هناك أي تغييرات منذ آخر عملية ترحيل، فستتم مطالبتك بذلك`No changes in schema detected.`. ومن ثم، يمكنك تكرار هذا الأمر دون خوف.

4) قم بمراجعة البرنامج النصي للترحيل الذي تم إنشاؤه وقم بتصحيحه إذا لزم الأمر.

5) تطبيق التغييرات على قاعدة البيانات مع`flask db upgrade`يأمر.

6) لاستعادة إصدار سابق من قاعدة البيانات، استخدم الأمر`flask db downgrade`يأمر.

## 100- مقدمة

يرى[README.md](./100/README.md)

## 200 - المتطلبات

يرى[README.md](./200/README.md)

## 300 – بناء تطبيقنا

يرى[README.md](./300/README.md)

## 400 - الخاتمة

يرى[README.md](./400/README.md)
