def create_init_this(state):
    def __on_entry(req):
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        print(f"[Walk] state_path={state_path_str}")

    state.on_entry = __on_entry
    return state
