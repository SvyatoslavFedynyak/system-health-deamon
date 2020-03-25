"""This module implements realization of collctor's worker"""

import re
import json
import datetime


class Worker:
    """Class for worker"""

    name = ''
    funcs = []
    func_reports = []
    worker_report = ''

    def __init__(self, name, module):
        self.name = name
        self.get_funcs(module)

    def get_funcs(self, module):
        """Get worker's functions from modules"""
        for item in dir(module):
            func = getattr(module, item)
            if callable(func) and re.match('^{0}'.format(self.name), func.__name__):
                self.funcs.append(func)

    def compose_report(self, reports):
        """Get list of func's reports and compose worker's report (json-formated string) from them"""
        report = {}
        report['name'] = self.name
        report['datetime'] = str(datetime.datetime.now())
        report['function_reports'] = []
        for func_report in reports:
            parsed_report = json.loads(func_report)
            report['function_reports'].append(parsed_report)
        return json.dumps(report, indent='\t')

    def run(self):
        """Invokes required functions and returns report"""
        self.func_reports.clear()
        self.worker_report = ''
        for func in self.funcs:
            self.func_reports.append(func())
        return self.compose_report(self.func_reports)