import sys
import signal
from threading import Thread
import time
from state_machine_py.state_machine import StateMachine
from context import Context
from state_creator_dict import state_creator_dict
from transition_dict import transition_dict


class ExampleDiagram():
    def __init__(self):
        """初期化"""
        self._state_machine = StateMachine(
            context=Context(),
            state_creator_dict=state_creator_dict,
            transition_dict=transition_dict)

        def __lines_getter():
            # 末尾に改行は付いていません
            line = input()

            # a way to exit the program
            if line.lower() == 'q':
                self._quit = True
                return None

            return [line]

        self.state_machine.lines_getter = __lines_getter

        # デバッグ情報を出力します
        self._state_machine.verbose = True

        # 終了フラグ
        self._quit = False

    @property
    def state_machine(self):
        """状態遷移マシン"""
        return self._state_machine

    def set_up(self):
        """__mainの定型処理"""
        self.init()

    def clean_up(self):
        """__mainの定型処理"""
        pass

    def run(self):
        """待機だけしています"""
        while not self._quit:
            time.sleep(1)

    def init(self):
        """ダイアグラムを初期状態に戻します"""

        # 以降、標準入力をトリガーにして状態を遷移します
        thr = Thread(target=self.listen_for_messages)
        thr.daemon = True
        thr.start()

    def listen_for_messages(self):
        """メインループ"""

        # （強制的に）ステートマシンを初期状態から始めます
        self.state_machine.start("[Init]")


def __main():
    """定型処理
    この関数はこの形にし、Exampleクラスの方に処理を書いてください"""

    def sigterm_handler(_signum, _frame) -> None:
        sys.exit(1)

    # 強制終了のシグナルを受け取ったら、強制終了するようにします
    signal.signal(signal.SIGTERM, sigterm_handler)

    example_diagram = ExampleDiagram()
    example_diagram.set_up()

    try:
        example_diagram.run()

    finally:
        # 強制終了のシグナルを無視するようにしてから、クリーンアップ処理へ進みます
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        example_diagram.clean_up()
        # 強制終了のシグナルを有効に戻します
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)


# Test
# python.exe -m main
if __name__ == "__main__":
    """サンプルを実行します"""
    sys.exit(__main())
