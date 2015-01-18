import os
import logging
from config import config

log = logging.getLogger('lazychannel.init')


def create_config(ws, cfg):
    if cfg.exists():
        logging.warn('Config exists, doing nothing')
        return
    try:
        os.makedirs(ws)
    except:
        log.debug('Skipping directory creation')

    with open(cfg.config, 'w+') as f:
        f.write("settings:\n")
        f.write("    audiodir: ~/Music/lazychannel\n")
        f.write("    videodir: ~/Videos/lazychannel\n")
        f.write("    limit: 2\n")
        f.write("channels:\n")
        f.write("    youtube:\n")
        f.write("        audio:\n")
        f.write("            ArgoFoxCreativeCommons: UC56Qctnsu8wAyvzf4Yx6LIw\n")
        f.write("        video:\n")
        f.write("            LinuxMusicMaster: MusicMasterUnlimited\n")
        logging.info('Created skeleton config. Populate with data')


def main(args, unknown):
    if unknown:
        raise Exception('%s are not recognized parameters' % ' '.join(unknown))

    ws = os.path.abspath(args.workspace)
    log.info('Creating %s' % ws)

    c = config(ws)
    create_config(ws, c)
