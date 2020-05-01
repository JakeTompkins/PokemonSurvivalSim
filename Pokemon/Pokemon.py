class Pokemon:
    def __init__(self, genome, position):
        self.genome = genome
        self.x = position["x"]
        self.y = position["y"]
        self.behaviors = []
