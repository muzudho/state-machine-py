import time
from state_machine_py.abstract_state import AbstractState
from tests.match_server.keywords import E_LOGIN, INIT


class InitState(AbstractState):

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return INIT

    def entry(self, req):
        edge_path = "/".join(req.edge_path)
        print(f"[Entry] edge_path={edge_path}")

        if edge_path == "":
            print("ログインします")
            req.intermachine.put_myself("Login my_name")
            return

        elif edge_path == f"{E_LOGIN}":
            # TODO サーバーからの Ok か Incorrect かのメッセージを待っています
            print("サーバーからの Ok か Incorrect かのメッセージを待っています")
            while True:
                # TODO ここでキューからメッセージを取得したい
                time.sleep(3)

        else:
            raise ValueError(f"Invalid edge_path={edge_path}")

        return None

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

        edge_path = "/".join(req.edge_path)
        print(f"[Exit] edge_path={edge_path}")

        if edge_path == "":
            # TODO サーバーへログインします
            print("サーバーへログインします")
            self.on_login(req)
            return E_LOGIN

        elif edge_path == f"{E_LOGIN}":
            # TODO サーバーからの Ok か Incorrect かのメッセージを待っています
            print("サーバーからの Ok か Incorrect かのメッセージを待っています")
            while True:
                # TODO ここでキューからメッセージを取得したい
                time.sleep(3)

        else:
            raise ValueError(f"Invalid edge_path={edge_path}")

    def on_login(self, req):
        """ログイン時"""
        pass
