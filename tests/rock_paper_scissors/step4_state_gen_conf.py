from tests.rock_paper_scissors.auto_gen.data.const import GAME, INIT

# State
from tests.rock_paper_scissors.step2n2_man_state.game import GameState
from tests.rock_paper_scissors.step2n2_man_state.init import InitState

# State wrapper
from tests.rock_paper_scissors.step3_man_sate.init import create_init
from tests.rock_paper_scissors.step3_man_sate.game import create_game

state_gen = {
    INIT: lambda: create_init(InitState()),
    GAME: lambda: create_game(GameState()),
}
