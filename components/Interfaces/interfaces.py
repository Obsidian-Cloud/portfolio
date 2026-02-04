import zope.interface as _z


# These are string documents. can use `list()` and `sort()`.

class IValidator(_z.Interface):
    """This `interface` shares a relationship with the `validator` and is
    implemented by the `composer` to initiate validation of JSON.
    """
    def validate(): # type:ignore
        """Executes the `validator`."""
        return _valid, _error # type: ignore


class IComposer(_z.Interface):
    """This `interface` shares a relationship with the `composer` and is
    implemented by the `routes` to initiate a request.
    """
    def execute_composer(query=None, cookie_val=None): # type: ignore
        """Executes the `composer`."""
        return response # type: ignore


class IMapper(_z.Interface):
    """This `interface` shares a relationship with the `mapper` and is
    implemented by the `composer` to initiate abstracted ORM CRUD 
    operations.
    """
    def execute_mapper(json=None, cookie_val=None): # type: ignore
        """Executes the mapper"""
        return response # type: ignore


class IResponse(_z.Interface):
    """This `interface` shares a relationship with the `routes` and is
    implemented by the `composer` to return a JSON response to the client. 
    """
    def _return(): # type: ignore
        """Returns a response"""


class ILoader(_z.Interface):
    """This `interface` shares a relationship with the `projects` and is
    implemented by the `mapper` to load projects. 
    """
    def start_mapper(model): # type: ignore
        """starts a mapper for the DB connection"""