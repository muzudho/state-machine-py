from tests.rock_paper_scissors.layer1_transition_map.game import GameState


def create():
    """振る舞い生成"""
    return DecoratedGameState()


class DecoratedGameState(GameState):
    def __init__(self):
        super().__init__()

    def on_entry(self, req):
        """この on_entry メソッドは省略することもできます。
        この状態に入ったときにする処理を書いてください

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        # on_entry の前に処理を書いていただけます
        super().on_entry(req)
        # on_entry の後に処理を書いていただけます

        # 改行を出力しないとフラッシュされませんので、明示的にフラッシュします
        print("Rock-paper-scissors(R,P,S): ", end='', flush=True)

    def on_exit(self, req):
        """この on_exit メソッドは省略することもできます。
        この状態から出たときにする処理を書いてください。
        ステートマシンが中断されたときは省略されます

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        # print("[RPS]L2 Begin on_exit")
        # on_exit の前に処理を書いていただけます
        super().on_exit(req)
        # on_exit の後に処理を書いていただけます

    def on_win(self, req):
        """この on_win メソッドは省略することもできます。
        Win辺

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        # on_win の前に処理を書いていただけます
        super().on_win(req)
        # on_win の後に処理を書いていただけます
        print("""+-----------------+
| Win: 勝ちました |
+-----------------+""")

    def on_draw(self, req):
        """この on_draw メソッドは省略することもできます。
        Draw辺

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        # on_draw の前に処理を書いていただけます
        super().on_draw(req)
        # on_draw の後に処理を書いていただけます
        print("""+----------------------+
| Draw: 引き分けました |
+----------------------+""")

    def on_lose(self, req):
        """この on_lose メソッドは省略することもできます。
        Lose辺

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        # on_lose の前に処理を書いていただけます
        super().on_lose(req)
        # on_lose の後に処理を書いていただけます
        print("""+------------------+
| Lose: 負けました |
+------------------+""")

    def on_loopback(self, req):
        """この on_loopback メソッドは省略することもできます。
        Looback辺

        Parameters
        ----------
        req : Request
            ステートマシンからステートへ与えられる引数のまとまり
        """
        # on_loopback の前に処理を書いていただけます
        super().on_loopback(req)
        # on_loopback の後に処理を書いていただけます
        print("""+--------------------+
| NoGame: やりなおし |
+--------------------+""")
