# EQMBox_CCC 
The EverQuest Emulator Multi-Box Command and Control Client

Original Author: Ronny Bull - (A.K.A. Cubber on eqemulator.org)

Python Version: 3.4

Original Date: 6/10/2016

Last Revision: 9/1/2016

Purpose:  This program is intended to run on a Linux system running 'EverQuest' under 'Wine'.
          It is dependent upon the 'xdotool' application being installed in order to spoof the
          keyboard and mouse movements on the client system.  When running the program will
          parse your EverQuest chat log file for the 'BOXED' character and look for keywords
          that trigger actions.  These actions are either a simulated key press such as a letter
          or number, or can also be a fully typed set of strings followed by an 'Enter' key.

IMPORTANT: Verify that your 'eqclient.ini' file contains the following line: LOG=TRUE


FAQ

Q. Can I use this to control multiple accounts running on 'separate' computers or virtual machines?

A. Yes, each account will require its own 'instance' of EQMBox_CCC.py running configured for the specific character to be controlled.  When all of the characters are in the same group they will act on commands that pertain to them as listed in the 'Config.py' file.  If a specific variable is set to "" then the character will not perform an action.  For example if you issue a '@healme' command in a group with a Warrior, Cleric, and Shaman both the Shaman and Cleric will heal you if configured for their heal spell and the Warrior will not do anything.  So if 'BOXING' multiple accounts at the same time with this script be careful to configure your 'Config.py' file on each system as you need it for your particular group.  This will take some experimentation.



Q. Will this work with multiple instances of EverQuest running on the same computer?

A. The short answer is no.  This application depends on having the game window in 'focus' in order to execute the keyboard commands.  It is impossible to have multiple windows in 'focus' at the same time.  


Q. Can this be used on the Live EverQuest servers?

A. While this code 'potentially' could be used to control 'Boxed' characters on a Live EverQuest server we do not encourage nor endorse it, and the maintainers of this project will in no way be held responsible for the actions of anyone who attempts it.  This was developed as a creative academic demonstration to introduce students to parsing log files with python and producing actions based upon specific events.  This code is developed and tested on 'Private' EQEmulator servers hosted by the developers, and is intended to be used 'ONLY' on EQEmulator servers where authorized by the server administrator.  
