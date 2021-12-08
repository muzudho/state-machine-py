from state_machine_py.abstract_state import AbstractState
from tests.edge_walk.keywords import GOAL


class GoalState(AbstractState):
    """Goal状態"""

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return GOAL

    def entry(self, req):
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

        # 現在位置の表示
        edge_path_str = '.'.join(req.edge_path)
        print(f"[Walk] Current state={self.name} edge_path={edge_path_str}")

        next_edge_name = req.intermachine.dequeue_myself()
        return next_edge_name
