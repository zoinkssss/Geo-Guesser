# Imports

from flask import(
Blueprint,
render_template,
request,
redirect,
flash,
url_for,
current_app as app
)
from .. import db, bcrypt
from .forms import RegistrationForm
from ..Models import User

# define Blueprint
auth_bp = Blueprint(
    'auth_bp',__name__,
    url_prefix='/auth/',
    template_folder='templates'
)
# define routes

# login
@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print(current_user, "is authenticated")
        return redirect(url_for('blueprint.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
print(user)
if user and bcrypt.check_password_hash(user.password, form.password.data ):
    print("logging user in")
    login_user(user)
    print(current_user)
    return redirect(url_for('bluprint.home'))
else:
    flash('Loggin Unsuccessful, Please check username and password', 'danger')
    return render_template('login.html' title='User Login', form=form)
    pass

# logout
@auth_bp.route('/logout/', methods=['GET', 'POST'])
def logout():
    return redirect(url_for('blueprint.login'))
    pass
  

# register
@auth_bp.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashes_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            alias=form.alias.data,
            password=hashes_password
            ) 
        db.session.add(user)
        db.session.commit()
        flash('Account has been created for {user.firstname} {user.lastname}')
        # once login is implemented - add auto login feature
        return redirect(url_for('home_bp_home'))

    return render_template('register.html', title='Register',form=form)

def login():
    if current_use.is_authenticated:
        print(current_user, "is authenticated")
return redirect(url_for('blueprint.home'))
form = LoginForm()
if form.validate_on_submit():
    user = User.qury.filter_by(email=form.email.data).first()
    print(user)
    if user and bcrypt.check_password_hash(user.password, form.password.data):
    print("logging user in")
    login_user(user)
    print(current_user)
    return redirect(url_or('blueprint.home'))
else:
    flash('Login Unsucessful, Please check username and password', 'danger')
    return render_template('login.html', title='Use Login', form=form)    

 