#!/usr/bin/env python3
# encoding: utf-8
from setuptools import setup, find_packages
from setuptools.command.sdist import sdist

import os
import sys


used = sys.version_info
required = (3, 6)

# if version of pip that doesn't understand the python_requires classifier, must be pip >= 9.0.0
# must be built using at least version 24.2.0 of setuptools
# in order for the python_requires argument to be recognized and the appropriate metadata generated
# python -m pip install --upgrade pip setuptools
if used[:2] < required:
    sys.stderr.write("Unsupported Python version: %s.%s. "
                     "Python 3.6 or later is required." % (sys.version_info.major, sys.version_info.minor))
    sys.exit(1)

short_desc = "A tkinter based GUI application that helps you count money."


def read_readme(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()



#class Sdist(sdist):
#    """Custom ``sdist`` command to ensure that mo files are always created."""
#
#    def run(self):
#        self.run_command('compile_catalog')
#        sdist.run(self)


from setuptools.command.install import install

class InstallWithCompile(install):
    def run(self):
        from babel.messages.frontend import compile_catalog
        compiler = compile_catalog(self.distribution)
        option_dict = self.distribution.get_option_dict('compile_catalog')
        compiler.domain = [option_dict['domain'][1]]
        compiler.directory = option_dict['directory'][1]
        compiler.run()
        super().run()


setup(name='count-money',
      version=__import__('count_money').__version__,
      description=short_desc,
      packages=find_packages(),
      long_description=read_readme('README.md'),  # for PyPI
      long_description_content_type="text/markdown",
      license='MIT',
      url='https://no-title.victordomingos.com/projects/contar-dinheiro/',  # homepage
      python_requires='>=3.6',
      setup_requires=['Babel'],

      #cmdclass={'sdist': Sdist},
      
      cmdclass = { 'install': InstallWithCompile, },
      
      classifiers=[
        'Development Status :: 5 - Production/Stable ',
        'Environment :: MacOS X',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux ',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
        'Topic :: Desktop Environment :: File Managers',
        'Topic :: System :: Filesystems',

      ],
    
      keywords='money count sum coins bills gui accounting commerce',
      entry_points={
          'console_scripts': [
              'count-money = count_money.__main__:main'
          ]
      },

      package_data={'': ['locales/*/*/*.mo', 'locales/*/*/*.po']},

      project_urls={
        'Documentation': 'https://github.com/victordomingos/ContarDinheiro.py/blob/master/README.md',
        'Source': 'https://github.com/victordomingos/ContarDinheiro.py',
        'Bug Reports': 'https://github.com/victordomingos/ContarDinheiro.py/issues',
      },
      )
