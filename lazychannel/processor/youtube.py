import requests
import logging
import subprocess
import shlex
import os
import unicodedata as ucode
from lazychannel.helpers import pexpand, output_dir, touch_file

log = logging.getLogger('lazychannel.worker.youtube')
LIMIT = 50
BASE_URL = "http://gdata.youtube.com/feeds/api/videos?max-results={}&alt=json&orderby=published&author={}"
CACHE_FILE = 'foo.cache'
AUDIO_DIR = os.path.join(os.path.sep, 'tmp')
VIDEO_DIR = os.path.join(os.path.sep, 'tmp')


def parse_config(cfg):
    settings = cfg.settings()
    global AUDIO_DIR
    global VIDEO_DIR
    global CACHE_FILE
    global LIMIT
    AUDIO_DIR = settings['audiodir']
    VIDEO_DIR = settings['videodir']
    CACHE_FILE = os.path.join(cfg.dir, 'youtube.cache')
    LIMIT = settings['limit']


def fetch_channel(uuid):
    channel_url = BASE_URL.format(LIMIT, uuid)
    channel_list = requests.get(channel_url).json()
    return channel_list


def download(uuid, out, media='audio'):
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
            call_downloader(out, link, media)
        else:
            log.debug('Cache Hit on: {} - skipping'.format(title))


def in_cache(link):
    # obnoxious bug
    link = "{}\n".format(link)

    if not os.path.exists(CACHE_FILE):
        touch_file(CACHE_FILE)

    with open(CACHE_FILE, 'r') as f:
        cache = f.readlines()
    if link in cache:
        return True
    return False


def call_downloader(outpath, link, media='audio'):
    outpath = "{}{}%(title)s.%(ext)s".format(outpath, os.path.sep)
    if media == 'video':
        c = "youtube-dl -o {} {}".format(outpath, link)
    else:
        c = "youtube-dl -x --audio-format=mp3 -o {} {}".format(outpath, link)
    cmd = shlex.split(c)
    subprocess.check_output(cmd)
    with open(CACHE_FILE, 'a+') as f:
        f.write("{}\n".format(link))


def main(channels, cfg):
    parse_config(cfg)
    log.info('Initialized youtube processor')
    # Extra loop for different formats - they need to be handled differently
    # related to issue #5
    for media in channels:
        for chan in channels[media]:
            log.info("Processing {}: {}".format(media, chan))
            if media == 'video':
                out = pexpand(os.path.join(VIDEO_DIR, chan))
            else:
                out = pexpand(os.path.join(AUDIO_DIR, chan))
            output_dir(out)
            download(channels[media][chan], out, media)
