from tests.match_server.machine_c.layer1.init import InitState


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_login(self, req):
        print(f"[C] Login")
