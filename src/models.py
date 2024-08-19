import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table characters
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Uid = Column(Integer)
    name = Column(String(114), nullable=False)
    gender = Column(String(20), nullable=False)
    eye_color =Column(String(20), nullable=False)
    hair_color = Column(String(30), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    skin_color = Column(String(20), nullable=False)
    homeworld = Column(Integer, ForeignKey('planets.id'))
    specie = Column(Integer, ForeignKey('species.id'))

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(characters)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
