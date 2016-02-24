config = dict()

# Recommended to be set to 127.0.0.1 for production, and then setup Nginx to this URL
# For debugging, feel free to use whatever host you want ("0.0.0.0")
config["HOST"] = "127.0.0.1"
config["PORT"] = 5000

# Enable for debugging
config["DEBUG"] = False

# Not sure if it works AT ALL, but if it does...
config["THREADED"] = True

# Site info displayed to the user
config["SITE_DATA"] = {
  "title": "Upflask"
}
