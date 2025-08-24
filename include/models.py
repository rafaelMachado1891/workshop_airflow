from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import func
from include.db import Base

class pokemon(Base):
    __tablename__ = 'pokemons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.now())