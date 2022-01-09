import sys
from tests.rock_paper_scissors.main_diagram import MainDiagram
from state_machine_py.main_finally import MainFinally


class Main():
    def __init__(self):
        self.__diagram = None

    def on_main(self):
        """ここで通常の処理"""

        # ダイアグラムの初期化
        self.__diagram = MainDiagram()
        self.__diagram.set_up()

        # ダイアグラムの実行
        self.__diagram.run()
        return 0

    def on_finally(self):
        # ここで終了処理
        self.__diagram.clean_up()
        return 1


if __name__ == "__main__":
    """サンプルを実行します"""
    sys.exit(MainFinally.run(Main()))
