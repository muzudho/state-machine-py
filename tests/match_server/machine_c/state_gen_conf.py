from tests.match_server.machine_c.layer2.init import DecoratedInitState
from tests.match_server.machine_c.layer2.lobby import DecoratedLobbyState
from tests.match_server.machine_c.layer2.reply import DecoratedReplyState
from tests.match_server.machine_c.layer2.game import DecoratedGameState
from tests.match_server.keywords import GAME, INIT, LOBBY, REPLY

state_gen = {
    INIT: lambda: DecoratedInitState(),
    LOBBY: lambda: DecoratedLobbyState(),
    REPLY: lambda: DecoratedReplyState(),
    GAME: lambda: DecoratedGameState(),
}
