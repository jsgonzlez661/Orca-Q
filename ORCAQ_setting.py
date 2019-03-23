from tkinter import Toplevel, Button, Frame, Label, Entry, IntVar
from tkinter import ttk
from tkinter import filedialog
from os.path import isfile

exe = ""
PAL = ""


def open_dirORCA(et_top):
	global exe
	global PAL
	dir_ORCA = filedialog.askopenfilename(title="Select ORCA dir", initialdir="C:\\Orca\\", filetypes=(("ORCA run", "*.exe"),))
	if(dir_ORCA!=None and dir_ORCA!=""):
		if(exe!=""):
			et_top.delete('0', "end")
			exe = dir_ORCA.replace("/","\\")		
			et_top.insert("end", exe)

def save_ini(num):
	global exe
	global PAL

	if(int(num.get())==0):
		PAL = 1
	else:
		PAL = 2

	setting_ini_w = open("setting.ini", 'w')
	setting_ini_w.write(str(PAL) + '\n')
	setting_ini_w.write(exe)
	setting_ini_w.close() 

def show_setting(root):
	global exe
	global PAL

	PALL, exe = read_ini()

	top = Toplevel(root, takefocus=True)
	top.focus_force()
	top.title("Setting ORCA-Q")
	top.iconbitmap("icons\\setting.ico")
	top.geometry("310x180")
	top.resizable(0,0)
	top.grab_set()
	top_frame = Frame(top, width=100, height=300)
	top_frame.pack()

	pall = IntVar(value=(PALL-1))

	top_qt = Label(top_frame, text="\nRun in series or parallel?")
	top_qt.grid(row=1, column=0, sticky="w")
	top_rb1 = ttk.Radiobutton(top_frame, text="Serie", value=0, variable=pall)
	top_rb1.grid(row=2, column=0)
	top_rb2 = ttk.Radiobutton(top_frame, text="Parallel", value=1, variable=pall)
	top_rb2.grid(row=2, column=1)

	top_dir = Label(top_frame, text="\nORCA Path:")
	top_dir.grid(row=4, column=0, sticky="w")
	et_top = ttk.Entry(top_frame, width=33)
	et_top.grid(row=5, column=0, columnspan=2, sticky="e")
	et_top.insert("end", exe)
	bt_top = ttk.Button(top_frame, text="Browse...", command=lambda:open_dirORCA(et_top))
	bt_top.grid(row=5, column=2, sticky="w")

	#print(pall.get())
	spe = Label(top_frame)
	spe.grid(row=6, column=0)
	bt_save = ttk.Button(top_frame, text="Save", command=lambda:save_ini(pall))
	bt_save.grid(row=7, column=0, columnspan=4)


def read_ini():
	global PAL
	global exe

	if(isfile("setting.ini")==True):
		setting_ini = open("setting.ini", 'r')
		PAL = int(setting_ini.readline())
		exe = setting_ini.readline()
		setting_ini.close() 
	else:
		PAL = 1
		exe = "C:\\Orca\\orca.exe"
		setting_ini_w = open("setting.ini", 'w')
		setting_ini_w.write(str(PAL) + '\n')
		setting_ini_w.write(exe)
		setting_ini_w.close() 
	return (PAL , exe)
