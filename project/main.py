# pylint: disable = missing-module-docstring, import-error, invalid-name, no-member
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Rating
from .data import get_data

main = Blueprint("main", __name__)


@main.route("/")
def index():
    """Route for homepage"""
    return render_template("home.html")


@main.route("/rate", methods=["GET"])
@login_required
def rate():
    """Route for rating an app get method"""
    movie_id, title, overview, img_url = get_data()
    username = current_user.username
    ratings = Rating.query.filter_by(movie_id=movie_id).all()
    return render_template(
        "rate.html",
        ratings=ratings,
        name=username,
        movie_id=movie_id,
        title=title,
        overview=overview,
        img_url=img_url,
    )


@main.route("/rate", methods=["POST"])
@login_required
def rate_post():
    """Movie rating route for post method"""
    data = request.form
    username = current_user.username
    movie_id = data["movie_id"]
    rating = data["rating"]
    comment = data["comment"]

    new_rating = Rating(
        username=username, movie_id=movie_id, rating=rating, comment=comment
    )

    db.session.add(new_rating)
    db.session.commit()
    return redirect(url_for("main.rate"))
