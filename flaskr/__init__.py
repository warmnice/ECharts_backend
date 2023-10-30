# 作用：一是包含应用工厂，二是告诉Python flaskr文件夹应当视作为一个包
import os
from flask import Flask
from .models import db
from flask_cors import CORS

# create_app：一个应用工厂函数
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/flaskr.sqlite'
    # 设置应用的缺省配置
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    CORS(app)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # 初始化数据库
    db.init_app(app)
    # 注册路由函数
    from .routes import configure_routes
    configure_routes(app)
    return app