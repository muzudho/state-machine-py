from tests.edge_walk.auto_gen.data.const import A, E_A, E_AN, E_IS, E_PEN, E_PIN, E_RETRY, E_THAT, E_THIS, E_WAS, GOAL, INIT, IS, THIS

ew_transition_obj = {
    "title": "Edge walk",
    "entry_state": INIT,
    "data": {
        INIT: {
            E_THAT: [INIT],
            E_THIS: [INIT, THIS],
            THIS: {
                E_WAS: [INIT],
                E_IS: [INIT, THIS, IS],
                IS: {
                    E_AN: [INIT],
                    E_A: [INIT, THIS, IS, A],
                    A: {
                        E_PIN: [INIT],
                        E_PEN: [GOAL]
                    }
                }
            }
        },
        GOAL: {
            E_RETRY: [INIT]
        }
    }
}
