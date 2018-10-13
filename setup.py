from setuptools import setup
from setuptools import find_packages

setup(name='gitreview',
      version='0.1',
      description='Small package to pull braches locally to review them',
      author='Gabriel de Marmiesse',
      author_email='gabriel.de-marmiesse@valeo.com',
      license='MIT',
      packages=find_packages(),
      entry_points={'console_scripts': ['pull_branch = gitreview:pull_branch']},
      install_requires=['click']
      )
