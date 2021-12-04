import re
from state_machine_py.abstract_state import AbstractState
from context import Context


class GoalState(AbstractState):
    """Goal状態"""

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return "[Goal]"

    def exit(self, context, line, edge_path):
        """次の辺の名前を返します
        Parameters
        ----------
        context : Context
            このステートマシンは、このContextが何なのか知りません。
            外部から任意に与えることができる変数です。 Defaults to None.
        line : str
            コマンドライン文字列

        Returns
        -------
        str
            辺の名前
        """

        # 現在位置の表示
        edge_path_str = '.'.join(edge_path)
        print(f"[Walk] Current state={self.name} edge_path={edge_path_str}")

        next_edge_name = line
        return next_edge_name
