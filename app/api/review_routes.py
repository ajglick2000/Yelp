from flask import Blueprint, request
from ..forms import ReviewForm, EditReviewForm
from ..models import db, Review, Listing
from datetime import date
from flask_login import login_required, current_user
from app.api.auth_routes import validation_errors_to_error_messages


review_routes = Blueprint("reviews", __name__)


@review_routes.route("/", methods=["POST"])
@login_required
def create_review():
    form = ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_review = Review(
            user=current_user,
            listing=Listing.query.get(form.data["listingId"]),
            title=form.data["title"],
            text=form.data["text"],
            rating=form.data["rating"],
        )
        db.session.add(new_review)
        db.session.commit()
        return new_review.to_dict
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 401


@review_routes.route("/<int:id>", methods=["PUT"])
def edit_review(id):
    form = EditReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        review = Review.query.get(id)
        review.title = form.data["title"]
        review.text = form.data["text"]
        review.rating = form.data["rating"]

        current_time = date.today()
        review.updated_at = current_time

        db.session.add(review)
        db.session.commit()
        return review.to_dict
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 401


@review_routes.route("/<int:id>", methods=["DELETE"])
def delete_review(id):
    review = Review.query.get(id)
    db.session.delete(review)
    db.session.commit()
    return {}


@review_routes.route("/<int:id>")
def get_review(id):
    review = Review.query.get(id)
    if review:
        return review.to_dict
    else:
        return {"error": ["No Review Found"]}
