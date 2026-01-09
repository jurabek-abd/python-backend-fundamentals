from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("length"))


@app.route("/length", methods=["GET", "POST"])
def length():
    return render_template("length.html")


@app.route("/weight", methods=["GET", "POST"])
def weight():
    return render_template("weight.html")


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    return render_template("temperature.html")
