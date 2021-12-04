from layer1_transition_map.game import GameState


def create():
    """振る舞い生成"""
    return DecoratedGameState()


class DecoratedGameState(GameState):
    def __init__(self):
        super().__init__()

    def entry(self, context):
        """この entry メソッドは省略することもできます。
        この状態に入ったときにする処理を書いてください"""
        # entry の前に処理を書いていただけます
        super().entry(context)
        # entry の後に処理を書いていただけます
        print("Rock-paper-scissors(R,P,S): ", end='')

        # 次の state_machine.leave(...) に渡す line 引数を返すこともできます
        return None

    def exit(self, context):
        """この exit メソッドは省略することもできます。
        この状態から出たときにする処理を書いてください。
        ステートマシンが中断されたときは省略されます"""
        # exit の前に処理を書いていただけます
        super().exit(context)
        # exit の後に処理を書いていただけます

    def on_win(self, context):
        """この on_win メソッドは省略することもできます。
        Win辺"""
        # on_win の前に処理を書いていただけます
        super().on_win(context)
        # on_win の後に処理を書いていただけます
        print("""+-----------------+
| Win: 勝ちました |
+-----------------+""")

    def on_draw(self, context):
        """この on_draw メソッドは省略することもできます。
        Draw辺"""
        # on_draw の前に処理を書いていただけます
        super().on_draw(context)
        # on_draw の後に処理を書いていただけます
        print("""+----------------------+
| Draw: 引き分けました |
+----------------------+""")

    def on_lose(self, context):
        """この on_lose メソッドは省略することもできます。
        Lose辺"""
        # on_lose の前に処理を書いていただけます
        super().on_lose(context)
        # on_lose の後に処理を書いていただけます
        print("""+------------------+
| Lose: 負けました |
+------------------+""")

    def on_loopback(self, context):
        """この on_loopback メソッドは省略することもできます。
        Looback辺"""
        # on_loopback の前に処理を書いていただけます
        super().on_loopback(context)
        # on_loopback の後に処理を書いていただけます
        print("""+--------------------+
| NoGame: やりなおし |
+--------------------+""")
