# State
INIT = "[Init]"
GAME = "[Game]"

# Edge
E_LOOPBACK = "----Loopback---->"
E_LOGGED_IN = "----LoggedIn---->"
E_WIN = "----Win---->"
E_DRAW = "----Draw---->"
E_LOSE = "----Lose---->"

transition_dict = {
    INIT: {
        E_LOOPBACK: INIT,
        E_LOGGED_IN: GAME,
    },
    GAME: {
        E_LOOPBACK: GAME,
        E_WIN: INIT,
        E_DRAW: INIT,
        E_LOSE: INIT,
    },
}
