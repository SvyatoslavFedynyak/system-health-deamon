import json
import modules.subcomposers as subcomposers


class Composer:
    '''Class for daemons composer
    It processes json report from manager,
    builds human-readable text reports
    and write it to output/error logs'''

    subcomposers = {}

    def __init__(self, stdout, stderr):
        self.stdout = stdout
        self.stderr = stderr
        self.get_subcomposers(subcomposers)

    def get_subcomposers(self, module):
        '''Get logger subcomposers from module'''
        for item in dir(module):
            composer = getattr(module, item)
            if callable(composer):
                self.subcomposers[composer.__name__.split('_')[0]] = composer

    def compose_report(self, json_report):
        '''Run all functional subcomposers and compose final report'''
        parsed_json_report = json.loads(json_report)
        final_report = '\n{0}\nDate: {1}'.format(
            parsed_json_report['name'], parsed_json_report['datetime'])
        for subcomposer_name in self.subcomposers:
            for worker_report in parsed_json_report['worker_reports']:
                if subcomposer_name == worker_report['name']:
                    final_report += '\n'
                    final_report += self.subcomposers[subcomposer_name](
                        json.dumps(worker_report))
                    break
        return final_report
                
    def run(self, json_report):
        with open(self.stdout, 'a') as stdout:
            stdout.write(self.compose_report(json_report))
