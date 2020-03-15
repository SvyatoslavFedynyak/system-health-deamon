import modules.functions.cpu_functions as cpu_functions
import modules.worker as worker
import datetime
import json
import asyncio


class Manager:
    ''' Class for workers manager'''

    workers = []
    reports = []

    def __init__(self):
        self.create_workers()

    def create_workers(self):
        ''' Create appropriate workers and put them in list'''
        self.workers.append(worker.Worker('CPU', cpu_functions))

    async def worker_wrapper(self, loop, worker):
        '''Async wrapper for workers run() func'''
        return await loop.run_in_executor(None, worker.run)

    def compose_report(self, reports):
        '''Get list of func's reports and compose worker's report (json-formated string) from them'''
        report = {}
        report['name'] = 'Daemon report'
        report['datetime'] = str(datetime.datetime.now())
        report['worker_reports'] = []
        for worker_report in reports:
            parsed_report = json.loads(worker_report)
            report['worker_reports'].append(parsed_report)
        return json.dumps(report, indent='\t')

    def run(self):
        '''Run all workers async, get report from result and add put it into dict'''
        # define event loop and tasks list
        ioloop = asyncio.new_event_loop()
        tasks = []

        # compose workers as tasks to event loop
        for worker_taks in self.workers:
            tasks.append(ioloop.create_task(self.worker_wrapper(ioloop, worker_taks)))
        
        # run tasks and get list of coroutines
        coroutines, _ = ioloop.run_until_complete(asyncio.wait(tasks))

        # get report pairs from coroutines
        for coroutine in coroutines:
            # coroutine.result() is dict with one pair
            self.reports.append(coroutine.result())

        ioloop.close()
        return self.compose_report(self.reports)
