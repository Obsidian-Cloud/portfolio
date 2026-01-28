# app.py
from flask import Flask
from flask_session import Session
from flask_json import FlaskJSON

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
from components.Interfaces.interfaces import IResponse
from components.Interfaces.interfaces import ILoader


# Construct the Flask app using the apps `__name__` dunder
app = Flask(__name__, static_folder='')
# Initialize Flask-JSON by passing the Flask app into the constructor
json = FlaskJSON(app)

## Set config for cookies session
# Who keeps track of the cookies. In this instance, the local filesystem
app.config["SESSION_TYPE"] = "filesystem"
# Cookies expire once the browser is closed
app.config["SESSION_PERMANENT"] = False
# unused at the moment
# Wrap the flask app in a cookies session(database level)
# Flasks built-in session handles client side cookies
Session(app)

# Register blueprints to externally expand the API through other modules.
app.register_blueprint(std_routes.std_routes_bp)
app.register_blueprint(io_routes.io_routes_bp)

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
mapper_instance = mapper.Mapper()
provideUtility(mapper_instance, IMapper)
#response_instance = io_routes._Response()
#provideUtility(response_instance, IResponse)








if __name__=='__main__':
    app.run(debug=True)
