import random
from pokemon_classes.pokemon import Pokemon
from api_class.API import get_pokemon_data, get_all_natures


class PokemonGenerator:
    def __init__(self, pokemon_pool, spawnPoint={"x": 0, "y": 0}):
        self.pokemon_pool = pokemon_pool
        self.defaultSpawn = spawnPoint

    def get_random_nature(self):
        all_natures = get_all_natures()

        return all_natures.choice()

    def get_random_pokemon_from_pool(self):
        pokemon_identifier_index = random.randint(
            0, len(self.pokemon_pool) - 1)
        pokemon_identifier = self.pokemon_pool[pokemon_identifier_index]

        return get_pokemon_data(pokemon_identifier)

    def generate_one_pokemon(self):
        pokemon_data = self.get_random_pokemon_from_pool()
        nature = self.get_random_nature()
        #genome = genome_generator(pokemon_data, nature)

    def generate_many_pokemon(self, number_of_pokemon):
        return [self.generate_many_pokemon() for x in range(number_of_pokemon)]
