from pydantic import BaseModel

class pokemonschema(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True