from state_machine_py.abstract_state import AbstractState
from tests.task_sharing.keywords import E_DECREASE, E_STOP, INIT


class InitState(AbstractState):
    """初期状態です"""

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return INIT

    def enter(self, req):
        # 入力を飛ばします
        return "pass_on"

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

        if req.context.number == 0:
            return E_STOP

        if req.context.number == None:
            pass

        elif req.context.number % 2 == 0:
            req.context.number /= 2

        return E_DECREASE
