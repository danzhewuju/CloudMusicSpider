#!/usr/bin/python3
import time


class TimeR:
    def getime(self, localtime):
        localtime //= 1000
        time_local = time.localtime(localtime)
        rtime = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return rtime


tt = 1510850662716
t = TimeR()
print(t.getime(tt))