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

Input:  

```
----E_2---->
----E_2_2---->
----E_2_2_2---->
----E_2_2_2_2---->
----E_1---->
```
