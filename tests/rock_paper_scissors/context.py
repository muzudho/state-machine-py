class Context():
    """ステートマシンは、このContextが何なのか知りません。
    外部から任意に与えることができる変数です"""

    def __init__(self):
        self._user_name = ""

    @property
    def user_name(self):
        """ログインユーザー名"""
        return self._user_name

    @user_name.setter
    def user_name(self, val):
        self._user_name = val
