#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Jose Gonzalez ~ All rights reserved.

from tkinter import Tk, Menu, PhotoImage, Frame, Button, Label, Scrollbar, Toplevel
from tkinter import ttk
from .functions import about_info, add_job, remove_select, remove_all, open_dirORCA, datafile, stopprocess, process
# from .settings import Toplevelwindows


class GUI(object):

    def __init__(self, root):
        self.root = root
        self.root.geometry('640x480')
        self.root.iconbitmap("icons\\orcaqx32.ico")
        self.root.title("ORCA-Q")
        self.root.resizable(0, 0)
        self.menubar()
        self.frame = Frame(self.root, width=640, height=480)
        self.frame.pack()
        self.buttonbar()
        self.body = Frame(self.root, width=100, height=200)
        self.body.pack()
        self.treeview()

    def menubar(self, **options):

        self.barMenu = Menu(self.root)
        self.root.config(menu=self.barMenu)
        self.root['menu'] = self.barMenu
        # --------- MENU SETTING --------- #
        self.archiveMenu = Menu(self.barMenu, tearoff=0)
        self.imgmenu_setting = PhotoImage(file="icons\\settingx16.png")
        # , command=lambda:show_setting(root))
        self.archiveMenu.add_command(
            label="Setting", image=self.imgmenu_setting, compound="left")

        self.archiveMenu.add_separator()

        self.archiveMenu.add_command(
            label="Exit", command=lambda: self.root.destroy())
        self.barMenu.add_cascade(label="Archive", menu=self.archiveMenu)

        # --------- MENU ADD --------- #
        self.jobsMenu = Menu(self.barMenu, tearoff=0)
        self.imgmenu_add = PhotoImage(file="icons\\addx16.png")
        self.jobsMenu.add_command(
            label="Add Jobs", image=self.imgmenu_add, compound="left", command=lambda: add_job(self.treeview))
        self.imgmenu_remove = PhotoImage(file="icons\\removex16.png")
        self.jobsMenu.add_command(
            label="Remove Jobs", image=self.imgmenu_remove, compound="left", command=lambda: remove_select(self.treeview))

        self.jobsMenu.add_separator()

        self.imgmenu_start = PhotoImage(
            file="icons\\startx16.png")
        self.jobsMenu.add_command(
            label="Start Jobs", image=self.imgmenu_start, compound="left")
        self.imgmenu_cancell = PhotoImage(file="icons\\cancelx16.png")
        # , command=lambda:cancell_ORCA())
        self.jobsMenu.add_command(
            label="Cancell Jobs", image=self.imgmenu_cancell, compound="left")

        self.jobsMenu.add_separator()

        self.imgmenu_cleanup = PhotoImage(file="icons\\cleanupx16.png")
        self.jobsMenu.add_command(
            label="Clean All", image=self.imgmenu_cleanup, compound="left", command=lambda: remove_all(self.treeview))
        self.barMenu.add_cascade(label="Jobs", menu=self.jobsMenu)

        self.helpMenu = Menu(self.barMenu, tearoff=0)
        self.helpMenu.add_command(label="Documentation")
        self.helpMenu.add_separator()
        self.helpMenu.add_command(
            label="About ORCA-Q", command=lambda: about_info())
        self.barMenu.add_cascade(label="Help", menu=self.helpMenu)

    def buttonbar(self, **options):

        self.imgbt1 = PhotoImage(file="icons\\add.png")
        self.bt1 = Button(self.frame, text="Add", image=self.imgbt1, width=46, height=46,
                          relief="flat", overrelief="groove", compound="top", command=lambda: add_job(self.treeview))
        self.bt1.grid(row=0, column=0, sticky="e", padx=10)

        self.imgbt2 = PhotoImage(file="icons\\remove.png")
        self.bt2 = Button(self.frame, text="Remove", image=self.imgbt2, width=46, height=46, relief="flat",
                          overrelief="groove", compound="top", command=lambda: remove_select(self.treeview))
        self.bt2.grid(row=0, column=1, sticky="e")

        self.separator_bt = Label(self.frame, width=1).grid(row=0, column=2)

        self.imgbt3 = PhotoImage(file="icons\\start.png")
        self.bt3 = Button(self.frame, text="Start", image=self.imgbt3, width=46, height=46, relief="flat",
                          overrelief="groove", compound="top", command=lambda: process(self.bt3, self.treeview))
        self.bt3.grid(row=0, column=3)

        self.imgbt4 = PhotoImage(file="icons\\cancel.png")
        self.bt4 = Button(self.frame, text="Cancell", image=self.imgbt4, width=46, height=46,
                          relief="flat", overrelief="groove", compound="top", command=lambda: stopprocess(self.bt3, self.treeview))
        self.bt4.grid(row=0, column=4, padx=10)

        self.separator_bt2 = Label(self.frame, width=1).grid(row=0, column=5)

        self.imgbt5 = PhotoImage(file="icons\\cleanup.png")
        self.bt5 = Button(self.frame, text="Clean All", image=self.imgbt5, width=46, height=46,
                          relief="flat", overrelief="groove", compound="top", command=lambda: remove_all(self.treeview))
        self.bt5.grid(row=0, column=6)

        self.imgbt6 = PhotoImage(file="icons\\setting.png")
        self.bt6 = Button(self.frame, text="Setting", image=self.imgbt6, width=46, height=46,
                          relief="flat", overrelief="groove", compound="top", command=lambda: self.Toplevelwindows())

        self.bt6.grid(row=0, column=7, padx=10)

        self.separator_bt3 = Label(
            self.frame, width=36, height=4).grid(row=0, column=8)

    def treeview(self, **options):
        self.treeview = ttk.Treeview(
            self.body, columns=("lastmod"), height=17)
        self.treeview.grid(row=0, column=0, columnspan=7)
        self.treeview.heading("#0", text="Name")
        # self.treeview.heading("size", text="Processor")
        self.treeview.heading("lastmod", text="Status")
        self.treeview.column("#0", anchor="w", width=455 + 40)
        # self.treeview.column("size", anchor="n", width=80)
        self.treeview.column("lastmod", anchor="n", width=80 + 40)

        self.scroll_treeview = Scrollbar(
            self.body, command=self.treeview.yview)
        self.scroll_treeview.grid(row=0, column=8, sticky="nsew")
        self.treeview.config(yscrollcommand=self.scroll_treeview.set)

        self.info_button = Label(self.body, text=" ")
        self.info_button.grid(row=1, column=0, sticky="ws")

    def Toplevelwindows(self, **options):

        self.top = Toplevel(self.root, takefocus=True)
        self.top.geometry("310x100")
        self.top.focus_force()
        self.top.title("Setting ORCA-Q")
        self.top.iconbitmap("icons\\setting.ico")
        self.top.resizable(0, 0)
        self.top.grab_set()
        self.top_frame = Frame(self.top, width=100, height=300)
        self.top_frame.pack()
        self.top_dir = Label(self.top_frame, text="\nORCA Path:")
        self.top_dir.grid(row=0, column=0, sticky="w")
        self.et_top = ttk.Entry(self.top_frame, width=33)
        self.et_top.grid(row=1, column=0, columnspan=2, sticky="e")
        self.et_top.insert("end", datafile())
        self.bt_top = ttk.Button(
            self.top_frame, text="Browse...", command=lambda: open_dirORCA(self.et_top))
        self.bt_top.grid(row=1, column=2, sticky="w")
