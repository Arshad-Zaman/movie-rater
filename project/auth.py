# pylint: disable = no-member, import-error, missing-module-docstring, invalid-name, simplifiable-if-expression, bad-continuation
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    """Route for login page"""
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    """Route for login form post method"""
    data = request.form
    username = data["username"]
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(username=username).first()

    # check if the user actually exists
    if not user:
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))

    login_user(user, remember=remember)
    return redirect(url_for("main.rate"))


@auth.route("/signup")
def signup():
    """Route for sign up page"""
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    """Route for sign up form post"""
    data = request.form
    username = data["username"]

    user = User.query.filter_by(username=username).first()
    # if above returns a user, then the username already exists in database

    if (
        user
    ):  # if a user is found, we want to redirect back to signup page so user can try again
        flash("Email address already exists")
        return redirect(url_for("auth.signup"))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(username=data["username"])

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    """Route for logging out"""
    logout_user()
    return redirect(url_for("main.index"))
