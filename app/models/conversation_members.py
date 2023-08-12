from .db import db, environment, SCHEMA, add_prefix_for_prod

conversation_member = db.Table(
    "conversation_members",
    db.Column(
        "member_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("users.id")),
        primary_key=True,
    ),
    db.Column(
        "conversation_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("conversations.id")),
        primary_key=True,
    ),
    schema=SCHEMA if (environment == "production") else None,
)
