import os
from functools import wraps

from flask import redirect, session


def valid_credentials(username, password):
    if username == "admin" and password == os.getenv("PASSWORD"):
        session["username"] = username
        session["logged_in"] = True

        return {"success": True}
    else:
        return {"success": False, "error": "Invalid credentials"}


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("logged_in", False):
            return redirect("/login")
        return func(*args, **kwargs)

    return wrapper
