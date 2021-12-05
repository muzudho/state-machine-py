import queue
import time
from threading import Thread
from state_machine_py.state_machine import StateMachine
from state_machine_py.multiple_state_machine import MultipleStateMachine
from tests.task_sharing.keywords import INIT
from tests.task_sharing.machine_a.context import Context as ContextA
from tests.task_sharing.machine_a.state_creator_dict import state_creator_dict as state_creator_dict_a
from tests.task_sharing.machine_a.transition_dict import transition_dict as transition_dict_a
from tests.task_sharing.machine_b.context import Context as ContextB
from tests.task_sharing.machine_b.state_creator_dict import state_creator_dict as state_creator_dict_b
from tests.task_sharing.machine_b.transition_dict import transition_dict as transition_dict_b


class MainDiagram():
    def __init__(self):
        """初期化"""
        self._line_queue = queue.Queue()

        self._multiple_state_machine = MultipleStateMachine()

        def __create_machine_a():
            state_machine = StateMachine(
                context=ContextA(),
                state_creator_dict=state_creator_dict_a,
                transition_dict=transition_dict_a)

            state_machine.verbose = True  # デバッグ情報を出力します
            return state_machine

        def __create_machine_b():
            state_machine = StateMachine(
                context=ContextB(),
                state_creator_dict=state_creator_dict_b,
                transition_dict=transition_dict_b)

            state_machine.verbose = True  # デバッグ情報を出力します
            return state_machine

        self._multiple_state_machine.machines["machine_a"] = __create_machine_a(
        )
        self._multiple_state_machine.machines["machine_b"] = __create_machine_b(
        )

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
        self._multiple_state_machine.machines["machine_a"].context.number = number

        self.init()

        """待機だけしています"""
        while not(self._multiple_state_machine.machines["machine_a"].is_terminate and self._multiple_state_machine.machines["machine_b"].is_terminate):
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
        self._multiple_state_machine.machines["machine_a"].start(INIT)
        self._multiple_state_machine.machines["machine_b"].start(INIT)
