from tests.two_machines_catchball.machine_b.step2n2_man_state.init import InitState


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_update(self, req):
        print(f"[B] number={req.context.number}")
