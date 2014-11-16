import importlib
import os
from config import config
from helpers import pexpand, output_dir


def main(args, unknown):
    if unknown:
        raise Exception('%s are not recognized parameters' % ' '.join(unknown))

    ws = pexpand(args.workspace)
    cfg = config(ws)
    if not args.d:
        output_dir(pexpand(cfg.settings()['dir']))
    else:
        output_dir(pexpand(args.d))

    channels = cfg.channels()

    for channel in channels.keys():
        action = importlib.import_module("..%s" % channel,
                                         "lazychannel.processor.%s" % channel)
        action.main(channels[channel], cfg)

    # if 'youtube' in channels.keys():
    #     from processor.youtube import youtube
    #     cache_path = "{}{}youtube-cache".format(ws, os.path.sep)
    #     yt = youtube(cache_file=cache_path)
    #     yt.main(channels['youtube'], args.d, ws)
