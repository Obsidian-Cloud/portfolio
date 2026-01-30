# composer.py
from enum import Enum


from zope.component import getUtility

from components.Interactor import request as _req

from components.Interfaces.interfaces import IValidator
from components.Interfaces.interfaces import IResponse
from components.Interfaces.interfaces import IMapper



class Composer():
    def __init__(self):
        self.valid = None
        self.error = None

    def execute_composer(self):
                print('execute composer')          
                json = self.retrieve_json()
                print(json)
                self.valid, self.error = self.validate_json(json)

                if self.valid:
                    print('composer valid')
                    self.execute_json()
                    response = self.create_response(self.error)
                    self.clear_instance_cache()
                    return response
                else:
                    print('composer not valid')
                    response = self.create_response(self.error)
                    self.clear_instance_cache()
                    return response

    def retrieve_json(self):
        json = _req.request_ds
        self.json = json.copy()
        _req.request_ds.clear()
        return self.json

    def validate_json(self, json):
        implementation = getUtility(IValidator)
        valid, error = implementation.validate(json)
        return valid, error

    def execute_json(self):
        pass

    def create_response(self, error):
        # create response obj(dict)
        if error:
            response = {'error': str(error)}
            return response

        response = {'not': 69}
        return response

    def clear_instance_cache(self):
        self.valid = None
        self.error = None


'''
The `composer` is the most 'stable' module in the interactor. A request 
is initialized through the `composer` interface, which is implemented by
the `controller`. The `composer` then retrieves the `JSON` that was sent
and stored from the client, from a dependency inverted data structure 
container. The `composer` then validates the JSON against custom cerberus 
validation schemes. If validation fails, a response is sent. If it 
passes, the `composer` executes whatever action was included within the 
`JSON` request body by implementing the mappers abstracted ORM interface.

:use cases: TBA

:returns: Returns JSON response.

'''


