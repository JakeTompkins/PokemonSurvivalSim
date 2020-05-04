class Pokemon:
    def __init__(self, raw_data, genome, secondary_stats, position):
        self.raw_data = raw_data
        self.genome = genome
        self.secondary_stats = secondary_stats
        self.position = position
        self.gender = ['M', 'F'].choice()
        self.level = 1
        self.behavior_model = None

    def level_up(self):
        self.level += 1
        self.genome.level_stats()
        self.secondary_stats.level_up(self.genome, self.level)
        self.behavior_model.update_listeners()
