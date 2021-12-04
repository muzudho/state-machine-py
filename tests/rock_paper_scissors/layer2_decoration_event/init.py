from layer1_transition_map.init import InitState


def create():
    """振る舞い生成"""
    return DecoratedInitState()


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_entry(self, context):
        """この on_entry メソッドは省略することもできます。
        初期状態に戻す処理を書いてください"""
        # 基底クラスの on_entry には何も書かれていない想定です
        print("Init: 初期状態に戻しました\nYour name: ", end='')

    def on_exit(self, context):
        """この on_exit メソッドは省略することもできます。
        初期状態に戻したあとの処理を書いてください"""
        # 基底クラスの on_exit には何も書かれていない想定です
        print("---- ---- ---- ----")

    def on_logged_in(self, context):
        """この on_logged_in メソッドは省略することもできます。
        ログイン成功時に行いたい処理を書いてください"""
        # on_logged_in の前に処理を書いていただけます
        super().on_logged_in(context)
        # on_logged_in の後に処理を書いていただけます
        print(f"Logged in: {context.user_name} がログインしました")

    def on_failed(self, context):
        """この on_failed メソッドは省略することもできます。
        ログイン失敗時に行いたい処理を書いてください"""
        # on_failed の前に処理を書いていただけます
        super().on_failed(context)
        # on_failed の後に処理を書いていただけます
        print(f"Login fail: ログインに失敗しました")
