# mapper.py
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy.orm import registry

metadata = MetaData()

orm_labs_table = Table(
    'orm_labs',  metadata,
    Column('lab_id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('note', Integer),
    Column('level', Integer),
    Column('active', Boolean),
    Column('updated', DateTime),
)

class Map():
    @staticmethod
    def start_mapper(model):
        mapper_registry = registry()
        mapper_registry.map_imperatively(model, orm_labs_table)
        print('mapper started')
