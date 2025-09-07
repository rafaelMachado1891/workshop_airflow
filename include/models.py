# include/models.py
from sqlalchemy import Column, Integer, String
from .db import Base

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f"<Pokemon(id={self.id}, name='{self.name}', type='{self.type}')>"