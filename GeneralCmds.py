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

from Targeting import *

# general commands that don't fit in any one category
class GeneralCmds:

    def __init__(self):
        print("DEBUG: Initializing GeneralCmds Class")

    # accept group invite
    def acceptGroupInv(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", "/inv"])
        subprocess.call(["xdotool", "key", "Return"])
        # TODO: handle the window popup that forces you to accept the loot rules for the new group

    # assist the character that called for @assist
    def assist(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/assist", " ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])

    # manual override command @manual <command> <substring> <substring> ...
    def manual(line):
        print("DEBUG: "+line)
        tokens = line.split()
        size = len(tokens) - 10
        COMMANDLIST = tokens[-size:]
        COMMAND = " ".join(COMMANDLIST)
        COMMAND = COMMAND[:-1]
        time.sleep(1)
        subprocess.call(["xdotool", "type", COMMAND])
        subprocess.call(["xdotool", "key", "Return"])

# End of Class
