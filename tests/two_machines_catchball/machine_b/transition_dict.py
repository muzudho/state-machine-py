from tests.task_sharing.keywords import INIT, E_DECREASE, E_STOP

transition_dict = {
    INIT: {
        E_DECREASE: INIT,
        E_STOP: None,
    },
}
