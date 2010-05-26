"""emacs timelog compatible thing"""
from datetime import datetime

def clock_in(reason, log_dir, _now=None):
    if _now is None:
        _now = datetime.now()
    return False

def clock_out(reason, log_dir, _now=None):
    if _now is None:
        _now = datetime.now()
    return False
