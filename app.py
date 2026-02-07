# app.py
import mimetypes
import logging
import os

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

mimetypes.add_type('text/javascript', '.mjs')
# currently using in routes...minimally.
logging.basicConfig(filename='portfolio.log')

### App Construction
# construct the Flask app using the apps `__name__` dunder
app = Flask(__name__)
# initialize Flask-JSON by passing the Flask app into the constructor
FlaskJSON(app)

### App Configuration
# set required secret key
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
# True for cookies over HTTPS only. False for localhost(HTTP) development.
# .dev domains require SSL since browsers access .dev over HTTPS 
# only. Might as well set it True for production.
app.config['SESSION_COOKIE_SECURE'] = False
# cookies expiration
app.config["PERMANENT_SESSION_LIFETIME"] = 259200

### Engine Configuration
#basedir = os.path.abspath(os.path.dirname(__file__))
#db_path = os.path.join(basedir, 'ormlabs.db')

#engine = create_engine(
#    f'sqlite:///{db_path}'
#)

## Alternate Engine Configuration
# for testing to create a local engine.
# the way this 'local' engine is implemented was a time constraint.
# it would usually be done with a switch.

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

# Register class instances with interfaces
composer_instance = composer.Composer()
provideUtility(composer_instance, IComposer)
validator_instance = validator.Validator()
provideUtility(validator_instance, IValidator)
orm_labs_map_instance = orm_labs_map.Map()
provideUtility(orm_labs_map_instance, ILoader)
mapper_instance = mapper.Mapper(engine)
provideUtility(mapper_instance, IMapper)


if __name__=='__main__':
    app.run(debug=True)
