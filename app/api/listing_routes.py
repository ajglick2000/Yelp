from flask import Blueprint, request, jsonify
from ..forms import ListingForm
from ..models import db, Listing, Review
from datetime import date
from flask_login import login_required, current_user
from app.api.auth_routes import validation_errors_to_error_messages


listing_routes = Blueprint("listings", __name__)


@listing_routes.route("/", methods=["POST"])
@login_required
def create_listing():
    form = ListingForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_listing = Listing(
            user=current_user,
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
    form = ListingForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        listing = Listing.query.get(id)
        listing.title = form.title.data
        listing.location = form.location.data
        listing.category = form.category.data
        listing.description = form.description.data
        listing.image_url = form.image_url.data
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
def get_listing(id):
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


@listing_routes.route("/<int:id>/favorite", methods=["POST"])
@login_required
def add_to_favorites(id):
    listing = Listing.query.get(id)
    if not listing:
        return {"error": ["No Listing Found"]}

    if listing in current_user.favorites:
        return {"error": ["Listing already in favorites"]}

    current_user.favorites.append(listing)
    db.session.commit()
    return {"message": f"Listing {listing.id} has been added to your favorites"}


@listing_routes.route("/<int:id>/favorite", methods=["DELETE"])
@login_required
def remove_from_favorites(id):
    listing = Listing.query.get(id)
    if not listing:
        return {"error": ["No Listing Found"]}

    if listing not in current_user.favorites:
        return {"error": ["Listing not in favorites"]}

    current_user.favorites.remove(listing)
    db.session.commit()
    return {"message": f"Listing {listing.id} removed from favorites"}


@listing_routes.route("/favorites")
@login_required
def get_user_favorites():
    return {
        "Favorites": {listing.id: listing.to_dict for listing in current_user.favorites}
    }
