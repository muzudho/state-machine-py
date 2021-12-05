from state_machine_py.abstract_state import AbstractState
from tests.task_sharing.keywords import E_DECREASE, E_STOP, INIT, MACHINE_A


class InitState(AbstractState):
    """初期状態です"""

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return INIT

    def entry(self, req):
        # 入力を飛ばします
        print("[B] entry")
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

        if req.context.number == None:
            print("[B] ボールを持っていないので、キャッチの姿勢を取ります")
            req.context.number = req.intermachine.get()
            req.intermachine.task_done()

        if req.context.number == None:
            print("[B] まだボールは飛んでこなかった")

        elif req.context.number == 1:
            print("[B] Stop")
            return E_STOP

        elif req.context.number % 2 == 0:
            print("[B] Calc")
            req.context.number /= 2

        else:
            print(f"[B] [{MACHINE_A}]に ボール[{req.context.number}] を渡したい")
            req.intermachine.put(MACHINE_A, req.context.number)
            req.context.number = None

        return E_DECREASE
