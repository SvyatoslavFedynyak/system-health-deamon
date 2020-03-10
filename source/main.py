import modules.manager as manager_module
import modules.logger as logger

manager = manager_module.Manager()
with open('deamon_report.json', 'w') as file:
    file.write(manager.run())
