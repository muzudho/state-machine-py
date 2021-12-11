from tests.edge_walk.layer1_transition_map.init_this import InitThisState
from tests.edge_walk.layer1_transition_map.init_this_is import InitThisIsState
from tests.edge_walk.layer1_transition_map.init_this_is_a import InitThisIsAState
from tests.edge_walk.layer2_decoration_event.init import DecoratedInitState
from tests.edge_walk.layer2_decoration_event.goal import DecoratedGoalState
from tests.edge_walk.keywords import A, GOAL, INIT, IS, THIS

state_gen = {
    INIT: {
        "": lambda: DecoratedInitState(),
        THIS: {
            "": lambda: InitThisState(),
            IS: {
                "": lambda: InitThisIsState(),
                A: {
                    "": lambda: InitThisIsAState(),
                }
            }
        }
    },
    GOAL: lambda: DecoratedGoalState(),
}
