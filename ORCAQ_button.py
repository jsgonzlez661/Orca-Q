from tkinter import filedialog
from subprocess import run, CalledProcessError
from os.path import isfile
from ORCAQ_setting import read_ini
from psutil import process_iter, Process
from tkinter import messagebox

list_jobs = []
out = []

def add_job(treeview):
	global list_jobs
	addjob = filedialog.askopenfilenames(title="Add Jobs", initialdir="C:\\Orca\\", filetypes=(("ORCA Input File", "*.inp"),))
	if(addjob!=None):
		ai =	list(addjob)
		for j in range(len(ai)):
			ai[j] = ai[j].replace("/","\\")
		lt = list(ai)
		if(list_jobs==[]):
			list_jobs = list(ai)
			for w in range(0,len(list_jobs)):
				chg = list_jobs[w].replace(".inp", ".out")
				out.append(chg)
		else:
			for i in lt:
				if(i not in list_jobs):
					list_jobs.append(i)	
					chg = i.replace(".inp", ".out")
					out.append(chg)

		n_pal, direc = read_ini()			
		for i in lt:			
		 	if(treeview.exists(i)==False):
		 		treeview.insert("", "end", text=i, values=(str(n_pal), "0%"), iid=i)


def cleanup_jobs(treeview):
	global list_jobs
	if(list_jobs!=[]):
		for i in list_jobs:
			treeview.delete(i)
		list_jobs = []

def remove_jobs(treeview):
	global list_jobs
	global out
	if(list_jobs!=[]):
		list_remove = treeview.selection()
		list_remove = list(list_remove)
		for rem in list_remove:
			treeview.delete(rem)
			list_jobs.remove(rem)			
			out.remove(rem.replace(".inp", ".out"))

def info_job():
	messagebox.showinfo("All processor files")



def start_b(treeview, bt3, menu):
	global list_jobs
	global out

	if(list_jobs!=[]):
		menu.entryconfig(2, state="disabled")	
		bt3.config(state="disabled")
		N_pal, exe_dir = read_ini()
		pal_list = []

		for w in list_jobs:
			x , y = treeview.item(w, option='values')
			pal_list.append(x)

		#dir = "C:\\Program Files\\CCleaner\\CCleaner.exe"
		if(isfile(exe_dir)==True):
			for j in range(len(list_jobs)):	

				if(int(pal_list[j])==2):									
					caller =  exe_dir + ' ' + list_jobs[j] + ' > ' + out[j]
					execute = run(caller, shell=True)
					try:
						execute.check_returncode()
						treeview.item(list_jobs[j], values=[2, "100%"])	
					except CalledProcessError:
						treeview.item(list_jobs[j], values=[2, "error"])	
							
				if(int(pal_list[j])==1):
					caller = "orca.exe " + list_jobs[j] + ' > ' + out[j]
					execute = run(caller, shell=True)
					try:
						execute.check_returncode()
						treeview.item(list_jobs[j], values=[1, "100%"])	
					except CalledProcessError:
						treeview.item(list_jobs[j], values=[1, "error"])

			menu.entryconfig(2, state="active")	
			bt3.config(state="active")
			info_job()	
				#print(caller)
				
def cancell_ORCA():
	if(list_jobs!=[]):
		for itera in process_iter():
			if(itera.name()=="orca.exe"):
				p = Process(itera.pid)
				p.kill()
