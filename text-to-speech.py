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
    agent = ("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 "
             "(KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2")
    p = mplayer.Player(args=('-user-agent', agent))
    while True:
        text = raw_input()
        url = (u"http://translate.google.com/"
               u"translate_tts?tl={0}&q={1}".format(
               language,
               urllib.quote(text)))
        print(url)
        p.loadfile(url)
