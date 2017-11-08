# 导入了大多数Flask扩展
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

# 由于还未初始化所需的程序实例, 所以没有初始化扩展,
# 创建扩展类时没有向构造函数传入参数.
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)  # 初始化程序实例
    app.config.from_object(config[config_name])  # 配置类在config.py中定义,其中保存的配置可以使用\
    # Flask app.config 配置对象提供的from_object()方法直接导入程序
    config[config_name].init_app(app)  # 子类调用基类的方法

    # 初始化扩展
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # 导入并注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 导入并注册auth蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')  # 参数增加了路由前缀

    return app
