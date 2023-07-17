from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import Listing


def listing_exists(form, field):
    id = field.data
    listing = Listing.query.get(id)
    if not listing:
        raise ValidationError("Listing not found.")


class ReviewForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    listingId = IntegerField("ListingId", validators=[listing_exists])
    text = StringField("Text", validators=[DataRequired()])
    rating = SelectField("Rating", choices=[1, 2, 3, 4, 5], validators=[DataRequired()])


class EditReviewForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    text = StringField("Text", validators=[DataRequired()])
    rating = SelectField("Rating", choices=[1, 2, 3, 4, 5], validators=[DataRequired()])
