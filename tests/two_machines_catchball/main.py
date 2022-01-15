import sys
import signal
import argparse

from state_machine_py.main_finally import MainFinally
from tests.two_machines_catchball.main_diagram import MainDiagram
from state_machine_py.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from state_machine_py.code_gen.json_reader_v11n100 import JsonReaderV11n100


class Main():
    def __init__(self):
        self.__diagram = None

    def on_main(self):
        """ここで通常の処理
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

        # ダイアグラムの初期化
        self.__diagram = MainDiagram(
            machinea_transition_doc, machineb_transition_doc)
        self.__diagram.set_up()
        # ダイアグラムの実行
        self.__diagram.run()

    def on_finally(self):
        # ここで終了処理
        self.__diagram.clean_up()
        return 1


if __name__ == "__main__":
    """サンプルを実行します"""
    sys.exit(MainFinally.run(Main()))
