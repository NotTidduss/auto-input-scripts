# Requirements:
#  - Skill to grind needs adjustments in script - see !!!.
#  - Characters to need to be positioned above to invincible target. I use the first invincible tile in stage 4-4.
#  - Characters should have as much SP as possible

########## ------------ Key bindings ------------ ##########
STOP_SCRIPT        = 'ESCAPE'
MOVE_UP          = 'w'
MOVE_LEFT        = 'a'
MOVE_RIGHT       = 'd'
MOVE_DOWN        = 's'
CONFIRM          = 'k'
CANCEL           = 'l'
OPEN_MENU        = 'i'
WAIT             = 'p'

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
# configure commands
move_up = Command(MOVE_UP, 0.1)
move_left = Command(MOVE_LEFT, 0.1)
move_right = Command(MOVE_RIGHT, 0.1)
move_down = Command(MOVE_DOWN, 0.1)
confirm = Command(CONFIRM, 0.3)
open_menu = Command(OPEN_MENU, 0.2)
wait = Command(WAIT, 6)
intermission = Command(WAIT, 0.1)
safetyCancel = Command(CANCEL, 0.1)

# set commands
commands = [
    wait,               # initial wait for turn
	move_up,            # move cursor to character
    intermission,
    confirm,            # open character menu
    move_down,          # choose special menu
    intermission,
    move_down, 
    intermission,
    confirm,            # open special menu
    move_down,          # choose skill              !!!
    intermission,
    move_down,
    intermission,
    move_down,
    intermission,
    confirm,            # open skill selection
    intermission,
    confirm,            # confirm target selection
    open_menu,          # open menu for END TURN
    move_down, 
    confirm,            # END TURN
    wait,
    safetyCancel        # in case the loop gets stuck, this might fix it
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