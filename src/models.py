import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    user_name = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    first_name= Column(String(50), nullable=False)
    last_name= Column(String(50), nullable=False)
    address = Column(String(150), nullable=False)
    starships_favorites = Column(Integer, ForeignKey('starships_favorites.id'))
    starships_favorites_relationship = relationship('StarshipsFavorites', back_populates='user_id_relationship')
    vehicles_favorites = Column(Integer, ForeignKey('vehicles_favorites.id'))
    vehicles_favorites_relationship = relationship('VehiclesFavorites', back_populates='user_id_relationship')
    planets_favorites = Column(Integer, ForeignKey('planets_favorites.id'))
    planets_favorites_relationship = relationship('PlanetsFavorites', back_populates='user_id_relationship')
    characters_favorites = Column(Integer, ForeignKey('characters_favorites.id'))
    characters_favorites_relationship= relationship('CharactersFavorites', back_populates='user_id_relationship')

class CharactersFavorites(Base):
    __tablename__='characters_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship('User', back_populates='characters_favorites_relationship')
    character_favorite = Column(Integer, ForeignKey('characters.id'))
    character_favorite_relationship= relationship('Character', back_populates='id_relationship')

class PlanetsFavorites(Base):
    __tablename__ = 'planets_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship('User', back_populates='planets_favorites_relationship')
    planet_favorite = Column(Integer, ForeignKey('planets_favorites.id'))
    planet_favorite_relationship= relationship('Planet', back_populates='id_relationship')

class StarshipsFavorites(Base):
    __tablename__ = 'starships_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship('User', back_populates='starships_favorites_relationship')
    starship_favorite= Column(Integer, ForeignKey('starship.id'))
    starship_favorite_relationship = relationship('Starship', back_populates='id_relationship')

class Starship(Base):
    __tablename__ ='starship'
    id = Column(Integer, ForeignKey('starships_favorites.id'), primary_key=True)
    id_relationship = relationship('StarshipsFavorites', back_populates='starship_favorite_relationship')
    uid = Column(Integer) 
    name = Column(String(50))
    model = Column(String(100))
    starship_class =Column(String(100))
    manufacturer = Column(String(100))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(String(100))
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating =Column(Integer)
    mglt = Column(Integer) 
    cargo_capacity = Column(Integer)
    consumables = Column(String(50)) 
    pilots = Column(Integer, ForeignKey('characters.id'))
    pilots_relationship = relationship('Character', back_populates='starship_pilot_relationship')
   
class VehiclesFavorites(Base):
    __tablename__ = 'vehicles_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship('User', back_populates='vehicles_favorites_relationship')
    vehicle_favorite = Column(Integer, ForeignKey('vehicle.id'))
    vehicle_favorite_relationship = relationship('Vehicle', back_populates='id_relationship')

class Vehicle(Base):
    __tablename__='vehicle'
    id = Column(Integer, ForeignKey('vehicles_favorites.id'), primary_key=True)
    id_relationship= relationship('VehiclesFavorites', back_populates='vehicle_favorite_relationship')
    uid = Column(Integer)
    name =Column(String(50))
    model = Column(String(50))
    vehicle_class = Column(String(50))
    manufacturer = Column(String(100))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(100))
    pilots = Column(Integer, ForeignKey('characters.id'))
    pilots_relationship = relationship('Character', back_populates='vehicle_pilot_relationship')
 
class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, ForeignKey('characters_favorites.character_favorite'), primary_key=True)
    id_relationship= relationship('CharactersFavorites', back_populates='character_favorite_relationship')
    uid = Column(Integer, nullable=False)
    name = Column(String(114), nullable=False)
    gender = Column(String(20), nullable=False)
    eye_color = Column(String(20), nullable=False)
    hair_color = Column(String(30), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    skin_color = Column(String(20), nullable=False)
    homeworld = Column(Integer, ForeignKey('planets.id'))
    homeworld_relationship=relationship('Planet', back_populates='characters_relationship')
    species = Column(Integer, ForeignKey('species.id'))
    species_relationship = relationship('Species', back_populates='characters_relationship')
    starship_pilot = Column(Integer, ForeignKey('starship.id'))
    starship_pilot_relationship = relationship('Starship', back_populates='pilots_relationship')
    vehicle_pilot = Column(Integer, ForeignKey('vehicle.id'))
    vehicle_pilot_relationship = relationship('Vehicle', back_populates='pilots_relationship')

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, ForeignKey('planets_favorites.id'), primary_key=True)
    id_relationship= relationship('PlanetsFavorites', back_populates='planet_favorite_relationship')
    uid = Column(Integer, nullable=False)
    name = Column(String(114), nullable=False)
    population = Column(String(30), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(120), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(Integer, nullable=False)
    species_relationship = relationship('Species', back_populates='planet_relationship')
    characters_relationship = relationship('Character', back_populates=' homeworld_relationship')

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    properties = Column(Integer, ForeignKey('species_properties.id'))
    properties_relationship = relationship('SpeciesProperty', back_populates='species_relationship')
    planet = Column(Integer, ForeignKey('planets.id'))
    planet_relationship = relationship('Planet', back_populates='species_relationship')
    characters_relationship = relationship('Character', back_populates='species_relationship')

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
    homeworld = Column(Integer, ForeignKey('planets.id'))
    homeworld_relationship = relationship('Planet', back_populates='species_relationship')
    species_relationship = relationship('Species', back_populates='properties_relationship')

# Crear una base de datos SQLite en memoria
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Dibujar el diagrama ER
render_er(Base, 'diagram.png')
