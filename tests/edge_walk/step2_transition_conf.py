from tests.edge_walk.step1_const_conf import A, E_A, E_AN, E_IS, E_RETRY, E_PEN, E_PIN, E_THAT, E_THIS, E_WAS, INIT, GOAL, IS, THIS

transition = {
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
                    E_PEN: [GOAL],
                },
            },
        }
    },
    GOAL: {
        E_RETRY: [INIT],
    }
}
