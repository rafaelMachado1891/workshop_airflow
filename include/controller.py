import requests
from include.db import Sessionlocal, engine, Base
from .models import pokemon
from .schema import pokemonschema
from random import randint

Base.metadata.create_all(bind=engine)

def gerar_numero_aleatorio(int):
    return randint(1,350)

def pegar_pokemon(id: int) -> pokemonschema:   
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = response.json()
    data_types = data['types']
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return pokemonschema(name=data['name'],type=types)

def adicionar_pokemon(pokemon_schema: pokemonschema) -> pokemon:
    with Sessionlocal() as db:
        db_pokemon = pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon