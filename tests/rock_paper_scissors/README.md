# state-machine-py-example

状態遷移マシン（[state-machine-pyパッケージ](https://pypi.org/project/state-machine-py/)）の使用例（＾～＾）

# Set up

```shell
python.exe -m pip install state_machine_py
```

# Run

```shell
python.exe -m tests.rock_paper_scissors.main
```

# Concept (Layer 1. Transition map)

![20211205blog1a1.png](./docs/img/20211205blog1a1.png)  
👆  

説明１  

* 上図は じゃんけんゲーム の StateMachine（状態遷移マシン） です
* 円は  State（状態） を表しています
* State から別の State に向かって伸びている線を Edge（辺）と呼びます。  
  エッジには向きがあります。また、このプログラムではエッジをツリー状にすることができます

説明２  

* State は、StateMachineの中で一意の名前を持ってください
* Edge は、 Stateの中で一意の名前を持ってください

```python
state_machine = StateMachine(
    context=Context(),
    state_creator_dict=state_creator_dict,
    transition_dict=transition_dict)
```

👆 ステートマシンの生成の説明は長くなるので `main.py` ソースコードを読んでください  

```python
state_machine.start("[Init]")
```

👆 ステートマシンの起動の説明は長くなるので `main.py` ソースコードを読んでください  

* State の名前はソースコード上では（必須ではありませんが）説明のために `[ ]` で囲んでいます

```python
    def run(self):
        """標準入力からの入力を受け取ります"""
        while True:
            # 末尾に改行は付いていません
            line = input()  # ブロックします

            # 'q' と打鍵することで、ステートマシンが実行中でも、ステートマシンを終了させます
            if line.lower() == 'q':
                self._quit = True
                self.state_machine.terminate()
                break

            self.state_machine.input_queue.put(line)
```

👆 ステートマシンに文字を渡す例

```python
from state_machine_py.abstract_state import AbstractState
from context import Context

class InitState(AbstractState):
    # 中略

    def exit(self, context, line, edge_path):

        if line=="LOGIN":
            return '-LoggedIn->'

        return '-Loopback->'
```

👆 遷移する方法は State の exit 時に、次の（下位の）エッジの名前を指定してください  

* Edge の名前はソースコード上では（必須ではありませんが）説明のために `- ->` で囲んでいます

![20211205blog2.png](./docs/img/20211205blog2.png)  
👆

* State と State のつながりは、 `transition_dict` という Dictionary に  
  格納しておきます。  
  ツリー構造になっていて、トップレベルとリーフには State が並びます。  
  その途中は エッジ です。  
* ツリー構造を下りるというのは、現在のエッジ位置のパスを１つ伸ばして　現在のステートへループバックすることと同じです

# Concept (Layer 2. Decoration event)

![20211129blog290a1.png](./docs/img/20211129blog290a1.png)  
👆  

説明１  

* Edge には、任意の名前の `on_xxxx` といったものを いくつでも付けることができます。  
  これは本書では `xxxx` を イベント（Event）、 `on_xxxx` を イベントハンドラ（EventHandler）と呼ぶとします
* `entry()` に紐づく `on_entry()` と、 `exit()` に紐づく `on_exit` だけ最初から用意されています

説明２  

`Layer 1` で状態遷移の実装に注力できるように、それ以外のコードは `Layer 2` に実装してください。  

# Context 変数とは

Context は StateMachine の外部から任意に与えられる変数です。  
このアルゴリズムは Context の中身について関知しません

## 内部実装

# State

```plain
State machine              State
-------------            ---------

    O  Start
    |
    |
 _arrive(next_state_name)
    |
    |
    +--------------------- entry()       // 初期化処理や、CleanUp が主な役割に
                             |           // なるかと思います
                             |
                             |           // 例えば req.intermachine.enqueue_myself("This is a command")
                             |           // を実行すると 自分自身（ステートマシン）の入力キューに
                             |           // 文字列を入力できます
    +------------------------+
    |
    |
    O  entry() で入力キューにコマンドを入れていればそれを実行、
    |  そうでなければ ここで待機ループ
    |
    |
  _leave(line)
    |
    |
    +--------------------- exit()       // 実行したい処理はここに書くことに
                             |          // なるかと思います
                             |
                             |          // 戻り値として 次の（下位の）エッジの名前を
                             |          // 返してください
    +------------------------+
    |
    |
    O  Start (繰り返し)
```
