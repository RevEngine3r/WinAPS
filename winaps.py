# Service installation and start arg parser
import sys
import os_utils
import config

if len(sys.argv) > 1:
    import pyuac

    if pyuac.isUserAdmin():
        import service

        args_action = {
            '-s': service.start,
            '-i': service.install_start,
        }

        for arg, action in args_action.items():
            if arg in sys.argv:
                action()
    else:
        pyuac.runAsAdmin()

    sys.exit(0)

import time
import psutil
from logger import logger as log

# ac, bt, None
last_state = None



def run_actions(actions):
    for atn in actions:
        os_utils.psexec(atn.split(' '), session_id=1)
        time.sleep(.3)


def on_battery():
    run_actions(config.get_commands_battery())


def on_ac():
    run_actions(config.get_commands_ac())


while 1:
    battery = psutil.sensors_battery()
    if (battery is not None) and (not battery.power_plugged):
        if last_state != 'bt':
            on_battery()
            last_state = 'bt'
            log.error('State changed to battery!')
    elif last_state != 'ac':
        on_ac()
        last_state = 'ac'
        log.debug('*** State changed to AC ***')
    time.sleep(3)
