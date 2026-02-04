# validator.py
from cerberus import Validator as _V

schema_submit = {
    'action': {'type': 'string'},
    'payload': {
        'type': 'dict',
        'schema': {
            'name': {'empty': False, 'type': 'string'},
            'note': {'type': 'string'},
            'level': {'type': 'integer'},
            'active': {'type': 'boolean'},
            'user_cookie': {'type': 'string'}
        }
    }
}

schema_update = {
    'action': {'type': 'string'},
    'payload': {
        'type': 'dict',
        'schema': {
            # the `ormlabs-check`(checkbox) carries with it the id of the
            # row to be deleted. this way, multiple attributes dont have
            # to be managed to accomplish the same goal. 
            'ormlabs-check': {'type': 'integer'},
            'name': {'empty': False, 'type': 'string'},
            'note': {'type': 'string'},
            'level': {'type': 'integer'},
            'active': {'type': 'boolean'},
            'user_cookie': {'type': 'string'}
        }
    }
}

schema_delete = {
    'action': {'type': 'string'},
    'payload': {
        'type': 'dict',
        'schema': {
            'ids': {
                'type': 'list',
                'schema': {'type': 'integer'}
            },
            'user_cookie': {'type': 'string'}
        }
    }
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
        self.schema = self.set_schema(self.action)
        self.valid = self._validator.validate(self.document, self.schema) # type:ignore
        valid = self.valid
        error = self._validator.errors # type: ignore

        print(error)
        self.clear_instance_cache()
        return valid, error

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
        print('match Action: ')
        match action:
            case 'submit':
                print('submit')
                return schema_submit
            case 'update':
                print('update')
                return schema_update
            case 'delete':
                print('delete')
                return schema_delete

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
