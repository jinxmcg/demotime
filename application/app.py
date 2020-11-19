from flask import Flask


def create_app(config_name):
    """Creates a flask app and expects the config name develpment or production"""
    app = Flask(__name__)

    # Capitalize so we get application.config.DevelopmentConfig
    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)
    # set a route
    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app