from tests.rock_paper_scissors.layer1_transition_map.init import InitState


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_your_name_prompt(self, req):
        """入力を取る前"""
        # 基底クラスの on_your_name_prompt には何も書かれていない想定です
        print("Init: 初期状態に戻しました\nYour name: ", end='')

    def on_entry(self, req):
        """この on_entry メソッドは省略することもできます。
        初期状態に戻したあとの処理を書いてください

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """

        print("---- ---- ---- ----")

    def on_logged_in(self, req):
        """この on_logged_in メソッドは省略することもできます。
        ログイン成功時に行いたい処理を書いてください

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        # on_logged_in の前に処理を書いていただけます
        super().on_logged_in(req)
        # on_logged_in の後に処理を書いていただけます
        print(f"Logged in: {req.context.user_name} がログインしました")

    def on_failed(self, req):
        """この on_failed メソッドは省略することもできます。
        ログイン失敗時に行いたい処理を書いてください

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        # on_failed の前に処理を書いていただけます
        super().on_failed(req)
        # on_failed の後に処理を書いていただけます
        print(f"Login fail: ログインに失敗しました")
