from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(), Length(min=5)])
	content= TextAreaField('Content', render_kw={"rows": 16, "cols": 8}, validators=[DataRequired()] )

	submit = SubmitField('Post')