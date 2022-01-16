from tests.edge_walk.auto_gen.data.const import E_THAT, E_THIS

class InitState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_THAT:
            self.on_that(req)
            return E_THAT

        elif msg == E_THIS:
            self.on_this(req)
            return E_THIS

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_that(self, req):
        pass

    def on_this(self, req):
        pass

