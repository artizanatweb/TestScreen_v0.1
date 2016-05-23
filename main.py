#!/usr/bin/env python

import pygame
import os
import sys
import signal
import Screen as scr


pygame.init()

# set process title so it can be killed on stop
try:
    import setproctitle
    setproctitle.setproctitle("jackpot-screen")
except:
    print "Can't set process name!"
    print "Install 'setproctitle' and try again."
    sys.exit(2)

if __name__ == '__main__':
    screen = scr.Screen()
    try:
        screen.setup()
        screen.loop()
    except (KeyboardInterrupt, SystemExit):
        # swServer.clear()
        print 'Keyboard Interrupt or System Exit'
    except:
        print "Exception: ", sys.exc_info()

    signal.signal(signal.SIGTERM, screen.signalTermHandler)


sys.exit(1)