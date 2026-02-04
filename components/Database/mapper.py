# mapper.py
import logging

from zope.component import getUtility

from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from components.Interactor import model
from components.Interfaces.interfaces import ILoader

logger = logging.getLogger(__name__)


class Mapper():
    def __init__(self, engine):
        # initialize basic attributes
        self.db_obj = None
        self._id = None
        self._ids = []
        self.user_cookie = None

        # initialize engine
        self.metadata = MetaData()
        self.engine = engine
        self.metadata.create_all(self.engine)
        self.ormlabs_model = model.OrmLabs

        # start the mapper
        self.start_mapper()
        print('Mapper Initialized')

    # a simple input action gateway
    def execute_mapper(self, json=None, cookie_val=None):
        # if 'cookie_val' comes through explicitly, then query
        if cookie_val:
            return self.get_by_cookie(cookie_val=cookie_val)
        
        assert json is not None
        if 'action' in json:
            match json['action']:
                case 'submit':
                    return self.insert_row(json)
                case 'update':
                    return self.update_row(json)
                case 'delete':                   
                    return self.delete_row(json)             
        else:
            logger.info('Mapper: "action" missing within function ' \
            '`execute_mapper`.')       

    # CRUD
    def insert_row(self, json):      
        with Session(self.engine) as session:
            # create 'db_obj'
            self.db_obj = self.create_db_obj(json)
            # add 'db_obj' to session
            session.add(self.db_obj)
            # commit 'db_obj' to session
            session.commit()
            # refresh the session to get the database-calculated values
            # like 'autoincrement' and 'server defaults'(eg., time).
            session.refresh(self.db_obj)
            # create response payload from ORM object instance
            response = self.create_response('submit', db_obj=self.db_obj)
            self.clear_cache()

            return response

    def update_row(self, json):
        _attr = [
            'name',
            'note',
            'level',
            'active'
        ]
        with Session(self.engine) as session:
            # set `self._id` and `self._cookie` attributes
            self.set_row_metadata(json)
            # get 'db_obj' from database using `self._id`
            self.db_obj = session.get(self.ormlabs_model, self._id)
            # tell the IDE to assert the returned object is not `None` 
            # since sqlalchemy cant determine imperative mappings(one of the pro/con)
            assert self.db_obj is not None
            # validate user with cookie hash
            if self.db_obj.user_cookie == self.user_cookie:
                for key in _attr:
                    # Get the value from JSON, default to None if key doesn't exist
                    value = json['payload'].get(key)
                    # Set the attribute dynamically
                    setattr(self.db_obj, key, value)

                # commit 'db_obj' update to session
                session.commit()
                # refresh session object(update time updated)
                session.refresh(self.db_obj)
                # create response payload
                # the mappers `update_row` becomes the source of truth
                # for the action to send back to the client.
                response = self.create_response('update', db_obj=self.db_obj)
                self.clear_cache()

                return response
            logger.info('mapperError: Session cookie does not match database cookie.')

    def delete_row(self, json):
        with Session(self.engine) as session:
            self.set_row_metadata(json)

            # if more than 1 'id'
            if len(self._ids) > 1:
                for id in self._ids:
                    self.db_obj = session.get(self.ormlabs_model, id)
                    assert self.db_obj is not None

                    if self.db_obj.user_cookie == self.user_cookie:
                        session.delete(self.db_obj)
                    logger.info('mapperError: Session cookie does not match database cookie.')
                
                session.commit()
                response = self.create_response('delete', ids=self._ids)
                self.clear_cache()

                return response
            
            # if only 1 'id'
            self.db_obj = session.get(self.ormlabs_model, self._ids[0])
            assert self.db_obj is not None
            if self.db_obj.user_cookie == self.user_cookie:
                session.delete(self.db_obj)

                session.commit()
                response = self.create_response('delete', ids=self._ids)
                self.clear_cache()

                return response
            logger.info('mapperError: Session cookie does not match database cookie.')    

    def get_by_cookie(self, cookie_val):
        with Session(self.engine) as session:
            # query all rows where the cookie matches
            results = session.query(self.ormlabs_model).filter_by(user_cookie=cookie_val).all()
            # convert to a list of dicts for jinja
            return [obj.to_dict() for obj in results]

    def clear_cache(self):
        self.db_obj = None
        self._id = None
        self._ids = []
        self.user_cookie = None

    def set_row_metadata(self, json):
        print('JSON PAYLOAD')
        print(json)
        if {'ormlabs-check', 'user_cookie'}.issubset(json['payload']):
            print('orm check')
            # set the id from the checkbox value
            self._id = json['payload']['ormlabs-check']
            # set the cookie hash
            self.user_cookie = json['payload']['user_cookie']

        elif {'ids', 'user_cookie'}.issubset(json['payload']):
            self._ids = json['payload']['ids']
            self.user_cookie = json['payload']['user_cookie']

    def create_response(self, action, db_obj=None, ids=None):
        response = {'action': None, 'payload': {}}

        if action == 'delete':
            response['payload']['ids'] =  ids
            response['action'] = action
            return response
        
        assert db_obj is not None
        # add the 'db_obj' attributes to a nested 'payload' dict.
        response['payload'] = db_obj.to_dict()
        # add the database action to the response.
        # client needs to handle view updates according to action.
        response['action'] = action
        # pop 'user_cookie' from response object
        response['payload'].pop('user_cookie')
        return response

    # if i had more time, these would be in a separate module in a 
    # seperate 'helper' class. or even split up into two other classes.
    # it would depend on the actual use case. for me, this works.
    def create_db_obj(self, json):
        _attr = {
            'id': None,
            'user_cookie': 'NA',
            'name': 'Default',
            'note': 'None',
            'level': 0,
            'active': True,
            'updated': None
        }

        for key in json['payload']:
            # change to .get() otherwise itll crash
            if self.ormlabs_model.__dict__[key]:
                for _key in _attr:
                    if key == _key:
                        _attr[_key] = json['payload'][key]
            logger.info('Mapper.py: `KeyError` inside function ' \
            '`create_db_object`.')
            # after logging, make sure loop doesnt continue
        return model.OrmLabs(**_attr)


    def start_mapper(self):
        print('startmapper')
        implementation = getUtility(ILoader)
        implementation.start_mapper(self.ormlabs_model)
