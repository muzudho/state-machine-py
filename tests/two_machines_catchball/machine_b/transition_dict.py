from tests.two_machines_catchball.keywords import INIT, E_DECREASE, E_STOP

transition_dict = {
    INIT: {
        E_DECREASE: INIT,
        E_STOP: None,
    },
}