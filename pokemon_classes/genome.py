MAX_STATS = {
    "speed": 504,
    "special_defense": 614,
    "special_attack": 535,
    "defense": 614,
    "attack": 526,
    "hp": 714
}


def calculate_stat_for_level_fifty(base_stat):
  # Perform appropriate calculation here


def calculate_aggression(attack):
    return (attack / MAX_STATS['attack']) * 100


def calculate_stats(raw_data):
    raw_stats = raw_data.stats
    # Get the base stats out of the data from the api
    base_speed = raw_stats[0].base_stat
    base_special_defense = raw_stats[1].base_stat
    base_special_attack = raw_stats[2].base_stat
    base_defense = raw_stats[3].base_stat
    base_attack = raw_stats[4].base_stat
    base_hp = raw_stats[5].base_stat
    # Calculate stats for the pokemon at lvl 50
    speed = calculate_stat_for_level_fifty(base_speed)
    special_defense = calculate_stat_for_level_fifty(base_special_defense)
    special_attack = calculate_stat_for_level_fifty(base_special_attack)
    defense = calculate_stat_for_level_fifty(base_defense)
    attack = calculate_stat_for_level_fifty(base_attack)
    hp = calculate_stat_for_level_fifty(base_hp)
    # Calculate composite status based on percentile of lvl 50 stat
    aggression = calculate_aggression(attack)
    # Other such calculations go here

    # Return a dictionary with all of the primary and secondary stats
    return {
        "speed": speed,
        "special_defense": special_defense,
        "special_attack": special_attack,
        "defense": defense,
        "attack": attack,
        "hp": hp,
        "aggression": aggression
        # Add other composite stats in the same fashion
    }
