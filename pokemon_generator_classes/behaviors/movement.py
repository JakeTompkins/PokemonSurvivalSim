def find_directions_to(mon1, mon2):
    mon1_position = mon1.position
    mon2_position = mon2.position
    # Use an array because the predator might need to zig zag
    directions_to_mon2 = []

    # Can only go in one direction on each axis, so use elif
    if mon1_position.y > mon2_position.y:
        directions_to_mon2.append('NORTH')
    elif mon1_position.y < mon2_position.y:
        directions_to_mon2.append('SOUTH')

    if mon1_position.x < mon2_position.x:
        directions_to_mon2.append('EAST')
    elif mon1_position.x > mon2_position.x:
        directions_to_mon2.append('WEST')

    return directions_to_mon2


def walk(pokemon, update_position):
    DIRECTIONS = ['NORTH, SOUTH, EAST, WEST']
    distance = pokemon.secondary_stats.stats.movement_speed

    for square in range(distance):
        current_position = pokemon.position
        x = current_position.x
        y = current_position.y

        # If the pokemon has a particular direction, move it there, otherwise move randomly
        direction = pokemon.direction or DIRECTIONS.choice()

        if direction is 'NORTH':
            y -= 1
        elif direction is 'SOUTH':
            y += 1
        elif direction is 'EAST':
            x += 1
        elif direction is 'WEST':
            x -= 1

        pokemon.position = {"x": x, "y": y}

        update_position(pokemon, current_position)

    return True


def stalk(predator, prey, update_position):
    predator_position = predator.position
    mon2_position = prey.position

    predator_current_direction = predator.direction
    directions_to_prey = find_directions_to(predator, prey)

    # This ensures that the predator will zig zag instead of making L movements
    # If there's only one direction and the pokemon is already moving in it, nothing needs to change
    for direction in directions_to_prey:
        if direction is not predator_current_direction:
            predator.direction = direction
            return walk(predator, update_position)


def flee(prey, predator, update_position):
    prey_position = prey.position
    predator_position = predator.position

    prey_current_direction = prey.direction
    direction_opposits = tuple(zip(['NORTH', 'EAST'], ['SOUTH', 'WEST']))
    directions_to_predator = find_directions_to(prey, predator)
    opposite_directions = []

    for d1, d2 in direction_opposits:
        if d1 in directions_to_predator:
            opposite_directions.push(d2)
        elif d2 in directions_to_predator:
            opposite_directions.push(d1)

    for direction in direction_opposits:
        if direction is not prey_current_direction:
            prey.direction = direction
            return walk(prey, update_position)
