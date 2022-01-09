from tests.two_machines_catchball.data.auto_gen.const import INIT, E_DECREASE, E_STOP

transition = {
    INIT: {
        E_DECREASE: [INIT],
        E_STOP: None,
    },
}
