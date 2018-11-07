"""
注册蓝图
"""
from main.views import public, user, admin, member, auth

from flask_sse import sse

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(member.bp)
    app.register_blueprint(auth.bp)

    app.register_blueprint(sse, url_prefix='/stream')

    return None