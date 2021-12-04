# Edge walk

エッジが階層構造をしていることを説明するためのサンプルです  

![20211205blog3.png](docs/img/20211205blog3.png)  
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
----E_2---->
----E_2_2---->
----E_2_2_2---->
----E_2_2_2_2---->
----E_1---->
```
