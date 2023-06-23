
if form.validate_on_submit():
    geo_location_file = None
    if form.picture.data:
        picture_file = save_picture(form.picture.data)
        geo_location_file = picture_file
        location = form.location.data
        geo_location = GeoLocation(filename=geo_location_file, location=location, difficulty=difficulty)
        db.session.add(geo_location)
        db.session.commit()
        flash('Geo Location has been added to the system', 'success')
        return redirect(url_for('bp.home'))
       
    return render_template('upload_geolocation.html', title='Upload GeoLocation', form=form)
    <form method="POST" action=" enctype=multipart/form-data">
{{ form.hidden_tag() }}
from flask import current_app as app
from PIL import Image
import os
import secrets

def save_pictures(form_picture):
   random_hex = secrets.token_hex(8)
   _, f_ent = os.path.splitext(form_picture.filename)
   picture_fn = random_hex + f_ext
   picture_path = os.path.join(app.root_path , 'geolocations', picture_fn)
   
   output_size = (125, 125)
i = Image.open(form_picture)
i.thumbnail(output_size)
i.save(picture_path)

return picture_fn

@bp.route('/geo/all', methods=['GET', 'POST'])
def geolocations_all():
   locations = GeoLocation.query.all()
   locations_file = url_for('bp.geolocations', filename=location.avatar_file)
   return render_template('geolocations.html',title='GeoLocation', locations=locations)







