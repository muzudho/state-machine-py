from state_machine_py.abstract_state import AbstractState
from tests.edge_walk.data.auto_gen.const import GOAL


class GoalState(AbstractState):
    """Goal状態"""

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return GOAL

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

        next_edge_name = req.intermachine.dequeue_myself()
        return next_edge_name

    def on_entry(self, req):
        pass
