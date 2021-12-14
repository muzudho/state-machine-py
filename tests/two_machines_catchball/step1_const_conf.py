# State machines
# --------------

MACHINE_A = "[[MachineA]]"
MACHINE_B = "[[MachineB]]"

# States
# ------
#
# "ステート定数": "ステートマシン図のノード名"
# 本レッスンではノード名を PascalCase にします（エッジと被らないように）

INIT = "Init"

# Edges
# -----
#
# "エッジ定数": "ステートマシン図のエッジ名"
# 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）
# ディクショナリーのキーとして State と被らないように頭に E_ を付けます

E_STOP = "stop"
E_INCREASE = "increase"
E_DECREASE = "decrease"
