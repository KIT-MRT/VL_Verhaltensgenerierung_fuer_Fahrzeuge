class StateMachine:
    def __init__(self, initial_state):
        self.currentState = initial_state
        self.currentState.run()

    def transition(self, event):
        self.currentState = self.currentState.next(event)
        self.currentState.run()


class State:
    def run(self):
        assert 0, "run not implemented"

    def next(self, event):
        assert 0, "next not implemented"


class Event:
    def __init__(self, event_description):
        self.event_description = event_description

    def __str__(self): return self.event_description

    def __eq__(self, other):
        return self.event_description == other.event_description

