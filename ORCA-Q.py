from tkinter import Tk, Frame, Button, Label, PhotoImage, Menu, Scrollbar
from tkinter import ttk
from tkinter import messagebox
from ORCAQ_setting import * 
from ORCAQ_button import *


root  = Tk()
root.geometry("640x480")
root.iconbitmap("icons orca-q\\orca-q-x32.ico")
root.title("ORCA-Q")
root.resizable(0 ,0)
# --------- Variable -------- #


# --------- End Variable -------- #

# --------- Functions --------- # 

def about_info():
	messagebox.showinfo("ORCA-Q version 0.1", "Program to run multiple ORCA files\nOpen Source\nVersion 0.1\n")

def exit_program():	
	value = messagebox.askokcancel("Exit","You want to exit ORCA-Q")	
	if(value==True):
		root.destroy()




# --------- End Functions --------- # 

# --------- Events --------- #

def info_change(event):
	info_button.config(text="Add a new jobs of ORCA")
def info_change2(event):
	info_button.config(text="Remove the selected jobs of ORCA")
def info_change3(event):
	info_button.config(text="Start the selected jobs of ORCA")
def info_change4(event):
	info_button.config(text="Cancel the selected jobs of ORCA")
def info_change5(event):
	info_button.config(text="Clean All ORCA jobs")
def info_change6(event):
	info_button.config(text="Setting Program ORCA-Q")

def info_none(event):
	info_button.config(text=" ")



# --------- End Events --------- #

# --------- Menu bar ---------

barMenu = Menu(root)
root.config(menu=barMenu)
root['menu'] = barMenu

archiveMenu     = Menu(barMenu, tearoff=0)
imgmenu_setting = PhotoImage(file="icons\\settingx16.png")
archiveMenu.add_command(label="Setting", image=imgmenu_setting, compound="left", command=lambda:show_setting(root))
archiveMenu.add_separator()
archiveMenu.add_command(label="Exit", command=lambda:exit_program())
barMenu.add_cascade(label="Archive", menu=archiveMenu)

jobsMenu    = Menu(barMenu, tearoff=0)
imgmenu_add = PhotoImage(file="icons\\addx16.png")      
jobsMenu.add_command(label="Add Jobs", image=imgmenu_add, compound="left", command=lambda:add_job(treeview))
imgmenu_remove = PhotoImage(file="icons\\removex16.png")
jobsMenu.add_command(label="Remove Jobs", image=imgmenu_remove, compound="left", command=lambda:remove_jobs(treeview))
jobsMenu.add_separator()

imgmenu_start = PhotoImage(file="icons\\startx16.png")
jobsMenu.add_command(label="Start Jobs", image=imgmenu_start, compound="left", command=lambda:start_b(treeview, bt3, jobsMenu))

imgmenu_cancell = PhotoImage(file="icons\\cancelx16.png")
jobsMenu.add_command(label="Cancell Jobs", image=imgmenu_cancell, compound="left", command=lambda:cancell_ORCA())
jobsMenu.add_separator()
imgmenu_cleanup = PhotoImage(file="icons\\cleanupx16.png")
jobsMenu.add_command(label="Clean All", image=imgmenu_cleanup, compound="left", command=lambda:cleanup_jobs(treeview))

barMenu.add_cascade(label="Jobs", menu=jobsMenu)

helpMenu = Menu(barMenu, tearoff=0)
helpMenu.add_command(label="Documentation")
helpMenu.add_separator()
helpMenu.add_command(label="About ORCA-Q", command=lambda:about_info())
barMenu.add_cascade(label="Help", menu=helpMenu)

# --------- End Menu bar --------- #

frame  = Frame(root, width=640, height=480)
frame.pack()

# --------- Button bar --------- #

imgbt1 = PhotoImage(file="icons\\add.png")
bt1    = Button(frame,text="Add", image=imgbt1, width=46, height=46, relief="flat",overrelief= "groove", compound="top", command=lambda:add_job(treeview))
bt1.bind("<Enter>", info_change)
bt1.bind("<Leave>", info_none)
bt1.grid(row=0, column=0, sticky="e", padx=10)

imgbt2 = PhotoImage(file="icons\\remove.png")
bt2    = Button(frame,text="Remove", image=imgbt2, width=46, height=46, relief="flat",overrelief= "groove", compound="top", command=lambda:remove_jobs(treeview))
bt2.bind("<Enter>", info_change2)
bt2.bind("<Leave>", info_none)
bt2.grid(row=0, column=1, sticky="e")

separator_bt = Label(frame, width=1).grid(row=0,column=2)

imgbt3 = PhotoImage(file="icons\\start.png")
bt3    = Button(frame,text="Start", image=imgbt3, width=46, height=46, relief="flat",overrelief= "groove", compound="top", command=lambda:start_b(treeview, bt3, barMenu))
bt3.bind("<Enter>", info_change3)
bt3.bind("<Leave>", info_none)
bt3.grid(row=0, column=3)

imgbt4 = PhotoImage(file="icons\\cancel.png")
bt4    = Button(frame,text="Cancell", image=imgbt4, width=46, height=46, relief="flat",overrelief= "groove", compound="top", command=lambda:cancell_ORCA())
bt4.bind("<Enter>", info_change4)
bt4.bind("<Leave>", info_none)
bt4.grid(row=0, column=4, padx=10)

separator_bt2 = Label(frame, width=1).grid(row=0,column=5)

imgbt5 = PhotoImage(file="icons\\cleanup.png")
bt5    = Button(frame, text="Clean All" , image=imgbt5, width=46, height=46, relief="flat", overrelief= "groove", compound="top", command=lambda:cleanup_jobs(treeview))
bt5.bind("<Enter>", info_change5)
bt5.bind("<Leave>", info_none)
bt5.grid(row=0, column=6)

imgbt6 = PhotoImage(file="icons\\setting.png")
bt6    = Button(frame, text="Setting" , image=imgbt6, width=46, height=46, relief="flat", overrelief= "groove", compound="top", command=lambda:show_setting(root))
bt6.bind("<Enter>", info_change6)
bt6.bind("<Leave>", info_none)
bt6.grid(row=0, column=7, padx=10)

separator_bt3 = Label(frame, width=36, height=4).grid(row=0,column=8)

# --------- End Button bar --------- #

# --------- Treeview --------- #

body = Frame(root, width=100, height=200)
body.pack()

treeview = ttk.Treeview(body, columns=("size", "lastmod"), height=17)
treeview.grid(row=0, column=0, columnspan=7)
treeview.heading("#0", text="Name")
treeview.heading("size", text="Processor")
treeview.heading("lastmod", text="Status")
#treeview.insert("", "end", text="input.inp", values=("2", "100%"))
treeview.column("#0", anchor="w", width=455) 
treeview.column("size", anchor="n", width=80) 
treeview.column("lastmod", anchor="n", width=80) 

scroll_treeview =Scrollbar(body, command=treeview.yview)             
scroll_treeview.grid(row=0, column=8, sticky="nsew")
treeview.config(yscrollcommand=scroll_treeview.set)

info_button = Label(body, text=" ")
info_button.grid(row=1, column=0, sticky="ws")

# --------- End Treeview --------- #



root.mainloop()
