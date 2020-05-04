from .movement import *

STAT_ACTIONS = {
    'aggression': [{'event_name': 'pokemon seen', 'action': stalk}],
    'self_preservation': [{'event_name': 'pokemon seen', 'action': flee}]
}


class BehaviorModel:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        # Might as well build them automatically
        self.create_listeners()

    def create_listeners(self):
        secondary_stats = pokemon.secondary_stats
        stats = secondary_stats['stats']

        for stat_name in STAT_ACTIONS:
            base_actions = STAT_ACTIONS[stat_name]

            for action in base_actions:
                event_name = action['event_name']
                stored_action = action['action']
                priority = stats[stat_name]

                self.listeners.append(
                    {'event_name': event_name, 'action': stored_action, 'pokemon': self.pokemon, 'priority': priority})

    def update_listeners(self):
        new_listeners = self.create()

        for new_listener in new_listeners:
            old_listener = next(
                [listener for listener in self.listeners if listener['action'] == new_listener['action']])

            old_listener['priority'] = new_listener['priority']
