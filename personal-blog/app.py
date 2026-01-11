import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session
from utils.article_manager import (
    delete_article_by_id,
    get_article_by_id,
    list_all_articles,
    save_article,
)
from utils.auth import auth, valid_credentials

load_dotenv()

PROJECT_ROOT = Path(__file__).parent
ARTICLES_DIR = PROJECT_ROOT / "articles"

ARTICLES_DIR.mkdir(exist_ok=True)


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

if not app.secret_key:
    raise ValueError("SECRET_KEY not found in environment variables!")


@app.route("/")
def index():
    return render_template("home.html", articles=list_all_articles())


@app.route("/article/<id>")
def article(id):
    article = get_article_by_id(id)
    return render_template("article.html", article=article)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        is_valid = valid_credentials(username, password)

        if is_valid["success"]:
            return redirect("/dashboard")
        else:
            flash(f"{is_valid['error']}", "error")

    return render_template("login.html")


@app.route("/dashboard")
@auth
def dashboard():
    return render_template("dashboard.html", articles=list_all_articles())


@app.route("/delete-article/<id>", methods=["GET", "POST"])
@auth
def delete_article(id):
    if request.method == "POST":
        delete_article_by_id(id)
    return redirect("/dashboard")


@app.route("/edit-article/<id>", methods=["GET", "POST"])
@auth
def edit_article(id):
    if request.method == "POST":
        result = save_article(
            request.form["title"], request.form["date"], request.form["content"], id
        )

        if result["success"]:
            return redirect("/dashboard")

    article = get_article_by_id(id)

    return render_template("edit_article.html", article={"id": id, **article})


@app.route("/add-article", methods=["GET", "POST"])
@auth
def add_article():
    if request.method == "POST":
        result = save_article(
            request.form["title"], request.form["date"], request.form["content"]
        )

        if result["success"]:
            return redirect("/dashboard")

    return render_template("add_article.html")


@app.route("/logout")
@auth
def logout():
    session["username"] = None
    session["logged_in"] = False

    return redirect("/")
