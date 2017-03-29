# -*- coding: utf-8 -*
from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

#权限检测


def permission_required(permission):
    def decorator(f):
        @wraps(f)  # 保留原有函数的名称和docstring
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
