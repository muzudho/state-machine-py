from tests.edge_walk.layer1_transition_map.init import InitState


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_exit(self, req):
        print("READMEを参考にして、エッジを入力してください")
