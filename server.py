#!/usr/bin/python3.5
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort
from werkzeug import secure_filename
from flask import Markup
import threading
from flask.ext.cache import Cache

# Initialize the Flask application
app = Flask(__name__)

# Caching
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

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

@app.route('/termsjp')
def termsjp():
  return render_template('termsjp.html', page=config["SITE_DATA"])

@app.route('/faqjp')
def faqjp():
  return render_template('faqjp.html', page=config["SITE_DATA"])

@app.route('/termses')
def termses():
  return render_template('termses.html', page=config["SITE_DATA"])

@app.route('/faqes')
def faqes():
  return render_template('faqes.html', page=config["SITE_DATA"])

@app.route('/termspl')
def termspl():
   return render_template('termspl.html', page=config["SITE_DATA"])

@app.route('/faqpl')
def faqpl():
   return render_template('faqpl.html', page=config["SITE_DATA"])

@app.route('/termssv')
def termssv():
   return render_template('termssv.html', page=config["SITE_DATA"])

@app.route('/faqsv')
def faqsv():
   return render_template('faqsv.html', page=config["SITE_DATA"])

@app.route('/termsde')
def termsde():
   return render_template('termsde.html', page=config["SITE_DATA"])

@app.route('/faqde')
def faqde():
   return render_template('faqde.html', page=config["SITE_DATA"])

@app.route('/termsnl')
def termsnl():
    return render_template('termsnl.html', page=config["SITE_DATA"])

@app.route('/faqnl')
def faqnl():
    return render_template('faqnl.html', page=config["SITE_DATA"])

@app.route('/termsar')
def termsar():
   return render_template('termsar.html', page=config["SITE_DATA"])

@app.route('/faqar')
def faqar():
   return render_template('faqar.html', page=config["SITE_DATA"])

@app.route('/jp')
def jp():
   return render_template('uploadjp.html', page=config["SITE_DATA"])

@app.route('/es')
def es():
   return render_template('uploades.html', page=config["SITE_DATA"])

@app.route('/pl')
def pl():
   return render_template('uploadpl.html', page=config["SITE_DATA"])

@app.route('/sv')
def sv():
   return render_template('uploadsv.html', page=config["SITE_DATA"])

@app.route('/de')
def de():
   return render_template('uploadde.html', page=config["SITE_DATA"])

@app.route('/nl')
def nl():
   return render_template('uploadnl.html', page=config["SITE_DATA"])

@app.route('/ar')
def ar():
   return render_template('uploadar.html', page=config["SITE_DATA"])

@app.route('/index.html')
def html():
   return render_template('upload.html', page=config["SITE_DATA"])

@app.route('/index.php')
def php():
   return render_template('upload.html', page=config["SITE_DATA"])

# Robots
@app.route('/robots.txt')
def robots():
   return app.send_static_file('robots.txt')

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
    debug=config["DEBUG"],
    threaded=config["THREADED"]
  )

