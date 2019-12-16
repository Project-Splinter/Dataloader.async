from setuptools import setup

INSTALL_REQUIREMENTS = ['torch']

setup(
    description='A asynchronous pytorch Dataloader for general neural network pipeline accelaration.',
    author='Ruilong Li',
    author_email='ruilongl@usc.edu',
    license='MIT License',
    version='0.0.0',
    name='dataloaderAsync',
    packages=['dataloaderAsync'],
    install_requires=INSTALL_REQUIREMENTS,
)