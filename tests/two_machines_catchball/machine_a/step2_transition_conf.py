from tests.two_machines_catchball.step1_const_conf import INIT, E_INCREASE, E_STOP

transition = {
    INIT: {
        E_INCREASE: [INIT],
        E_STOP: None,
    },
}
