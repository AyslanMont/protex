from flask import Flask, render_template

app = Flask(__name__)

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/dobrado")
def dobrado():
    return render_template("dobrado.html")


@app.route("/dobrado-producao")
def dobrado_producao():
    return render_template("dobrado_producao.html")

@app.route("/estampa")
def estampa():
    return render_template("estampa.html")

@app.route("/estampa-producao")
def estampa_producao():
    return render_template("estampa_producao.html")
