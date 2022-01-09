from tests.edge_walk.data.auto_gen.const import A, GOAL, INIT, IS, THIS

# State
from tests.edge_walk.step2n2_man_state.goal import GoalState
from tests.edge_walk.step2n2_man_state.init import InitState
from tests.edge_walk.step2n2_man_state.init_this import InitThisState
from tests.edge_walk.step2n2_man_state.init_this_is import InitThisIsState
from tests.edge_walk.step2n2_man_state.init_this_is_a import InitThisIsAState

# State wrapper
from tests.edge_walk.step3_man_state.goal import create_goal
from tests.edge_walk.step3_man_state.init_this_is_a import create_init_this_is_a
from tests.edge_walk.step3_man_state.init_this_is import create_init_this_is
from tests.edge_walk.step3_man_state.init_this import create_init_this
from tests.edge_walk.step3_man_state.init import create_init

state_gen = {
    INIT: {
        "": lambda: create_init(InitState()),
        THIS: {
            "": lambda: create_init_this(InitThisState()),
            IS: {
                "": lambda: create_init_this_is(InitThisIsState()),
                A: {
                    "": lambda: create_init_this_is_a(InitThisIsAState()),
                },
            },
        },
    },
    GOAL: lambda: create_goal(GoalState()),
}
