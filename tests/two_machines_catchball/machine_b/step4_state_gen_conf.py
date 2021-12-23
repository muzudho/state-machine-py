from tests.two_machines_catchball.step1_const_conf import INIT

# State
from tests.two_machines_catchball.machine_b.step2n2_man_state.init import InitState

# State wrapper
from tests.two_machines_catchball.machine_b.step3_man_state.init import (
    create_init,
)

state_gen = {
    INIT: lambda: create_init(InitState()),
}
