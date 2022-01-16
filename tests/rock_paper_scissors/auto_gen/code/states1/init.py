from tests.rock_paper_scissors.auto_gen.data.const import E_LOGIN, E_LOOPBACK

class InitState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_LOOPBACK:
            self.on_loopback(req)
            return E_LOOPBACK

        elif msg == E_LOGIN:
            self.on_login(req)
            return E_LOGIN

        elif msg == None:
            return None

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_loopback(self, req):
        pass

    def on_login(self, req):
        pass

