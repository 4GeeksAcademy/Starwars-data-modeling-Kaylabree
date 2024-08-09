import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(300), nullable=True)
    character_pic = Column(String(512), nullable=True)


class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(300), nullable=True)
    character_pic = Column(String(512), nullable=True)
  
class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("character.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    user_id = Column(Integer,ForeignKey("user.id"))

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    register_id = Column(Integer, ForeignKey("register.id"))

class login(Base):
    __tablename__ = "login"
    id = Column(Integer, primary_key=True)
    success = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"))

class Register(Base):
    __tablename__ = "register"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
