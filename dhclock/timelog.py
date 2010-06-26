"""emacs timelog compatible thing"""
from __future__ import with_statement
import os
from datetime import datetime

CLOCK_IN = 0
CLOCK_OUT = 1

def clock_in(reason, log_path, _now=None):
    return clock(CLOCK_IN, reason, log_path, _now)

def clock_out(reason, log_path, _now=None):
    return clock(CLOCK_OUT, reason, log_path, _now)

def clock(inout, reason, log_path, now):
    control_dict = {
        CLOCK_IN: dict(
            this_guy='i',
            that_guy='o',
            order_error='already clocked in',
            ),
        CLOCK_OUT: dict(
            this_guy='o',
            that_guy='i',
            order_error='not clocked in',
            ),
        }[inout]
    if now is None:
        now = datetime.now()
    lastline = None
    if os.path.exists(log_path):
        with open(log_path, 'r') as f:
            lines = f.readlines()
            if lines:
                lastline = lines[-1]
        logfile = open(log_path, 'a')
    else:
        if inout == CLOCK_OUT:
            raise RuntimeError(control_dict['order_error'])
        logfile = open(log_path, 'w')
    if lastline:
        parts = lastline.strip().split(' ')
        if len(parts) != 4:
            raise RuntimeError('invalid log file')
        if parts[0] != control_dict['that_guy']:
            raise RuntimeError(control_dict['order_error'])

    logfile.write(
        ' '.join(
            [
                control_dict['this_guy'],
                now.strftime("%Y/%m/%d"),
                now.strftime("%H:%M:%S"),
                reason + '\n',
                ],
            ),
        )
    logfile.close()
    return (control_dict['this_guy'], now)
