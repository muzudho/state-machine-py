from threading import Thread
from state_machine_py.multiple_state_machine import MultipleStateMachine
from tests.edge_walk.context import Context
from tests.edge_walk.data.auto_gen.const import INIT, MACHINE_A
from tests.edge_walk.step4_state_gen_conf import state_gen
from tests.edge_walk.step2_transition_conf import transition


class MainDiagram():
    def __init__(self):
        """初期化"""
        self._multiple_state_machine = MultipleStateMachine()

        self._state_machine = self._multiple_state_machine.create_machine(
            machine_key=MACHINE_A,
            context=Context(),
            state_gen=state_gen,
            transition=transition)

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

        def SplitTextBlock(text_block):
            """受信したテキストブロックを行の配列にして返します"""
            lines = text_block.split('\n')

            # 例えば 'abc\n' を '\n' でスプリットすると 'abc' と '' になって、
            # 最後に空文字列ができます。これは無視します
            if lines[len(lines)-1] == '':
                lines = lines[:-1]

            return lines

        is_quit = False

        """入力受付の待機ループをしています"""
        while True:
            # 末尾に改行は付いていません
            text_block = input()  # ブロックします

            lines = SplitTextBlock(text_block)

            for line in lines:

                # `#` で始まる行はコメントとして無視します
                if line.startswith('#'):
                    pass

                # a way to exit the program
                # （ステートマシンが動いている最中でも割り込んで）ステートマシンを終了させます
                elif line.lower() == 'q':
                    self._state_machine.terminate()
                    is_quit = True
                    print("[Work] Break 1")
                    break

                # ステートマシーンに渡します
                else:
                    self._state_machine.input_queue.put(line)

            if is_quit:
                print("[Work] Break 2")
                break

        print("[Work] After loop")

        # 実行中のスレッド１があれば終了するまで待機するのがクリーンです
        if not(self._thread1 is None) and self._thread1.is_alive():
            print("[Work] Before join")
            self._thread1.join()
            print("[Work] After join")
            self._thread1 = None

        print("[Work] Run finished")

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
        self._state_machine.start([INIT])  # ここでブロック
