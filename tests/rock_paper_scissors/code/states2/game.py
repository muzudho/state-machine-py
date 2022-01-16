from tests.rock_paper_scissors.auto_gen.code.states1.game import GameState
from tests.rock_paper_scissors.auto_gen.data.const import (
    E_DRAW,
    E_LOOPBACK,
    E_LOSE,
    E_WIN,
)
from state_machine_py.intermachine import Intermachine
from state_machine_py.multiple_state_machine import MultipleStateMachine
from state_machine_py.request import Request
from tests.rock_paper_scissors.context import Context


def create_game(state):
    def __on_entry(req):
        """この on_update メソッドは省略することもできます。
        この状態から出たときにする処理を書いてください。
        ステートマシンが中断されたときは省略されます

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """

        # 改行を出力しないとフラッシュされませんので、明示的にフラッシュします
        print("Rock-paper-scissors(R,P,S): ", end="", flush=True)

    def __on_trigger(req):
        msg = req.intermachine.dequeue_myself()

        # 相手は P（パー） を出しているとします
        if msg == "S":
            return E_WIN
        elif msg == "P":
            return E_DRAW
        elif msg == "R":
            return E_LOSE
        else:
            return E_LOOPBACK

    def __on_win(req):
        """この on_win メソッドは省略することもできます。
        Win辺

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        print(
            """+-----------------+
| Win: 勝ちました |
+-----------------+"""
        )

    def __on_draw(req):
        """この on_draw メソッドは省略することもできます。
        Draw辺

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        print(
            """+----------------------+
| Draw: 引き分けました |
+----------------------+"""
        )

    def __on_lose(req):
        """この on_lose メソッドは省略することもできます。
        Lose辺

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        print(
            """+------------------+
| Lose: 負けました |
+------------------+"""
        )

    def __on_loopback(req):
        """この on_loopback メソッドは省略することもできます。
        Looback辺

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        print(
            """+--------------------+
| NoGame: やりなおし |
+--------------------+"""
        )

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_win = __on_win
    state.on_draw = __on_draw
    state.on_lose = __on_lose
    state.on_loopback = __on_loopback
    return state


# Test
# python.exe -m rock_paper_scissors.code.states.game
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
