# config   
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# factory
def create_app(): 
    app = Flask(__name__)

    # database config
    load_dotenv()
    URI = os.getenv("URI")
    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models 
    models.db.init_app(app)
    migrate = Migrate(app, models.db)              

    # index route
    @app.route('/')
    def index(): 
        return redirect('/reptiles')

    # register reptiles blueprint 
    from . import reptile 
    app.register_blueprint(reptile.bp)

    # return the app 
    return app