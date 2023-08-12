from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import date
from .conversation_members import conversation_member


class Conversation(db.Model):
    __tablename__ = "conversations"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("listings.id")), nullable=False
    )

    messages = db.relationship(
        "Message", back_populates="conversation", cascade="all, delete-orphan"
    )
    listing = db.relationship("Listing", back_populates="conversations")
    members = db.relationship(
        "User", secondary=conversation_member, back_populates="conversations"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "listingId": self.listing_id,
            "members": [member.to_dict() for member in self.members],
            "messages": [message.to_dict() for message in self.messages],
        }
