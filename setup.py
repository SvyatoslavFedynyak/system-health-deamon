import os
import shutil
import setuptools
import setuptools.command.install as install

CONFIG_DIR = os.path.join('/etc', 'system-health-daemon')
LOG_DIR = os.path.join('/var', 'log', 'system-health-daemon')
CONFIG_PATH = os.path.join(CONFIG_DIR, 'daemon.cfg')
SERVICE_PATH = os.path.join('/lib', 'systemd', 'system', 'system-health-daemon.service')

with open('requirements.txt') as f:
    required = f.read().splitlines()

class PostInstallCommand(install.install):
    """Make dirs for config and log"""
    def run(self):
        install.install.run(self)
        if not os.path.exists(CONFIG_DIR):
            os.mkdir(CONFIG_DIR)
        if not os.path.exists(LOG_DIR):
            os.mkdir(LOG_DIR)

        # Config setup
        shutil.copy(os.path.join('system_health_daemon', 'config', 'daemon.cfg'), CONFIG_PATH)
        os.chown(CONFIG_PATH, 0, 0)

        # Systemd unit setup
        shutil.copy(os.path.join('system_health_daemon', 'config', 'systemd-unit.service'), SERVICE_PATH)
        os.chown(SERVICE_PATH, 0, 0)


setuptools.setup(

    # Package metadata
    name='system_health_daemon',
    version='1.0',
    description='System Health Daemon',
    author='Svyatoslav Fedynyak',
    author_email='svyatoslav912@gmail.com',
    url='https://github.com/SvyatoslavFedynyak/system-health-deamon',

    # Requirements
    python_requires='>3.8',
    packages=setuptools.find_packages(),
    install_requires=required,
    include_package_data=True,
    cmdclass={
        'install': PostInstallCommand
    },
    entry_points={
        'console_scripts':
        ['system-health-daemon = system_health_daemon.main:main']
    }
)