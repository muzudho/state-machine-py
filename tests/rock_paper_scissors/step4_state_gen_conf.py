from tests.rock_paper_scissors.step3_man.init import DecoratedInitState
from tests.rock_paper_scissors.step3_man.game import DecoratedGameState
from tests.rock_paper_scissors.step1_const_conf import GAME, INIT

state_gen = {
    INIT: lambda: DecoratedInitState(),
    GAME: lambda: DecoratedGameState(),
}
