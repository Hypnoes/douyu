#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time,os,sys
import re

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
        "7" : "游侠",
        "1" : "骑士",
        "2" : "子爵",
        "3" : "伯爵",
        "4" : "公爵",
        "5" : "国王",
        "6" : "皇帝"
        }

def le_col(level, label=""):
    if int(level) == 0:
        return "         "
    if 10 > int(level) > 0:
        return color["4"](label + "0" + level)
    if 20 > int(level) >= 10:
        return color["5"](label + level)
    if int(level) >= 20:
        return color["6"](label + level)

def t_col(level):
    l = int(level)
    if 10 > l:
        return c.yellow("0" + level) 
    if 30 > l >= 10:
        return c.green(level)
    if 40 > l >= 30:
        return c.cyan(level)
    if 50 > l >= 40:
        return c.blue(level)
    if 80 > l >= 50:
        return c.magenta(level)
    if 100> l > 80:
        return c.red(level)
    if l > 100:
        return c.yellow(level)

def col(msg):
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
        n = "[%s]" % (color[str(7 - int(msg["nl"]))](title[msg["nl"]]))
        
    if "col" not in msg:
        msg["col"] = "0"
    txt = "[%s] :: %s > %s" % (t_col(msg["level"]), c.cyan(msg["nn"], style="underline"), color[msg["col"]](msg["txt"]))
    
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
def danmu_fn(msg):
    try:
        print(col(msg), end="\n")
    except Exception as e:
        print(e)
    finally:
        pass
    
@dmc.default
def default_fn(msg):
    print("", end='\r')

dmc.start(blockThread=True)

