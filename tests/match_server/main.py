import sys
import signal

from tests.match_server.main_diagram import MainDiagram


def __main():
    """定型処理
    この関数はこの形にし、 MainDiagram クラスの方に処理を書いてください"""

    def sigterm_handler(_signum, _frame) -> None:
        sys.exit(1)

    # 強制終了のシグナルを受け取ったら、強制終了するようにします
    signal.signal(signal.SIGTERM, sigterm_handler)

    # ダイアグラムの初期化
    example_diagram = MainDiagram()
    example_diagram.set_up()

    try:
        # ダイアグラムの実行
        example_diagram.run()

    finally:
        # 強制終了のシグナルを無視するようにしてから、クリーンアップ処理へ進みます
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        example_diagram.clean_up()
        # 強制終了のシグナルを有効に戻します
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)


if __name__ == "__main__":
    """サンプルを実行します"""
    sys.exit(__main())
