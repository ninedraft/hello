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
import os
import argparse

import requests
import appdirs

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def scriptdir():
    return path.dirname(path.realpath(__file__))


def configuration_dir():
    return appdirs.user_config_dir(appname="hello", appauthor=False)


def location_from_file():
    config = configuration_dir() + "/location"
    try:
        with open(config, "r", encoding="UTF8") as loc:
            return loc.readline().strip() or None
    except:
        return None


def location_by_ip():
    try:
        ipinfo = requests.get("http://ipinfo.io/json", timeout=1.0)
        return ipinfo.json()["region"]
    except:
        return None


def location_by_timezone():
    return time.tzname[0]


def save_location(loc):
    config_dir = configuration_dir()
    os.makedirs(name=config_dir, exist_ok=True)
    with open(config_dir + "/location", mode='w+', encoding="UTF8") as loc_file:
        loc_file.write(str(loc))


def pc_location():
    loc = location_from_file()
    if not loc:
        loc = location_by_ip() or location_by_timezone() or "Tel-Aviv"
        save_location(loc)
    return loc


def ascii():
    ascii_dir = scriptdir() + "/data/ascii"
    files = [file
             for file in os.listdir(ascii_dir)
             if path.isfile(path.join(ascii_dir, file))]
    ascii_file = path.join(ascii_dir,  random.choice(files))
    with open(ascii_file, "r", encoding="UTF8") as ascii_art:
        return ascii_art.read()


def wquote():
    try:
        with open(scriptdir() + "/data/wquotes.txt", mode='r', encoding="UTF8") as wquotes_file:
            wq = random.choice(wquotes_file.readlines()).strip()
            return wq.replace("―", "\n\t―").replace("\\n", "\n")
    except:
        return "Unable to get wquote text: " + str(sys.exc_info()[0])


def weather():
    weath = ""
    try:
        location = pc_location()
        weath = requests.get("http://wttr.in/" +
                             location + "?0", timeout=1.0).text
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
    parser = argparse.ArgumentParser(description="A lovely welcome script")
    parser.add_argument("--locate", action="store_const",
                        const=True, default=False,
                        help="locate this pc")
    if parser.parse_args().locate:
        loc = location_by_ip() or location_by_timezone() or "Tel-Aviv"
        print("Location found: " + loc)
        save_location(loc)
    random.seed(time.time())
    print(weather())
    print(ascii() + "\n")
    print(splash())


if __name__ == "__main__":
    sys.exit(main())
