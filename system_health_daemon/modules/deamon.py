"""This module implements realization of data collector daemon"""

import modules.abstract_deamon as deamon
import modules.manager as manager
import modules.logger as logger
import time

DEFAULT_STD = '/dev/null'

class CollectorDaemon(deamon.AbstractDaemon):
    """Class for daemon which will be doing all the stuff"""

    def __init__(self,
                 config):
        
        deamon.AbstractDaemon.__init__(self, config['pid_path'], DEFAULT_STD, config['output_log'], config['error_log'])
        self.interval = config['interval']
        self.manager = manager.Manager()
        self.logger = logger.Logger(self.stdout, self.stderr)


    def run(self):
        while True:
            json_report = self.manager.run()
            self.logger.run(json_report)
            time.sleep(int(self.interval))