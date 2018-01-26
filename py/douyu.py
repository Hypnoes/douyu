#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time,os,sys
import re
from functools import partial

import colors as c
from danmu import DanMuClient

color = {
        "0" : c.white,
        "1" : c.blue,
        "2" : c.green,
        "3" : c.magenta,
        "4" : c.yellow,
        "5" : c.cyan,
        "6" : c.red
        }

title = {
        "7" : c.color("游侠", fg='white', style='bold'),
        "1" : c.color("骑士", fg='blue', style='bold'),
        "2" : c.color("子爵", fg='green', style='bold'),
        "3" : c.color("伯爵", fg='pink', style='bold'),
        "4" : c.color("公爵", fg='yellow', style='bold'),
        "5" : c.color("国王", fg='red', style='bold'),
        "6" : c.color("皇帝", fg='gold', style='bold')
        }

def le_col(level, label="") -> str:
    ''' label level '''
    lv = int(level)
    if lv == 0:
        return "         "
    if 10 > lv > 0:
        return c.yellow(label + "0" + level, style='negative')
    if 20 > lv >= 10:
        return c.cyan(label + level, style='negative')
    if lv >= 20:
        return c.red(label + level, style='negative')

def t_col(level) -> str:
    ''' user level '''
    l = int(level)
    if 10 > l:
        return c.yellow("0" + level, style='negative') 
    if 30 > l >= 10:
        return c.green(level, style='negative')
    if 40 > l >= 30:
        return c.cyan(level, style='negative')
    if 50 > l >= 40:
        return c.blue(level, style='negative')
    if 80 > l >= 50:
        return c.magenta(level, style='negative')
    if 100> l > 80:
        return c.red(level, style='negative')
    if l > 100:
        return c.yellow(level, style='negative')

def col(msg) -> str:
    ''' assembly danmu '''
    b = "[]"
    if "bnn" in msg and "bl" in msg:
        bnn = msg["bnn"]
        r1 = r"[a-zA-Z0-9]{0,6}"
        r2 = r"[^\x00-\xff]{0,3}"
        try:
            x1 = len(''.join(re.findall(r1, bnn)))
        except Exception as e:
            x1 = 0
        try:
            x2 = len(''.join(re.findall(r2, bnn))) * 2
        except Exception as e:
            x2 = 0
        x = x1 + x2
        if x != 6:
            bnn = " " * (6 - x) + bnn + "@"
        else: 
            bnn = bnn + "@"
        b = "[%s]" % (le_col(msg["bl"], bnn)) 
    
    n = "[游客]"
    if "nl" in msg:
        n = "[%s]" % (title[msg["nl"]])
    if "col" not in msg:
        msg["col"] = "0"
    txt = "[%s] :: %s > %s" % (t_col(msg["level"]), 
            c.cyan(msg["nn"], style="underline"), color[msg["col"]](msg["txt"]))
    
    return n + b + txt

try:
    dmc = DanMuClient(sys.argv[1])
    if not dmc.isValid():
        raise Exception("Invalid URL")
except IndexError as ie:
    print(c.red("No enough parameters."))
    exit(1)
except Exception as e:
    print(c.red(e.args[1]))
    exit(1)

@dmc.danmu
def danmu_fn(msg) -> None:
    try:
        print(col(msg), end="\n")
    except Exception as e:
        print(e)
    finally:
        pass
    
@dmc.default
def default_fn(msg) -> None:
    print("", end='\r')

dmc.start(blockThread=True)

