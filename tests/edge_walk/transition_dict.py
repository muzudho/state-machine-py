from tests.edge_walk.keywords import E_A, E_AN, E_IS, E_OK, E_PEN, E_PIN, E_THAT, E_THIS, E_WAS, INIT, GOAL

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
