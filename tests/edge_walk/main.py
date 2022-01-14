import sys
import argparse

from state_machine_py.main_finally import MainFinally
from state_machine_py.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from state_machine_py.code_gen.json_reader_v11n100 import JsonReaderV11n100
from tests.edge_walk.main_diagram import MainDiagram


class Main():
    def __init__(self):
        self.__diagram = None

    def on_main(self):
        """定型処理
        この関数はこの形にし、Exampleクラスの方に処理を書いてください"""
        parser = argparse.ArgumentParser(description='設定ファイルを読み込みます')
        parser.add_argument('conf', help='設定ファイルへのパス')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        toml_doc = TomlReaderV11n90.read_file(args.conf)

        # TOMLの内容を読み取ります
        transition_file_path = toml_doc['transition_file']

        # JSONファイルを読込みます
        transition_doc = JsonReaderV11n100.read_file(
            transition_file_path)

        # ダイアグラムの初期化
        self.__diagram = MainDiagram(transition_doc)
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
