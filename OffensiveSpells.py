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

# class for triggering offensive spells 
# NOTE: DD1, DD2, DD3, DOT1, DOT2, DOT3, SLOW, MALO, SNARE, ROOT, etc.. 
#	must be defined in Config.py

class OffensiveSpells:

    def __init__(self):
        print("DEBUG: Initializing Heals Class")

    #  Direct Damage Spell 1 
    def dd1(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", DD1])
        subprocess.call(["xdotool", "key", "Return"])

    #  Direct Damage Spell 2 
    def dd2(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", DD2])
        subprocess.call(["xdotool", "key", "Return"])

    #  Direct Damage Spell 3 
    def dd3(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", DD3])
        subprocess.call(["xdotool", "key", "Return"])

    #  Direct Damage Spell 4 
    def dd4(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", DD4])
        subprocess.call(["xdotool", "key", "Return"])

    #  Direct Damage Spell 5 
    def dd5(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", DD5])
        subprocess.call(["xdotool", "key", "Return"])

    #  Damage Over Time Spell 1 
    def dot1(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", DOT1])
        subprocess.call(["xdotool", "key", "Return"])

    #  Damage Over Time Spell 2 
    def dot2(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", DOT2])
        subprocess.call(["xdotool", "key", "Return"])

    #  Damage Over Time Spell 3 
    def dot3(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", DOT3])
        subprocess.call(["xdotool", "key", "Return"])

    #  Damage Over Time Spell 4 
    def dot4(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", DOT4])
        subprocess.call(["xdotool", "key", "Return"])

    #  Damage Over Time Spell 5 
    def dot5(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", DOT5])
        subprocess.call(["xdotool", "key", "Return"])

    #  AOE Spell 1 
    def aoe1(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", AOE1])
        subprocess.call(["xdotool", "key", "Return"])

    #  AOE Spell 2 
    def aoe2(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", AOE2])
        subprocess.call(["xdotool", "key", "Return"])

    #  AOE Spell 3 
    def aoe3(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", AOE3])
        subprocess.call(["xdotool", "key", "Return"])

    #  AOE Spell 4 
    def aoe4(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", AOE4])
        subprocess.call(["xdotool", "key", "Return"])

    #  AOE Spell 5 
    def aoe5(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", AOE5])
        subprocess.call(["xdotool", "key", "Return"])

    #  SLOW 
    def slow(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", SLOW])
        subprocess.call(["xdotool", "key", "Return"])

    #  MALO
    def malo(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", MALO])
        subprocess.call(["xdotool", "key", "Return"])

    #  SNARE
    def snare(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", SNARE])
        subprocess.call(["xdotool", "key", "Return"])

    #  ROOT
    def root(line):
        print("DEBUG: "+line)
        subprocess.call(["xdotool", "type", ROOT])
        subprocess.call(["xdotool", "key", "Return"])


    # TODO: implement more offensive spells and corresponding AA's

# End of Class
