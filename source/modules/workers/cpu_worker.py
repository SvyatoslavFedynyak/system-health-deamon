import modules.workers.worker as worker

class CpuWorker(worker.worker):
    '''Class for CPU worker'''

    async def run(self):
        '''Invokes required functions and returns report'''
        return get_cpu_load()

def get_cpu_load():
    '''Returns CPU load in %'''
    return 100