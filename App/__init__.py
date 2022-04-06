import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    
    from .routes import model_ml
    
	# blueprint for auth routes in our app
    app.register_blueprint(model_ml.model_ml)
    
    return app


app = create_app()
