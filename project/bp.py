# pylint: disable = import-error, missing-module-docstring, invalid-name, no-member
from flask import Blueprint, render_template, jsonify, request
from flask_login import current_user
from .models import Rating, RatingSchema
from . import db

bp = Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)


@bp.route("/reviews")
def reviews():
    """Route for React page"""
    return render_template("index.html")


@bp.route("/load_comments", methods=["POST", "GET"])
def load_comments():
    """Route to send reviews to front-end"""
    username = current_user.username
    comments = Rating.query.filter_by(username=username).all()
    rating_schema = RatingSchema(many=True)
    output = rating_schema.dump(comments)

    return jsonify(output)


@bp.route("/recieve_data", methods=["POST", "GET"])
def recieve_data():
    """Route to recieve data from front-end and save all"""
    results_json = request.json

    username = current_user.username
    Rating.query.filter_by(username=username).delete()

    for item in results_json:
        new_rating = Rating(
            username=username,
            movie_id=item["movie_id"],
            rating=item["rating"],
            comment=item["comment"],
        )
        db.session.add(new_rating)
        db.session.commit()

    return jsonify(results_json)
