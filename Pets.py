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

# a class for controlling BOXED character pets
class Pets:

    def __init__(self):
        print("DEBUG: Initializing GeneralCmds Class")

    # pet attack
    def petAttack(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", "/pet attack"])
        subprocess.call(["xdotool", "key", "Return"])

    # pet hold 
    def petHold(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", "/pet hold"])
        subprocess.call(["xdotool", "key", "Return"])

    # pet taunt 
    def petTaunt(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", "/pet taunt"])
        subprocess.call(["xdotool", "key", "Return"])

    # pet back off
    def petBackOff(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", "/pet back off"])
        subprocess.call(["xdotool", "key", "Return"])

    # pet focus
    def petFocus(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", "/pet focus"])
        subprocess.call(["xdotool", "key", "Return"])

    # pet feign 
    def petFeign(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", "/pet feign"])
        subprocess.call(["xdotool", "key", "Return"])

    # TODO: implement other pet functions, pet buffs, swarm pets, and AA's
    #       pet heal

# End of Class
