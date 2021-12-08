from threading import Thread
from state_machine_py.multiple_state_machine import MultipleStateMachine
from tests.rock_paper_scissors.context import Context
from tests.rock_paper_scissors.state_creator_dict import state_creator_dict
from tests.rock_paper_scissors.keywords import INIT, MACHINE_A
from tests.rock_paper_scissors.transition_dict import transition_dict


class MainDiagram():
    def __init__(self):
        """初期化"""
        self._multiple_state_machine = MultipleStateMachine()

        self._state_machine = self._multiple_state_machine.create_machine(
            machine_key=MACHINE_A,
            context=Context(),
            state_creator_dict=state_creator_dict,
            transition_dict=transition_dict)

        # デバッグ情報を出力します
        # self._state_machine.verbose = True

        # 終了フラグ
        self._quit = False

    @property
    def state_machine(self):
        """状態遷移マシン"""
        return self._state_machine

    def set_up(self):
        """初期化（リセット）"""
        self.init()

    def clean_up(self):
        """終了処理"""
        pass

    def run(self):
        """標準入力からの入力を受け取ります"""
        while True:
            # 末尾に改行は付いていません
            line = input()  # ブロックします

            # 'q' と打鍵することで、ステートマシンが実行中でも、ステートマシンを終了させます
            if line.lower() == 'q':
                self._quit = True
                self.state_machine.terminate()
                break

            self.state_machine.input_queue.put(line)

    def init(self):
        """ダイアグラムを初期状態に戻します"""

        # 以降、標準入力をトリガーにして状態を遷移します
        thr = Thread(target=self.listen_for_messages)
        thr.daemon = True
        thr.start()

    def listen_for_messages(self):
        """メインループ"""

        # （強制的に）ステートマシンを初期状態から始めます
        self.state_machine.start(INIT)
