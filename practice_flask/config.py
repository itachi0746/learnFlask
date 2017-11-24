import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 设置True, 每次请求结束后会提交数据库的变动
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号
    MAIL_PORT = 25
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USE_TLS = True
    # MAIL_USE_SSL = True  # 好像不行
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # 通过在虚拟环境/命令行 set MAIL_USERNAME=xxxx@qq.com
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # 密码要设置成第三方授权码
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'  # 邮件标题前缀
    FLASKY_MAIL_SENDER = os.environ.get('MAIL_USERNAME')
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')  # 管理员的邮件地址
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql+pymysql://root:123456@localhost/data_dev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'mysql://root:123456@localhost/data_test'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://root:123456@localhost/data_prd'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}