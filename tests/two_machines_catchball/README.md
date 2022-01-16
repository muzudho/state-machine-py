# two_machines_catchbal

異なるプログラム Aさんと Bさんが うまく連携することを示します。  

![20211205blog4a2.png](docs/img/20211205blog4a2.png)  

```plain
Aさん: 渡されたボールに奇数なら書かれていたら 3倍して1を加えた数に書き直します
      1 が書かれていたら処理を終了します
      どちらにしろ Bさんにボールを投げ返します

Bさん: 渡されたボールに偶数が書かれていたら 2で割った数に書き直します
      1 が書かれていたら処理を終了します
      どちらにしろ Aさんにボールを投げ返します

ボールをキャッチしてくれる人がいなければ このプログラムは終了します
```

# Set up

```shell
python.exe -m pip install state_machine_py
```

## Auto generation

定義ファイルの自動生成

```shell
# Windows
python.exe -m state_machine_py.const_py_maker "tests/two_machines_catchball/data/const.json" "tests/two_machines_catchball/auto_gen/data/const.py"
#                                             ---------------------------------------------- -----------------------------------------------------
#                                             Input (.json)                                   Output (.py)
```

状態遷移図の自動生成:  

```shell
python.exe -m state_machine_py.graph_generator "tests/two_machines_catchball/conf.toml" "machinea_transition_file" "machinea_output_graph_text_file"
python.exe -m state_machine_py.graph_generator "tests/two_machines_catchball/conf.toml" "machineb_transition_file" "machineb_output_graph_text_file"
#                                              ---------------------------------------- -------------------------- ---------------------------------
#                                              1.                                       2.                         3.
# 1. 設定ファイル（TOML形式）
# 2. 入力ファイル（JSON形式）を指すプロパティの名前
# 3. 出力ファイル（テキストファイル形式）を指すプロパティの名前
```

# Run

```shell
python.exe -m tests.two_machines_catchball.main "tests/two_machines_catchball/conf.toml"
#                                               ----------------------------------------
#                                               設定ファイル（.toml）
```

Input 1:

```plain
6
```

Input 2:

```plain
27
```
