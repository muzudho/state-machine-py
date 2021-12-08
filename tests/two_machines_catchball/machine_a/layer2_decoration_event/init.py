from tests.two_machines_catchball.machine_a.layer1_transition_map.init import InitState


class DecoratedInitState(InitState):
    def __init__(self):
        super().__init__()

    def on_entry(self, req):
        print(f"[A] number={req.context.number}")
