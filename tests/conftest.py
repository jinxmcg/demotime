import pytest


from application.app import create_app

@pytest.fixture
def app():
    app = create_app("testing")
    config_module = f"application.config.TestingConfig"
    app.config.from_object(config_module) 
    app.config["MONGO_URI"] = "mongodb://"+app.config['MONGO_INITDB_USERNAME']+":"+app.config['MONGO_INITDB_PASSWORD']+"@"+app.config['MONGO_INITDB_HOSTNAME']+":"+app.config['MONGO_INITDB_PORT']+"/"+app.config['MONGO_INITDB_DATABASE']    
    return app
