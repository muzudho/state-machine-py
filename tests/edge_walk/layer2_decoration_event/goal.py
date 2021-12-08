from tests.edge_walk.layer1_transition_map.goal import GoalState


class DecoratedGoalState(GoalState):
    def __init__(self):
        super().__init__()
