from pybo import app, db, migrate
import config

app.config.from_object(config)

# ORM
db.init_app(app)
migrate.init_app(app, db)


from pybo.views import main_views

app.register_blueprint(main_views.bp)

app.debug = True