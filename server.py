#!/usr/bin/python3
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort
from werkzeug import secure_filename
from flask import Markup

# Initialize the Flask application
app = Flask(__name__)

# Config file
from conf import config

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'f/'

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['ass', 'odt', 'docx', 'doc', 'css', 'zip', 'ogg', 'mp3', 'wmv', 'mp4', 'txt', 'webm', 'gif', 'jpeg', 'jpg', 'png'])

# This is to set the File size limit (In MB, change the 40)
app.config['MAX_CONTENT_LENGTH'] = 40 * 1024 * 1024

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# STATIC AND TEMPLATES
@app.route('/')
def home():
  return render_template('upload.html', page=config["SITE_DATA"])

@app.route('/terms')
def terms():
  return render_template('terms.html', page=config["SITE_DATA"])

@app.route('/faq')
def faq():
  return render_template('faq.html', page=config["SITE_DATA"])

@app.route('/apple-touch-icon.png')
def appleTouch():
  return send_from_directory('static', 'logo/152px.png')

# Route that will process the file upload
@app.route('/file', methods=['POST'])
def file():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file',
                                filename=filename))

# Returns the filename to the user
@app.route('/f/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

# Error handling
def error_page(error, code):
  return render_template('error.html', page=config["SITE_DATA"], error=error, code=code)

@app.errorhandler(404)
def page_not_found(e):
    return error_page(error="404 dude. Check the URL.", code=404), 404

@app.errorhandler(500)
def internal_error(e):
    return error_page(error="Even I don't know what happened", code=500), 500

@app.errorhandler(403)
def no_permission(e):
    return error_page(error="No no", code=403), 403

@app.errorhandler(413)
def too_big(e):
    return error_page(error="Did you even check the Terms dude?", code=413), 413

# Start app
if __name__ == '__main__':
  app.run(
    port=config["PORT"],
    host=config["HOST"],
    debug=config["DEBUG"]
  )

