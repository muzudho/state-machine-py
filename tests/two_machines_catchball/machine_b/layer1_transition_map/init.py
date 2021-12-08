from state_machine_py.abstract_state import AbstractState
from tests.two_machines_catchball.keywords import E_DECREASE, E_STOP, INIT, MACHINE_A


class InitState(AbstractState):
    """初期状態です"""

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return INIT

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
            req.context.number = int(req.intermachine.dequeue())
            req.intermachine.task_done()

        if req.context.number == None:
            print("[B] まだボールは飛んでこなかった")

        elif req.context.number == 1:
            print("[B] ボールが 1 になったので停止します。ボールは投げます")
            req.intermachine.enqueue(MACHINE_A, req.context.number)
            req.context.number = None
            return E_STOP

        elif req.context.number % 2 == 0:
            req.context.number /= 2
            print(f"[B] ボールを {req.context.number} に上書きした")

        else:
            print(f"[B] {MACHINE_A}に ボール{req.context.number} を投げた")
            req.intermachine.enqueue(MACHINE_A, req.context.number)
            req.context.number = None

        return E_DECREASE
