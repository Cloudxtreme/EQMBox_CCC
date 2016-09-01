#    This file is part of EQMBox_CCC.

#    EQMBox_CCC is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    EQMBox_CCC is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with EQMBox_CCC.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import time

# classes
from Config import *
from Targeting import *

# class for triggering buffs
# NOTE: HPBUFF, REGEN, HASTE, DS, etc ... must be defined in Config.py
class Buffs:

    def __init__(self):
        print("DEBUG: Initializing Buffs Class")

    # HP Buff requesting party member (must be WHITELISTED in Config.py)
    def hitPoints(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/target ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.call(["xdotool", "type", HPBUFF])
        subprocess.call(["xdotool", "key", "Return"])

    # REGEN buff requesting party member (must be WHITELISTED in Config.py)
    def regen(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/target ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.call(["xdotool", "type", REGEN])
        subprocess.call(["xdotool", "key", "Return"])

    # HASTE buff requesting party member (must be WHITELISTED in Config.py)
    def haste(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/target ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.call(["xdotool", "type", HASTE])
        subprocess.call(["xdotool", "key", "Return"])

    # DMGSHIELD buff requesting party member (must be WHITELISTED in Config.py)
    def dmgShield(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/target ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.call(["xdotool", "type", DMGSHIELD])
        subprocess.call(["xdotool", "key", "Return"])

# End of Class
