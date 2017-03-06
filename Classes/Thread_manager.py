import os
import curses

class Thread_manager:
    def __init__(self,func,*args):
        print (args)
        #Constants
        self.UMASK = 0
        self.WORKDIR = "/"
        self.MAXFD = 1024
        self.REDIRECT_tO = os.devnull

        self.stdscr = curses.initscr()

        self.args = args
        self.func = func

        self.create_deamon()

        return self.pid

    def create_deamon(self):
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

        self.func(self.args)

    def remove_deamon(self):
        os._exit(self.pid)
