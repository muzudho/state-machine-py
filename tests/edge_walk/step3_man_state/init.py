def create_init(state):
    def __on_entry(req):
        """入力を取る前"""
        # 現在位置の表示
        state_path_str = "/".join(req.state_path)
        print(
            f"""[Walk] Current state_path={state_path_str}
READMEを参考にして、エッジを入力してください"""
        )

    state.on_entry = __on_entry
    return state
