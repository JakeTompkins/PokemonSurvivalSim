from .Environment.Environment import Environment

environment = Environment('Test Biome', 10, 2, range(5))
environment.build()

print(environment.grid)
