#!/usr/bin/env python

from distutils.core import setup
import glob

data_files=glob.glob('srs/prange/data/*.txt')

setup(name='prange',
      version='0.1',
      description='A Complex Python Progress Meter',
      author='Logan Zoellner',
      author_email='nagolinc@gmail.com',
      url='https://github.com/nagolinc/prange',
      
      packages=['prange'],
      package_dir={'prange': 'src/prange'},
      data_files=[('data',data_files)]
     )
