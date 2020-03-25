import configparser
import argparse
import sys
import os

sys.path.append(os.path.dirname(__file__))

import modules.deamon as daemon

def main():

    # Argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="command, given to daemon. Possible options: start|stop|restart", type=str)
    parser.add_argument("-c", "--config", help="config file path", type=str)
    args = parser.parse_args()

    # Get app paths and parse config file
    config = configparser.ConfigParser()
    if args.config:
        config_path = args.config
    else:
        config_path = os.path.abspath(os.path.join('/etc', 'system-health-daemon', 'daemon.cfg'))

    with open(config_path, 'r') as file:
        config.read_file(file)
    
    daemon_obj = daemon.CollectorDaemon(config['Collector'])
    
    if args.command == 'start':
        daemon_obj.start()
    elif args.command == 'stop':
        daemon_obj.stop()
    elif args.command == 'restart':
        daemon_obj.restart()
    else:
        print(args.help)
        sys.exit(2)

if __name__ == "__main__":
    main()