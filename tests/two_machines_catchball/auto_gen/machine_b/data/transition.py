from tests.two_machines_catchball.auto_gen.data.const import E_DECREASE, E_STOP, INIT

machineb_transition_obj = {
    "title": "Two Machines Catchball - Machine B",
    "entry_state": INIT,
    "data": {
        INIT: {
            E_DECREASE: [INIT],
            E_STOP: None
        }
    }
}
