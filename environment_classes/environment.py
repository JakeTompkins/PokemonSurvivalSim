class Environment:
    def __init__(self, biome_name, size, pokemon_generator, number_of_pokemon, event_engine):
        self.grid_size = size
        self.name = biome_name
        self.event_engine = event_engine
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
            listeners = pokemon.behavior_model.listeners
            event_engine.register_listeners(listeners)

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
        return self.assess_pokemon_seen(pokemon)

    def assess_pokemon_seen(self, seeing_pokemon):
        all_pokemon = self.pokemons

        def measure_distance(seen_pokemon):
            position_1 = seeing_pokemon.position
            position_2 = seen_pokemon.position

            x_distance = abs(position_1.x - position_2.x)
            y_distance = abs(position_1.y - position_2.y)

            max_distance = max(x_distance, y_distance)
            min_distance = min(x_distance, y_distance)

            return min_distance * 1.5 + (max_distance - min_distance)

        perception = seeing_pokemon.secondary_stats.stats['perception']

        for pokemon in all_pokemon:
          if pokemon == seeing_pokemon:
            continue

          camouflage = pokemon.secondary_stats.stats['camouflage']
          distance = measure_distance(seeing_pokemon, pokemon)

          if perception - camouflage >= distance:
            self.event_engine.register_event('spot', seeing_pokemon, pokemon)

    def build(self):
        self.build_grid()
        self.generate_initial_pokemon()
