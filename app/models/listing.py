from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import date
from .review import Review
from .user_favorites import user_favorite


class Listing(db.Model):
    __tablename__ = "listings"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    category = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    image_url = db.Column(db.String, nullable=True)
    created_at = db.Column(db.Date, nullable=False, default=date.today)
    updated_at = db.Column(db.Date, nullable=False, default=date.today)

    user = db.relationship("User", back_populates="listings")
    reviews = db.relationship(
        "Review", back_populates="listing", cascade="all, delete-orphan"
    )
    favorited_by = db.relationship(
        "User", secondary=user_favorite, back_populates="favorites"
    )
    conversations = db.relationship("Conversation", back_populates="listing", lazy='dynamic')

    @property
    def rating(self):
        aggregate_rating = (
            db.session.query(db.func.avg(Review.rating))
            .filter(Review.listing_id == self.id)
            .scalar()
        )
        print(aggregate_rating)
        return aggregate_rating or 0

    def to_dict(self, is_favorite=False):
        return {
            "id": self.id,
            "userId": self.user_id,
            "title": self.title,
            "location": self.location,
            "category": self.category,
            "description": self.description,
            "imageUrl": self.image_url,
            "rating": self.rating,
            "isFavorite": is_favorite,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }
