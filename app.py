import os
from flask import Flask

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
    secret_flavor = app.config.get("SECRET_FLAVOR")
    welcome_mesage = "Drink more Raspberry Pure Leaf!!! DO IT NOW!!! FINISH IT!!!"

    return welcome_mesage


