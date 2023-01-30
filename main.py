#!/usr/bin/python3

import curses
import os
import random
import time

start = 'init'
sleep_interval = 0 # was 2
the_void = os.open('/dev/null', os.O_WRONLY)
video_player = "vlc" # was omxplayer --no-osd --hw
assets_directory = "assets"

def play_video(path):
    original_file_descriptor = os.dup(1)
    os.dup2(the_void, 1)
    os.system(video_player + " " + path)
    os.dup2(original_file_descriptor, 1)

if start == 'init':
  try:

    # Initialize main window
    main_window = curses.initscr()

    # Shut off output
    curses.noecho()
    # Shut off line buffer
    curses.cbreak()
    # Make cursor and special keys available
    main_window.keypad(False)
    curses.curs_set(0)

    # Define colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Assign defined colors
    main_window.bkgd(curses.color_pair(1))
    main_window.refresh()

    # Add output
    main_window.addstr(4, 9, "KNIGHT Industries, System Security Interface")
    main_window.addstr(5, 9, "Version 0.9.1, Alpha E")

    # Wait...
    main_window.refresh()
    time.sleep(sleep_interval)

    # Add output
    main_window.addstr(7, 9, "Serial Number:                             Alpha Delta 227529, Mk. II")
    main_window.addstr(8, 9, "Vehicle Registration:          CALIFORNIA KNIGHT              05/1982")
    main_window.addstr(9, 9, "Authorized Operator:           Kraus,  Marcel              1984/06/29")

    # Wait...
    main_window.refresh()
    time.sleep(sleep_interval)

    # Add output
    main_window.addstr(11, 9, "> System Main: Loading main containment enclosure...")
    main_window.addstr(12, 9, "Data Link Layer                                                  [OK]")
    main_window.addstr(13, 9, "Communication Layer                                              [OK]")
    main_window.addstr(14, 9, "Application Layer                                                [OK]")

	# Wait...
    main_window.refresh()
    time.sleep(sleep_interval)

    # Add output
    main_window.addstr(16, 9, "> System Security: Loading main security enclosure...")
    main_window.addstr(17, 9, "Firewalls                                                        [OK]")
    main_window.addstr(18, 9, "Logging/Keychecks                                             [ERROR]")
    main_window.addstr(19, 9, "WARNING: Unrecognizable object \"whte_rbt.obj\" found. Proceeding...")

	# Wait...
    main_window.refresh()
    time.sleep(sleep_interval)

    # Add output
    main_window.addstr(21, 9, "> System Multimedia: Loading multimedia enclosure...")
    main_window.addstr(22, 9, "Video Playback                                                   [OK]")
    main_window.addstr(23, 9, "Voice Recognition                                          [DISABLED]")

	# Wait...
    main_window.refresh()
    time.sleep(sleep_interval)

    # Add output
    main_window.addstr(25, 9, "System Ready")
    main_window.refresh()

    # Wait for keypress
    while True:
        all_assets = os.listdir(assets_directory)
        assets = []
        for i in all_assets:
            if i[0] != ".":
                assets.append(i)

        available_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "s", "t", "u", "v", "w", "x"]
        key = main_window.getch()

        if key == ord('r'):
            play_video("'" + assets_directory + "/" + random.choice(assets) + "'")
        elif chr(key) in available_keys:
            play_video(assets_directory + "/" + chr(key) + "_*.*")

  except:
      # Abort by user, terminal or source code
      main_window.keypad(False)
      curses.echo()
      curses.nocbreak()
      curses.endwin()

else:
    print ("Startinitialisierung nicht gesetzt")
