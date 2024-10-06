Flask-babylonjs

# Flask BabylonJS

基于“如何使用 Flask 蓝图和 Flask-SQLAlchemy 构建大型 Flask 应用程序”，位于<https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy>

基于“Flask SQLAlchemy”，位于<https://github.com/vanHeemstraSystems/flask-sqlalchemy/>

基于“工厂模式”<https://github.com/vanHeemstraSystems/factory-pattern>

按如下方式运行该应用程序：

1) Enter `flask_app`目录：`$ cd flask_app`
2) If non-existent, create a virtual environment inside the `flask_app`目录：`$ python3 -m venv .venv`（苹果系统：`$ virtualenv .venv`)

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
4）运行`pip install -r requirements.txt`5）将Flask App设置到app目录：`(.venv) $ export FLASK_APP=app`6）设置Flask环境为开发：`(.venv) $ export FLASK_ENV=development`7）运行烧瓶应用程序：`(.venv) $ flask run`8）根据提示打开Web界面
9) 使用`CTRL+c`退出网络服务器。
10) 或者运行flask命令行界面：`(.venv) $ flask shell`11）执行任何flask命令：>>>
12) 使用`exit()`退出命令行界面。

## 100 - 简介

看[README.md](./100/README.md)

## 200 - 要求

看[README.md](./200/README.md)

## 300 - 构建我们的应用程序

看[README.md](./300/README.md)

## 400 - Conclusion

看[README.md](./400/README.md)
