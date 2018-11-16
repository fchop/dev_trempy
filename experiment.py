#!/usr/bin/env python
"""Experiment with the trempy package."""

from trempy.read.read import read

init_dict = read('simulate.trempy.ini')

print(init_dict)
