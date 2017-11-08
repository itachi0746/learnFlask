from flask import render_template, redirect, request, url_for, flash
from . import auth
from .. import db
from flask_login import login_user, current_user, logout_user, login_required
from ..models import User
from .forms import LoginForm
from ..email import send_email


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # 验证表单数据
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):  # 用户存在且密码正确
            login_user(user, form.remember_me.data)  # 在用户会话中把用户标记为已登录
            return redirect(request.args.get('next') or url_for('main.index'))  # 返回原来的网页或者主页
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)  # GET直接返回登录页面


# 登出用户路由
@auth.route('/logout')
@login_required  # 登录需要! 如果未认证的用户访问这个路由,会被拦截
def logout():
    logout_user()  # 删除并重设用户会话
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


# # 注册路由
# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(email=form.email.data,
#                     username=form.username.data,
#                     password=form.password.data)
#         db.session.add(user)
#         db.session.commit()  # 不像之前那样延后提交,因为确认令牌需要用到用户的id
#         token = user.generate_confirmation_token()
#         send_email(user.mail, 'Confirm Your Account',
#                    'auth/email/confirm', user=user, token=token)  # 发送确认邮件
#         flash('A confirmation email has been sent to you by emil.')
#         return redirect(url_for('auth.login'))
#     return render_template('auth/register.html', form=form)


# # 确认用户登录的函数
# @auth.route('/confirm/<token>')
# @login_required  # 登录需要! 如果未认证的用户访问这个路由,会被拦截
# def confirm(token):
#     if current_user.confirmed:  # 检查当前登录用户是否认证过
#         return redirect(url_for('main.index'))
#     if current_user.confirm(token):
#         flash('You have confirmed your account. Thanks!')
#     else:
#         flash('The confirmation link is invalid or has expired.')
#     return redirect(url_for('main.index'))
#
#
# @auth.route('/unconfirmed')
# def unconfirmed():
#     if current_user.is_anonymous() or current_user.confirmed:
#         return redirect(url_for('main.index'))
#     return  render_template('auth/unconfirmed.html')
#
#
# # 重新发送用户确认邮件
# @auth.route('/confirm')
# @login_required
# def resend_confirmation():
#     token = current_user.generate_confirmation_token()
#     send_email(current_user.email, 'Confirm Your Account',
#                'auth/email/confirm', user=current_user, token=token)
#     flash('A new confirmation email has been sent to you by email.')
#     return redirect(url_for('main.index'))
