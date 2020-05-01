from environment_classes.environment import Environment
from pokemon_generator_classes.pokemon_generator import PokemonGenerator

pokemon_generator = PokemonGenerator(['charmander', 'squirtle', 'bulbasaur'])
environment = Environment('Test Biome', 10, pokemon_generator, 2)
environment.build()
