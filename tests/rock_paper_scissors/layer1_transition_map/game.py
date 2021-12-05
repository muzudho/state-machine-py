import re
from state_machine_py.abstract_state import AbstractState
from state_machine_py.request import Request
from context import Context


class GameState(AbstractState):
    def __init__(self):
        super().__init__()

        """Rock-paper-scissors（じゃんけん）
        R
        -
        R or P or S
        """
        self._janken_pattern = re.compile(r'^([RPS])$')

    @property
    def name(self):
        return "[Game]"

    def on_win(self, req):
        """----Win---->時"""
        pass

    def on_lose(self, req):
        """----Lose---->時"""
        pass

    def on_draw(self, req):
        """----Draw---->時"""
        pass

    def on_loopback(self, req):
        """----Loopback---->時"""
        pass

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

        matched = self._janken_pattern.match(req.line)
        if matched:
            janken = matched.group(1)

            # 相手は P（パー） を出しているとします
            if janken == 'R':
                self.on_lose(req)
                return '----Lose---->'
            elif janken == 'S':
                self.on_win(req)
                return '----Win---->'
            else:
                self.on_draw(req)
                return '----Draw---->'

        self.on_loopback(req)
        return '----Loopback---->'


# Test
# python.exe -m layer1_transition_map.game
if __name__ == "__main__":
    context = Context()
    state = GameState()

    line = 'R'
    req = Request(context, line, [])
    edge = state.exit(req)
    if edge == '----Lose---->':
        print('.', end='')
    else:
        print('f', end='')

    line = 'S'
    req = Request(context, line, [])
    edge = state.exit(req)
    if edge == '----Win---->':
        print('.', end='')
    else:
        print('f', end='')

    line = 'P'
    req = Request(context, line, [])
    edge = state.exit(req)
    if edge == '----Draw---->':
        print('.', end='')
    else:
        print('f', end='')

    line = 'W'
    req = Request(context, line, [])
    edge = state.exit(req)
    if edge == '----Loopback---->':
        print('.', end='')
    else:
        print('f', end='')
