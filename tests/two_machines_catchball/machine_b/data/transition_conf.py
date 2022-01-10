from tests.two_machines_catchball.auto_gen.data.const import INIT, E_DECREASE, E_STOP

transition = {
    INIT: {
        E_DECREASE: [INIT],
        E_STOP: None,
    },
}
