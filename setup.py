from setuptools import find_packages
from setuptools import setup

setup(name='patchclamp',
      version='0.1',
      author='Eamon Byrne',
      packages=find_packages(),
      install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'pyabf',
        'glob',
        'seaborn',
        'matplotlib',
    ],
     )