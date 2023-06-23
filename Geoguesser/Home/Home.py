from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__,template_folder="Templates")
from ..Models import User

home_bp = Blueprint('home_bp',__name__,template_folder='templates')

@home_bp.route('/')
@home_bp.route('/home/')
def home():
    return render_template('Home.html', title='Home')
    
@home_bp.route('/users/')
def all_users():
    all = User.query.all()
    return render_template('User.html', title='Users', users=all)









