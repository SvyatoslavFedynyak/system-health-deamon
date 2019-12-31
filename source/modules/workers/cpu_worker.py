class CpuWorker:
    '''Class for CPU worker'''

    functions = []

    def __init__(self):
        pass

    def run(self):
        '''Invokes required functions and returns report'''
        functions.append(get_cpu_load)

def get_cpu_load():
    '''Returns CPU load in %'''
    return 100