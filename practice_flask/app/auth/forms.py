from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


# 用户登录表单
class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])  # 几个验证函数
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')  # 表示复选框
    submit = SubmitField('Log in')


# # 用户注册表单
# class RegistrationForm(Form):
#     email = StringField('Email', validators=[DataRequired(), Length(1, 64),
#                                              Email()])
#     # Regexp验证函数,确保username字段只包含字母,数字,下划线和点号.
#     username = StringField('Username', validators=[
#         DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
#                                               'Usernames must have only letters, '
#                                               'numbers, dots or underscores')])
#     # EqualTo验证函数,验证两个密码字段中的值是否一致.第一个参数是另一个字段
#     password = PasswordField('Password', validators=[
#         DataRequired(), EqualTo('password2', message='Passwords must match.')])
#     password2 = PasswordField('Confirm password', validators=[DataRequired()])
#     submit = SubmitField('Register')
#
#     # 以下两个自定义的验证函数,如果在表单类中定义了以 validate_ 开头且后面跟着字段名的
#     # 方法,这个方法和常规的验证函数一起调用,确保填写的值在数据库没出现过
#     def validate_email(self, field):
#         if User.query.filter_by(email=field.data).first():
#             raise ValidationError('Email already registered.')
#
#     def validate_username(self, field):
#         if User.query.filter_by(user=field.data).first():
#             raise ValidationError('Username already in user.')
