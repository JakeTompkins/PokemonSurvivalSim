import requests

ROOT_URL = 'https://pokeapi.co/api/v2/'


def get_pokemon_data(identifier):
    if type(identifier) is not int and type(identifier) is not str:
        raise Exception(
            f'Pokemon must be queried by name or ID, got type {type(identifier)}')

    full_url = f"{ROOT_URL}Pokemon/{identifier}"
    result = requests.get(full_url)
