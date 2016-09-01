#!/usr/bin/python

# Program Name: EQMBox_CCC.py 
#               'The EverQuest Multi-Box Command and Control Client'
# Author: Ronny Bull (A.K.A. Cubber)
# Python Version: 3.4
# Original Date: 6/10/2016
# Last Revision: 6/16/2016

# Purpose:  This program is intended to run on a Linux system running 'EverQuest' under 'Wine'.
#           It is dependent upon the 'xdotool' application being installed in order to spoof the
#           keyboard and mouse movements on the client system.  When running the program will
#           parse your EverQuest chat log file for the 'BOXED' character and look for keywords
#           that trigger actions.  These actions are either a simulated key press such as a letter
#           or number, or can also be a fully typed set of strings followed by an 'Enter' key.

# IMPORTANT: Verify that your 'eqclient.ini' file contains the following line: Log=TRUE
#            This program will perform a check, but it is good to verify it manually anyway!

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
import sys
import os

from os import listdir
from os.path import isfile, join


# classes
from Config import *
from DepCheck import *
from CharacterList import *
from Movement import *
from GeneralCmds import *
from Melee import *
from Skillup import *
from Pets import *
from OffensiveSpells import *
from UtilitySpells import *
from UtilityAA import *
from Heals import *
from Buffs import *
from Clickies import *
from Targeting import *


#### MAIN PROGRAM ####

# dependency checks
DepCheck.verifyOS()
DepCheck.verifyXdotool()
DepCheck.verifyLogging()

# program banner 
# TODO: NEED FUNKY ASCII ART HERE 
print("\n\nStarting The EverQuest Multi-Box Command and Control Client\n")

# get character info
# TODO: this should produce a list of characters and server bindings based on 
# output from directory listing and parsing for character UI files.
ALLFILES = [u for u in listdir(EQHOME) if isfile(join(EQHOME, u))]
sub = "UI_"
UIFILES = [s for s in ALLFILES if sub in s]

# create linked list of characters and generate menu
CHARLIST = LinkedList()

count = 0
for i in UIFILES:
    count = count + 1
    tmp = i.split("_")
    # need linked list to store character/server list to return to menu
    CHARNAME = tmp[1]
    CHARSERVER = tmp[2].split(".")
    CHARSERVER = CHARSERVER[0]
    CHARLIST.add(CHARNAME, CHARSERVER)

iterator = iter(CHARLIST)
count = 0
for c in CHARLIST:
    print("%d: %s" % (count, next(iterator)))
    count = count + 1

# ask user to pick character to control from list
CHARNUM = input("\n\nEnter the number of the character you would like to control from the list: ")
BOXCHAR = CHARLIST.getName(CHARNUM)
SERVER = CHARLIST.getServer(CHARNUM)

# generate logfile path
LOGPATH = "Logs/eqlog_%s_%s.txt" % (BOXCHAR, SERVER) 
LOGFILE = EQHOME+LOGPATH
DepCheck.verifyLogFile(BOXCHAR, LOGFILE)

# get game window focus
# NOTE: This gets a bit funky where there are other windows with the string "EverQuest" in thier title
# so lets change the window name to something a bit more unique
WINDOWNAME = "EverQuest-%s" % BOXCHAR
subprocess.call(["xdotool", "search", "--name", "EverQuest", "set_window", "--name", WINDOWNAME])

time.sleep(2)

# set window focus
subprocess.call(["xdotool", "search", "--name", "EverQuest", "windowactivate"])

# begin parsing log file for triggers and perform actions
try:

    # open log file
    with open(LOGFILE, 'r+') as f:
        # move to the end of the file
        f.truncate()

        # loop over each new line of the file in realtime and
        # act on keywords from chat messages parsed from logfile by calling 
        # the proper method from the corresponding class for the action
        while True:
            line = f.readline()
            if line:
                #print("DEBUG: "+line)

                #### GENERAL COMMANDS ####

                # accept group invite
                if 'invites you to join a group' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        GeneralCmds.acceptGroupInv(line)

                # assist on target
                if '@assist' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        GeneralCmds.assist(line)

                # manual command input
                if '@manual' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        GeneralCmds.manual(line)


                #### MOVEMENT COMMANDS ####

                # follow controlling character
                if '@follow' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Movement.follow(line)

                # move bot forward
                if '@forward' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Movement.forward(line)

                # move bot backward
                if '@reverse' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Movement.reverse(line)

                # turn bot right
                if '@right' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Movement.right(line)

                # turn bot left
                if '@left' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Movement.left(line)


                #### MELEE COMMANDS ####

                # attack with melee weapon
                if '@attack' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Melee.attack(line)

                # autofire ranged weapon
                if '@range' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Melee.autofire(line)

                
                #### HEAL COMMANDS ####

                # heal controlling character 
                if '@hme' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Heals.healMe(line)

                # duration heal controlling character 
                if '@dhme' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Heals.durHealMe(line)

                # heal target
                if '@heal' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Heals.healTarget(line)

                # duration heal target
                if '@durheal' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Heals.durHeal(line)


                #### BUFF COMMANDS ####

                # cast HP buff on requesting character 
                if '@hpbuff' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Buffs.hitPoints(line)

                # cast REGEN buff on requesting character 
                if '@regen' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Buffs.regen(line)

                # cast HASTE buff on requesting character 
                if '@haste' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Buffs.haste(line)

                # cast DMGSHIELD buff on requesting character 
                if '@ds' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Buffs.dmgShield(line)
  

                #### OFFENSIVE SPELL COMMANDS ####

                # Direct Damage Spell 1 
                if '@dd1' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.dd1(line)

                # Direct Damage Spell 2 
                if '@dd2' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.dd2(line)

                # Direct Damage Spell 3 
                if '@dd3' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.dd3(line)

                # Direct Damage Spell 4 
                if '@dd4' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.dd4(line)

                # Direct Damage Spell 5 
                if '@dd5' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.dd5(line)

                # Damage Over Time Spell 1 
                if '@dot1' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.dot1(line)

                # Damage Over Time Spell 2 
                if '@dot2' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.dot2(line)

                # Damage Over Time Spell 3 
                if '@dot3' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.dot3(line)

                # Damage Over Time Spell 4 
                if '@dot4' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.dot4(line)

                # Damage Over Time Spell 5 
                if '@dot5' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.dot5(line)

                # AOE Spell 1 
                if '@aoe1' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.aoe1(line)

                # AOE Spell 2 
                if '@aoe2' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.aoe2(line)

                # AOE Spell 3 
                if '@aoe3' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.aoe3(line)

                # AOE Spell 4 
                if '@aoe4' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.aoe4(line)

                # AOE Spell 5 
                if '@aoe5' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.aoe5(line)


                # slow 
                if '@slow' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.slow(line)

                # malo
                if '@malo' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.malo(line)

                # snare
                if '@snare' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.snare(line)

                # root
                if '@root' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        OffensiveSpells.root(line)


                #### UTILITY SPELL COMMANDS ####

                # bind 
                if '@bindme' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        UtilitySpells.bindMe(line)

                # invis
                if '@invisme' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        UtilitySpells.invisMe(line)

                # itu 
                if '@itume' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        UtilitySpells.ituMe(line)

                # sow
                if '@sowme' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        UtilitySpells.sowMe(line)

                # crack
                if '@crack' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        UtilitySpells.crackMe(line)


                #### Utility AA ####

                # mage group invis
                if '@mageinvis' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        UtilityAA.mageGroupInvisAA(line)

                # mage CoH
                if '@coh' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        UtilityAA.mageCoHAA(line)

		
                #### CLICKIES ####

                # jboots 
                if '@jboots' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Clickies.jBoots(line)

                # gobby earing 
                if '@gobby' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Clickies.gobbyEaring(line)

                # shaman cudgel 
                if '@cudgel' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Clickies.shmCudgel(line)

                # VT root ring 
                if '@rootring' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Clickies.rootRing(line)


                #### PETS ####

                # pet attack
                if '@petattack' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Pets.petAttack(line)

                # pet hold
                if '@pethold' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Pets.petHold(line)

                # pet taunt
                if '@pettaunt' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Pets.petTaunt(line)

                # pet back off
                if '@petbackoff' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Pets.petBackOff(line)
		
                # pet focus
                if '@petfocus' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Pets.petFocus(line)

                # pet feign
                if '@petfeign' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Pets.petFeign(line)


                #### SKILLUP AUTOMATION ####
                
                # NOTE: requres the following syntax in group chat
                #       @skillup <cycles> <hotkey> <refesh time>
                #       cycles:       amount of times you want to "press the macro button"
                #       hotkey:       the specific key that the macro is bound to in the main hotbar
                #       refresh time: time to wait for skill refresh in between cycles
                if '@skillup' in line:
                    if DepCheck.verifyRequest(line) == 0:
                        Skillup.skillBuilder(line)

            # end outer if

        # end while

    # end with

# handle ctrl+c for clean exit
except KeyboardInterrupt:
    print("")
    print("Closing The EverQuest Multi-Box Command and Control Client")

finally:
    # close log file and exit
    f.close()
    sys.exit()
