#!/usr/bin/env python

import logging

from falafel.logger import Formatter
from falafel.logger import nocolors

def main(colors=True):
    lg = logging.getLogger('test')
    lg.setLevel('DEBUG')
    sh = logging.StreamHandler()
    if colors:
        fmt = Formatter()
    else:
        fmt = Formatter(pre=nocolors, lenstrip=None, contline=None)
    sh.setFormatter(fmt)
    lg.addHandler(sh)

    lg.info('Started')
    lg.critical('test critical\n\tmore text\ndone')
    a = 3.1415
    lg.info("hello %d %s  " %(a, "thats it"))
    lg.info('Finished')

if __name__ == '__main__':
    main()
