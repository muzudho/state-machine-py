from tests.edge_walk.auto_gen.data.const import E_IS, E_WAS

class InitThisState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_WAS:
            self.on_was(req)
            return E_WAS

        elif msg == E_IS:
            self.on_is(req)
            return E_IS

        elif msg == None:
            return None

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_was(self, req):
        pass

    def on_is(self, req):
        pass

