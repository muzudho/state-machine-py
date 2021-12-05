from tests.task_sharing.layer1_transition_map.stop import StopState


def create():
    """振る舞い生成"""
    return DecoratedStopState()


class DecoratedStopState(StopState):
    def __init__(self):
        super().__init__()
