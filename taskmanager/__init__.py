import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
if os.path.exists("env.py"):
    import env


# create instance of imported flask class
app = Flask(__name__)
# app configurations come from env file
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")  # local
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri  # heroku


# create instance of imported SQLAlchemy class
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# imported last because it will rely on app and db variables
from taskmanager import routes  # noqa
