from flask import Flask

app = Flask(__name__)

from pybo.views import main_views

app.register_blueprint(main_views.bp)

app.debug = True