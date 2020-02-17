# tst_app/__init__.py

from flask import Flask

# Initialize the tst_app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from tst_app import views

# Load the config file
app.config.from_object("config")
