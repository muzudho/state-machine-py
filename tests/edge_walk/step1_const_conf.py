# State machines
# --------------

MACHINE_A = "MachineA"

# States
# ------
#
# "ステート定数": "ステートマシン図のノード名"
# 本レッスンではノード名を PascalCase にします（エッジと被らないように）

INIT = "Init"
THIS = "This"
IS = "Is"
A = "A"
GOAL = "Goal"

# Edges
# -----
#
# "エッジ定数": "ステートマシン図のエッジ名"
# 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）
# ディクショナリーのキーとして State と被らないように頭に E_ を付けます

E_LOOPBACK = ""  # ループバックは空文字列
E_THAT = "that"
E_THIS = "this"
E_WAS = "was"
E_IS = "is"
E_AN = "an"
E_A = "a"
E_PIN = "pin"
E_PEN = "pen"
E_RETRY = "retry"
