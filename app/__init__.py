import os
from flask import Flask, url_for
from werkzeug.routing import Rule

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    print('debug')

    from .auth_module import auth, default_redirect
    app.register_blueprint(auth.authbp)
    app.register_blueprint(default_redirect.default_redirect_bp)

    from .scheduling_module import scheduling
    app.register_blueprint(scheduling.schedulingbp)


    return app