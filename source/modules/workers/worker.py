import asyncio

class worker:
    def __init__(self, name):
        self.name = name

    @property
    def functions(self):
        '''List of worksers functions'''
        return self.reports

    async def run(self):
        '''Overridde this in specialized workers'''