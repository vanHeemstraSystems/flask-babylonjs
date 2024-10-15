कुप्पी-babylonjs

# फ्लास्क बेबीलोनजेएस

> बेबीलोन.जेएस 3डी दृश्यों के साथ एक पायथन फ्लास्क एप्लिकेशन

"फ्लास्क ब्लूप्रिंट और फ्लास्क-SQLAlchemy के साथ एक बड़े फ्लास्क अनुप्रयोग की संरचना कैसे करें" पर आधारित<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

"फ्लास्क SQLAlchemy" पर आधारित<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

"फ़ैक्टरी पैटर्न" पर आधारित<https://github.com/vanHeemstraSystems/factory-pattern>

"Mermaid.js के साथ पाठ-आधारित इकाई संबंध आरेख" पर आधारित<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

"टेलविंड्ससीएसएस गेटिंग स्टार्टेड" पर आधारित<https://tailwindcss.com/docs/installation>

"फ्लोबाइट" पर आधारित<https://github.com/themesberg/flowbite>

~ "फ़्लोबाइट + टेलविंड सीएसएस क्रैश कोर्स | रिएक्ट और नेक्स्ट.जेएस (पूर्ण ट्यूटोरियल) के लिए फ़्लोबाइट सीखें" पर आधारित<https://www.youtube.com/watch?v=FTNBPSPy6P8>~

"टेलविंड सीएसएस फ्लास्क - फ्लोबाइट" पर आधारित<https://flowbite.com/docs/getting-started/flask/>

"टेलविंड फ्लास्क स्टार्टर" पर आधारित<https://github.com/themesberg/tailwind-flask-starter>

"SQLite के लिए DB ब्राउज़र" पर आधारित<https://sqlitebrowser.org/>, उपयोग<https://dbhub.io/wvanheemstra>

"फ्लास्क-माइग्रेट का उपयोग करके फ्लास्क-एसक्यूएलकेमी माइग्रेशन कैसे करें" पर आधारित<https://www.digitalocean.com/community/tutorials/how-to-perform-flask-sqlalchemy-migrations-using-flask-migrate>

इस URL को इसके साथ खोलें`https://github.dev/`के बजाय`https://github.com/`विज़ुअल स्टूडियो कोड वेब-आधारित आईडीई का उपयोग करने के लिए।

इस एप्लिकेशन को इस प्रकार चलाएँ:

1) दर्ज करें`flask_app`निर्देशिका:`$ cd flask_app`2) यदि अस्तित्व में नहीं है, तो अंदर एक आभासी वातावरण बनाएं`flask_app`निर्देशिका:`$ python3 -m venv .venv`(मैक ओएस:`$ virtualenv .venv`)

निम्नलिखित के मामले में, इसकी सलाह का पालन करें:

वर्चुअल वातावरण सफलतापूर्वक नहीं बनाया गया क्योंकि सुनिश्चिप नहीं है
उपलब्ध।

डेबियन/उबंटू सिस्टम पर, आपको Python3-venv इंस्टॉल करना होगा
निम्नलिखित कमांड का उपयोग करके पैकेज।

    sudo apt-get update
    sudo apt install python3.10-venv

आपको उस कमांड के साथ sudo का उपयोग करने की आवश्यकता हो सकती है।  Python3-venv स्थापित करने के बाद
पैकेज, अपने आभासी वातावरण को फिर से बनाएं।

MacOS पर देखें<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3) आभासी वातावरण प्रारंभ करें और दर्ज करें:`. .venv/bin/activate`(मैक ओएस:`source .venv/bin/activate`)
4) भागो`$ pip install -r requirements.txt`5) भागो:`$ cd app`तब`$ npm install`अंत में`$ cd ..`
6) Set the Flask App to app directory: `(.venv) $ export FLASK_APP=app`7) विकास के लिए फ्लास्क पर्यावरण को सही पर सेट करें:`(.venv) $ export FLASK_DEBUG=True`8) SQLAlchemy डेटाबेस URI सेट करें:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, डिफ़ॉल्ट है`sqlite:///app.db`9) SQLAlchemy ट्रैक संशोधन सेट करें:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10) गुप्त कुंजी सेट करें:`(.venv) $ export SECRET_KEY=********`11) फ्लास्क ऐप चलाएँ:`(.venv) $ flask run`12) संकेतानुसार वेब इंटरफ़ेस खोलें
13) प्रयोग करें`CTRL+c`वेब सर्वर से बाहर निकलने के लिए.
14) वैकल्पिक रूप से फ्लास्क कमांड लाइन इंटरफ़ेस चलाएँ:`(.venv) $ flask shell`15) किसी भी फ्लास्क कमांड को निष्पादित करें: >>>
16) प्रयोग करें`exit()`कमांड लाइन इंटरफ़ेस से बाहर निकलने के लिए।

## 100 - परिचय

देखना[README.md](./100/README.md)

## 200 - आवश्यकताएँ

देखना[README.md](./200/README.md)

## 300 - हमारे एप्लिकेशन का निर्माण

देखना[README.md](./300/README.md)

## 400 - निष्कर्ष

देखना[README.md](./400/README.md)
