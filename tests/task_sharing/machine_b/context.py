class Context():
    """ステートマシンは、このContextが何なのか知りません。
    外部から任意に与えることができる変数です"""

    def __init__(self):
        self._number = None

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, val):
        self._number = val
