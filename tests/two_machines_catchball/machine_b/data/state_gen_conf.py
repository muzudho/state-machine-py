from tests.two_machines_catchball.auto_gen.data.const import INIT

# State
from tests.two_machines_catchball.machine_b.code.states1.init import InitState

# State wrapper
from tests.two_machines_catchball.machine_b.code.states2.init import (
    create_init,
)

state_gen = {
    INIT: lambda: create_init(InitState()),
}
