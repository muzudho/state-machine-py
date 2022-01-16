import re

from tests.rock_paper_scissors.auto_gen.data.const import E_LOGIN, E_LOOPBACK, INIT

"""ログイン
    kifuwarabe
    ----------
    1. username (1-32 characters)
    """
__user_name_pattern = re.compile(r"^([0-9A-Za-z_-]{1,32})$")


def create_init(state):
    def __on_entry(req):
        """入力を取る前"""
        # 基底クラスの on_your_name_prompt には何も書かれていない想定です
        print("Init: 初期状態に戻しました\nYour name: ", end="")

    def __on_trigger(req):
        msg = req.intermachine.dequeue_myself()

        matched = __user_name_pattern.match(msg)
        if matched:
            req.context.user_name = matched.group(1)
            return E_LOGIN

        return E_LOOPBACK

    def __on_logged_in(req):
        """この on_logged_in メソッドは省略することもできます。
        ログイン成功時に行いたい処理を書いてください

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        print(f"""---- ---- ---- ----
Logged in: {req.context.user_name} がログインしました""")

    def __on_loopback(req):
        """この on_loopback メソッドは省略することもできます。
        ログイン失敗時に行いたい処理を書いてください

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        print(f"""---- ---- ---- ----
Login fail: ログインに失敗しました""")

    state.on_entry = __on_entry
    state.on_trigger = __on_trigger
    state.on_logged_in = __on_logged_in
    state.on_loopback = __on_loopback
    return state
