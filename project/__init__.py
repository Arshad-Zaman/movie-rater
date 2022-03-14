# pylint: disable= import-error, no-member, missing-module-docstring, invalid-name, simplifiable-if-expression, import-outside-toplevel, cyclic-import, unused-variable, bad-option-value
import os
from dotenv import find_dotenv, load_dotenv  # type: ignore
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

load_dotenv(find_dotenv())

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    """create app"""
    app = Flask(__name__)
    # set up a separate route to serve the index.html file generated
    # by create-react-app/npm run build.
    # By doing this, we make it so you can paste in all your old app routes
    # from Milestone 2 without interfering with the functionality here.

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for react parts of app
    from .bp import bp as bp_blueprint

    app.register_blueprint(bp_blueprint)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
