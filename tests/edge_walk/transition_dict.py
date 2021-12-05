from tests.edge_walk.keywords import INIT, GOAL


E_THAT = "-that->"
E_THIS = "-this->"
E_WAS = "-was->"
E_IS = "-is->"
E_AN = "-an->"
E_A = "-a->"
E_PIN = "-pin->"
E_PEN = "-pen->"
E_OK = "-ok->"

transition_dict = {
    INIT: {
        E_THAT: INIT,
        E_THIS: {
            E_WAS: INIT,
            E_IS: {
                E_AN: INIT,
                E_A: {
                    E_PIN: INIT,
                    E_PEN: GOAL,
                },
            },
        }
    },
    GOAL: {
        E_OK: INIT,
    }
}
