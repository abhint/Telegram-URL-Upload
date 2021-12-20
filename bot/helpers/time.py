#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T

import time


def time_data(_time):
    day = _time // (24 * 3600)
    _time = _time % (24 * 3600)
    hour = _time // 3600
    _time %= 3600
    minutes = _time // 60
    _time %= 60
    seconds = _time
    if day != 0:
        return "%dd %dh %dm %ds" % (day, hour, minutes, seconds)
    if hour != 0:
        return "%dh %dm %ds" % (hour, minutes, seconds)
    else:
        return "%dm %ds" % (minutes, seconds)
