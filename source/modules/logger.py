import json

class Logger:
    '''Class for daemons logger
    It processes json report from manager,
    builds human-readable text reports
    and write it to output/error logs'''

    composers = []

    def __init__(self, stdout, stderr):
        self.stdout = stdout
        self.stderr = stderr

    def get_composers(self, module):
        '''Get logger composers from module'''
        for item in dir(module):
            composer = getattr(module, item)
            if callable(composer):
                self.composers.append(composer)


    def compose_report(self, json_report):
        '''Run all functional composers and compose final report'''
        final_report = ''
        