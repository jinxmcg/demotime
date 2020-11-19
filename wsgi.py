import os

from application.app import create_app

#we create the app using the FLASK_CONFIG env
app = create_app(os.environ["FLASK_CONFIG"])