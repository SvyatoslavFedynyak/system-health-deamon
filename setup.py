import setuptools

with open('../requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='system-health-daemon',
    version='1.0',
    packages=setuptools.find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts':
        ['system-health-daemon = main:main']
    }
)