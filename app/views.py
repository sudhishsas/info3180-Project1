"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
from operator import length_hint
import os
from app import app, db
from flask import render_template, request, redirect, url_for,flash,send_from_directory 
from .models import PropertiesProfie
from .form import PropertyForm
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route("/properties/create",methods=["POST", "GET"])
def create():
    myform = PropertyForm()

    if request.method == 'GET':
        return render_template('create.html',form=myform )

    if request.method == 'POST' and myform.validate_on_submit():
        
        photo =  myform.photo.data  
        filename = secure_filename(photo.filename)
        photo.save((os.path.join(app.config['UPLOAD_FOLDER'], filename)))
        
        title = myform.title.data
        num_bed = myform.num_bed.data
        num_bath = myform.num_bath.data
        location  = myform.location.data
        type_ = myform.type.data
        price = myform.price.data
        text_ =  myform.text.data
        
        propinfo = PropertiesProfie(title = title , 
                                    num_bed = num_bed, num_bath = num_bath, 
                                    location = location, type = type_ ,
                                    price = price, text = text_, photo_name = filename) 
        
        db.session.add(propinfo)
        db. session.commit()

        #flash('Successfully added a new property','success')
        return redirect(url_for('home'))

    flash_errors(myform)
    return render_template('create.html', form = myform)

@app.route('/properties')
def showprop():
    
    filename = get_uploaded_images()
    if get_prop_info() != []:
        rootdir = 'uploads/'
        lenght =length_hint(get_prop_info())
        return render_template('properties.html', filenames= filename , prop = get_prop_info() ,rootdiri = rootdir,len = lenght)
    else: 
        flash("database is empty no properties to show", 'danger')
        return redirect('properties.html')
    

###
# The functions below should be applicable to all Flask apps.
###
@app.route('/properties/<int:id>')
def viewprop(id):
    view_prop = PropertiesProfie.query.get_or_404(id)
    return render_template('viewprop.html', view_prop = view_prop,rootdiri = 'uploads/')


@app.route('/properties/create/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), path=filename)


def get_uploaded_images():
    rootdir = os.getcwd()
    file_store=[]
    for subdir, dirs, files in os.walk('app/static/uploads'):
        for file in files:
            file_store.append(os.path.join(rootdir,subdir, file))
    return file_store

def get_prop_info():
    prop_info = PropertiesProfie.query.all()
    return prop_info

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    flash(error)
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
