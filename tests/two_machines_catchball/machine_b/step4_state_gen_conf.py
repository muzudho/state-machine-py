from tests.two_machines_catchball.auto_gen.data.const import INIT

# State
from tests.two_machines_catchball.machine_b.step2n2_man_state.init import InitState

# State wrapper
from tests.two_machines_catchball.machine_b.step3_man_state.init import (
    create_init,
)

state_gen = {
    INIT: lambda: create_init(InitState()),
}
