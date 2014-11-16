import requests
import logging
import subprocess
import shlex
import os
import unicodedata as ucode
from lazychannel.helpers import pexpand, output_dir

log = logging.getLogger('lazychannel.worker.youtube')
BASE_URL = "http://gdata.youtube.com/feeds/api/videos?max-results=50&alt=json&orderby=published&author={}"
cache_file = 'foo.cache'


def parse_config(cfg):
    pass


def fetch_channel(uuid):
    channel_url = BASE_URL.format(uuid)
    channel_list = requests.get(channel_url).json()
    return channel_list


def download(uuid, out):
    videos = fetch_channel(uuid)
    if 'entry' not in videos['feed']:
        log.error('No feed found, assuming account deleted.')
        return
    for v in videos['feed']['entry']:
        link = v['link'][0]['href']
        title = ucode.normalize('NFKD', v['title']['$t'])
        title = title.encode('ascii', 'ignore')
        if not in_cache(link):
            log.info('Fetching {}'.format(title))
            call_downloader(out, link)
        else:
            log.debug('Cache Hit on: {} - skipping'.format(title))


def in_cache(link):
    # obnoxious bug
    link = "{}\n".format(link)
    with open(self.cache_file, 'r') as f:
        cache = f.readlines()
    if link in cache:
        return True
    return False


def call_downloader(outpath, link):
    outpath = "{}{}%(title)s.%(ext)s".format(outpath, os.path.sep)
    c = "youtube-dl -x --audio-format=mp3 -o {} {}".format(outpath, link)
    cmd = shlex.split(c)
    subprocess.check_output(cmd)
    with open(cache_file, 'a+') as f:
        f.write("{}\n".format(link))


def main(channels, cfg):
    log.info('Initialized youtube processor')
    BASE_OUT = cfg.settings()['dir']
    for chan in channels:
        log.info("Processing {}".format(chan))
        out = pexpand(os.path.join(BASE_OUT, chan))
        output_dir(out)
        download(channels[chan], out)
