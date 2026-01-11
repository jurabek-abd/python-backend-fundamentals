import os

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session
from flask_wtf.csrf import CSRFProtect
from flask_wtf.form import FlaskForm
from utils.article_manager import (
    ArticleForm,
    delete_article_by_id,
    get_article_by_id,
    list_all_articles,
    save_article,
)
from utils.auth import auth, create_sessions, validate_credentials

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

if not app.secret_key:
    raise ValueError("SECRET_KEY not found in environment variables!")

csrf = CSRFProtect(app)


@app.route("/")
def index():
    return render_template("home.html", articles=list_all_articles())


@app.route("/article/<id>")
def article(id):
    result = get_article_by_id(id)
    if not result["success"]:
        flash(result["error"], "error")
        return redirect("/")
    return render_template("article.html", article=result["article"])


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        is_valid = validate_credentials(username, password)

        if not is_valid["success"]:
            flash(str(is_valid["error"]), "error")
        else:
            create_sessions(username)
            return redirect("/dashboard")

    return render_template("login.html", form=FlaskForm())


@app.route("/dashboard")
@auth
def dashboard():
    return render_template("dashboard.html", articles=list_all_articles())


@app.route("/delete-article/<id>", methods=["POST"])
@auth
@csrf.exempt
def delete_article(id):
    result = delete_article_by_id(id)
    if not result["success"]:
        flash(str(result["error"]), "error")
    else:
        flash("Article deleted")
    return redirect("/dashboard")


@app.route("/edit-article/<id>", methods=["GET", "POST"])
@auth
def edit_article(id):
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        result = save_article(form.title.data, form.date.data, form.content.data, id)

        if result["success"]:
            return redirect("/dashboard")

    result = get_article_by_id(id)

    if not result["success"]:
        flash(result["error"], "error")
        return redirect(f"/edit-article/{id}")

    return render_template(
        "edit_article.html", article={"id": id, **result["article"]}, form=form
    )


@app.route("/add-article", methods=["GET", "POST"])
@auth
def add_article():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        result = save_article(form.title.data, form.date.data, form.content.data)

        if result["success"]:
            return redirect("/dashboard")

    return render_template("add_article.html", form=form)


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")
