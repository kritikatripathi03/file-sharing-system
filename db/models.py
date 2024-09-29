from sqlalchemy import Column, Integer, String
from db.base_class import Base
from pydantic import BaseModel

class SignupRequest(BaseModel):
    username: str
    password: str


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)  # Store hashed passwords
    user_type = Column(String)  # "admin" or "client"