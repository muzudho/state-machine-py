from tests.task_sharing.keywords import INIT, E_INCREASE, E_STOP

transition_dict = {
    INIT: {
        E_INCREASE: INIT,
        E_STOP: None,
    },
}
