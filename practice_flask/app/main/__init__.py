from flask import Blueprint

# 创建蓝本
main = Blueprint('main', __name__)  # 参数: 蓝本的名字, 蓝本所在的包或者模块

# 导入这两个模块能把路由和错误处理程序与蓝本关联起来
# 在脚本末尾导入是为了避免循环导入,因为在这两个模块中还要导入main
from . import views, errors