import yaml
import os
import logging

#CONFIG = os.path.expanduser('~/.lazychannel/config.yaml')

class config:
    def __init__(self,ws):
        self.config = os.path.join(ws, 'config.yaml')

    # i'm so sorry, this is ugly.
    def config_dir(self):
        return os.path.sep.join(self.config.split(os.path.sep)[0:-1])

    def config_exists(self):
        if os.path.exists(self.config):
            return True
        return False

    def load_config(self):
        if self.config_exists():
            with open(self.config, 'r') as f:
                conf = yaml.safe_load(f.read())
            return conf
        logging.critical('Unable to locate config. Perhaps you need to run'
                         ' lazychannel init?')
