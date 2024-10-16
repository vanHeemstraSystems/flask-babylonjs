Flask-babylonjs

# Flask BabylonJS

> 具有 Babylon.js 3D 场景的 Python Flask 应用程序

基于“如何使用 Flask 蓝图和 Flask-SQLAlchemy 构建大型 Flask 应用程序”，位于<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

基于“Flask SQLAlchemy”，位于<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

基于“工厂模式”<https://github.com/vanHeemstraSystems/factory-pattern>

基于“基于文本的实体关系图与 Mermaid.js”，位于<https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/>

基于“TailwindsCSS 入门”，位于<https://tailwindcss.com/docs/installation>

基于“FlowBite”<https://github.com/themesberg/flowbite>

~基于“Flowbite + Tailwind CSS 速成课程 | 学习 Flowbite for React 和 Next.js（完整教程）”，地址：<https://www.youtube.com/watch?v=FTNBPSPy6P8>~

基于“Tailwind CSS Flask - Flowbite”，位于<https://flowbite.com/docs/getting-started/flask/>

基于“Tailwind Flask Starter”，位于<https://github.com/themesberg/tailwind-flask-starter>

基于“DB Browser for SQLite”，位于<https://sqlitebrowser.org/>， 使用<https://dbhub.io/wvanheemstra>

基于“如何使用 Flask-Migrate 执行 Flask-SQLAlchemy 迁移”，位于<https://www.digitalocean.com/community/tutorials/how-to-perform-flask-sqlalchemy-migrations-using-flask-migrate>

打开此网址`https://github.dev/`而不是`https://github.com/`使用基于 Web 的 Visual Studio Code IDE。

# 执行摘要

按如下方式运行该应用程序：

1) 输入`flask_app`目录：`$ cd flask_app`2）如果不存在，则在内部创建一个虚拟环境`flask_app` directory: `$ python3 -m venv .venv`（苹果系统：`$ virtualenv .venv`)

如果出现以下情况，请遵循其建议：

虚拟环境没有创建成功，因为ensurepip没有
可用的。

在 Debian/Ubuntu 系统上，需要安装 python3-venv
使用以下命令进行打包。

    sudo apt-get update
    sudo apt install python3.10-venv

您可能需要将 sudo 与该命令一起使用。  安装 python3-venv 后
包，重新创建您的虚拟环境。

在 macOS 上请参阅<https://sourabhbajaj.com/mac-setup/Python/virtualenv.html>

3）启动虚拟环境，输入：`. .venv/bin/activate`（苹果系统：`source .venv/bin/activate`）
4）运行`$ pip install -r requirements.txt`5）运行：`$ cd app`然后`$ npm install`最后`$ cd ..`6）将Flask App设置到app目录：`(.venv) $ export FLASK_APP=app`7）将Flask环境设置为True进行开发：`(.venv) $ export FLASK_DEBUG=True`8) 设置 SQLAlchemy 数据库 URI：`(.venv) $ export SQLALCHEMY_DATABASE_URI=...`，默认为`sqlite:///app.db`9）设置SQLAlchemy轨道修改：`(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True`10）设置密钥：`(.venv) $ export SECRET_KEY=********`11）运行烧瓶应用程序：〜`(.venv) $ flask run`~`(.venv) $ python3 run.py`12）根据提示打开Web界面
13) 使用`CTRL+c`退出网络服务器。
14) 或者运行flask命令行界面：`(.venv) $ flask shell`15) 执行任何 Flask 命令：>>>
16) 使用`exit()`退出命令行界面。

一般来说，在开发 Flask 应用程序时，您可以采取以下步骤来管理数据库迁移：

1）修改数据库模型。

2）如果没有`migrations`目录还存在于`flask_app`目录，运行` (.venv) flask_app $ flask db init`.

3) 生成迁移脚本`flask db migrate -m "some comment"`命令。如果自上次迁移以来没有发生任何更改，系统将提示您`No changes in schema detected.`。因此，您可以毫无恐惧地重复此命令。

4) 检查生成的迁移脚本并根据需要进行更正。

5) 将更改应用到数据库`flask db upgrade`命令。

6) 要恢复以前的数据库版本，请使用`flask db downgrade`命令。

## 100 - 简介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 构建我们的应用程序

看[README.md](./300/README.md)

## 400 - 结论

看[README.md](./400/README.md)
