# 17.0.0

* transition_dict は変数名を transition、ファイル名を transition_conf にリネーム

# 16.0.0

* state_creator_dict は名前が長いので変数名を state_gen （State generator）、ファイル名を state_gen_conf にリネーム

# 15.0.0

* state.exit() を state.entry() にリネーム
* state.on_exit() を廃止。 必要なら自分で定義してもらうように変更

# 14.0.0

state.entry(), state.on_entry() 廃止。 代わりに state.exit(), state.on_exit() に統合してください

# 13.0.0

* intermachine.put_myself(line) を intermachine.enqueue_myself(line) にリネーム
* intermachine.dequeue_myself() 追加
* intermachine.put(...) を intermachine.enqueue(...) にリネーム
* intermachine.get(...) を intermachine.dequeue(...) にリネーム
* state_machine.dequeue_line() を state_machine.dequeue_item() にリネーム

* request.line を廃止。 代わりに req.intermachine.dequeue_myself() としてください
* state_machine._leave(...) の line 引数廃止。 代わりに同上
* Request(...) の intermachine 引数を必須に変更
* MultipleStateMachineクラスの使用が必須に変更

# 12.0.0

state_machine.entry() の戻り値廃止。 代わりに req.intermachine.put_myself(line) としてください

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
