from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import(
    DataRequired,
    Email,
    EqualTo,
    Length,
    ValidationError
 )

from ..Models import User

class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname')
    lastname = StringField('Lastname')
    email = StringField('Email')
    alias = StringField('Alias/Username')
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm_password') 
    sumbit = SubmitField('Submit')

    class UploadGeoLocationForm(FlaskForm):
    picture = FileField('Geo Location Picture', validators=[FileAllowed(['jpg', 'png', 'jfif'])])
    difficulty = StringField('Difficulty', valiators=[DataRequired(), Length(min=4, max=20)])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Upload')  
    


   <ul class="nav nav-pills flex-column flex-md-row">
 {% if current_user,is_authenticated %}
{% if current_user.has_role('commencement_reviewer') or current_user.has_role('yearbook_reviewer') or current_user.has_role('yearbook_reviewer') or curretn_user.has_role('admin') %}
<li class="nav-item"><a class="nav-item nav-link" href="{{ url_for('search_bp.search') }}"><i class="bi bi-search></i>&nbsp;Search</a></l>
{% endif %}
<li class="nav-item"><a class="nav-item nav-link" href="{{ url_for('profile_bp.profile')}}"><i class+"bi bi-person-circle"></i>&nbsp;{{ current_user.username}}</a></li>
<li class="nav-item"><a class="nav-item nav-link" href="{{ url_for('auth_bp.logout')}}">Logout</a></li>

10 50