from tests.task_sharing.machine_b.layer1_transition_map.init import InitState


def create():
    """振る舞い生成"""
    return DecoratedInitState()


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_exit(self, req):
        print(f"[B] number={req.context.number}")
