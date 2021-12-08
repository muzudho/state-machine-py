from state_machine_py.abstract_state import AbstractState
from tests.two_machines_catchball.keywords import E_INCREASE, E_STOP, INIT, MACHINE_B


class InitState(AbstractState):
    """初期状態です"""

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return INIT

    def entry(self, req):
        # 入力を飛ばします
        req.intermachine.put_myself("pass_on")  # 意味のないコマンド

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
            print("[A] ボールを持っていないので、キャッチの姿勢を取ります")
            req.context.number = req.intermachine.get()
            req.intermachine.task_done()

        if req.context.number == None:
            print("[A] まだボールは飛んでこなかった")

        elif req.context.number == 1:
            print("[A] ボールが 1 になったので停止します。ボールは投げます")
            req.intermachine.put(MACHINE_B, req.context.number)
            req.context.number = None
            return E_STOP

        elif req.context.number % 2 == 1:
            req.context.number = 3 * req.context.number + 1
            print(f"[A] ボールを {req.context.number} に上書きした")

        else:
            print(f"[A] {MACHINE_B}に ボール{req.context.number} を投げた")
            req.intermachine.put(MACHINE_B, req.context.number)
            req.context.number = None

        return E_INCREASE
