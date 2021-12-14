from tests.edge_walk.step2n2_man_state.init_this import InitThisState
from tests.edge_walk.step2n2_man_state.init_this_is import InitThisIsState
from tests.edge_walk.step2n2_man_state.init_this_is_a import InitThisIsAState
from tests.edge_walk.step3_man_state.init import DecoratedInitState
from tests.edge_walk.step3_man_state.goal import DecoratedGoalState
from tests.edge_walk.step1_const_conf import A, GOAL, INIT, IS, THIS

state_gen = {
    INIT: {
        "": lambda: DecoratedInitState(),
        THIS: {
            "": lambda: InitThisState(),
            IS: {
                "": lambda: InitThisIsState(),
                A: {
                    "": lambda: InitThisIsAState(),
                },
            },
        },
    },
    GOAL: lambda: DecoratedGoalState(),
}
