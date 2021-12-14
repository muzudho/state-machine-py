from state_machine_py.abstract_state import AbstractState
from tests.edge_walk.step1_const_conf import INIT


class InitState(AbstractState):
    """初期状態です"""

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return INIT

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

        # 現在位置の表示
        state_path_str = '/'.join(req.state_path)
        print(f"[Walk] Current state={self.name} state_path={state_path_str}")

        self.on_prompt(req)

        next_edge_name = req.intermachine.dequeue_myself()
        return next_edge_name

    def on_prompt(self, req):
        """入力を取る前"""
        pass
