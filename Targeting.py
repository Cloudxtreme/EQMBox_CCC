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

# class for parsing chat files and getting target information
class Targeting:

    def __init__(self):
        print("DEBUG: Initializing Targeting Class")

    # requesting player pulled from groupsay context
    def requested(line):
        tokens = line.split()
        TARGET = tokens[5]
        #print("Target: %s" % TARGET)
        return TARGET

    # get specified target from message
    def specific(line):
        tokens = line.split()
        TARGET = tokens[10]
        TARGET = TARGET[:-1]
        #print("Target: %s" % TARGET)
        return TARGET

# End of Class

