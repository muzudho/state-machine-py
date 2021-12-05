import re
from state_machine_py.abstract_state import AbstractState
from state_machine_py.request import Request
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

    def on_logged_in(self, req):
        """ログイン成功時"""
        pass

    def on_failed(self, req):
        """ログイン失敗時"""
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

        matched = self._user_name_pattern.match(req.line)
        if matched:
            req.context.user_name = matched.group(1)

            self.on_logged_in(req)
            return '----LoggedIn---->'

        self.on_failed(req)
        return '----Loopback---->'


# Test
# python.exe -m layer1_transition_map.init
if __name__ == "__main__":
    context = Context()
    state = InitState()

    line = 'kifuwarabe'
    req = Request(context, line, [])
    edge = state.exit(req)
    if edge == '----LoggedIn---->':
        print('.', end='')
    else:
        print('f', end='')

    line = 'ya !'
    req = Request(context, line, [])
    edge = state.exit(req)
    if edge == '----Loopback---->':
        print('.', end='')
    else:
        print('f', end='')
