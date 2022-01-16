from tests.rock_paper_scissors.auto_gen.data.const import GAME, INIT

# State
from tests.rock_paper_scissors.auto_gen.code.states1.game import GameState
from tests.rock_paper_scissors.auto_gen.code.states1.init import InitState

# State wrapper
from tests.rock_paper_scissors.code.states2.init import create_init
from tests.rock_paper_scissors.code.states2.game import create_game

state_gen = {
    INIT: lambda: create_init(InitState()),
    GAME: lambda: create_game(GameState()),
}
