class MultipleStateMachine():

    def __init__(self):
        self._machines = {}

    @property
    def machines(self):
        return self._machines
