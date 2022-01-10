from tests.rock_paper_scissors.auto_gen.data.transition import E_DRAW, E_LOGIN, E_LOSE, E_WIN, GAME, INIT

rps_transition_obj = {
    "title": "Rock Paper Scissors",
    "entry_state": INIT,
    "data": {
        INIT: {
            "": [INIT],
            E_LOGIN: [GAME]
        },
        GAME: {
            "": [GAME],
            E_WIN: [INIT],
            E_DRAW: [INIT],
            E_LOSE: [INIT]
        }
    }
}
