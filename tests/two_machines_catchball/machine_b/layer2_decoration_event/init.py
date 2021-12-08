from tests.two_machines_catchball.machine_b.layer1_transition_map.init import InitState


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_exit(self, req):
        print(f"[B] number={req.context.number}")
