from flask import Flask

# Import the Config Object
from config import Config

# Import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

# Import the Migrate Object
from flask_migrate import Migrate

app = Flask(__name__)
# Complete the Config cycle for our Flask App
# And give access to our Database(when we have one) along with our SECRET_KEY
app.config.from_object(Config)

# Init our database (db)
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app,db)

from homework_2 import routes,models