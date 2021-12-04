from layer2_decoration_event.init import create as create_init
from layer2_decoration_event.game import create as create_game

state_creator_dict = {
    "[Init]": create_init,  # 初期値
    "[Game]": create_game
}
