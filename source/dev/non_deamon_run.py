import sys
import os

SOURCE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(SOURCE_DIR)

import modules.deamon as daemon

def main():

    config = {}
    output = os.path.join(SOURCE_DIR, 'tmp/output.log')
    error = os.path.join(SOURCE_DIR, 'tmp/error.log')
    
    open(output, 'w').close()
    open(error, 'w').close()

    config['pid_path'] = os.path.join(SOURCE_DIR, 'tmp/daemon.pid')
    config['output_log'] = output
    config['error_log'] = error
    config['interval'] = 3

    daemon_obj = daemon.CollectorDaemon(config)

    daemon_obj.run()
    

if __name__ == "__main__":
    main()