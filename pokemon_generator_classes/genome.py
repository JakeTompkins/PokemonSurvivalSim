from random import randint


class Genome:
    def __init__(self, raw_data, nature):
        self.raw_data
        self.nature

        # set ivs
        self.set_ivs()

        # Set stats
        self.set_base_stats()
        self.current_stats = self.base_stats

    def get_random_iv(self):
        return randint(1, 32)

    def set_ivs(self):
        self.attack_iv = self.get_random_iv()
        self.special_attack = self.get_random_iv()
        self.defense_iv = self.get_random_iv()
        self.special_defense_iv = self.get_random_iv()
        self.speed = self.get_random_iv()
        self.hp = self.get_random_iv()

    def set_nature_influencesd_stats(self):
        self.increased_stat = self.nature['increased_stat']['name']
        self.decreased_stat = self.nature['decreased_stat']['name']

    def set_base_stats(self):
        raw_data = self.raw_data
        stats = raw_data['stats']

        base_stats = {}
        for stat in stats:
            name = stat['stat']['name']
            value = stat['base_value']

            iv = self[f'{name}_iv']

            base_stats[name] = value + iv

        self.base_stats = base_stats

    def level_stat(self, stat_name):
        current_value = self.current_stats[stat_name]
        base_value = self.base_stats[stat_name]

        flat_increase = base_value * .02
        nature_increase = self.increased_stat == stat_name
        nature_decrease = self.decreased_stat == stat_name

        if nature_increase:
            return current_value + ((flat_increase) * 1.1)
        elif nature_decrease:
            return current_value + ((flat_increase) * .9)
        return current_value + flat_increase

    def level_stats(self):
        for stat in self.current_stats:
            current_stats[stat] = self.level_stat(stat)
