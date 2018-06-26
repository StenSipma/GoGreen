import os
from flask import Flask, redirect, url_for


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABSE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        SEND_FILE_MAX_AGE_DEFAULT=1  # temp for image
    )

    if test_config is None:
        # load the instance config, if it extests, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
        os.makedirs(os.path.join(app.instance_path, 'generated'))
    except OSError:
        pass

    from . import home, auth, db, ranking, friends, about, tips
    db.init_app(app)
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(ranking.bp)
    app.register_blueprint(friends.bp)
    app.register_blueprint(about.bp)
    app.register_blueprint(tips.bp)

    @app.route('/')
    def main():
        return redirect(url_for('home.home'))  # temp

    return app
