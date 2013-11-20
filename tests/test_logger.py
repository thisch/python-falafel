#!/usr/bin/env python

import logging

from falafel.logger import Formatter

def main():
    lg = logging.getLogger('test')
    lg.setLevel('DEBUG')
    sh = logging.StreamHandler()
    sh.setFormatter(Formatter())
    lg.addHandler(sh)

    lg.info('Started')
    lg.critical('test critical\n\tmore text\ndone')
    a = 3.1415
    lg.info("hello %d %s  " %(a, "thats it"))
    lg.info('Finished')

if __name__ == '__main__':
    main()
