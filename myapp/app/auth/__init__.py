# -*- coding: utf-8 -*
from flask import Blueprint
#  创建蓝本
auth = Blueprint('auth', __name__)
#  避免循环导入，所以放在最后导入
from . import views
