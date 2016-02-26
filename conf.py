config = dict()

# Recommended to be set to 127.0.0.1 for production, and then setup Nginx to this URL.
# For debugging, feel free to use whatever host you want ("0.0.0.0").
# Set "PORT" to any http port you desire.
config["HOST"] = "127.0.0.1"
config["PORT"] = 5000

# Enable for debugging.
config["DEBUG"] = False

# This is the path to the upload directory
config['UPLOAD_FOLDER'] = 'f/'

# This is to set the File size limit (In MB, change the 40)
config['MAX_CONTENT_LENGTH'] = 40 * 1024 * 1024

# These are the extension that we are accepting to be uploaded
config['ALLOWED_EXTENSIONS'] = set(['ass', 'odt', 'docx', 'doc', 'css', 'zip', 'ogg', 'mp3', 'wmv', 'mp4', 'txt', 'webm', 'gif', 'jpeg', 'jpg', 'png','psd','mkv','flac'])

# Threading with just Python, use Gunicorn or uWSGI for multi-threading.
config["THREADED"] = True

# Site info displayed to the user.
config["SITE_DATA"] = {
  "title": "Upflask"
}
