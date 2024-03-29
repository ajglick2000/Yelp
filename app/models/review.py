from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import date

class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    listing_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("listings.id")), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(5000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, nullable=False, default=date.today)
    updated_at = db.Column(db.Date, nullable=False, default=date.today)


    user = db.relationship("User", back_populates="user_reviews")
    listing = db.relationship("Listing", back_populates="reviews")

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "listingId":self.listing_id,
            "title": self.title,
            "text": self.text,
            "rating": self.rating,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }
