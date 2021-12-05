class Intermachine():
    """マシーン間で値を受け渡しするのに使います"""

    def __init__(self, owner_maltiple_state_machine, machine_key):
        self._owner = owner_maltiple_state_machine
        self._machine_key = machine_key

    def put(self, destination_machine_key, item):
        self._owner.input_queues[destination_machine_key].put(item)

    def get(self):
        return self._owner.input_queues[self._machine_key].get()

    def task_done(self):
        return self._owner.input_queues[self._machine_key].task_done()
