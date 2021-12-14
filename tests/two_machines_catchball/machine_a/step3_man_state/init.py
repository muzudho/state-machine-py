from tests.two_machines_catchball.machine_a.step2n2_man_state.init import InitState


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_update(self, req):
        print(f"[A] number={req.context.number}")
