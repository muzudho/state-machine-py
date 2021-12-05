# Edge walk

エッジが木構造をしていることを説明するためのサンプルです  

![20211205blog3a1.png](docs/img/20211205blog3a1.png)  
👆  
従来の 状態遷移マシンの構造に比べて、エッジの途中に 疑似の状態 がある感じです。  
エッジのパスを更新しながらループバックしているのと同じです。  

# Set up

```shell
cd tests/edge_walk

# Product
python.exe -m pip install state_machine_py
```

# Run

```shell
# cd tests/edge_walk

python.exe -m main
```

Input:  

```
-this->
-is->
-a->
-pen->
-ok->
```
