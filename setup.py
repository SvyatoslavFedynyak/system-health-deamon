import os
import shutil
import setuptools
import setuptools.command.install as install

with open('requirements.txt') as f:
    required = f.read().splitlines()

class PostInstallCommand(install.install):
    """Make dirs for config and log"""
    def run(self):
        install.install.run(self)
        config_dir = os.path.join('/etc', 'system-health-daemon')
        log_dir = os.path.join('/var', 'log', 'system-health-daemon')
        if not os.path.exists(config_dir):
            os.mkdir(config_dir)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        shutil.copy(os.path.join('source', 'config', 'daemon.cfg'), os.path.join('/etc', 'system-health-daemon', 'daemon.cfg'))


setuptools.setup(
    name='system-health-daemon',
    version='1.0',
    description='System Health Daemon',
    author='Svyatoslav Fedynyak',
    python_requires='~=3.8',
    packages=setuptools.find_packages(),
    install_requires=required,
    include_package_data=True,
    url='https://github.com/SvyatoslavFedynyak/system-health-deamon',
    cmdclass={
        'install': PostInstallCommand
    },
    entry_points={
        'console_scripts':
        ['system-health-daemon = source.main:main']
    }
)