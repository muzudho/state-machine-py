from tests.two_machines_catchball.data.auto_gen.const import INIT

# State
from tests.two_machines_catchball.machine_a.step2n2_man_state.init import InitState

# State wapper
from tests.two_machines_catchball.machine_a.step3_man_state.init import (
    create_init,
)

state_gen = {
    INIT: lambda: create_init(InitState()),
}
