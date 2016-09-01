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

# class for Melee actions
class Melee:

    def __init__(self):
        print("DEBUG: Initializing Melee Class")

    # attack!
    def attack(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", "/attack"])
        subprocess.call(["xdotool", "key", "Return"])

    # autofire ranged weapon
    def autofire(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", "/autofire"])
        subprocess.call(["xdotool", "key", "Return"])

    # TODO: add methods in for the most used melee AA's and Discs

# End of Class
