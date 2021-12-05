from tests.task_sharing.layer2_decoration_event.init import create as create_init
from tests.task_sharing.layer2_decoration_event.stop import create as create_stop
from tests.task_sharing.keywords import STOP, INIT

state_creator_dict = {
    INIT: create_init,  # 初期値
    STOP: create_stop,
}
