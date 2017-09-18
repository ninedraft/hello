#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
    A lovely welcome script
    version: 0.0.1
    https://github.com/ninedraft/hello
    author: ninedraft
    license: MIT
    Just put it on autostart of your terminal emulator.
    Cats and sun are included!
"""

import random
import time
import sys
from os import path

import requests

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


cats = [
    '''      \\    /\\
       )  ( ')
      (  /  )
 jgs   \\(__)|''',
    '''          |\\___/|
          )     (             .              '
         =\\     /=
           )===(       *
          /     \\
          |     |
         /       \\
         \\       /
  _/\\_/\\_/\\__  _/_/\\_/\\_/\\_/\\_/\\_/\\_/\\_/\\_/\\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  jgs|  |  |  |  |  |  |  |  |  |  |  |  |  |
 ''',
    '''  /\\_/\\
 ( o.o )
  > ^ <'''
]


def rcat():
    return random.choice(cats)


def wquote():
    try:
        with open("/data/wquotes.txt", mode='r', encoding="UTF8") as wquotes_file:
            wq = random.choice(wquotes_file.readlines()).strip()
            return wq.replace("―", "\n\t―").replace("\\n", "\n")
    except:
        return "Unable to get wquote text: " + str(sys.exc_info()[0])


def weather():
    weath = ""
    try:
        weath = requests.get("http://wttr.in/moscow?0", timeout=1.0).text
    except:
        return wquote()
    return weath


def scriptdir():
    return path.dirname(path.realpath(__file__))


def splash():
    try:
        with open(scriptdir() + "/data/splashes.txt", mode='r', encoding="UTF8") as splashes_file:
            return random.choice(splashes_file.readlines()).strip()
    except:
        return "Unable to get splash text: " + str(sys.exc_info()[0])


def main():
    random.seed(time.time())
    print(weather())
    print(rcat() + "\n")
    print(splash())


if __name__ == "__main__":
    sys.exit(main())
