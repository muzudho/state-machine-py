from tests.rock_paper_scissors.layer2_decoration_event.init import DecoratedInitState
from tests.rock_paper_scissors.layer2_decoration_event.game import DecoratedGameState
from tests.rock_paper_scissors.keywords import GAME, INIT

state_gen = {
    INIT: lambda: DecoratedInitState(),
    GAME: lambda: DecoratedGameState(),
}
