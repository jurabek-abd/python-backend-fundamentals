import os
from pathlib import Path
from time import time
from typing import cast
from uuid import uuid4

import frontmatter
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

PROJECT_ROOT = Path(__file__).parent.parent
ARTICLES_DIR = PROJECT_ROOT / "articles"

ARTICLES_DIR.mkdir(exist_ok=True)


class ArticleForm(FlaskForm):
    title = StringField(
        "Article Title",
        validators=[
            DataRequired(),
            Length(min=4, max=200),
        ],
    )
    date = StringField("Article Date", validators=[DataRequired()])
    content = TextAreaField(
        "Article Content",
        validators=[
            DataRequired(),
            Length(min=30, max=50000),
        ],
    )


def delete_article_by_id(article_id):
    article_file = ARTICLES_DIR / f"{article_id}.md"

    if not os.path.exists(article_file):
        return {"success": False, "error": "Article not found - 404"}

    os.remove(article_file)
    return {"success": True}


def list_all_articles():
    articles = []

    files = list(ARTICLES_DIR.iterdir())

    if not files:
        return []

    for file in files:
        if file.suffix == ".md":
            article_id = file.stem
            with open(file, "r", encoding="utf-8") as f:
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


def get_article_by_id(article_id):
    article_file = ARTICLES_DIR / f"{article_id}.md"

    if not os.path.exists(article_file):
        return {"success": False, "error": "404 - Not found"}

    with open(article_file, "r", encoding="utf-8") as f:
        metadata, content = frontmatter.parse(f.read())

    article = {"title": metadata["title"], "date": metadata["date"], "content": content}

    return {"success": True, "article": article}


def save_article(title, date, content, article_id=None):
    if article_id is None:
        article_id = f"{int(time())}_{uuid4().hex}"

    filename = ARTICLES_DIR / f"{article_id}.md"

    metadata = {
        "title": title,
        "date": date,
    }

    post = frontmatter.Post(content)
    post.metadata = cast(dict, metadata)

    with open(filename, "wb") as f:
        frontmatter.dump(post, f)

    return {"success": True}
