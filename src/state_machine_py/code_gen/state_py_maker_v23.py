import sys
import argparse

from main_finally import MainFinally
from code_gen.state_files_gen_v18 import gen_state_files_v18
from code_gen.json_reader_v17n2 import JsonReaderV17n2

class Main:
    """状態を定義した .pyファイルを作成します

    Examples
    --------
    # Windows
    python.exe -m lesson23.state_py_maker "example-const.json" "example-transition.json" "lesson23_projects.house3n2.data.auto_gen.const" "lesson23/house3n2/auto_gen/states"
    #                                     -------------------- ------------------------- ------------------------------------------------ -----------------------------------
    #                                     定数定義ファイル       状態遷移定義ファイル        import文に書く文字列                              出力ディレクトリ
    """

    def on_main(self):
        parser = argparse.ArgumentParser(description='ステートを定義した .pyファイルを作成します')
        parser.add_argument('input_const', help='定数を定義した入力ファイル(.json)')
        parser.add_argument('input_transition', help='状態遷移を定義した入力ファイル(.json)')
        parser.add_argument('import_module', help='import文に書く文字列')
        parser.add_argument('output', help='状態を定義したファイルを出力するディレクトリ')
        args = parser.parse_args()

        print(f'args.input_const : {args.input_const}') # Example: "lesson18n2_projects/house3/data/const.json"
        print(f'args.input_transition : {args.input_transition}') # Example: "lesson20_projects/house3n2/data/auto_gen/transition3.json"
        print(f'args.import_module : {args.import_module}') # Example: "lesson23_projects.house3n2.data.auto_gen.const"
        print(f'args.output : {args.output}') # Example: "lesson23/house3n2/auto_gen/states"


        # JSONファイルから、定数と遷移の設定を読込みます
        const_json_obj = JsonReaderV17n2.read_file(args.input_const)
        transition_json_obj = JsonReaderV17n2.read_file(args.input_transition)

        # 状態の .py スクリプトを出力します
        gen_state_files_v18(
            dir_path=args.output,
            const_py_dict=const_json_obj,
            transition_py_dict=transition_json_obj,
            import_from_path=args.import_module,
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
