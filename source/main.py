import modules.manager as manager_module
import modules.logger as logger

manager = manager_module.Manager()
manager.run()
print(manager.reports)
