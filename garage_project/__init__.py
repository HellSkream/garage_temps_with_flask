import os
from dotenv import load_dotenv
from flask import Flask
from garage_project import garage_proj, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    database.init_app(app)
    
    app.register_blueprint(garage_proj.bp)
    print(f"Current Enviroment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app
