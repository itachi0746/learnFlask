from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin  # 记录用户的认证状态
from . import login_manager, db
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


# class Permission:
#     FOLLOW = 0x01
#     COMMENT = 0x02
#     WRITE_ARTICLES = 0x04
#     MODERATE_COMMENTS = 0x08
#     ADMINISTER = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # default = db.Column(db.Boolean, default=False, index=True)  # 只有一个角色的default字段要设为True
    # permissions = db.Column(db.Integer)  # 整数,表示位标志
    users = db.relationship('User', backref='role', lazy='dynamic')

    # @staticmethod
    # def insert_roles():  # 在数据库中创建角色
    #     roles = {
    #         'User': (Permission.FOLLOW |
    #                  Permission.COMMENT |
    #                  Permission.WRITE_ARTICLES, True),
    #         'Moderator': (Permission.FOLLOW |
    #                       Permission.COMMENT |
    #                       Permission.WRITE_ARTICLES |
    #                       Permission.MODERATE_COMMENTS, False),
    #         'Administrator': (0xff, False)
    #     }
    #     for r in roles:
    #         role = Role.query.filter_by(name=r).first()
    #         if role is None:
    #             role = Role(name=r)
    #         role.permissions = roles[r][0]
    #         role.default = roles[r][1]
    #         db.session.add(role)
    #     db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # confirmed = db.Column(db.Boolean, default=False)

    @property  # 把方法变为属性来调用
    def password(self):
        raise AttributeError('password is not a readable attribute')  # 不能读取

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)  # 只能设置(只写属性)

    # 将密码和储存在User模型中的密码散列值进行比较,如果返回True,就表明密码正确
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # # 生成令牌,有效时间默认为1小时
    # def generate_confirmation_token(self, expiration=3600):
    #     s = Serializer(current_app.config['SECRET_KEY'], expiration)
    #     return s.dumps({'confirm': self.id})
    #
    # # 检验令牌
    # def confirm(self, token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         data = s.loads(token)
    #     except:
    #         return False
    #     if data.get('confirm') != self.id:  # 检查令牌中的id是否和存储在current_user中的已登录用户匹配
    #         return False
    #     self.confirmed = True
    #     db.session.add(self)
    #     return True

    def __repr__(self):
        return '<User %r>' % self.username


# 回调函数,如果找到用户则返回用户对象,否则None
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
