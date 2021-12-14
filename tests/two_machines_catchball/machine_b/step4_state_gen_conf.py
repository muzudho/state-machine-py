from tests.two_machines_catchball.machine_b.step3_man_state.init import (
    DecoratedInitState,
)
from tests.two_machines_catchball.step1_const_conf import INIT

state_gen = {
    INIT: lambda: DecoratedInitState(),
}
