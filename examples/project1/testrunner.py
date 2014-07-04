#!/usr/bin/env python
from __future__ import print_function

import argparse
import os
import logging

from falafel import findout_terminal_width
from falafel import test_list
from falafel.runners import FalafelTestRunner
from falafel.loaders import FalafelTestLoader


parser = argparse.ArgumentParser(description='custom test runner for '
                                 'project1')
parser.add_argument("-S", "--suite", help="Test suite",
                    choices=['moda', 'modb'], type=str, required=True)
parser.add_argument("--test", action='append', help="Testcase(s)/Test(s) "
                    "to run")
parser.add_argument("-L", "--list", action="store_true",
                    help="List tests which match the specified "
                    "suite/testcases(s)")
parser.add_argument("--pdb", action="store_true",
                    help="drop into pdb/ipdb in case of a failure/error")
parser.add_argument("--log", action="store_true",
                    help='write all log messages + header and footer of '
                    'each test to a logfiles in a dirctory specified with '
                    '--logdirectory. If the logdirectory does not exist '
                    'it gets automatically.')
parser.add_argument("-d", "--logdirectory",
                    help="log directory [default=%(default)s]",
                    default='log')
parser.add_argument("--debug", action="store_true",
                    help="print logging messages")
parser.add_argument("--interactive", '--enable-interactive-tests',
                    action="store_true", dest='interactive',
                    help="if not set then all interactive tests are skipped")

args = parser.parse_args()

pkg = args.suite
allowed_tests = args.test

width = findout_terminal_width()

print(" info ".center(width, '='))
print("suite: %s" % pkg)
print("tests: %s" % allowed_tests)
print("interactive tests: %s" % args.interactive)
print('=' * width)

if args.interactive:
    os.environ['INTERACTIVE_TESTS'] = '1'

loader = FalafelTestLoader(allowed_tests=allowed_tests)
suite = loader.discover('mypackage.' + pkg)

tdata = []
if args.debug or args.list:
    with_skipped = args.list
    tdata = test_list(suite, with_skipped=with_skipped)
    if not with_skipped:
        print("The following tests will be run:", end='')
    try:
        from tabulate import tabulate
    except ImportError:
        for data in tdata:
            print("  %-30s\t(in %s)%s" % data)
    else:
        headers = ['class.method', 'module']
        if not with_skipped:
            headers.append('skipped')
        print('\n%s' % tabulate(tdata, headers=headers))
    print("%d tests available" % len(tdata))
    if args.list:
        exit()

logdir = args.logdirectory if args.log else None
runner = FalafelTestRunner(
    verbosity=2, logger='st', debug=args.debug,
    logdirectory=logdir, width=width, pdb=args.pdb)
runner.run(suite)
