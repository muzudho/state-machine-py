import re
from state_machine_py.abstract_state import AbstractState
from context import Context


class InitState(AbstractState):
    """初期状態です"""

    def __init__(self):
        super().__init__()

        """ログイン
        kifuwarabe
        ----------
        1. username (1-32 characters)
        """
        self._user_name_pattern = re.compile(r'^([0-9A-Za-z_-]{1,32})$')

    @property
    def name(self):
        return "[Init]"

    def on_logged_in(self, context):
        """ログイン成功時"""
        pass

    def on_failed(self, context):
        """ログイン失敗時"""
        pass

    def leave(self, context, line, edge_path):
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

        matched = self._user_name_pattern.match(line)
        if matched:
            context.user_name = matched.group(1)

            self.on_logged_in(context)
            return '----LoggedIn---->'

        self.on_failed(context)
        return '----Loopback---->'


# Test
# python.exe -m layer1_transition_map.init
if __name__ == "__main__":
    context = Context()
    state = InitState()

    line = 'kifuwarabe'
    edge = state.leave(context, line)
    if edge == '----LoggedIn---->':
        print('.', end='')
    else:
        print('f', end='')

    line = 'ya !'
    edge = state.leave(context, line)
    if edge == '----Loopback---->':
        print('.', end='')
    else:
        print('f', end='')
