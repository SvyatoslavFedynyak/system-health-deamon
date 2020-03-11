import modules.manager as manager_module
import modules.logger as logger_module

manager = manager_module.Manager()
logger = logger_module.Logger('log.log', '/dev/null')
logger.run(manager.run())
