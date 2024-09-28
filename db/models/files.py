from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_type = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User")