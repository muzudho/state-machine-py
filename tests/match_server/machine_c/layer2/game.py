from tests.match_server.machine_c.layer1.game import GameState


class DecoratedGameState(GameState):
    def __init__(self):
        super().__init__()
