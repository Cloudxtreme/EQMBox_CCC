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

# basic remote movement control class for BOXED character
class Movement:

    def __init__(self):
        print("DEBUG: Initializing Movement Class")

    # move bot forward for .5 seconds
    def forward(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "keydown", "w"])
        time.sleep(.5)
        subprocess.call(["xdotool", "keyup", "w"])

    # move bot backwards for .5 seconds
    def reverse(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "keydown", "s"])
        time.sleep(.5)
        subprocess.call(["xdotool", "keyup", "s"])

    # turn bot right for .5 seconds
    def right(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "keydown", "d"])
        time.sleep(.5)
        subprocess.call(["xdotool", "keyup", "d"])

    # turn bot left for .5 seconds
    def left(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "keydown", "a"])
        time.sleep(.5)
        subprocess.call(["xdotool", "keyup", "a"])

    # auto-follow the requesting character
    def follow(line):
        print("DEBUG: "+line)
        # get character name from groupsay "soandso tells the group"
        TARGET = Targeting.requested(line)
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/target", " ", TARGET])
        subprocess.call(["xdotool", "key", "Return"])
        time.sleep(1)
        subprocess.call(["xdotool", "type", "/follow"])
        subprocess.call(["xdotool", "key", "Return"])

# End of Class
