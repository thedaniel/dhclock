#!/usr/bin/env/python

from distutils.core import setup

setup(
    name='dhclock',
    description='dhclock - emacs timelog compatible tools',
    author='Daniel Hengeveld',
    author_email='danielwh@gmail.com',
    url='http://helloanteater.com',
    packages=['dhclock'],
    scripts=['scripts/dhclock'],
    )
