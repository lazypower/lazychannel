import os
from config import config
from helpers import pexpand, output_dir


def main(args, unknown):
    if unknown:
        raise Exception('%s are not recognized parameters' % ' '.join(unknown))

    ws = pexpand(args.workspace)
    c = config(ws).load_config()
    output_dir(pexpand(args.d))

    if 'youtube' in c:
        from processor.youtube import youtube
        cache_path = "{}{}youtube-cache".format(ws, os.path.sep)
        yt = youtube(cache_file=cache_path)
        yt.main(c['youtube'], args.d, ws)
