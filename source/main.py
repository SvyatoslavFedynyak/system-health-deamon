import modules.deamon as daemon
import sys
import os

if __name__ == '__main__':
    env_path = os.path.abspath('.')

    if len(sys.argv) < 2:
        print("Usage: {0} start|stop|restart".format(sys.argv[0]))
        sys.exit(2)

    daemon = daemon.CollectorDaemon(pidfile= env_path + '/tmp/daemon.pid',
                                    stdin='/dev/null',
                                    stdout= env_path + '/tmp/output.log',
                                    stderr= env_path + '/tmp/error.log')
    if sys.argv[1] == 'start':
        daemon.start()
    elif sys.argv[1] == 'stop':
        daemon.stop()
    elif sys.argv[1] == 'restart':
        daemon.restart()
    else:
        print("Unknown command '{0}'".format(sys.argv[1]))
        sys.exit(2)
