import os
from functools import wraps

from flask import redirect, session


def validate_credentials(username, password):
    if not username == "admin":
        return {"success": False, "error": "Invalid username"}

    if not password == os.getenv("PASSWORD"):
        return {"success": False, "error": "Invalid password"}

    return {"success": True}


def create_sessions(username):
    session["username"] = username
    session["logged_in"] = True


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("logged_in", False):
            return redirect("/login")
        return func(*args, **kwargs)

    return wrapper
