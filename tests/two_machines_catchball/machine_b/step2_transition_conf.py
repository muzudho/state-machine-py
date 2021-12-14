from tests.two_machines_catchball.step1_const_conf import INIT, E_DECREASE, E_STOP

transition = {
    INIT: {
        E_DECREASE: [INIT],
        E_STOP: None,
    },
}
