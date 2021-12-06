from tests.two_machines_catchball.machine_a.layer1_transition_map.init import InitState


def create():
    """振る舞い生成"""
    return DecoratedInitState()


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_exit(self, req):
        print(f"[A] number={req.context.number}")
