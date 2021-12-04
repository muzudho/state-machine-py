import re
from state_machine_py.abstract_state import AbstractState
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

    def on_win(self, context):
        """----Win---->時"""
        pass

    def on_lose(self, context):
        """----Lose---->時"""
        pass

    def on_draw(self, context):
        """----Draw---->時"""
        pass

    def on_loopback(self, context):
        """----Loopback---->時"""
        pass

    def exit(self, context, line, edge_path):
        """次の辺の名前を返します
        Parameters
        ----------
        context : Context
            このステートマシンは、このContextが何なのか知りません。
            外部から任意に与えることができる変数です。 Defaults to None.
        line : str
            コマンドライン文字列

        Returns
        -------
        str
            辺の名前
        """

        matched = self._janken_pattern.match(line)
        if matched:
            janken = matched.group(1)

            # 相手は P（パー） を出しているとします
            if janken == 'R':
                self.on_lose(context)
                return '----Lose---->'
            elif janken == 'S':
                self.on_win(context)
                return '----Win---->'
            else:
                self.on_draw(context)
                return '----Draw---->'

        self.on_loopback(context)
        return '----Loopback---->'


# Test
# python.exe -m layer1_transition_map.game
if __name__ == "__main__":
    context = Context()
    state = GameState()

    line = 'R'
    edge = state.exit(context, line)
    if edge == '----Lose---->':
        print('.', end='')
    else:
        print('f', end='')

    line = 'S'
    edge = state.exit(context, line)
    if edge == '----Win---->':
        print('.', end='')
    else:
        print('f', end='')

    line = 'P'
    edge = state.exit(context, line)
    if edge == '----Draw---->':
        print('.', end='')
    else:
        print('f', end='')

    line = 'W'
    edge = state.exit(context, line)
    if edge == '----Loopback---->':
        print('.', end='')
    else:
        print('f', end='')
