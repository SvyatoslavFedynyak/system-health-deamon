import json
import modules.composers as composers


class Logger:
    '''Class for daemons logger
    It processes json report from manager,
    builds human-readable text reports
    and write it to output/error logs'''

    composers = {}

    def __init__(self, stdout, stderr):
        self.stdout = stdout
        self.stderr = stderr
        self.get_composers(composers)

    def get_composers(self, module):
        '''Get logger composers from module'''
        for item in dir(module):
            composer = getattr(module, item)
            if callable(composer):
                self.composers[composer.__name__.split('_')[0]] = composer

    def compose_report(self, json_report):
        '''Run all functional composers and compose final report'''
        parsed_json_report = json.loads(json_report)
        final_report = '\n{0}\nDate: {1}'.format(
            parsed_json_report['name'], parsed_json_report['datetime'])
        for composer_name in self.composers:
            for worker_report in parsed_json_report['worker_reports']:
                if composer_name == worker_report['name']:
                    final_report += '\n'
                    final_report += self.composers[composer_name](
                        json.dumps(worker_report))
                    break
        return final_report
                
    def run(self, json_report):
        with open(self.stdout, 'a') as stdout:
            stdout.write(self.compose_report(json_report))
