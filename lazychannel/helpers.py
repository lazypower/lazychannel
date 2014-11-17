import os
import logging

log = logging.getLogger('lazychannel.helpers')


def pexpand(path):
    return os.path.abspath(os.path.expanduser(path))


def output_dir(out):
    if not os.path.exists(out):
        log.info("Creating directory {}".format(out))
        os.makedirs(out)


def touch_file(path):
    with open(path, 'w') as f:
        os.utime(path, None)
