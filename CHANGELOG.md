# 11.0.0

lines_getter 廃止  
State machine の input_queue プロパティや、 terminate() メソッドを直接使ってください  

# 10.0.13

Multiple state machine の input_queues を廃止、 State machine の input_queue を直接利用  

# 10.0.0 - 10.0.12

* StateMachine
  * Change leave_and_loop(...) to private
  * Change arrive_sequence(...) to private
  * Change arrive(...) to private
  * Change leave(...) to private

内部処理変更のため  

# 9.0.7

次のエッジの名前に ""（Noneではなく空文字列）を指定したなら、踏みとどまるという挙動の追加  

# 9.0.0

ステートマシン間の通信方法の準備  

# 8.0.4

Multiple state machine に create_machine() 追加  

# 8.0.3

Intermachine を準備  

# 8.0.2

永遠に停止の Terminate 機能を準備  

# 8.0.0

lines_getter を StateMachine のプロパティー化  

old: state_machine.start(self, next_state_name, lines_getter)  
new: state_machine.start(self, next_state_name)  

old: state_machine.leave_and_loop(self, lines_getter)  
new: state_machine.leave_and_loop(self)  

# 7.0.0

entry(), on_entry(), exit(), on_exit() の引数を Requestオブジェクト に変更  

# 6.0.0

state.leave(...) を廃止。 state.exit(...) に統合  