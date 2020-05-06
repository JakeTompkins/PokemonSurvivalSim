from .ticker import Ticker


class Engine:
    def __init__(self, interval):
        self.listeners = {}
        self.event_queue = []
        self.ticker_interval = interval
        self.ticker = Ticker(interval, self.emit_tick)

        self.ticker.start()

    def emit_tick(self):
        return self.register_event('tick')

    def register_listeners(self, listeners):
        for listener in listeners:
            event_name = listener['event_name']

            if self.listeners[event_name] is None:
              # Create an array if none exists
                self.listeners[evet_name] = []

            self.listeners[event_name].append(listener)
            # allows us to find the listener again if necessary to remove
        return listeners

    def unregister_listener(self, listener):
        for list in self.listeners.values():
            if listener in list:
                list.remove(listener)
        # Just to be clear it worked
        return True

    def register_event(self, event_name, pokemon, *args):
        self.event_queue.append([event_name, pokemon, *args])

    def execute_action_for_pokemon(self, listener_array, *args):
        action_taken = False
        index = 0
        while action_taken == False:
            action = listener_array[index]['action']
            action_taken = action(*args)

            if action_taken is not True and action_taken is not False:
                raise Exception('Action needs to return true or false')

            index += 1

            if index == len(listener_array):
                break

    def group_listeners_by_pokemon(self, listeners):
        pokemon_ids = {}
        for listener in listeners:
            pokemon = listener['pokemon']
            # This is the id of the object in memory, not the id of the pokemon in the pai
            pokemon_id = id(pokemon)
            # Make sure there's an array there if it's the first time this id has been seen
            if pokemon_ids[pokemon_id] is None:
                pokemon_ids[pokemon_id] = []

            pokemon_ids[pokemon_id].append(listener)
        # This returns a 2 dimensional array with listeners grouped by pokemon they were registered by
        return pokemon_ids.values()

    def sort_listeners_by_priority(self, listeners):
        return listeners.sort(key=lambda x: x['priority'], reverse=True)

    def emit_events(self):
        for event_args in self.event_queue:
            name, pokemon, *args = event_args
            relevant_listeners = self.listeners[name]
            grouped_listeners = self.group_listeners_by_pokemon(
                relevant_listeners)
            sorted_listeners = [self.sort_listeners_by_priority(
                listener_arr) for listener_arr in grouped_listeners]

            for listeners_arr in sorted_listeners:
                self.execute_action_for_pokemon(listeners_arr, pokemon, *args)
