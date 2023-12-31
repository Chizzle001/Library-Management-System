from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TEST'
    
    from .view import views
    from .auth import auth
    
    
    app.register_blueprint(views, url_prefrix ='/')
    app.register_blueprint(auth, url_prefrix ='/')
    
    
    
    return app