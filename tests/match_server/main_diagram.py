import time
from threading import Thread
from state_machine_py.multiple_state_machine import MultipleStateMachine

from tests.match_server.keywords import INIT, MACHINE_C, MACHINE_S
from tests.match_server.machine_c.context import Context as ContextC
from tests.match_server.machine_c.state_dict import state_dict as state_dict_c
from tests.match_server.machine_c.transition_dict import transition_dict as transition_dict_c
# from tests.match_server.machine_s.context import Context as ContextB
# from tests.match_server.machine_s.state_gen import state_gen as state_gen_b
# from tests.match_server.machine_s.transition_dict import transition_dict as transition_dict_b


class MainDiagram():
    def __init__(self):
        """初期化"""
        self._multiple_state_machine = MultipleStateMachine()

        machine_a = self._multiple_state_machine.create_machine(
            MACHINE_C,
            context=ContextC(),
            state_gen=state_dict_c,
            transition_dict=transition_dict_c)
        machine_a.verbose = True  # デバッグ情報を出力します

        # machine_b = self._multiple_state_machine.create_machine(
        #     MACHINE_B,
        #     context=ContextB(),
        #     state_gen=state_gen_b,
        #     transition_dict=transition_dict_b)
        # # machine_b.verbose = True  # デバッグ情報を出力します

    def set_up(self):
        """__mainの定型処理"""
        pass

    def clean_up(self):
        """__mainの定型処理"""
        pass

    def run(self):

        # 改行を付けなかったなら、フラッシュを明示します
        print("このサンプルはデモです", end='', flush=True)

        self.init()

        """待機だけしています"""
        while not(self._multiple_state_machine.machines[MACHINE_C].is_terminate):
            # and self._multiple_state_machine.machines[MACHINE_S].is_terminate
            time.sleep(1)

    def init(self):
        """ダイアグラムを初期状態に戻します"""

        # 以降、標準入力をトリガーにして状態を遷移します
        thr_c = Thread(target=self.work_of_machine_c, daemon=True)
        thr_c.start()

        # thr_b = Thread(target=self.work_of_machine_b)
        # thr_b.daemon = True
        # thr_b.start()

    def work_of_machine_c(self):
        # （強制的に）ステートマシンを初期状態から始めます
        self._multiple_state_machine.machines[MACHINE_C].start(INIT)

    # def work_of_machine_b(self):
    #     # （強制的に）ステートマシンを初期状態から始めます
    #     self._multiple_state_machine.machines[MACHINE_B].start(INIT)
