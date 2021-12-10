from tests.two_machines_catchball.machine_b.layer2_decoration_event.init import DecoratedInitState
from tests.two_machines_catchball.keywords import INIT

state_gen = {
    INIT: lambda: DecoratedInitState(),
}
