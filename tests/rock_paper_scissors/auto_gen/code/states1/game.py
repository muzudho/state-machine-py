from tests.rock_paper_scissors.auto_gen.data.const import E_DRAW, E_LOOPBACK, E_LOSE, E_WIN

class GameState():
    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = self.on_trigger(req)

        # 分岐
        if msg == E_LOOPBACK:
            self.on_loopback(req)
            return E_LOOPBACK

        elif msg == E_WIN:
            self.on_win(req)
            return E_WIN

        elif msg == E_DRAW:
            self.on_draw(req)
            return E_DRAW

        elif msg == E_LOSE:
            self.on_lose(req)
            return E_LOSE

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

    def on_win(self, req):
        pass

    def on_draw(self, req):
        pass

    def on_lose(self, req):
        pass

