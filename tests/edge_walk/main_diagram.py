from threading import Thread
from state_machine_py.state_machine import StateMachine

from tests.edge_walk.context import Context
from tests.edge_walk.keywords import INIT
from tests.edge_walk.state_creator_dict import state_creator_dict
from tests.edge_walk.transition_dict import transition_dict


class MainDiagram():
    def __init__(self):
        """初期化"""
        self._state_machine = StateMachine(
            context=Context(),
            state_creator_dict=state_creator_dict,
            transition_dict=transition_dict)

        # デバッグ情報を出力します
        # self._state_machine.verbose = True

        # スレッド
        self._thread1 = None

    def set_up(self):
        """__mainの定型処理"""
        self.init()

    def clean_up(self):
        """__mainの定型処理"""
        pass

    def run(self):
        """入力受付の待機ループをしています"""
        while True:
            # 末尾に改行は付いていません
            line = input()  # ブロックします

            # a way to exit the program
            if line.lower() == 'q':
                # ステートマシンを終了させます
                self._state_machine.terminate()
                break

            # ステートマシーンに渡します
            self._state_machine.input_queue.put(line)

        # 実行中のスレッド１があれば終了するまで待機するのがクリーンです
        if not(self._thread1 is None) and self._thread1.is_alive():
            self._thread1.join()
            self._thread1 = None

    def init(self):
        """ダイアグラムを初期状態に戻します"""

        # スレッド１が起動中に ここを通らないでください

        # スレッド１を開始します
        self._thread1 = Thread(target=self.listen_for_messages, daemon=True)
        # self._thread1.daemon = True
        self._thread1.start()

    def listen_for_messages(self):
        """メインループ"""

        # （強制的に）ステートマシンを初期状態から始めます
        self._state_machine.start(INIT)  # ここでブロック
