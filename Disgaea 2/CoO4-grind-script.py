# Requirements:
#  - The Cave of Ordeal 4 Stage must be selected in the stage select.
#  - Characters to be levelled must be on top of the character list.
#  - Characters have the stats to one-shot (big bang + blade rush) enemies for as many clears as possible.

########## ------------ Key bindings ------------ ##########
STOP_SCRIPT        = 'ESCAPE'
MOVE_UP          = 'w'
MOVE_LEFT        = 'a'
MOVE_RIGHT       = 'd'
MOVE_DOWN        = 's'
CONFIRM          = 'k'
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
wait = Command(WAIT, 3.5)
intermission = Command(WAIT, 0.1)

# set commands
commands = [
    wait,               # initial wait, switch into game
	confirm,            # select stage
    wait,               # wait until stage is loaded
    confirm,            # open base panel menu
    intermission,
    confirm,            # choose ULTIMA
    intermission,
    confirm,            # open ULTIMA menu for moving
    intermission,
    move_up,            # move into right position
    intermission,
    move_up,
    intermission,
    move_up,
    intermission,
    move_up,
    confirm,            # confirm movement
    intermission,
    confirm,            # open ULTIMA menu for attacking
    move_down,          # move cursor to Special
    intermission,
    move_down,
    confirm,            # open Special menu
    move_down,            # select Winged Slayer
    intermission,
    move_down,
    intermission,
    move_down,
    confirm,            # confirm Special selection
    intermission,
    confirm,            # confirm target
    move_down,          # move back to base panel
    intermission,
    move_down,
    intermission,
    move_down,
    intermission,
    move_down,
    confirm,            # open basel menu, again
    intermission,
    confirm,            # choose Fan
    intermission,
    confirm,            # open Fan menu
    intermission,
    confirm,            # choose move           
    move_right,         # move into the right position
    intermission,
    move_right,
    move_up,
    intermission,
    move_up,
    intermission,
    move_up,
    confirm,            # confirm position
    intermission,
    intermission,
    confirm,            # open Fan menu for attacking
    move_down,          # select Special
    intermission,
    move_down,  
    confirm,            # open Special menu
    intermission,       # select Blade Rish
    confirm,            # confirm selection
    intermission,
    confirm,            # confirm target
    open_menu,          # open menu for EXECUTE
    confirm,            # EXECUTE
    wait,
    intermission,
    wait,
    confirm,            # confirm bonus
    intermission,
    confirm             # finish stage
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