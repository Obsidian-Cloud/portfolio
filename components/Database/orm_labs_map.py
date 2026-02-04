# mapper.py
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.orm import registry

metadata = MetaData()

ormlabs_users = Table(
    'ormlabs_users',  metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_cookie', String),
    Column('name', String),
    Column('note', String),
    Column('level', Integer),
    Column('active', Integer),
    Column('updated', DateTime, server_default=func.now()),
)

class Map():
    @staticmethod
    def start_mapper(model):
        mapper_registry = registry()
        mapper_registry.map_imperatively(model, ormlabs_users)
        print('mapper started')
