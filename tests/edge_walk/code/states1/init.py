from state_machine_py.abstract_state import AbstractState
from tests.edge_walk.auto_gen.data.const import INIT, E_THAT, E_THIS


class InitState(AbstractState):
    """初期状態です"""

    def __init__(self):
        super().__init__()

    # @property
    # def name(self):
    #    return INIT

    def update(self, req):
        """次の辺の名前を返します

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり

        Returns
        -------
        str
            辺の名前
        """

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_THAT:
            self.on_that(req)
            return E_THAT

        elif msg == E_THIS:
            self.on_this(req)
            return E_THIS

        elif msg == None:
            return None

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        """入力を取る前"""
        pass

    def on_trigger(self, req):
        next_edge_name = req.intermachine.dequeue_myself()
        return next_edge_name
        # return req.context.pull_trigger()

    def on_that(self, req):
        pass

    def on_this(self, req):
        pass
