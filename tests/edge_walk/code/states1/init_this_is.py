from state_machine_py.abstract_state import AbstractState
from tests.edge_walk.auto_gen.data.const import IS, E_A, E_AN


class InitThisIsState(AbstractState):
    def __init__(self):
        super().__init__()

    # @property
    # def name(self):
    #    return IS

    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_AN:
            self.on_an(req)
            return E_AN

        elif msg == E_A:
            self.on_a(req)
            return E_A

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        """入力を取る前"""
        pass

    def on_trigger(self, req):
        next_edge_name = req.intermachine.dequeue_myself()
        return next_edge_name
        # return req.context.pull_trigger()

    def on_an(self, req):
        pass

    def on_a(self, req):
        pass
