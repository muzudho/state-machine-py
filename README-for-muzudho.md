# Readme myself

## Publish

๐ [Pythonในใฏใชใใใฃใฆใฉใใใฃใฆใใใชใใทใฅใใใใ ใ๏ผ๏ผพ๏ฝ๏ผพ๏ผ๏ผ](https://crieit.net/drafts/61a3496b73b42)  

```shell
# __init__.py ใฏใใฉใซใใผใซๅฅใใฆ็ฝฎใๅฟ่ฆใใใใใใงใใ
# setup.cfg, setup.py ใฎ version ใๆดๆฐใใฆใใ ใใใ

# Build
python.exe -m build

# Upload
# Test
python.exe -m twine upload --repository testpypi dist/* --verbose
# Product
python.exe -m twine upload dist/*

# Install
# Test (1ๅๅคฑๆใใฆใใ2ๅใใใจๆๅใใใใจใใใ)
python.exe -m pip install --index-url https://test.pypi.org/simple/ --no-deps state_machine_py
                                                                              ----------------
                                                                              YOUR-API-NAME-HERE
                                                                                              ==1.0.0
                                                                                              -------
                                                                                              Version
# Product
python.exe -m pip install state_machine_py==18.0.22
#                                           -------
#                                           Please, Latest version
# 1ๅๅคฑๆใใฆใใ๏ผๅใใใจๆๅใใใใจใใใใพใ

# Uninstall
python.exe -m pip uninstall state_machine_py
```

## Documents

๐ [state-machine-py](https://pypi.org/project/state-machine-py/)  
