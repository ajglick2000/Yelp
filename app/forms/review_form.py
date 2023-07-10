from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired


class NewReview(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    text = StringField("Text", validators=[DataRequired()])
    rating = SelectField('Rating', choices=[1, 2, 3, 4, 5], validators=[DataRequired()])
    submit = SubmitField("Submit")


class EditReview(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    text = StringField("Text", validators=[DataRequired()])
    rating = SelectField('Rating', choices=[1, 2, 3, 4, 5], validators=[DataRequired()])
    submit = SubmitField("Submit")