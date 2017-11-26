from flask import render_template, request, jsonify
from . import main


# 要注册程序全局的错误处理程序, 必须使用app_errorhandler
@main.app_errorhandler(403)
def forbidden(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'forbidden'})
        response.status_code = 403
        return response
    return render_template('403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    """使用HTTP内容协商处理错误, 只为接受JSON格式而不接受HTML格式
    的客户端生成JSON格式响应"""
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    if request.accept_mimytypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'internal server error'})
        response.status_code = 500
        return response
    return render_template('500.html'), 500
