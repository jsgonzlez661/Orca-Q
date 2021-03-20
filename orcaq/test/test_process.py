#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Jose Gonzalez ~ All rights reserved.


from multiprocessing import Process
import tkinter as tk
import sys
import os
import subprocess


orca = 'C:\\Orca\\orca.exe'


def runCalculation():
    global orca
    os.system('{0} {1} > {2}'.format(orca, 'water.inp', 'water.out'))


def process2(**options):
    o = Process(name='orca', target=runCalculation, daemon=True)
    o.start()
    # winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)


def stopprocess():
    subprocess.run('taskkill /f /im orca.exe', stdout=subprocess.DEVNULL)
    # winsound.PlaySound("SystemHand", winsound.SND_ALIAS)


def gui():
    root = tk.Tk()
    root.geometry("200x200")
    button = tk.Button(root, text='RUN', command=lambda: process2())
    button.pack()
    button2 = tk.Button(root, text='TERMINATE', command=lambda: stopprocess())
    button2.pack()
    root.mainloop()


if __name__ == '__main__':
    gui()
