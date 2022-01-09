import re
from state_machine_py.abstract_state import AbstractState
from state_machine_py.intermachine import Intermachine
from state_machine_py.multiple_state_machine import MultipleStateMachine
from state_machine_py.request import Request
from tests.rock_paper_scissors.context import Context
from tests.rock_paper_scissors.data.auto_gen.const import E_LOGIN, E_LOOPBACK, INIT


class InitState(AbstractState):
    """初期状態です"""

    def __init__(self):
        super().__init__()

        """ログイン
        kifuwarabe
        ----------
        1. username (1-32 characters)
        """
        self._user_name_pattern = re.compile(r"^([0-9A-Za-z_-]{1,32})$")

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

        self.on_your_name_prompt(req)

        matched = self._user_name_pattern.match(req.intermachine.dequeue_myself())

        self.on_update(req)

        if matched:
            req.context.user_name = matched.group(1)

            self.on_logged_in(req)
            return E_LOGIN

        self.on_failed(req)
        return E_LOOPBACK

    def on_your_name_prompt(self, req):
        """入力を取る前"""
        pass

    def on_update(self, req):
        pass

    def on_logged_in(self, req):
        """ログイン成功時"""
        pass

    def on_failed(self, req):
        """ログイン失敗時"""
        pass


# Test
# python.exe -m rock_paper_scissors.step2n2_man_state.init
if __name__ == "__main__":
    intermachine = Intermachine(MultipleStateMachine(), "[[TestMachine]]")
    context = Context()
    state = InitState()

    req = Request(context=context, intermachine=intermachine)
    req.intermachine.enqueue_myself("kifuwarabe")
    edge = state.update(req)
    if edge == E_LOGIN:
        print(".", end="")
    else:
        print("f", end="")

    req = Request(context=context, intermachine=intermachine)
    req.intermachine.enqueue_myself("ya !")
    edge = state.update(req)
    if edge == E_LOOPBACK:
        print(".", end="")
    else:
        print("f", end="")
