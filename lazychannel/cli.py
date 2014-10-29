#!/usr/bin/python

import argparse
import sys
import importlib
import logging

def basic_args(parser):  # pragma: no cover
    parser.add_argument('--debug', action='store_true',
                        help='display debug output, implies -v')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='display additional logging information')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='squash all output')


def global_args(parser):  # pragma: no cover
    basic_args(parser)
    parser.add_argument('-w', '--workspace', default='~/.lazychannel',
                        help='the workspace')



def setup_parser():
    p = argparse.ArgumentParser(prog='lazychannel',
                                description="An easy way to keep up with"
                                            "music in the 21st century")
    sp = p.add_subparsers(title='actions', dest='action', metavar='actions')

    init = sp.add_parser('init', help='Create config file')
    init.add_argument('workspace', default='~/.lazychannel',
                      help='Define path to warehouse config and databases')

    basic_args(init)

    return p


def setup_logging(verbose=None, debug=None):  # pragma: no cover
    logger = logging.getLogger('cabs')
    logger.setLevel(logging.INFO)
    if debug:
        logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    if verbose:
        f = '%(asctime)s %(levelname)s %(name)s: %(message)s'
    else:
        f = '%(levelname)s %(name)s: %(message)s'

    formatter = logging.Formatter(f)
    ch.setFormatter(formatter)

    if verbose is None:
        ch = logging.NullHandler()

    logger.addHandler(ch)
    return logger


def main(args=None):
  parser = setup_parser()
  known, unknown = parser.parse_known_args(args)

  log = setup_logging(verbose=known.verbose, debug=known.debug)

  # TODO: make this cleaner
  if known.action == 'init':
      known.action = 'generate'


  log.debug('arguments: %s, unknowns: %s' % (str(known), str(unknown)))

  try:
    action = importlib.import_module("..%s" % known.action,
                                     'lazychannel.%s' % known.action)
    log.debug('accessing %s.main' % known.action)
    exit = action.main(known, unknown)
  except Exception as e:
    if known.debug:
        log.exception(e.message)
    else:
        log.critical(e.message)
    exit = 1

    sys.exit(exit)




if __name__ == "__main__":
    main()
