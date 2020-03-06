import modules.workers.worker as worker

class CpuWorker(worker.Worker):
    '''Class for CPU worker'''

    name = 'CPU'

    def run(self):
        '''Invokes required functions and returns report'''
        return {
            self.name : get_cpu_load()
        }

def get_cpu_load():
    '''Returns CPU load in %'''
    return 100