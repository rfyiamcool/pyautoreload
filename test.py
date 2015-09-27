# coding:utf-8

import m
from pyautoreload import *
import time


if __name__ == '__main__':
    while True:
        pyautoreload.reload_module(m)
        m.test()
        time.sleep(1)
