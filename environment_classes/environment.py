class Environment:
    def __init__(self, biome_name, size, pokemon_generator, number_of_pokemon):
        self.grid_size = size
        self.name = biome_name
        self.number_of_pokemon = number_of_pokemon
        self.pokemon_generator = pokemon_generator

    def build_grid(self):
        self.grid = [[None for col in range(self.grid_size)]
                     for row in range(self.grid_size)]

    def generate_initial_pokemon(self):
        self.pokemons = self.pokemon_generator.generate_pokemon(
            self.number_of_pokemon)

        for pokemon in self.pokemons:
            self.handle_pokemon_position(pokemon)

    def get_pokemon_old_position(self, pokemon):
        for row_index, row in enumerate(self.grid):
            for col_index, col in enumerate(row):
                if col is pokemon:
                    return {"y": row_index, "x": col_index}

    def handle_pokemon_position(self, pokemon, *args):
        # First remove the pokemon from its old position
        # *args allows us to pass the current position in instead of having to check. Might refactor a little to make that standard
        old_polsition = args[0] or self.get_pokemon_old_position(pokemon)
        old_x = old_polsition["x"]
        old_y = old_polsition["y"]
        self.grid[old_y][old_x] = None

        # Then put it in its new position
        position = pokemon.position
        new_y = position['y']
        new_x = position['x']

        # Ensure the mon doesn't leave the grid
        new_y = 0 if new_y < 0 else new_y
        new_y = self.grid_size if new_y > self.grid_size else new_y
        nex_x = 0 if new_x < 0 else new_x
        new_x = self.grid_size if new_x > self.grid_size else new_x

        self.grid[row][col] = pokemon

    def build(self):
        self.build_grid()
        self.generate_initial_pokemon()
