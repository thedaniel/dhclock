#!/usr/bin/env python
import os
from optparse import OptionParser
from ConfigParser import ConfigParser

from dhclock import timelog

# TODO this should have the same default as emacs
LOG_PATH = os.path.expanduser('~/.timelog')
CONFIG_PATH = os.path.expanduser('~/.dhclock')

def clock():
    parser = OptionParser()
    parser.add_option(
        '-l',
        '--log',
        dest='log_path',
        help="location of timelog file",
        )
    parser.add_option(
        '--c',
        '--config',
        dest='config_path',
        help="path to config file",
        )
    opts, args = parser.parse_args()
    log_path = opts.log_path # None if unset
    config_path = opts.config_path
    if config_path is None:
        config_path = CONFIG_PATH
    if os.path.exists(config_path):
        conf = ConfigParser()
        conf.read([config_path])
        log_path = conf.get('log_path', None)
    if log_path is None:
        log_path = LOG_PATH
    if len(args) != 2:
        parser.error('use: clock.py in/out reason')
    if args[0] == 'in':
        timelog.clock_in(args[1], log_path)
    elif args[0] == 'out':
        timelog.clock_out(args[1], log_path)
    elif args[0] == 'switch':
        timelog.clock_out('switch', log_path)
        timelog.clock_in(args[1], log_path)
    else:
        parser.error('use: clock.py in/out/switch reason')
