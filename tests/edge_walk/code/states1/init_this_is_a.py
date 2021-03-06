from state_machine_py.abstract_state import AbstractState
from tests.edge_walk.auto_gen.data.const import A, E_PEN, E_PIN


class InitThisIsAState(AbstractState):
    def __init__(self):
        super().__init__()

    # @property
    # def name(self):
    #    return A

    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_PIN:
            self.on_pin(req)
            return E_PIN

        elif msg == E_PEN:
            self.on_pen(req)
            return E_PEN

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        """入力を取る前"""
        pass

    def on_trigger(self, req):
        next_edge_name = req.intermachine.dequeue_myself()
        return next_edge_name
        # return req.context.pull_trigger()

    def on_pin(self, req):
        pass

    def on_pen(self, req):
        pass
