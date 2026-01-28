# mapper.py
import inspect
from annotationlib import get_annotations
from dataclasses import dataclass
from datetime import datetime
from zope.component import getUtility
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import Session
from components.Interactor import model
from components.Interfaces.interfaces import ILoader



class Mapper():
    def __init__(self):
        self.metadata = MetaData()
        self.engine = self.get_tenant_engine()
        self.metadata.create_all(self.engine)
        
        self.ormlabs_model = model.OrmLabs
        self.movie_model = model.Movie
        self.start_mapper()
        print('Mapper Initialized')

    # CRUD
    def insert_row(self):      
        with Session(self.engine) as session:
            
            session.add('any object')          
            session.commit()

    def update_row(self, row_id):        
        with Session(self.engine) as session:
            
            
            session.commit()

    def delete_row(self, row_id):
        with Session(self.engine) as session:
            
            session.delete('any object')
            session.commit()
    
    # helper
    def check_for_db_entry(self):
        with Session(self.engine) as engine:
            pass


    # initialization
    def get_tenant_engine(self):
        self.engine = create_engine(
        'sqlite:///movies.db',
        connect_args={'autocommit': False}
        )
        return self.engine
    
    def start_mapper(self):
        print('startmapper')
        implementation = getUtility(ILoader)
        implementation.start_mapper(self.ormlabs_model)



# use dictionaries to insert into tables
sharkdown = {
    'title': 'sharkdown',
    'overview': '2 badass sharks',
    'runtime': 69,
    'original_language': 'eng',
    'budget': '$1',
    'release_date': '2010',
    'vote_count': 50.0,
    'vote_average': 5.0,
}

model.Movie(**sharkdown)

