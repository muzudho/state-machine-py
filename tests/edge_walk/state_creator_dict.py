from layer2_decoration_event.init import create as create_init
from layer2_decoration_event.goal import create as create_goal

state_creator_dict = {
    "[Init]": create_init,  # 初期値
    "[Goal]": create_goal,
}
