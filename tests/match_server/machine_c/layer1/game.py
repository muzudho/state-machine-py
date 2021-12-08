from state_machine_py.abstract_state import AbstractState
from tests.match_server.keywords import GAME


class GameState(AbstractState):

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return GAME

    def exit(self, req):
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

        edge_path = "/".join(req.edge_path)
        raise ValueError(f"Invalid edge_path={edge_path}")
