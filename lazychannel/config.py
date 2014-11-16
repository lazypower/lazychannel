import yaml
import os
import logging


class config:
    def __init__(self, ws):
        ws = os.path.expanduser(ws)
        self.config = os.path.join(ws, 'config.yaml')
        self.log = logging.getLogger('lazychannel.config')

    def exists(self):
        if os.path.exists(self.config):
            return True
        return False

    def load_config(self):
        if self.exists():
            with open(self.config, 'r') as f:
                conf = yaml.safe_load(f.read())
            return conf
        self.log.critical('Unable to locate config. Perhaps you need to run'
                          ' lazychannel init?')
