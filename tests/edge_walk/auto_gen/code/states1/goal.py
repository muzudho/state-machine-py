from tests.edge_walk.auto_gen.data.const import E_RETRY

class GoalState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_RETRY:
            self.on_retry(req)
            return E_RETRY

        else:
            raise ValueError(f"Unexpected msg:{msg}")

    def on_entry(self, req):
        pass

    def on_trigger(self, req):
        return req.context.pull_trigger()

    def on_retry(self, req):
        pass

