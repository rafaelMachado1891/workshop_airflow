import requests
from include.db import Sessionlocal, engine, Base
from include.models import Pokemon
from include.schema import pokemonschema
from random import randint

Base.metadata.create_all(bind=engine)

def gerar_numero_aleatorio():
    return randint(1,350)

def pegar_pokemon(id: int):   
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = response.json()
    types = ', '.join(type['type']['name'] for type in data['types'])
    return pokemonschema(name=data['name'], type=types)

def adicionar_pokemon(pokemon_schema: pokemonschema) -> Pokemon:
    with Sessionlocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema['name'], type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon