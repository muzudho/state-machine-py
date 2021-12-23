from tests.rock_paper_scissors.step1_const_conf import GAME, INIT

# State
from tests.rock_paper_scissors.step2n2_man_state.game import GameState
from tests.rock_paper_scissors.step2n2_man_state.init import InitState

# State wrapper
from tests.rock_paper_scissors.step3_man_sate.init import create_decorated_init
from tests.rock_paper_scissors.step3_man_sate.game import create_decorated_game

state_gen = {
    INIT: lambda: create_decorated_init(InitState()),
    GAME: lambda: create_decorated_game(GameState()),
}
