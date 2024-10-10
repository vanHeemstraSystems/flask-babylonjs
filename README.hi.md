कुप्पी-babylonjs

# फ्लास्क बेबीलोनजेएस

> स्लगलाइन

"फ्लास्क ब्लूप्रिंट और फ्लास्क-SQLAlchemy के साथ एक बड़े फ्लास्क अनुप्रयोग की संरचना कैसे करें" पर आधारित<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

"फ्लास्क SQLAlchemy" पर आधारित<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

"फ़ैक्टरी पैटर्न" पर आधारित<https://github.com/vanHeemstraSystems/factory-pattern>

"Mermaid.js के साथ पाठ-आधारित इकाई संबंध आरेख" पर आधारित<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

"फ्लोबाइट" पर आधारित<https://github.com/themesberg/flowbite>

इस URL को इसके साथ खोलें`https://github.dev/` instead of `https://github.dev/`विज़ुअल स्टूडियो कोड वेब-आधारित आईडीई का उपयोग करने के लिए।

इस एप्लिकेशन को इस प्रकार चलाएँ:

1) दर्ज करें`flask_app`निर्देशिका:`$ cd flask_app`2) यदि अस्तित्व में नहीं है, तो अंदर एक आभासी वातावरण बनाएं`flask_app` directory: `$ python3 -m venv .venv`(मैक ओएस:`$ virtualenv .venv`)

In case of the following, follow its advice:

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
4) भागो`$ pip install -r requirements.txt`5) नीचे की ओर जाएँ`app`निर्देशिका:`$ cd app`और भाग खड़ा हुआ:`$ npm install`6) वापस ऊपर जाएँ`flask_app`निर्देशिका:`$ cd ../`7) फ्लास्क ऐप को ऐप डायरेक्टरी पर सेट करें:`(.venv) $ export FLASK_APP=app`8) विकास के लिए फ्लास्क पर्यावरण को सही पर सेट करें:`(.venv) $ export FLASK_DEBUG=True`9) SQLAlchemy डेटाबेस URI सेट करें:`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`, डिफ़ॉल्ट है`sqlite:///app.db`10) SQLAlchemy ट्रैक संशोधन सेट करें:`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`11) गुप्त कुंजी सेट करें:`(.venv) $ export SECRET_KEY=********`12) फ्लास्क ऐप चलाएँ:`(.venv) $ flask run`13) संकेतानुसार वेब इंटरफ़ेस खोलें
14) प्रयोग करें`CTRL+c`वेब सर्वर से बाहर निकलने के लिए.
15) वैकल्पिक रूप से फ्लास्क कमांड लाइन इंटरफ़ेस चलाएँ:`(.venv) $ flask shell`16) किसी भी फ्लास्क कमांड को निष्पादित करें: >>>
17) प्रयोग करें`exit()`कमांड लाइन इंटरफ़ेस से बाहर निकलने के लिए।

## 100 - परिचय

देखना[README.md](./100/README.md)

## 200 - आवश्यकताएँ

देखना[README.md](./200/README.md)

## 300 - हमारे एप्लिकेशन का निर्माण

देखना[README.md](./300/README.md)

## 400 - निष्कर्ष

देखना[README.md](./400/README.md)
