# import Flask dependency
from flask import Flask

# Create a new Flask app instance.
app = Flask(__name__)

# Create Flask Route
@app.route('/')
# Create a function called hello_world().
def hello_world():
    return 'Hello world'
# Just completed first Flask route.
# EXPORT our FLASK_APP environment variable from COMMAND LINE in same directory as scripts (for Mac) - command on next line.
# export FLASK_APP=app.py
# Type "flask run" from COMMAND LINE. 
# Copy url generated on COMMAND LINE and paste in web browser.
