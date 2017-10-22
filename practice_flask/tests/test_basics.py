import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')  # 使用测试配置
        self.app_context = self.app.app_context()  # 产生一个程序上下文
        self.app_context.push()
        db.create_all()  # 根据类模型创建数据库

    def tearDown(self):
        db.session.remove()
        db.drop_all()  # 删除表
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])