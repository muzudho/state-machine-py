from tests.edge_walk.layer1_transition_map.init import InitState


def create():
    """振る舞い生成"""
    return DecoratedInitState()


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_entry(self, req):
        print("READMEを参考にして、エッジを入力してください")
        return super().on_entry(req)
