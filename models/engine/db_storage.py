#!/usr/bin/python3
"""module for db engine"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import models
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class DBStorage:
    """class for database storage"""

    __engine = None
    __session = None

    def __init__(self):
        """initialize dbstorage class"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        DB_URL = "mysql+mysqldb://{}:{}@{}/{}"\
            .format(user, pwd, host, db)
        self.__engine = create_engine(DB_URL, pool_pre_ping=True)

    if os.getenv("HBNB_ENV") == "test":
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query current database session all objects
        depending on class name"""
        classes = ["State", "City", "User", "Place", "Review", "Amenity"]
        objs = {}
        if cls is None:
            for class_name in classes:
                model = eval(class_name)
                query = self.__session.query(model).all()
                for obj in query:
                    key = obj.__class__.__name__ + "." + obj.id
                    objs[key] = obj
        else:
            query = self.__session.query(cls).all()
            for obj in query:
                key = obj.__class__.__name__ + "." + obj.id
                objs[key] = obj
        return objs

    def new(self, obj):
        """add new object to session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create the current db session from the engine"""
        Base.metadata.create_all(self.__engine)
        r_session = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(r_session)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session"""
        self.__session.close_all()
