import modules.workers.cpu_worker as cpu_worker
import asyncio


class Manager:

    ''' Class for workers manager'''

    workers = []
    reports = {}

    def __init__(self):
        self.create_workers()

    def create_workers(self):
        ''' Create appropriate workers and put them in list'''
        self.workers.append(cpu_worker.CpuWorker())

    async def worker_wrapper(self, loop, worker):
        '''Async wrapper for workers run() func'''
        return await loop.run_in_executor(None, worker.run)

    def run(self):
        '''Run all workers async, get report from result and add put it into dict'''
        # define event loop and tasks list
        ioloop = asyncio.get_event_loop()
        tasks = []

        # compose workers as tasks to event loop
        for worker in self.workers:
            tasks.append(ioloop.create_task(self.worker_wrapper(ioloop, worker)))
        
        # run tasks and get list of coroutines
        coroutines, _ = ioloop.run_until_complete(asyncio.wait(tasks))

        # get report pairs from coroutines
        for coroutine in coroutines:
            # coroutine.result() is dict with one pair
            report_dict = coroutine.result()

            # loop will run only once but it's only way (I suppose) to get unknown key:value
            for key in report_dict:
                self.reports[key] = report_dict[key]
        ioloop.close()  
