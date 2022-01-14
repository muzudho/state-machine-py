from tests.rock_paper_scissors.auto_gen.data.const import E_DRAW, E_LOGIN, E_LOOPBACK, E_LOSE, E_WIN, GAME, INIT

rps_transition_doc = {
    "title": "Rock Paper Scissors",
    "entry_state": INIT,
    "data": {
        INIT: {
            E_LOOPBACK: [INIT],
            E_LOGIN: [GAME]
        },
        GAME: {
            E_LOOPBACK: [GAME],
            E_WIN: [INIT],
            E_DRAW: [INIT],
            E_LOSE: [INIT]
        }
    }
}
