from tests.rock_paper_scissors.layer2_decoration_event.init import create as create_init
from tests.rock_paper_scissors.layer2_decoration_event.game import create as create_game
from tests.rock_paper_scissors.keywords import GAME, INIT

state_creator_dict = {
    INIT: create_init,  # 初期値
    GAME: create_game
}
