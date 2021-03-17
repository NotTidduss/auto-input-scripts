# Requirements:
#  - Adell is positioned next to dimensional guide.
#  - Cave of Ordeal is on the very bottom of the stage selection.
#  - Characters to be levelled must be on top of the character list.
#  - Characters have the stats to one-shot (big bang + blade rush) enemies for as many clears as possible.

########## ------------ Key bindings ------------ ##########
STOP_SCRIPT        = 'ESCAPE'
ACTION_UP          = 'w'
ACTION_LEFT        = 'a'
ACTION_RIGHT       = 'd'
ACTION_DOWN        = 's'
ACTION_SELECT      = 'ENTER'
ACTION_MENU        = 'TAB'
ACTION_RETURN      = 'BACKSPACE'

################## Command infrastructure ##################
import keyboard
import time

class Command:
  def __init__(self, key, duration, is_silence = False):
    self.key = key
    self.duration = duration
    self.is_silence = is_silence
  def execute(self):
    if (self.is_silence):
      print("Silence for " + str(self.duration) )
      time.sleep(self.duration)
    else:
      print("Key " + self.key + "   for " + str(self.duration) + " seconds.")
      keyboard.press(self.key)
      time.sleep(self.duration)
      keyboard.release(self.key)

### -- Scenario to select stage, move chars and clear -- ###
# TODO: find, set and test inputs
confirm_win = Command(ACTION_SELECT, 0.5)
run_left = Command(ACTION_LEFT, 3)
run_right = Command(ACTION_RIGHT, 3)
stop = Command(ACTION_UP, 1, True)

commands = [
	run_left, 
	confirm_win, 
	run_right, 
	confirm_win
	]

########################## Logic ###########################
is_continue = True
STOP_EVENT = keyboard.KeyboardEvent('down', STOP_SCRIPT, STOP_SCRIPT)

def stop_script(keyboard_event):
  if(keyboard_event.name == STOP_EVENT.name):
    print("Goodbye.")
    global is_continue
    is_continue = False

if __name__ == "__main__":
  global is_continue
  keyboard.on_press(stop_script)
  while is_continue:
    for command in commands:
      command.execute()