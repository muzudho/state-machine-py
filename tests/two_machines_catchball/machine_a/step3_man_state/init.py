def create_init(state):
    def __on_update(req):
        print(f"[A] number={req.context.number}")

    state.__on_update = __on_update
    return state
