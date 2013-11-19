#!/usr/bin/env python
import os
import logging
from falafel import findout_terminal_width
from falafel import test_list
from falafel.runners import FalafelTestRunner
from falafel.loaders import FalafelTestLoader


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='my custom test runner')
    parser.add_argument("-S", "--suite", help="Test suite",
                        choices=['moda', 'modb'], type=str, required=True)
    parser.add_argument("--test", action='append', help="Testcase(s) to run")
    parser.add_argument("-L", "--list", action="store_true",
                        help="List tests which match the specified "
                        "suite/testcases(s)")
    parser.add_argument("--pdb", action="store_true",
                        help="drop into pdb/ipdb in case of a failure/error")
    parser.add_argument("--debug", action="store_true",
                        help="print logging messages")
    parser.add_argument("--interactive", '--enable-interactive-tests',
                        action="store_true", dest='interactive',
                        help="if not set then all interactive tests are skipped")

    args = parser.parse_args()

    pkg = args.suite
    allowed_tests = args.test

    width = findout_terminal_width()

    print " info ".center(width, '=')
    print "suite: ", pkg
    print "tests: ", allowed_tests
    print "interactive tests:", args.interactive
    print '=' * width

    if args.interactive:
        os.environ['INTERACTIVE_TESTS'] = '1'

    loader = FalafelTestLoader(allowed_tests=allowed_tests)
    suite = loader.discover('mypackage.' + pkg)

    tdata = []
    if args.list:
        tdata = test_list(suite)
        try:
            from tabulate import tabulate
        except ImportError:
            for data in tdata:
                print "  %-30s\t(in %s)%s" % data
        else:
            print '\n', tabulate(
                tdata, headers=['class.method', 'module', 'skipped'])
        print "%d tests available" % suite.countTestCases()
        exit()

    # logging.basicConfig(level='DEBUG')
    logger = logging.getLogger('st')
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    runner = FalafelTestRunner(
        verbosity=2, logger=logger, debug=args.debug,
        width=width, pdb=args.pdb)
    runner.run(suite)
