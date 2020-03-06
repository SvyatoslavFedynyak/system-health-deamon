class Worker:
    '''Class for abstract worker'''

    def __init__(self):
        pass

    @property
    def functions(self):
        '''List of worksers functions'''

    def run(self):
        '''Overridde this in specialized workers
        Should return pair of worker_name:string_report'''
