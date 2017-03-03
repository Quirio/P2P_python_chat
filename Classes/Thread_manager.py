import os
import curses

class Thread_manager:
    def __init__(self,func,args):
        #Constants
        self.UMASK = 0
        self.WORKDIR = "/"
        self.MAXFD = 1024
        self.REDIRECT_tO = os.devnull

        self.stdscr = curses.initscr()

        self.create_deamon(func,args="")

    def create_deamon(self,action_func,args=""):
        try:
            self.pid = os.fork()
        except OSError, e:
            raise Exception, "%s [%d]" % (e.strerror, e.errno)

        if (self.pid == 0):
            os.setsid()
            os.chdir(self.WORKDIR)
            os.umask(self.UMASK)
        else:
            os._exit(0)

        action_func(*args)

    def remove_deamon(self):
        os._exit(self.pid)
