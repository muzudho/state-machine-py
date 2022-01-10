import time
from threading import Thread
from state_machine_py.multiple_state_machine import MultipleStateMachine
from tests.two_machines_catchball.auto_gen.data.const import INIT, MACHINE_A, MACHINE_B
from tests.two_machines_catchball.machine_a.context import Context as ContextA
from tests.two_machines_catchball.machine_a.data.state_gen_conf import (
    state_gen as state_gen_a,
)
from tests.two_machines_catchball.machine_a.data.transition_conf import (
    transition as transition_a,
)
from tests.two_machines_catchball.machine_b.context import Context as ContextB
from tests.two_machines_catchball.machine_b.data.state_gen_conf import (
    state_gen as state_gen_b,
)
from tests.two_machines_catchball.machine_b.data.transition_conf import (
    transition as transition_b,
)


class MainDiagram:
    def __init__(self):
        """初期化"""
        self._multiple_state_machine = MultipleStateMachine()

        machine_a = self._multiple_state_machine.create_machine(
            MACHINE_A,
            context=ContextA(),
            state_gen=state_gen_a,
            transition=transition_a,
        )
        # machine_a.verbose = True  # デバッグ情報を出力します

        machine_b = self._multiple_state_machine.create_machine(
            MACHINE_B,
            context=ContextB(),
            state_gen=state_gen_b,
            transition=transition_b,
        )
        # machine_b.verbose = True  # デバッグ情報を出力します

    def set_up(self):
        """__mainの定型処理"""
        pass

    def clean_up(self):
        """__mainの定型処理"""
        pass

    def run(self):

        # 改行を付けなかったなら、フラッシュを明示します
        print("最初に数字を入力してください:", end="", flush=True)
        line = input()  # ブロックします

        number = int(line)
        # Aさんに数を渡します
        self._multiple_state_machine.machines[MACHINE_A].context.number = number

        self.init()

        """待機だけしています"""
        while not (
            self._multiple_state_machine.machines[MACHINE_A].is_terminate
            and self._multiple_state_machine.machines[MACHINE_B].is_terminate
        ):
            time.sleep(0)

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
        self._multiple_state_machine.machines[MACHINE_A].start([INIT])

    def work_of_machine_b(self):
        # （強制的に）ステートマシンを初期状態から始めます
        self._multiple_state_machine.machines[MACHINE_B].start([INIT])
