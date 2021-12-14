from tests.edge_walk.step2n2_man_state.init import InitState


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_prompt(self, req):
        """入力を取る前"""
        print("READMEを参考にして、エッジを入力してください")
