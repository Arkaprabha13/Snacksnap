from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .session import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
    recipes = relationship("Recipe", back_populates="owner")
    followers = relationship("Follow", back_populates="followed_user")
    following = relationship("Follow", back_populates="follower_user")

class Recipe(Base):
    __tablename__ = "recipes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    ingredients = Column(String)
    instructions = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="recipes")

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    recipe = relationship("Recipe")
    user = relationship("User")

class Like(Base):
    __tablename__ = "likes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    
    user = relationship("User")
    recipe = relationship("Recipe")
