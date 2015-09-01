#!/usr/bin/python

import curses
import os
import signal
import time
import traceback

start = 'init'
sleep_interval = 2;

if start == 'init':
  try:

  
    # Initialize main window
    stdscr = curses.initscr()
    
    # Shut off output
    curses.noecho()
    # Shut off line buffer
    curses.cbreak()
    # Make cursor and special keys available
    stdscr.keypad(0)
    curses.curs_set(0)
    
    # Define colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    # Assign defined colors
    stdscr.bkgd(curses.color_pair(1))
    stdscr.refresh()
    
    # Add output
    stdscr.addstr(0, 0, "KNIGHT Industries, System Security Interface")
    stdscr.addstr(1, 0, "Version 0.9.1, Alpha E")
    stdscr.addstr(2, 0, "")

    # Wait...    
    stdscr.refresh()
    time.sleep(sleep_interval)

    # Add output
    stdscr.addstr(3, 0, "Serial Number:                                                 Alpha Delta 227529, Rev. B")
    stdscr.addstr(4, 0, "Vehicle Registration:                              CALIFORNIA KNIGHT              05/1982")
    stdscr.addstr(5, 0, "Authorized Drivers:                                Knight, Michael             1952/07/17")
    stdscr.addstr(6, 0, "                                                   Kraus,  Marcel              1984/06/29")
    stdscr.addstr(7, 0, "")

    # Wait...
    stdscr.refresh()
    time.sleep(sleep_interval)

    # Add output
    stdscr.addstr( 8, 0, "> System Main")
    stdscr.addstr( 9, 0, "Loading main containment enclosure...")
    stdscr.addstr(10, 0, "Data Link Layer                                                                     [OK]")
    stdscr.addstr(11, 0, "Communication Layer                                                                 [OK]")
    stdscr.addstr(12, 0, "Application Layer                                                                   [OK]")
    stdscr.addstr(13, 0, "")
	
	# Wait...
    stdscr.refresh()
    time.sleep(sleep_interval)
    
    # Add output
    stdscr.addstr(14, 0, "> System Multimedia")
    stdscr.addstr(15, 0, "Loading multimedia enclosure...")
    stdscr.addstr(16, 0, "Audio Playback                                                                      [OK]")
    stdscr.addstr(17, 0, "Video Playback                                                                      [OK]")
    stdscr.addstr(18, 0, "Voice Recognition                                                             [DISABLED]")
    stdscr.addstr(19, 0, "")
    
	# Wait...
    stdscr.refresh()
    time.sleep(sleep_interval)
    
    # Add output
    stdscr.addstr(20, 0, "> System Security")
    stdscr.addstr(21, 0, "Loading main security enclosure...")
    stdscr.addstr(22, 0, "Primary Firewall                                                                    [OK]")
    stdscr.addstr(23, 0, "Secondary Firewall                                                                  [OK]")
    stdscr.addstr(24, 0, "Logging/Keychecks                                                                [ERROR]")
    stdscr.addstr(25, 0, "WARNING: Unrecognizable object \"whte_rbt.obj\" found. Proceeding... ")
    stdscr.addstr(26, 0, "")
       
	# Wait...
    stdscr.refresh()
    time.sleep(sleep_interval)
    
    # Add output
    stdscr.addstr(27, 0, "System Ready")
    stdscr.addstr(28, 0, "")
    stdscr.refresh()
    
    # Wait for keypress
    while True:
        key = stdscr.getch()
        
        available_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
        dictate_voice = "Anna"
        dictate_rate = 225
             
        # Break if abort key is pressed
        if key == ord('z'):
            break
        elif chr(key) in available_keys:
        	# Handle dictate playback
            if os.path.isfile("dictates/" + chr(key) + ".txt"):
                os.system("say -r " + str(dictate_rate) + " -v " + dictate_voice + " -f " + "dictates/" + chr(key) + ".txt")
        	# Handle audio playback
            elif os.path.isfile("audios/" + chr(key) + ".wav"):
                os.system("afplay audios/" + chr(key) + ".wav")
        	# Handle video playback
            elif os.path.isfile(path = "videos/" + chr(key) + ".mp4"):
            	# Opens video in default player
                os.system("open videos/" + chr(key) + ".mp4")
        	# Fallback to error message
            else:
                stdscr.addstr("\n> ERROR: A handler file for key \"" + chr(key) + "\" was not found. Create a file to handle this key.")          
            
    # Exit Curses and return to default console
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
           
  except:
      # Abort by user, terminal or source code
      stdscr.keypad(0)
      curses.echo()
      curses.nocbreak()
      curses.endwin()
      traceback.print_exc() 

else:
    print ("Startinitialisierung nicht gesetzt")
