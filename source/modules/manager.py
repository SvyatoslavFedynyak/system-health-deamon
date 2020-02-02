import modules.workers.cpu_worker as cpu_worker
import asyncio

class Manager:

    ''' Class for workers manager'''

    workers = []

    def __init__(self):
        pass

    def create_workers(self):
        ''' Create appropriate workers and put them in list'''
        self.workers.append(cpu_worker.CpuWorker())

    def run(self):
        '''Run all workers async, get report from result and add put it into dict'''
        for worker in self.workers:
            # workers 
            self.reports[worker.name] = await worker.run()
        return self.reports

    @property
    def reports(self):
        '''Dict with {name, report} items'''
        return self.reports
        