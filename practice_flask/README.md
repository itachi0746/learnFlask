Flasky
======

本项目是由Python实现的社交博客网站。
后端使用Python3编写，基于Flask框架，并以Jinja2作为模板引擎。使用MySQL数据库。
前端部分使用的是bootstrap CSS框架。   项目部署在阿里云，服务器操作系统为Ubuntu 16.04，
使用Gunicorn处理动态请求，搭配gevent库实现异步响应。前端反向代理服务器使用Nginx。
监测使用Supervisor来守护进程。