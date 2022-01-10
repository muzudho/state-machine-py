def create_init(state):
    def __on_entry(req):
        """入力を取る前"""
        # 基底クラスの on_your_name_prompt には何も書かれていない想定です
        print("Init: 初期状態に戻しました\nYour name: ", end="")

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

    def __on_failed(req):
        """この on_failed メソッドは省略することもできます。
        ログイン失敗時に行いたい処理を書いてください

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        print(f"""---- ---- ---- ----
Login fail: ログインに失敗しました""")

    state.on_entry = __on_entry
    state.on_logged_in = __on_logged_in
    state.on_failed = __on_failed
    return state
