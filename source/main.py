import modules.manager as manager_module
import modules.logger as logger

manager = manager_module.Manager()
manager.create_workers()
reports = manager.run()
print(reports)
