# composer.py
from enum import Enum


from zope.component import getUtility

from components.Interactor import request as _req

from components.Interfaces.interfaces import IValidator
from components.Interfaces.interfaces import IResponse
from components.Interfaces.interfaces import IMapper



class Composer():
    def __init__(self):
        self.validated = None

    def execute_composer(self):              
                json = self.retrieve_json()
                print('JSON')
                print(json)

                self.validate_json(json)
                print('VALIDATED')
                print(self.validated)

                if self.validated:
                    self.execute_json()
                    self.return_response()
                    self.clear_instance_cache()
                else:
                    self.clear_instance_cache()
                    self.return_response()

    def retrieve_json(self):
        json = _req.request_ds
        self.json = json.copy()
        _req.request_ds.clear()
        return self.json

    def validate_json(self, json):
        self.validated = None

        implementation = getUtility(IValidator)
        self.validated = implementation.validate(json)
        return self.validated

    def execute_json(self):
        pass

    def return_response(self):
        pass

    def clear_instance_cache(self):
        self.validated = None
        print('clear instance')


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


