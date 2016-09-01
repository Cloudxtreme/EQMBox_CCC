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
import threading

# a general class for automating skill increases
class Skillup:

    def __init__(self):
        print("DEBUG: Initializing Skillup Class")

    # skillBuilder(): parses number of attempts, specific key to press, and refresh time in seconds
    # from the log line passed to the method. Requires a skillup macro setup on the main hotbar of 
    # the BOXED character.

    # Example trigger syntax: @skillup <cycles> <hotkey> <refesh time>.

    # cycles:       amount of times you want to "press the macro button"
    # hotkey:       the specific key that the macro is bound to in the main hotbar
    # refresh time: time to wait for skill refresh in between cycles 
    def skillBuilder(line):
        print("DEBUG: "+line)
        tokens = line.split()
        cycles = int(tokens[10])
        hotkey = tokens[11]
        refreshTimer = tokens[12]
        refreshTimer = float(refreshTimer[:-1])

        # loop on number of cycles, pausing in between each cycle to wait for skills to refresh
        for x in range(0, cycles):
             subprocess.call(["xdotool", "key", hotkey])
             time.sleep(refreshTimer)

# End of Class
