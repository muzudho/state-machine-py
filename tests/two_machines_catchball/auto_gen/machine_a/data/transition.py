from tests.two_machines_catchball.auto_gen.data.const import E_INCREASE, E_STOP, INIT

machinea_transition_doc = {
    "title": "Two Machines Catchball - Machine A",
    "entry_state": INIT,
    "data": {
        INIT: {
            E_INCREASE: [INIT],
            E_STOP: None
        }
    }
}
