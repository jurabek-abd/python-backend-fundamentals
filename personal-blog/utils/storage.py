import os
from pathlib import Path
from time import time
from typing import cast
from uuid import uuid4

import frontmatter

PROJECT_ROOT = Path(__file__).parent.parent
ARTICLES_DIR = PROJECT_ROOT / "articles"

ARTICLES_DIR.mkdir(exist_ok=True)


def create_article(title, content, date):
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


def read_article(article_id):
    filename = ARTICLES_DIR / f"{article_id}.md"

    if not os.path.exists(filename):
        print("This blog doesn't exist")
        return

    with open(filename, "r") as f:
        metadata, content = frontmatter.parse(f.read())

    return (metadata, content)


def list_articles():
    results = []

    files = ARTICLES_DIR.iterdir()

    for file in files:
        if file.suffix == ".md":
            article_id = file.stem
            with open(file, "r") as f:
                metadata, content = frontmatter.parse(f.read())

                article = {"id": article_id, "content": content, **metadata}

                results.append(article)

    results.sort(key=lambda x: x["date"], reverse=True)
    return results


for article in list_articles():
    print(article)
