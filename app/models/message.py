from .db import db, environment, SCHEMA, add_prefix_for_prod


class Message(db.Model):
    __tablename__ = "messages"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())

    conversation_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("conversations.id")),
        nullable=False,
    )

    text = db.Column(db.String(5000), nullable=False)

    conversation = db.relationship("Conversation", back_populates="messages")
    user = db.relationship("User", back_populates="messages")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "text": self.text,
            "timestamp": self.timestamp.isoformat(),
        }
