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
import sys
import os
import platform

from os.path import isfile

from Config import *
from Targeting import *

# DepCheck - verifies dependencies are met prior to running
#            also contains a method to validate users
class DepCheck:

    def __init__(self):
        print("DEBUG: Checking dependencies")
      

    # verify the plaftform is Linux 
    def verifyOS():
        if platform.system() != 'Linux': 
            print("Here is a nickle, go get yourself a real Operating System kid!") 
            print("") 
            print("Note: This application only works on Linux due to the xdotool dependency.") 
            sys.exit() 
 

    # perform dependency check for xdotool 
    def verifyXdotool():
        print("DEBUG: xdootool install path:")
        if subprocess.call(["which", "xdotool"]) == 1: 
            print("") 
            print("ERROR: xdotool is either not installed on the system or not in your path. Please install it via your distro's package manager or from source and add it to your path") 
            sys.exit() 
        print("") 
 

    # verify that LOG=TRUE in eqclient.ini 
    def verifyLogging():
        # open eqclient.ini for reading 
        # search the file for LOG=TRUE 
        # if not found error out 
        # else proceed on 
        if 'Log=TRUE' in open(EQHOME+"eqclient.ini").read():
            print("DEBUG: Logging is enabled")
        else:
            print("ERROR: Please enable logging in your 'eqclient.ini' file by setting Log=TRUE")
            sys.exit() 

    def verifyLogFile(BOXCHAR, LOGFILE):
        if os.path.isfile(LOGFILE):
            print("\n\nControlling [%s] using the following log file: %s" % (BOXCHAR, LOGFILE))
            print("")
        else:
            print("\n\nERROR: No chat log file exists for the selected character.  Please verify that 'Log=TRUE' in 'eqclient.ini', then log the character into the game and re-run this utility.")
            sys.exit()

    # verifyRequest() - verifies that the user sending the command is on the whitelist 
    def verifyRequest(line):
        # pull character name from command request 
        name = Targeting.requested(line)
 
        # check name against whitelist 
        if name in WHITELIST: 
            print("AUTHORIZED: User - [%s] - is authorized to control this bot." % name) 
            return 0    # accept 
        else: 
            print("WARNING: An unauthorized user - [%s] - attempted to send this bot a command!" % name) 
            return 1    # reject 

#End of Class
