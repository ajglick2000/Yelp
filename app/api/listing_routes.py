from flask import Blueprint, request, jsonify
from ..forms import NewListing, EditListing
from ..forms import NewReview
from ..models import db, Listing, Review
from datetime import date
from flask_login import login_required, current_user


listing_routes = Blueprint("listings", __name__)


def validation_errors_to_error_messages(validation_errors):
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages


@listing_routes.route("/", methods=["POST"])
@login_required
def listings():
    form = NewListing()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_listing = Listing(
            user_id=current_user.id,
            title=form.title.data,
            location=form.location.data,
            category=form.category.data,
            description=form.description.data,
            image_url=form.image_url.data,
        )

        db.session.add(new_listing)
        db.session.commit()
        return new_listing.to_dict
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 401


@listing_routes.route("/")
def get_listings():
    all_listings = {}
    listings = Listing.query.all()
    for listing in listings:
        all_listings[listing.id] = listing.to_dict
    return all_listings


@listing_routes.route("/<int:id>", methods=["PUT"])
def edit_listing(id):
    form = EditListing()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        listing = Listing.query.get(id)
        listing.title = form.title.data
        listing.location = form.location.data
        listing.category = form.category.data
        listing.description = form.description.data
        current_time = date.today()
        listing.updated_at = current_time

        db.session.add(listing)
        db.session.commit()
        return listing.to_dict
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 401


@listing_routes.route("/<int:id>", methods=["DELETE"])
def delete_listing(id):
    listing = Listing.query.get(id)
    db.session.delete(listing)
    db.session.commit()
    return {"message": f"deleted listing {id}"}


@listing_routes.route("/<int:id>")
def listing(id):
    listing = Listing.query.get(id)
    if listing:
        return listing.to_dict
    else:
        return {"error": ["No Listing Found"]}


@listing_routes.route("/<int:id>/reviews", methods=["GET"])
def listing_reviews(id):
    listing_reviews = Review.query.filter(Review.listing_id == id).all()
    if listing_reviews:
        all_reviews = {}
        for review in listing_reviews:
            all_reviews[review.id] = review.to_dict
        return all_reviews
    else:
        return {"error": ["No Reviews found for this Listing"]}


@listing_routes.route("/<int:id>/reviews", methods=["POST"])
@login_required
def review(id):
    form = NewReview()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_review = Review(
            user_id=current_user.id,
            listing_id=id,
            title=form.data["title"],
            text=form.data["text"],
            rating=form.data["rating"],
        )

        listing = Listing.query.get(id)
        listing_reviews = Review.query.filter(Review.listing_id == id).all()
        total_ratings = int(form.data["rating"])
        print(total_ratings)
        for listing_review in listing_reviews:
            total_ratings = total_ratings + int(listing_review.rating)
        average_rating = total_ratings / (len(listing_reviews) + 1)
        listing.rating = (round(average_rating)) * 2

        db.session.add(new_review)
        db.session.commit()
        return new_review.to_dict
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 401
