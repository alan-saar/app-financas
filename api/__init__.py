from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api

app = Flask(__name__)

app.config.from_object("config")

db = SQLAlchemy(app)

marshmallow = Marshmallow(app)

migration = Migrate(app, db)

api = Api(app)

from .models import conta_model # noqa (db init não funciona com partial import no topo do arquivo)
from .views import conta_view
