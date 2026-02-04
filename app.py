# app.py
import logging

from flask import Flask
from flask_json import FlaskJSON

from sqlalchemy import create_engine

from zope.interface import classImplements
from zope.component import provideUtility
# import external routes
from components.Interactor.routes import std_routes
from components.Interactor.routes import io_routes
# import concrete classes
from components.Database import orm_labs_map
from components.Database import mapper
from components.Interactor import composer
from components.Validator import validator
# import interfaces(they arent actual classes. more like a document with strings)
from components.Interfaces.interfaces import IComposer
from components.Interfaces.interfaces import IValidator
from components.Interfaces.interfaces import IMapper
from components.Interfaces.interfaces import ILoader
import mimetypes

mimetypes.add_type('text/javascript', '.mjs')

logging.basicConfig(filename='portfolio.log')

### App Construction
# Construct the Flask app using the apps `__name__` dunder
app = Flask(__name__, static_folder='')
# Initialize Flask-JSON by passing the Flask app into the constructor
FlaskJSON(app)

### App Configuration
# cookies(session object)
app.config['SECRET_KEY'] = 'c34307275db9d9799ce0af21785ae1ead8fbeafcc21152fc5e420b6f5c2b72a1'
# True for cookies over HTTPS only. False for localhost development.
app.config['SESSION_COOKIE_SECURE'] = False
# cookies expiration
app.config["PERMANENT_SESSION_LIFETIME"] = 86400

### Engine Configuration
engine = create_engine(
    'sqlite:///ormlabs.db',
    connect_args={'autocommit': False}
)
        
### Route Configuration
# Register blueprints to externally expand the API through other modules.
app.register_blueprint(std_routes.std_routes_bp)
app.register_blueprint(io_routes.io_routes_bp)

### Zope Interface Configuration
# `zope.interface.classImplements` 
# Link interfaces to the objects that provide
classImplements(composer.Composer, IComposer)
classImplements(validator.Validator, IValidator)
classImplements(mapper.Mapper, IMapper)
classImplements(orm_labs_map.Map, ILoader)
#classImplements(io_routes._Response, IResponse)

# Register class instances with interfaces
composer_instance = composer.Composer()
provideUtility(composer_instance, IComposer)
validator_instance = validator.Validator()
provideUtility(validator_instance, IValidator)
orm_labs_map_instance = orm_labs_map.Map()
provideUtility(orm_labs_map_instance, ILoader)
mapper_instance = mapper.Mapper(engine)
provideUtility(mapper_instance, IMapper)
#response_instance = io_routes._Response()
#provideUtility(response_instance, IResponse)








if __name__=='__main__':
    app.run(debug=True)
