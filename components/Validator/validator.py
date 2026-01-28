# validator.py
from cerberus import Validator as _V

schema_submit = {
    'action': {'type': 'string'},
    'payload': {
        'type': 'dict',           # Define the type as a dictionary
        'schema': {               # Use 'schema' to define the inner rules
            'ormlabs-check': {'type': 'boolean'},
            'name': {'type': 'string'},
            'note': {'type': 'string'},
            'level': {'type': 'string'},
            'active': {'type': 'string'}
        }
    }
}

schema_update = {
    'action': {'type': 'boolean'}
}

schema_delete = {
    
}

class Validator():
    def __init__(self): 
        self.action = None
        self.schema = None
        self.document = None
        self.valid = None
        self._validator = _V()

    def validate(self, document):
        """`Validator()` is created dynamically at runtime. Therefore the
        IDE cant verify the 'methods' at compile time.
        
        :returns: True or False depending on validation
        """
        self.document = document
        self.action = self.get_action(self.document)

        match self.action:
            case 'delete':
                print('ACTION: DELETE')
            case _:
                pass
        self.schema = self.set_schema(self.action)
        self.valid = self._validator.validate(self.document, self.schema) # type:ignore
        
        valid = self.valid
        print('errors:')
        print(self._validator.errors) # type: ignore
        self.clear_instance_cache()
        return valid

    def get_action(self, document):
        match document:
            case {'action': 'submit'}:
                return 'submit'
            case {'action': 'update'}:
                return 'update'
            case {'action': 'delete'}:
                return 'delete'
            case '':
                print('`action=""` inline attribute missing from html button')
                return None
            case _:
                print('"action" key missing from request payload')
                return None

    def set_schema(self, action):
        match action:
            case 'submit':
                return schema_submit
            case 'update':
                return schema_update

    def clear_instance_cache(self):
        self.valid = None
        self.document = None

#   mapping types:
#
#   binary
#   boolean
#   container
#   date
#   datetime
#   dict
#   float
#   integer
#   list
#   number
#   set
#   string
