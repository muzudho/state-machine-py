# Edge walk

エッジが木構造をしていることを説明するためのサンプルです  

![20211205blog3a1.png](docs/img/20211205blog3a1.png)  
👆  
従来の 状態遷移マシンの構造に比べて、エッジの途中に 疑似の状態 がある感じです。  
エッジのパスを更新しながらループバックしているのと同じです。  

# Set up

```shell
python.exe -m pip install state_machine_py
```

# Run

```shell
python.exe -m tests.edge_walk.main
```

👇複数行を一気に貼り付けても動きます（ FIXME 入力が速すぎてエラーになる？）。  

Input:  

```
-this->
-is->
-a->
-pen->
-ok->
q
```

Version 9.0.7 から exit(...)の返り値（エッジ）に空文字列を指定することで **踏みとどまり** を表現できるようになりました。  
