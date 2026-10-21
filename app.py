from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/dobrado")
def dobrado():
    return render_template("dobrado.html")