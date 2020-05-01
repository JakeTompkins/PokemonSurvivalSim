from ..PokemonGenerator.PokemonGenerator import PokemonGenerator


class Environment:
    def __init__(self, biome_name, size, number_of_pokemon, pokemon_pool):
        self.grid_size = size
        self.name = biome_name
        self.number_of_pokemon = number_of_pokemon
        self.pokemon_generator = PokemonGenerator(pokemon_pool)

    def build_grid(self):
        self.grid = [[None for col in range(self.grid_size)]
                     for row in range(self.grid_size)]

    def generate_initial_pokemon(self):
        self.pokemons = self.pokemon_generator.generate_pokemon(
            self.number_of_pokemon)

        for pokemon in self.pokemons:
            self.handle_pokemon_position(pokemon)

    def handle_pokemon_position(self, pokemon):
        position = pokemon.position
        row = position['y']
        col = position['x']

        self.grid[row][col] = pokemon

    def build(self):
        self.build_grid()
        self.generate_initial_pokemon()
