# State machines
# --------------

MACHINE_A = "MachineA"

# States
# ------
#
# "ステート定数": "ステートマシン図のノード名"
# 本レッスンではノード名を PascalCase にします（エッジと被らないように）

INIT = "Init"
GAME = "Game"

# Edges
# -----
#
# "エッジ定数": "ステートマシン図のエッジ名"
# 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）
# ディクショナリーのキーとして State と被らないように頭に E_ を付けます

E_LOOPBACK = "loopback"  # 汎用
E_LOGIN = "login"
E_LOSE = "lose"
E_WIN = "win"
E_DRAW = "draw"
