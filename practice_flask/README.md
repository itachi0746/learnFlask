Flasky
======

本项目是由Python实现的[社交博客网站](http://120.79.43.210/)。
后端使用**Python3**编写，基于`Flask`框架，并以`Jinja2`作为模板引擎。使用`MySQL`数据库。前端部分使用的是`bootstrap` CSS框架。  
项目部署在阿里云，服务器操作系统为`Ubuntu 16.04`，使用`Gunicorn`处理动态请求，搭配`gevent`库实现异步响应。前端反向代理服务器使用`Nginx`。监测使用`Supervisor`来守护进程。
