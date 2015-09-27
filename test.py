# coding:utf-8

import time

import m
import pyautoreload

if __name__ == '__main__':
    while True:
        pyautoreload.reload_module(m)
        m.test()
        time.sleep(1)
