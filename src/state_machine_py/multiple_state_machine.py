
import queue

from state_machine_py.intermachine import Intermachine


class MultipleStateMachine():

    def __init__(self):
        self._machines = {}
        self._input_queues = {}
        self._intermachines = {}

    @property
    def machines(self):
        return self._machines

    @property
    def input_queues(self):
        return self._input_queues

    def append_machine(self, machine_key, machine):
        self._machines[machine_key] = machine
        self._input_queues[machine_key] = queue.Queue()
        self._intermachines[machine_key] = Intermachine()
