import os
import logging
from config import config
from helpers import pexpand

log = logging.getLogger('lazychannel.sync')


def parse_youtube(channels, out, ws):
    from processor.youtube import youtube
    logging.info('Initialized youtube processor')
    cache_path = "{}{}youtube-cache".format(ws, os.path.sep)
    yt = youtube(cache_path)
    for chan in channels:
        log.info("Processing {}".format(chan))
        odir = pexpand(os.path.join(out, chan))
        if not os.path.exists(odir):
            output_dir(odir)
        yt.download(channels[chan], odir)


def output_dir(out):
    if not os.path.exists(out):
        log.info("Creating directory {}".format(out))
        os.makedirs(out)


def main(args, unknown):
    if unknown:
        raise Exception('%s are not recognized parameters' % ' '.join(unknown))

    ws = pexpand(args.workspace)
    c = config(ws).load_config()
    output_dir(pexpand(args.d))

    if 'youtube' in c:
        parse_youtube(c['youtube'], args.d, ws)

    log.info('Sync Complete - \oo/, Rock on my friend.')
