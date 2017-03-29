# -*- coding: utf-8 -*
from flask import Blueprint
from ..models import Permission

#创建蓝本
main = Blueprint('main', __name__)


@main.app_context_processor  # 把permission类加入模板
def inject_permissions():
    return dict(Permission=Permission)

from . import views, errors  # 避免多次导入
