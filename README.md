# state-machine-py

状態遷移マシン

## Install

```shell
# Windows
python.exe -m pip install state_machine_py
```

## Example

📖 [state-machine-py-example](https://github.com/muzudho/state-machine-py-example)  

## Publish

📖 [Pythonスクリプトってどうやってパブリッシュするんだぜ（＾～＾）？](https://crieit.net/drafts/61a3496b73b42)  

```shell
# Build
python.exe -m build

# Upload
# Test
python.exe -m twine upload --repository testpypi dist/* --verbose
# Product
python.exe -m twine upload dist/*

# Install
# Test
python.exe -m pip install --index-url https://test.pypi.org/simple/ --no-deps state_machine_py
                                                                              ----------------
                                                                              YOUR-API-NAME-HERE
```
