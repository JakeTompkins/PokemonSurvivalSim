import random
from ..Pokemon.Pokemon import Pokemon
from ..API.API import get_pokemon_data


class PokemonGenerator:
    def __init__(self, pokemon_pool):
        self.pokemon_pool = pokemon_pool
        self.defaultSpawn = {"x": 0, "y": 0}

    def get_random_pokemon_from_pool(self):
        pokemon_identifier_index = random.randint(0, len(self.pokemon_pool))
        pokemon_identifier = self.pokemon_pool[pokemon_identifier_index]

        return get_pokemon_data(pokemon_identifier)

    def generate_pokemon(self, number_of_pokemon):
        pokemon_data = map(self.get_random_pokemon_from_pool,
                           range(number_of_pokemon))

        return map(Pokemon, pokemon_data)
