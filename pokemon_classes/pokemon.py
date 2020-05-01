class Pokemon:
    def __init__(self, raw_data, position):
        self.stats = raw_data
        self.position = position
        self.behaviors = []
