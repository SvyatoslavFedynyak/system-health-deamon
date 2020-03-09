import re


class Worker:
    '''Class for abstract worker'''

    name = ''
    funcs = []
    func_reports = {}
    worker_report = ''

    def get_funcs(self, module):
        '''Get worker's functions from modules'''
        for item in dir(module):
            func = getattr(module, item)
            if callable(func) and re.match('^{0}'.format(self.name), func.__name__):
                self.funcs.append(func)

    def run(self):
        '''Overridde this in specialized workers
        Should return pair of worker_name:string_report'''
