from flask import Flask
from flask_restx import Api
from .api.views import api_namespace
from .config.config import config_dict
from .utils import db
from .model.persons import Person
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound, MethodNotAllowed


def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app, 
              title='Person Data API',
              description='A simple REST API capable of CRUD operations on a "person"'
            )

    api.add_namespace(api_namespace, path='/api')

    @api.errorhandler(NotFound)
    def handle_not_found(error):
        return {'message': 'Not found'}, 404
    
    @api.errorhandler(MethodNotAllowed)
    def handle_method_not_allowed(error):
        return {'message': 'Method not allowed'}, 404

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'Person': Person,
        }

    return app