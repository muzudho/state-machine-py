from state_machine_py.abstract_state import AbstractState
from tests.match_server.keywords import GAME


class GameState(AbstractState):

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return GAME

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

        state_path = "/".join(req.state_path)
        raise ValueError(f"Invalid state_path={state_path}")
