from tests.match_server.machine_c.layer1.reply import ReplyState


class DecoratedReplyState(ReplyState):
    def __init__(self):
        super().__init__()
