import os
import sys
import time

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
        sys_input = open(self.stdin, 'r')
        sys_output = open(self.stdout, 'a+')
        sys_error = open(self.stderr, 'a+', 0)
        os.dup2(sys_input.fileno(), sys.stdin.fileno())
        os.dup2(sys_output.fileno(), sys.stdout.fileno())
        os.dup2(sys_error.fileno(), sys.stderr.fileno())