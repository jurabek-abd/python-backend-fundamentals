from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("length"))


@app.route("/length")
def length():
    return render_template("length.html")


@app.route("/weight")
def weight():
    return render_template("weight.html")


@app.route("/temperature")
def temperature():
    return render_template("temperature.html")
