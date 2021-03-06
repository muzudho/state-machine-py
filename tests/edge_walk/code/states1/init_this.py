from state_machine_py.abstract_state import AbstractState
from tests.edge_walk.auto_gen.data.const import THIS, E_IS, E_WAS


class InitThisState(AbstractState):
    def __init__(self):
        super().__init__()

    # @property
    # def name(self):
    #    return THIS

    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_WAS:
            self.on_was(req)
            return E_WAS

        elif msg == E_IS:
            self.on_is(req)
            return E_IS

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        """入力を取る前"""
        pass

    def on_trigger(self, req):
        next_edge_name = req.intermachine.dequeue_myself()
        return next_edge_name
        # return req.context.pull_trigger()

    def on_was(self, req):
        pass

    def on_is(self, req):
        pass
