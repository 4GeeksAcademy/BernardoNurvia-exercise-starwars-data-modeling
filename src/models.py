import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)
    name = Column(String(114), nullable=False)
    gender = Column(String(20), nullable=False)
    eye_color = Column(String(20), nullable=False)
    hair_color = Column(String(30), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    skin_color = Column(String(20), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet', back_populates='characters')
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship('Species', back_populates='characters')

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)
    name = Column(String(114), nullable=False)
    population = Column(String(30), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(120), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(Integer, nullable=False)
    species = relationship('Species', back_populates='planet')
    characters = relationship('Character', back_populates='planet')

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    properties_id = Column(Integer, ForeignKey('species_properties.id'))
    properties = relationship('SpeciesProperty', back_populates='species')
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet', back_populates='species')
    characters = relationship('Character', back_populates='species')

class SpeciesProperty(Base):
    __tablename__ = 'species_properties'
    id = Column(Integer, primary_key=True)
    classification = Column(String(100), nullable=False)
    designation = Column(String(100), nullable=False)
    average_height = Column(Integer)
    average_lifespan = Column(Integer)
    hair_colors = Column(String(50), nullable=False)
    skin_colors = Column(String(50), nullable=False)
    eye_colors = Column(String(50), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet')
    species = relationship('Species', back_populates='properties')

# Crear una base de datos SQLite en memoria
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Dibujar el diagrama ER
render_er(Base, 'diagram.png')
