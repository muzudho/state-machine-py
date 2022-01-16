from state_machine_py.abstract_state import AbstractState
from tests.edge_walk.auto_gen.data.const import GOAL, E_RETRY


class GoalState(AbstractState):
    """Goal状態"""

    def __init__(self):
        super().__init__()

    # @property
    # def name(self):
    #    return GOAL

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
        if msg == E_RETRY:
            self.on_retry(req)
            return E_RETRY

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        next_edge_name = req.intermachine.dequeue_myself()
        return next_edge_name
        # return req.context.pull_trigger()

    def on_retry(self, req):
        pass
