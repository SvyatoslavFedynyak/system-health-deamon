import modules.abstract_deamon as deamon
import modules.manager as manager
import modules.logger as logger
import time

DEFAULT_STD = '/dev/null'

class CollectorDaemon(deamon.AbstractDaemon):
    '''Class for daemon which will be doing all the stuff'''

    def __init__(self,
                 config):
        
        deamon.AbstractDaemon.__init__(self, config['pid_path'], '/dev/null', config['output_log'], config['error_log'])
        self.interval = config['interval']
        self.manager = manager.Manager()
        self.logger = logger.Logger(self.stdout, self.stderr)


    def run(self):
        while True:
            self.logger.run(self.manager.run())
            time.sleep(int(self.interval))