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

# class for triggering clicky items
# NOTE: JBOOTS, GOBBYEARING, etc ... must be defined in Config.py
class Clickies:

    def __init__(self):
        print("DEBUG: Initializing Clickies Class")

    # Activate JBOOTS
    def jBoots(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", JBOOTS])
        subprocess.call(["xdotool", "key", "Return"])

    # Activate GOBBYEARING
    def gobbyEaring(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", GOBBYEARING])
        subprocess.call(["xdotool", "key", "Return"])

    # Activate SHMCUDGEL
    def shmCudgel(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", SHMCUDGEL])
        subprocess.call(["xdotool", "key", "Return"])

    # Activate SHMCUDGEL
    def rootRing(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", ROOTRING])
        subprocess.call(["xdotool", "key", "Return"])

    # TODO: Add more clicky items

# End of Class
