import requests
from include.db import Sessionlocal, engine, Base
from include.models import Pokemon
from include.schema import pokemonschema
from random import randint

Base.metadata.create_all(bind=engine)

def gerar_numero_aleatorio():
    return randint(1,350)

def pegar_pokemon(id: int)-> dict:   
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = response.json()
    types = ', '.join(t['type']['name'] for t in data['types'])
    return {"name": data["name"], "type": types}

def adicionar_pokemon(pokemon_dict: dict) -> int:
    with Sessionlocal() as db:
        db_pokemon = Pokemon(name=pokemon_dict["name"], type=pokemon_dict["type"])
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon.id