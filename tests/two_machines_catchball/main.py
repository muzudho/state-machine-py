import sys
import signal
import argparse

from tests.two_machines_catchball.main_diagram import MainDiagram
from state_machine_py.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from state_machine_py.code_gen.json_reader_v11n100 import JsonReaderV11n100


def __main():
    """定型処理
    この関数はこの形にし、 MainDiagram クラスの方に処理を書いてください"""
    parser = argparse.ArgumentParser(description='設定ファイルを読み込みます')
    parser.add_argument('conf', help='設定ファイルへのパス')
    args = parser.parse_args()

    # 設定ファイル（.toml）読取
    toml_doc = TomlReaderV11n90.read_file(args.conf)

    # TOMLの内容を読み取ります
    machinea_transition_file = toml_doc['machinea_transition_file']
    machineb_transition_file = toml_doc['machineb_transition_file']

    # JSONファイルを読込みます
    machinea_transition_doc = JsonReaderV11n100.read_file(
        machinea_transition_file)
    machineb_transition_doc = JsonReaderV11n100.read_file(
        machineb_transition_file)

    def sigterm_handler(_signum, _frame) -> None:
        sys.exit(1)

    # 強制終了のシグナルを受け取ったら、強制終了するようにします
    signal.signal(signal.SIGTERM, sigterm_handler)

    # ダイアグラムの初期化
    example_diagram = MainDiagram(
        machinea_transition_doc, machineb_transition_doc)
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
