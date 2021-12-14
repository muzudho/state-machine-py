# State machines

MACHINE_A = "MachineA"

# States
# ------
#
# ディクショナリーのキーとして Edge と被らないように PascalCase にします

INIT = "Init"
if INIT:  # インデントを付けてるだけ
    THIS = "This"
    if THIS:
        IS = "Is"
        if IS:
            A = "A"

GOAL = "Goal"

# Edges
# -----
#
# ディクショナリーのキーとして State と被らないように頭に snake_case にします

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
