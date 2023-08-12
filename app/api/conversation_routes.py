from flask import Blueprint, request
from ..forms import ReviewForm, EditReviewForm, ConversationForm, MessageForm
from ..models import db, Review, Listing, Conversation, User, Message
from datetime import date
from flask_login import login_required, current_user
from app.api.auth_routes import validation_errors_to_error_messages

conversation_routes = Blueprint("conversations", __name__)


@conversation_routes.route("/<int:id>/<int:userId>")
@login_required
def get_conversation(id, userId):
    listing = Listing.query.get(id)
    if listing.user != current_user:
        return {"error": ["User does not own this listing"]}
    user = User.query.get(userId)

    conversation = listing.conversations.filter(
        Conversation.members.contains(user)
    ).first()

    return {message.id: message.to_dict() for message in conversation.messages}


@conversation_routes.route("/<int:id>/<int:userId>", methods=["POST"])
@login_required
def send_message(id, userId):
    listing = Listing.query.get(id)
    if listing.user != current_user:
        return {"error": ["User does not own this listing"]}
    user = User.query.get(userId)

    conversation = listing.conversations.filter(
        Conversation.members.contains(user)
    ).first()

    if not conversation:
        conversation = Conversation(listing=listing)
        conversation.members.append(current_user)
        conversation.members.append(listing.user)
        db.session.add(conversation)
        db.session.commit()

    form = MessageForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_message = Message(
            user=current_user,
            conversation=conversation,
            text=form.text.data,
        )
        conversation.messages.append(new_message)
        db.session.commit()
        return new_message.to_dict()
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}, 401
