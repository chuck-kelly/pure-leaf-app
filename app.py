from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Drink more Raspberry Pure Leaf!!! DO IT NOW!!! FINISH IT!!!"
