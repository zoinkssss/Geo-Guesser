from Geoguesser import create_app, db, bcrypt

from Geoguesser.Models import User

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

# user = User(
#     firsname='',
#     lastname='',
#     alias='',
#     email='',
#     password='',
# )

# db.session.add(user)
# db.session.commit()