from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("cats")
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

from project import models, routes
