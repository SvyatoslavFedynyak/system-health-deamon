import modules.workers.worker as worker
import modules.functions.cpu_functions as functions
import json

class CpuWorker(worker.Worker):
    '''Class for CPU worker'''

    name = 'CPU'

    def __init__(self):
        self.get_funcs(functions)

    def compose_report(self, reports):
        '''Get list of func's reports and compose worker's report (string) from them'''
        report = ''
        json_data = json.dumps(reports['CPU_currentTimes'])
        parsed_json = json.load(json_data)
        report += 'CPU times:\n'
        for idx, cpu in enumerate(parsed_json):
            report += '--- CPU{0} ---\n user time: {1}\nsystem time: {2}'.format(str(idx), cpu['user'], cpu['system'])
        return report

    def run(self):
        '''Invokes required functions and returns report'''
        for func in self.funcs:
            self.func_reports[func.__name__] = func()
        return {
            self.name : self.compose_report(self.func_reports)
        }

