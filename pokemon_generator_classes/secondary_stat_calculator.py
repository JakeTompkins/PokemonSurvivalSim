from api_class.API import get_pokemon_data


class SecondaryStats:
    def __init__(self, initial_stats, re_calculate):
        self.stats = initial_stats
        self.re_calculate = re_calculate

    def level_up(self, genome, level):
        self.stats = self.re_calculate(genome, level)


class SecondaryStatGenerator:
    def __init__(self, pokemon_pool):
        self.pokemon_pool = pokemon_pool
        self.pokemon_pool_raw_data = []

        self.get_pokemon_pool_raw_data = []

    def get_pokemon_pool_raw_data(self):
        self.get_pokemon_pool_raw_data = [get_pokemon_data(
            pokemon) for pokemon in self.pokemon_pool]

    def calculate_stat_max_at_level(self, base_stat, level):
        max_iv = 31
        max_nature_bonus_percent = .1
        flat_increase_per_level = base_stat * .02
        levels_beyond_first = level - 1

        return base_stat + ((flat_increase_per_level * levels_beyond_first) * max_nature_bonus_percent) + 31

    def calculate_stat_maxes_at_level(self, stat_name, level):
        if not level:
            level = 1

        all_base_stats = [data['stats'] for data in self.pokemon_pool_raw_data]
        base_stats = [next(filter(lambda x: x['stat']['name'] == stat_name, stat_block), None)
                      for stat_block in all_base_stats]
        max_stats = [self.calculate_stat_max_at_level(
            stat, level) for stat in base_stats]

        return max_stats

    def get_secondary_stat_percent(self, stat_name, stat_value, level):
        max_possible_for_pool = max(
            self.calculate_stat_maxes_at_level(stat_name, level))
        return (stat_value / max_possible_for_pool) * 100

    def calculate_aggression(self, attack, level):
        return self.get_secondary_stat_percent('attack', attack, level)

    def calculate_movement_speed(self, speed, level):
        return self.get_secondary_stat_percent('speed', speed, level)

    def calculate_sight(self, special_attack, level):
        return self.get_secondary_stat_percent('special_attack', special_attack, level)

    def calculate_camouflage(self, special_defense, level):
        return self.get_secondary_stat_percent('special_defense', special_defense, level)

    def calculate_longevity(self, hp, level):
        return self.get_secondary_stat_percent('hp', hp, level)

    def calculate_self_preservation(self, defense, level):
        return self.get_secondary_stat_percent('defense', defense, level)

    def calculate_secondary_stats(self, genome, level):
        if not level:
            level = 1

        current_stats = genome['current_stats']

        # Get current stats
        current_speed = current_stats['speed']
        current_special_defense = current_stats['special_defense']
        current_special_attack = current_stats['special_attack']
        current_defense = current_stats['current_defense']
        current_attack = current_stats['current_attack']
        current_hp = current_stats['hp']

        # Calculate composite status based on percentile of lvl 50 stat
        aggression = calculate_aggression(current_attack, level)
        movement_speed = calculate_movement_speed(current_speed, level)
        sight = calculate_sight(current_special_attack, level)
        camouflage = calculate_camouflage(current_special_defense, level)
        longevity = calculate_longevity(current_hp, level)
        self_preservation = calculate_self_preservation(current_defense, level)

        # We need to be able to recalculate from the pokemon model wihout creating a new instance of this class, so we can pass the calculation function for use within the instance of SecondaryStats
        return SecondaryStats({
            "aggression": aggression,
            "movement_speed": movement_speed,
            "sight": sight,
            "camouflage": camouflage,
            "longevity": longevity,
            "self_preservation": self_preservation,
        }, self.calculate_secondary_stats)
