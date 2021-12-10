from tests.edge_walk.layer2_decoration_event.init import DecoratedInitState
from tests.edge_walk.layer2_decoration_event.goal import DecoratedGoalState
from tests.edge_walk.keywords import GOAL, INIT

state_gen = {
    INIT: lambda: DecoratedInitState(),
    GOAL: lambda: DecoratedGoalState(),
}
