#!/bin/env python
# --coding: utf-8 --

import urllib
import mplayer
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        language = argv[1]
    else:
        language = "ru"
    agent = ("Mozilla/5.0 (Windows NT 6.1; WOW64) "
             "AppleWebKit/537.17 "
             "(KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17")

    p = mplayer.Player(args=('-user-agent', agent, '-ao', 'pulse'))
    p.cmd_prefix = ''
    while True:
        text = raw_input()
        url = (u"http://translate.google.com/"
               u"translate_tts?tl={0}&q={1}".format(
               language,
               urllib.quote(text)))
        print(url)
        p.loadfile(url, 1)
