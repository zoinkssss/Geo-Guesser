from . import db, login_manager
from flask import current_app as app
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
   return User.get(user_id)

class User(db.Model, UserMixin):
   __tablename__ = 'user'
   id = db.Column(db.Integer, primary_key=True)
   firstname = db.Column(db.String(50), nullable=False)
   lastname = db.Column(db.String(50), nullable=False)
   alias = db.Column(db.String(50), nullable=False, unique=True)
   email = db.Column(db.String(128), nullable=False, unique=True)
   password = db.Column(db.String(60), nullable=False)
   avatar = db.Column(db.String(40), nullable=False, default='default.png')
   account_created = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
   active = db.Column(db.Boolean, default=True, nullable=False)



class ScoreBoard(db.Model):
   __tablename__='scoreboard'
   id = db.Column('id', db.Intger, primary_key=True, unique=True, nullable=False)
   user_id = db.Column('user_id', db.Integer, primary_key=True,unique=True, nullable=False)
   score =db.Column('score', db.Integer, db.ForeignKy('user.id'), nullable=False)
   scored_at = db.Column('scored_at', db.DateTime, default=datetime.utcnow, nullable=False)
   user = db.relationship("User")


class GeoLocation(db.model):
   picture = db.Column('picture', db.Integer, primary_key=True, unique=True, nullable=False)
   id = db.Column('id', db.Integer, primary_key=True, unique=True, nullable=False )
   filename = db.Column('filename', db.integer, primary_key=True, unique=True, nullable=False )
   location = db.Column ('location', db.integer, primary_key=True, unique=True, nullable=False)
   difficulty = db.Column('difficulty')


   <ul class="nav nav-pills flex-column flex-md-row">
 {% if current_user,is_authenticated %}
{% if current_user.has_role('commencement_reviewer') or current_user.has_role('yearbook_reviewer') or current_user.has_role('yearbook_reviewer') or curretn_user.has_role('admin') %}
<li class="nav-item"><a class="nav-item nav-link" href="{{ url_for('search_bp.search') }}"><i class="bi bi-search></i>&nbsp;Search</a></l>
{% endif %}
<li class="nav-item"><a class="nav-item nav-link" href="{{ url_for('profile_bp.profile')}}"><i class+"bi bi-person-circle"></i>&nbsp;{{ current_user.username}}</a></li>
<li class="nav-item"><a class="nav-item nav-link" href="{{ url_for('auth_bp.logout')}}">Logout</a></li>


   