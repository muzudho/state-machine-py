from tests.two_machines_catchball.data.auto_gen.const import INIT, E_INCREASE, E_STOP

transition = {
    INIT: {
        E_INCREASE: [INIT],
        E_STOP: None,
    },
}
