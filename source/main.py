import modules.deamon as daemon
import argparse
import sys
import os

def load_config(path):
    '''Loads config from file'''
    config_dict = {}
    with open(path, 'r') as fp:
        for line in fp.read().splitlines():
            line = line.rstrip()
            if line != '':
                if line[0] != '#':
                    pair = line.split('=')
                    config_dict[pair[0]] = pair[1]
    return config_dict

if __name__ == '__main__':

    env_path = os.path.abspath(os.path.dirname(''))

    # Argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="command, given to daemon. Possible options: start|stop|restart", type=str)
    parser.add_argument("-c", "--config", help="config file path", type=str)
    args = parser.parse_args()

    # Get app paths and parse config file
    if args.config:
        config_path = args.config
    else:
        config_path = os.path.abspath(os.path.join(env_path, '..', 'config', 'daemon.cfg'))
    config = load_config(config_path)

    root_dir = config['root_dir']
    pid_path = os.path.abspath(os.path.join(root_dir, config['pid_path']))
    output_path = os.path.abspath(os.path.join(root_dir, config['output_log']))
    error_path = os.path.abspath(os.path.join(root_dir, config['error_log']))

    daemon = daemon.CollectorDaemon(pidfile=pid_path,
                                    stdin='/dev/null',
                                    stdout=output_path,
                                    stderr=error_path)
    if args.command == 'start':
        daemon.start()
    elif args.command == 'stop':
        daemon.stop()
    elif args.command == 'restart':
        daemon.restart()
    else:
        print(args.help)
        sys.exit(2)
