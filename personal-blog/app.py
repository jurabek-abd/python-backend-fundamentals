import os
from functools import wraps
from pathlib import Path

# from time import time
# from typing import cast
# from uuid import uuid4
import frontmatter
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session

load_dotenv()

PROJECT_ROOT = Path(__file__).parent
ARTICLES_DIR = PROJECT_ROOT / "articles"

ARTICLES_DIR.mkdir(exist_ok=True)


def list_all_articles():
    articles = []

    files = ARTICLES_DIR.iterdir()

    if not files:
        return []

    for file in files:
        if file.suffix == ".md":
            article_id = file.stem
            with open(file, "r") as f:
                metadata, content = frontmatter.parse(f.read())

                article = {
                    "id": article_id,
                    "content": content,
                    "title": metadata["title"],
                    "date": metadata["date"],
                }

                articles.append(article)

    articles.sort(key=lambda x: x["date"], reverse=True)
    return articles


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

if not app.secret_key:
    raise ValueError("SECRET_KEY not found in environment variables!")


@app.route("/")
def index():
    return render_template("home.html", articles=list_all_articles())


@app.route("/article/<id>")
def article(id):
    article_file = ARTICLES_DIR / f"{id}.md"

    if not os.path.exists(article_file):
        article = {
            "title": "404 Error - Article Not Found",
            "date": "N/A",
            "content": "N/A",
        }
        return render_template("article.html", article=article)

    with open(article_file, "r") as f:
        metadata, content = frontmatter.parse(f.read())

    article = {"title": metadata["title"], "date": metadata["date"], "content": content}

    return render_template("article.html", article=article)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == os.getenv("PASSWORD"):
            session["username"] = username
            session["logged_in"] = True

            return redirect("/dashboard")
        else:
            flash("Invalid credentials", "error")

    return render_template("login.html")


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("logged_in", False):
            return redirect("/login")
        return func(*args, **kwargs)

    return wrapper


@app.route("/dashboard")
@auth
def dashboard():
    return render_template("dashboard.html", articles=list_all_articles())


@app.route("/delete-article/<id>", methods=["GET", "POST"])
@auth
def delete_article(id):
    if request.method == "POST":
        article_file = ARTICLES_DIR / f"{id}.md"

        if os.path.exists(article_file):
            os.remove(article_file)
            return redirect("/dashboard")
    return redirect("/dashboard")
