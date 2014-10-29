import os

def pexpand(path):
    return os.path.abspath(os.path.expanduser(path))
