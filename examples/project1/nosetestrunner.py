#!/usr/bin/env python
from __future__ import print_function

from nose import run
from nose.plugins.xunit import Xunit
from nose.plugins.logcapture import LogCapture

from falafel.loaders import FalafelTestLoader
from falafel import findout_terminal_width
from falafel import iterate_tests
from falafel import test_list
from falafel.logger import Formatter


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='my custom test runner')
    parser.add_argument("-S", "--suite", help="Test suite",
                        choices=['moda', 'modb'], type=str, required=True)
    parser.add_argument("--progressive", action='store_true',
                        help="nose test progressive plugin")
    parser.add_argument( "--debug", action="store_true",
                        help="print logging messages")
    parser.add_argument( "--logcapture", action="store_true",
                        help="capture logging messages")

    args = parser.parse_args()

    pkg = args.suite
    suite = FalafelTestLoader().discover('mypackage.' + pkg)

    width = findout_terminal_width()

    print(" info ".center(width, '='))
    print("suite: ", pkg)
    print('=' * width)

    print(" found the following tests ".center(width, '='))

    testfuncs = list(iterate_tests(suite._tests))
    tdata = test_list(suite)
    try:
        from tabulate import tabulate
    except ImportError:
        for data in tdata:
            print("  %-30s\t(in %s)%s" % data)
    else:
        print('\n', tabulate(
            tdata, headers=['class.method', 'module', 'skipped']))
    print("%d tests available" % suite.countTestCases())
    print('=' * width)

    argv = [__file__, '-v', '--with-xunit']
    plugins = [Xunit()] # NOTE: due to the xunit plugin the testrun output
                        # gets garbaged
    # plugins = []

    if args.logcapture:
        argv += [
            '--logging-format=%(asctime)s |%(levelname)-8s | %(message)s',
            '--logging-datefmt=%H:%M:%S']
        plugins += [LogCapture()]
    else:
        import logging
        import sys
        logger = logging.getLogger('st')
        if args.debug:
            logger.setLevel(logging.DEBUG)
            logger.propagate = False
            hdl = logging.StreamHandler(sys.stdout)
            fmt = Formatter()
            hdl.setFormatter(fmt)
        else:
            hdl = logging.NullHandler()
        logger.addHandler(hdl)

    if args.progressive:
        from noseprogressive.plugin import ProgressivePlugin
        argv += ['--with-progressive']
        plugins += [ProgressivePlugin()]

    run(argv=argv, suite=testfuncs, plugins=plugins)
