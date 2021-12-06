import queue
import time
from threading import Thread
from state_machine_py.multiple_state_machine import MultipleStateMachine
from tests.two_machines_catchball.keywords import INIT, MACHINE_A, MACHINE_B
from tests.two_machines_catchball.machine_a.context import Context as ContextA
from tests.two_machines_catchball.machine_a.state_creator_dict import state_creator_dict as state_creator_dict_a
from tests.two_machines_catchball.machine_a.transition_dict import transition_dict as transition_dict_a
from tests.two_machines_catchball.machine_b.context import Context as ContextB
from tests.two_machines_catchball.machine_b.state_creator_dict import state_creator_dict as state_creator_dict_b
from tests.two_machines_catchball.machine_b.transition_dict import transition_dict as transition_dict_b


class MainDiagram():
    def __init__(self):
        """初期化"""
        self._multiple_state_machine = MultipleStateMachine()

        machine_a = self._multiple_state_machine.create_machine(
            MACHINE_A,
            context=ContextA(),
            state_creator_dict=state_creator_dict_a,
            transition_dict=transition_dict_a)
        # machine_a.verbose = True  # デバッグ情報を出力します

        machine_b = self._multiple_state_machine.create_machine(
            MACHINE_B,
            context=ContextB(),
            state_creator_dict=state_creator_dict_b,
            transition_dict=transition_dict_b)
        # machine_b.verbose = True  # デバッグ情報を出力します

    def set_up(self):
        """__mainの定型処理"""
        pass

    def clean_up(self):
        """__mainの定型処理"""
        pass

    def run(self):

        # 改行を付けなかったなら、フラッシュを明示します
        print("最初に数字を入力してください:", end='', flush=True)
        line = input()  # ブロックします

        number = int(line)
        # Aさんに数を渡します
        self._multiple_state_machine.machines[MACHINE_A].context.number = number

        self.init()

        """待機だけしています"""
        while not(self._multiple_state_machine.machines[MACHINE_A].is_terminate and self._multiple_state_machine.machines[MACHINE_B].is_terminate):
            time.sleep(1)

    def init(self):
        """ダイアグラムを初期状態に戻します"""

        # 以降、標準入力をトリガーにして状態を遷移します
        thr_a = Thread(target=self.work_of_machine_a)
        thr_a.daemon = True
        thr_a.start()

        thr_b = Thread(target=self.work_of_machine_b)
        thr_b.daemon = True
        thr_b.start()

    def work_of_machine_a(self):
        # （強制的に）ステートマシンを初期状態から始めます
        self._multiple_state_machine.machines[MACHINE_A].start(INIT)

    def work_of_machine_b(self):
        # （強制的に）ステートマシンを初期状態から始めます
        self._multiple_state_machine.machines[MACHINE_B].start(INIT)
