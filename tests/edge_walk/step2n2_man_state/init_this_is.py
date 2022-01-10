from state_machine_py.abstract_state import AbstractState
from tests.edge_walk.auto_gen.data.const import IS


class InitThisIsState(AbstractState):
    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return IS

    def update(self, req):

        self.on_entry(req)

        next_edge_name = req.intermachine.dequeue_myself()
        return next_edge_name

    def on_entry(self, req):
        """入力を取る前"""
        pass
