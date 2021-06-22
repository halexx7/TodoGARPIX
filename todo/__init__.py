from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from .models.task_model import reset_db
from .resources import init_api


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    init_api(app)
    reset_db()
    return app
