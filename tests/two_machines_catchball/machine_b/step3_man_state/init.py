def create_init(state):
    def __on_update(req):
        print(f"[B] number={req.context.number}")

    state.on_update = __on_update
    return state
