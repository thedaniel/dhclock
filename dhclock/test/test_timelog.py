from __future__ import with_statement

"""tests for dhclock.timelog"""

import datetime
import os
import tempfile
import unittest

from dhclock import timelog
from dhclock.test import util

class TestClockInOut(unittest.TestCase):
    def test_no_file_in(self):
        tempdir = tempfile.mkdtemp()
        now = datetime.datetime(2010, 05, 01)
        timelog.clock_in(reason='test', log_dir=tempdir, _now=now)
        assert 'timelog' in os.listdir(tempdir)
        with open(os.path.join(tempdir, 'timelog'), 'w') as f:
            lines = f.readlines()
            assert len(lines) == 1
            assert lines[0] == ' '.join(
                [
                    'i',
                    now.strftime("%Y/%m/%d"),
                    now.strftime("%H:%M:%S"),
                    'test',
                    ]
                )

    def test_no_file_out(self):
        tempdir = tempfile.mkdtemp()
        now = datetime.datetime(2010, 05, 01)
        e = util.raises(
            RuntimeError,
            timelog.clock_out,
            reason='test',
            log_dir=tempdir,
            _now=now,
            )
        assert str(e) == 'not clocked in'
        assert 'timelog' not in os.listdir(tempdir)

    def test_empty_file(self):
        tempdir = tempfile.mkdtemp()
        f = open(os.path.join(tempdir, 'timelog'), 'w')
        f.close()
        now = datetime.datetime(2010, 05, 01)
        timelog.clock_in(reason='test', log_dir=tempdir, _now=now)
        assert 'timelog' in os.listdir(tempdir)
        with open(os.path.join(tempdir, 'timelog')) as f:
            lines = f.readlines()
            assert len(lines) == 1
            assert lines[0] == ' '.join(
                [
                    'i',
                    now.strftime("%Y/%m/%d"),
                    now.strftime("%H:%M:%S"),
                    'test',
                    ]
                )

    def test_wrong_order(self):
        tempdir = tempfile.mkdtemp()
        with open(os.path.join(tempdir, 'timelog'), 'w') as f:
            f.write('i 2010/03/16 12:20:19 misc\n')
        now = datetime.datetime(2010, 03, 17)
        e = util.raises(
            RuntimeError,
            timelog.clock_out,
            reason='test',
            log_dir=tempdir,
            _now=now,
            )
        assert str(e) == "already clocked in"
        assert 'timelog' in os.listdir(tempdir)
        with open(os.path.join(tempdir, 'timelog')) as f:
            lines = f.readlines()
            assert lines == ['i 2010/03/16 12:20:19 misc']

    def test_partial_file(self):
        tempdir = tempfile.mkdtemp()
        with open(os.path.join(tempdir, 'timelog'), 'w') as f:
            f.write('i 2010/03/16 12:20:19 misc\n')
            f.write('o 2010/03/16 12:22:19 out\n')
        now = datetime.datetime(2010, 03, 17)
        with open(os.path.join(tempdir, 'timelog'), 'w') as f:
            lines = f.readlines()
            assert len(lines) == 1
            assert lines ==[
                [
                    'i 2010/03/16 12:20:19 misc',
                    'o 2010/03/16 12:22:19 out',
                    ],
                ' '.join(
                    [
                        'i',
                        now.strftime("%Y/%m/%d"),
                        now.strftime("%H:%M:%S"),
                        'test',
                        ]
                    ),
                ]

class TestReports(unittest.TestCase):
    def test_summary(self):
        pass #nyi
    def test_timeseries(self):
        pass #nyi

if __name__ == "__main__":
    unittest.main()
