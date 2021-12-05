# Readme for me

# Set up

```shell
cd tests/edge_walk

# Test
python.exe -m pip install --index-url https://test.pypi.org/simple/ --no-deps state_machine_py

# Product
python.exe -m pip install state_machine_py
```

# Run

```shell
# cd tests/edge_walk

python.exe -m main
```

このサンプルでは行ごとのコマンド入力なので、複数行を同時に貼り付けても処理してくれます。  

Input:  

```
-this->
-is->
-a->
-pen->
-ok->
q
```
