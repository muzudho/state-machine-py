from tests.edge_walk.auto_gen.data.const import A, GOAL, INIT, IS, THIS

# State
from tests.edge_walk.code.states1.goal import GoalState
from tests.edge_walk.code.states1.init import InitState
from tests.edge_walk.code.states1.init_this import InitThisState
from tests.edge_walk.code.states1.init_this_is import InitThisIsState
from tests.edge_walk.code.states1.init_this_is_a import InitThisIsAState

# State wrapper
from tests.edge_walk.code.states2.goal import create_goal
from tests.edge_walk.code.states2.init_this_is_a import create_init_this_is_a
from tests.edge_walk.code.states2.init_this_is import create_init_this_is
from tests.edge_walk.code.states2.init_this import create_init_this
from tests.edge_walk.code.states2.init import create_init

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
