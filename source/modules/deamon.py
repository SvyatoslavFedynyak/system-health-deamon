import os
import sys
import time
import atexit

DEFAULT_STD = '/dev/null'


class AbstractDeamon():
    '''Class for main deamon process'''

    def __init__(self,
                 pidfile,
                 stdin=DEFAULT_STD,
                 stdout=DEFAULT_STD,
                 stderr=DEFAULT_STD):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def deamonize(self):
        '''Main method for running deamon'''
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as error:
            sys.stderr.write('Fork #1 failed: {0} ({1})\n'.format(
                error.errno, error.strerror))
            sys.exit(1)

        os.chdir("/")
        os.setsid()
        os.umask(0)

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as error:
            sys.stderr.write('Fork #1 failed: {0} ({1})\n'.format(
                error.errno, error.strerror))
            sys.exit(1)

        sys.stdout.flush()
        sys.stderr.flush()
        with open(self.stdin, 'r') as sys_input:
            os.dup2(sys_input.fileno(), sys.stdin.fileno())
        with open(self.stdout, 'a+') as sys_output:
            os.dup2(sys_output.fileno(), sys.stdout.fileno())
        with open(self.stderr, 'a+', 0) as sys_error:
            os.dup2(sys_error.fileno(), sys.stderr.fileno())

        atexit.register(self.delpid)
        pid = str(os.getpid())
        with open(self.pidfile, 'w+') as pidf:
            pidf.write("{0}\n".format(pid))

    def delpid(self):
        '''Removes PID file'''
        os.remove(self.pidfile)

    def start(self):
        '''Starts the deamon'''
        try:
            with open(self.pidfile, 'r') as pidf:
                pid = int(pidf.read().strip())
        except IOError:
            pid = None

        if pid:
            message = "pidfile {0} already exist. Daemon already running?\n"
            sys.stderr.write(message.format(self.pidfile))
            sys.exit(1)

        self.deamonize()
        self.run()

    def stop(self):
        """Stop the daemon"""
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
        except IOError:
            pid = None

        if not pid:
            message = "pidfile {0} does not exist. Daemon not running?\n"
            sys.stderr.write(message.format(self.pidfile))
            return
