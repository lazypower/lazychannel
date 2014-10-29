import requests
import logging
import subprocess
import shlex
import os

class youtube:
    def __init__(self):
        self.log = logging.getLogger('worker.youtube')
        self.BASE_URL = "http://gdata.youtube.com/feeds/api/videos?max-results=1&alt=json&orderby=published&author={}"


    def fetch_channel(self, uuid):
        channel_url = self.BASE_URL.format(uuid)
        channel_list = requests.get(channel_url).json()
        return channel_list

    def download(self, uuid, out):
        videos = self.fetch_channel(uuid)
        if not 'entry' in videos['feed']:
            self.log.error('No feed found, assuming account deleted.')
            return
        for v in videos['feed']['entry']:
            self.log.debug('fetching {}'.format(v['title']['$t']))
            self.call_downloader(out, v['link'][0]['href'])

    def call_downloader(self, outpath, link):
        outpath = "{}{}%(title)s.%(ext)s".format(outpath, os.path.sep)
        c = "youtube-dl -x --audio-format=mp3 -o {} {}".format(outpath, link)
        cmd = shlex.split(c)
        subprocess.check_output(cmd)


#
# for i in c['feed']['entry']:
#     print i['link'][0]['href']
