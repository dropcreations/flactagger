from setuptools import setup, find_packages

setup(
    name='mutagenFLAC',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'mutagen',
    ],
    entry_points='''
    [console_scripts]
    mutagenFLAC=mutagenFLAC:main
    '''
)
