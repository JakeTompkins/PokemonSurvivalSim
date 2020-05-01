class Pokemon:
    def __init__(self, raw_data, position):
        self.stats = raw_data
        self.x = position["x"]
        self.y = position["y"]
        self.behaviors = []
