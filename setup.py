#!/usr/bin/env python

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(name='IntroToSignalProcessing',
      version='0.1',
      description='Introduction to Signal Processing Notebooks for GRCon 2021',
      url='https://github.com/TheWylieStCoyote/Introduction_to_Signal_Processing_GRCon21',
      author='Wylie Standage-Beier',
      packages='notebooks',
      python_requires='>=3.0',
      install_requires=['jupyter','scipy','numpy','ipywidgets','matplotlib','matplotlib-helper','ipython'])
