
from flask_wtf.form import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')