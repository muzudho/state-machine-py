from tests.rock_paper_scissors.step2n2_man_state.init import InitState


def create_decorated_init(state):
    def __on_your_name_prompt(req):
        """入力を取る前"""
        # 基底クラスの on_your_name_prompt には何も書かれていない想定です
        print("Init: 初期状態に戻しました\nYour name: ", end="")

    def __on_update(req):
        """この on_update メソッドは省略することもできます。
        初期状態に戻したあとの処理を書いてください

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """

        print("---- ---- ---- ----")

    def __on_logged_in(req):
        """この on_logged_in メソッドは省略することもできます。
        ログイン成功時に行いたい処理を書いてください

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        print(f"Logged in: {req.context.user_name} がログインしました")

    def __on_failed(req):
        """この on_failed メソッドは省略することもできます。
        ログイン失敗時に行いたい処理を書いてください

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        print(f"Login fail: ログインに失敗しました")

    state.on_your_name_prompt = __on_your_name_prompt
    state.on_update = __on_update
    state.on_logged_in = __on_logged_in
    state.on_failed = __on_failed
    return state
