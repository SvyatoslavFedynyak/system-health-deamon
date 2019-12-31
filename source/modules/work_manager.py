import modules.workers.cpu_worker as cpu_worker

class work_manager:
    def __init__(self):
        pass

    def echo(self):
        print('work-manger')
        worker = cpu_worker.cpu_worker()
        worker.echo()