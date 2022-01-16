from tests.edge_walk.auto_gen.data.const import E_A, E_AN

class InitThisIsState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_AN:
            self.on_an(req)
            return E_AN

        elif msg == E_A:
            self.on_a(req)
            return E_A

        elif msg == None:
            return None

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_an(self, req):
        pass

    def on_a(self, req):
        pass

