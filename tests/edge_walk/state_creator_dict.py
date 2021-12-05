from tests.edge_walk.layer2_decoration_event.init import create as create_init
from tests.edge_walk.layer2_decoration_event.goal import create as create_goal
from tests.edge_walk.keywords import GOAL, INIT

state_creator_dict = {
    INIT: create_init,  # 初期値
    GOAL: create_goal,
}
