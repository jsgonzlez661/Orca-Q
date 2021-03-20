#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Jose Gonzalez ~ All rights reserved.

from tkinter import messagebox, filedialog, TclError
# from multiprocessing import Process, Queue
from os.path import isfile
import os
import subprocess
import threading


def about_info():
    messagebox.showinfo(
        "ORCA-Q version 1.0", "Program to run multiple ORCA files\nOpen Source\nVersion 1.0\n")

list_jobs = []


def add_job(treeview):
    global list_jobs
    addjob = filedialog.askopenfilenames(
        title="Add Jobs", initialdir="C:\\Orca\\", filetypes=(("ORCA Input File", "*.inp"),))
    if addjob != None:
        addjob = list(addjob)
        for job in addjob:
            link = job.replace('/', '\\')
            try:
                treeview.insert("", "end", text=link,
                                    values=("0%",), iid=link)
                list_jobs.append(link)
            except TclError:
                pass


def remove_select(treeview):
    global list_jobs
    if list_jobs != []:
        removes = list(treeview.selection())
        for rem in removes:
            treeview.delete(rem)
            list_jobs.remove(rem)


def remove_all(treeview):
    global list_jobs
    if list_jobs != []:
        for job in list_jobs:
            treeview.delete(job)
        list_jobs = []


orca = ""


def datafile():

    global orca

    if(isfile("orca.path") == True):
        with open('orca.path', 'r') as setting:
            orca = setting.readline().strip()
    else:
        orca = "C:\\Orca\\orca.exe"
        with open('orca.path', 'w') as setting:
            setting.write(orca)

    return orca


def open_dirORCA(et_top):
    global orca
    dir_ORCA = filedialog.askopenfilename(
        title="Select ORCA dir", initialdir="C:\\Orca\\", filetypes=(("ORCA run", "*.exe"),))
    if(dir_ORCA != None and dir_ORCA != ""):
        et_top.delete('0', "end")
        orca = dir_ORCA.replace("/", "\\")
        with open('orca.path', 'w') as setting:
            setting.write(orca)
        et_top.insert("end", orca)


def runCalculation(button, tree):
    orca = datafile()
    if list_jobs != []:
        for job in list_jobs:
            tree.item(job, values=["0%"])
            os.system('{0} {1} > {2}'.format(
                orca, job, job.replace('.inp', '.out')))
            tree.item(job, values=["100%"])
        button.config(state="normal")


def process(button, tree, **options):
    global list_jobs
    orca = datafile()
    button.config(state="disable")
    hilo1 = threading.Thread(target=runCalculation,
                             args=(button, tree), daemon=True)
    hilo1.start()


def stopprocess(button, tree, **options):
    subprocess.run('taskkill /f /im orca.exe',
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # if list_jobs != []:
    #     for job in list_jobs:
    #         tree.item(job, values=["ERROR"])
    button.config(state="normal")
