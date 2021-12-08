from tests.match_server.machine_c.layer1.lobby import LobbyState


class DecoratedLobbyState(LobbyState):
    def __init__(self):
        super().__init__()
