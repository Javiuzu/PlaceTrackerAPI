#We create the different databases here
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from app.database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, index=True)
    hashed_password = Column(String)  #hash in 512 with salt and pepper


class Places(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, index=True)
    description = Column(String)
    country = Column(String, index=True)
    date = Column(Date)
    visited = Column(Boolean)
    #TODO add images to database
