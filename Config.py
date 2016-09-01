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

# Configuration File: Config.py
# Purpose: User defined variable configuration for the EQMBox_CCC.py tool
# Usage: Change the variables below to the specific needs of the character that you want to control
#        This includes things that are either character or machine specific like: Game Directory Path, 
#        Spell Slot Numbers (/cast #), Ability Macro Numbers (/doabity #), and AA ID's. 

# NOTE:  You MUST define a whitelist of characters at the bottom of this file
#        that are allowed to control the BOXED character via in-game chat messages.


#### USER DEFINED VARIABILES - CHANGE THE VALUES TO SUIT YOUR NEEDS ####


# eq installation directory
EQHOME = "/home/username/.PlayOnLinux/wineprefix/EverQuest_Live/drive_c/Program Files/Sony/EverQuest F2P/"


# melee attack in-game commands
ATTACK = "/attack"
RANGE = "/autofire"


# spell sets (for loading and unloading)
# feature not implemented yet
SS_DEFAULT = "/memspellset 1"
SS_BUFFS = "/memspellset 2"


# ** SPELLS **
# The following variables describe spell casting actions
# You my comment out a line for a particular character with 
# a '#' symbol if that particular action is not needed.
# Change the following values to your spell gem slot ID numbers

# Note: You may also substitute the '/cast' command with a '/alt activate <AA-ID>' 
#       to activate an alternate advancement version of the spell instead
#       ie. '/alt activate 1210'  - for Mage Group Invis AA
#       to get the AA ID number open up the alt advancement window in the game client,
#       select the AA you wish to program, and then in the description look for the 
#       line that provides the AA ID or you can refer to the list here:
#       http://articles.eqresource.com/altactlist.php

# in-game heal commands (spell gem slots)
HEAL = "/cast 10"
DURHEAL = "/cast 11"

# in-game buff commands
HASTE = "/cast 8"
REGEN = "/cast 9"
DMGSHIELD = ""
HPBUFF = "/cast 5"

# in-game offensive spell commands
# specify and AoE or Single target spell for each slot needed
# feel free to substitute slots for other spells, as long as you
# remember what's going on when you go to @DD3 a DoT spell.
DD1 = "/cast 6"
DD2 = ""
DD3 = ""
DD4 = ""
DD5 = ""
DOT1 = "/cast 1"
DOT2 = "/cast 2"
DOT3 = "/cast 3"
DOT4 = "/cast 4"
DOT5 = "/cast 5"
AOE1 = ""
AOE2 = ""
AOE3 = ""
AOE4 = ""
AOE5 = ""
SLOW = "/alt activate 3729"
AOESLOW = "/alt activate 856"
MALO = "/alt activate 1041"
SNARE = ""
ROOT = "/alt activate 171"

# in-game utility buff spell comands
BIND = ""
INVIS = "/alt activate 630"
ITU = ""
SOW = ""
CRACK = ""


# ** CLICKIES **
# uses /useitem command, items must be either equiped or in one of the first 10 bag slots
# List of codes for /useitem <slot>
# Charm = 0
# Left Ear = 1
# Head = 2
# Face = 3
# Right Ear = 4
# Neck = 5
# Shoulders = 6
# Arms = 7
# Back = 8
# Left Wrist = 9
# Right Wrist = 10
# Range = 11
# Hands = 12
# Primary = 13
# Secondary = 14
# Left Ring = 15
# Right Ring = 16
# Chest = 17
# Legs = 18
# Feet = 19
# Waist = 20
# Power Source = 21
# Ammo = 22
# Bag Slot 1 = 23
# Bag Slot 2 = 24
# Bag Slot 3 = 25
# Bag Slot 4 = 26
# Bag Slot 5 = 27
# Bag Slot 6 = 28
# Bag Slot 7 = 29
# Bag Slot 8 = 30
# Bag Slot 9 = 31
# Bag Slot 10 = 32

# Note: Regarding clicking items inside of bags 
#       if an item is in bag slot 1 then it is the first 
#       slot in your inventory where a bag can be placed.
#       This would be access by using </useitem 23>

#       If there is a bag in that slot then in order to
#       access the items inside of it you need to call the
#       sub-slot ID.  So if your jboots are in <BAG1, SLOT1>
#       then you would access them by using </useitem 23 0>
#       where the second number is the <SLOT_ID>

# define clickies here
JBOOTS = "/useitem 23 0"
SHMCUDGEL = "/useitem 23 1"
GOBBYEARING = ""
ROOTRING = "/useritem 23 1"


# WHITELIST: list of characters allowed to send this bot commands
# NOTE: the 'You' name is a special name indicating the BOXED character
#       by adding this to the whitelist 'You' allow access to triggering
#       actions by the BOXED character's sent chat messages.  This is handy
#       when you want to use the @skillup feature provided in this application
#       or wish to perform other automation tasks localy on the BOXED account.
WHITELIST = ['You',
            'character1', 
            'character2', 
            'character3', 
            'character4']

#### END USER DEFINED ####
