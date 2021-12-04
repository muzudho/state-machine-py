from layer1_transition_map.goal import GoalState


def create():
    """振る舞い生成"""
    return DecoratedGoalState()


class DecoratedGoalState(GoalState):
    def __init__(self):
        super().__init__()
