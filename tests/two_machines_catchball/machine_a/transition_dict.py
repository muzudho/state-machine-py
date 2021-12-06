from tests.two_machines_catchball.keywords import INIT, E_INCREASE, E_STOP

transition_dict = {
    INIT: {
        E_INCREASE: INIT,
        E_STOP: None,
    },
}
