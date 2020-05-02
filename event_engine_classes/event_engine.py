class EventEngine:
    def __init__(self):
        self.listeners = {}

    def register_listener(self, event_name, action, pokemon):
        if self.listeners[event_name] is None:
          # Create an array if none exists
            self.listeners[evet_name] = []
        # Listener object needs to know the action and the pokemon performing it
        listener = {"action": action, "pokemon": pokemon}
        self.listeners.append(listener)
        # allows us to find the listener again if necessary to remove
        return listener

    def emit_event(self, event_name, *args):
        relevant_listeners = self.listeners[event_name]

        for listener in relevant_listeners:
            action = listener.action
            pokemon = listener.pokemon
            # *args is for when an event involvmes multiple pokemon, i.e. battles. This allows us to pass the second, third etc pokemon to the action
            return action(pokemon, *args)

    def unregister_listener(self, listener):
        for list in self.listeners.values():
            if listener in list:
                list.remove(listener)
        # Just to be clear it worked
        return True
