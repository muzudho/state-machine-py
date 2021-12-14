from tests.rock_paper_scissors.step1_const_conf import (
    E_DRAW,
    E_LOGIN,
    E_LOOPBACK,
    E_LOSE,
    E_WIN,
    GAME,
    INIT,
)


transition = {
    INIT: {
        E_LOOPBACK: [INIT],
        E_LOGIN: [GAME],
    },
    GAME: {
        E_LOOPBACK: [GAME],
        E_WIN: [INIT],
        E_DRAW: [INIT],
        E_LOSE: [INIT],
    },
}
