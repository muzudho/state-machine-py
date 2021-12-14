import re
from state_machine_py.abstract_state import AbstractState
from state_machine_py.intermachine import Intermachine
from state_machine_py.multiple_state_machine import MultipleStateMachine
from state_machine_py.request import Request
from tests.rock_paper_scissors.context import Context
from tests.rock_paper_scissors.step1_const_conf import (
    E_DRAW,
    E_LOOPBACK,
    E_LOSE,
    E_WIN,
    GAME,
)


class GameState(AbstractState):
    def __init__(self):
        super().__init__()

        """Rock-paper-scissors（じゃんけん）
        R
        -
        R or P or S
        """
        self._janken_pattern = re.compile(r"^([RPS])$")

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
        self.on_update(req)

        matched = self._janken_pattern.match(req.intermachine.dequeue_myself())
        if matched:
            janken = matched.group(1)

            # 相手は P（パー） を出しているとします
            if janken == "R":
                self.on_lose(req)
                return E_LOSE
            elif janken == "S":
                self.on_win(req)
                return E_WIN
            else:
                self.on_draw(req)
                return E_DRAW

        self.on_loopback(req)
        return E_LOOPBACK

    def on_update(self, req):
        pass

    def on_win(self, req):
        pass

    def on_lose(self, req):
        pass

    def on_draw(self, req):
        pass

    def on_loopback(self, req):
        pass


# Test
# python.exe -m layer1_transition_map.game
if __name__ == "__main__":
    intermachine = Intermachine(MultipleStateMachine(), "[[TestMachine]]")
    context = Context()
    state = GameState()

    req = Request(context, intermachine)
    req.intermachine.enqueue_myself("R")
    edge = state.update(req)
    if edge == E_LOSE:
        print(".", end="")
    else:
        print("f", end="")

    req = Request(context, intermachine)
    req.intermachine.enqueue_myself("S")
    edge = state.update(req)
    if edge == E_WIN:
        print(".", end="")
    else:
        print("f", end="")

    req = Request(context, intermachine)
    req.intermachine.enqueue_myself("P")
    edge = state.update(req)
    if edge == E_DRAW:
        print(".", end="")
    else:
        print("f", end="")

    req = Request(context, intermachine)
    req.intermachine.enqueue_myself("W")
    edge = state.update(req)
    if edge == E_LOOPBACK:
        print(".", end="")
    else:
        print("f", end="")
