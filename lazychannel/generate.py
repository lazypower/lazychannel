import os
import logging
import config

log = logging.getLogger('lazychannel.init')

def create_config(ws, cfg):
    try:
        os.makedirs(ws)
    except:
        pass
    with open(cfg.config, 'w+') as f:
        f.write("youtube:\n")
        f.write("    name: uuid")
        logging.info('Created skeleton config. Populate with data')

def main(args, unknown):
    if unknown:
        raise Exception('%s are not recognized parameters' % ' '.join(unknown))

    ws = os.path.abspath(args.workspace)
    log.info('Creating %s' % ws)

    c = config(ws)

    try:
        create_config(ws, c)
    except OSError:
        log.error('%s already exists' % ws)
        return 1
