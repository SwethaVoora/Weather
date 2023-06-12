from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = 'weather.db'

def Create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SECRET_KEY'] = 'secretkey'

    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .models import City  

    create_database(app)

    return app

def create_database(app):
    
    from .models import City
    if not path.exists('website/'+DB_NAME):
        with app.app_context():
          db.create_all()
          print('Database has been created.')
