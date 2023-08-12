from .db import db, environment, SCHEMA, add_prefix_for_prod

user_favorite = db.Table(
    "user_favorites",
    db.Column(
        "user_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("users.id")),
        primary_key=True,
    ),
    db.Column(
        "listing_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("listings.id")),
        primary_key=True,
    ),
    schema=SCHEMA if (environment == "production") else None,
)
