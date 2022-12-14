#scrambler
#meta 1 - gerar embaralhamento - (igual ao c++)
#meta 1/2 - gerar embaralhamento de todos os puzzles
#meta 2 - adicionar timer
#meta 3 - guardar tempos e fazer continhas (botão de reset)
#meta 4 - gerar graficos
#meta 5 - gerar desenho do scramble
#meta 6 - ler stackmat
#meta 10 - ler dados wca e dizer em qual posição estaria 

import random
import time
# from msvcrt import getch
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile

import datetime
import csv
import numpy as np

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)


root = tk.Tk() 
root.title('timezinho') 
root.geometry('1000x600+1200+200') 
# root.geometry('1000x600') 
# root.iconphoto(False, tk.PhotoImage(file='/path/to/ico/icon.png'))

# Label 
row1 = ttk.LabelFrame(root)
row2 = ttk.LabelFrame(root)
row3 = ttk.LabelFrame(root)
# row3 = ttk.Frame(root)

row1.pack()
row2.pack()
# row2.pack(side=tk.TOP,anchor = tk.W)
row3.pack(side=tk.LEFT,anchor = tk.N)
# row3.pack()


t0 = 0
t1 = 0

actual_scramble = tk.StringVar()
actual_timer = tk.StringVar()

flag_R = 0
flag_L = 0
flag_U = 0
flag_D = 0
flag_F = 0
flag_B = 0

flag_Rw = 0
flag_Lw = 0
flag_Uw = 0
flag_Dw = 0
flag_Fw = 0
flag_Bw = 0

flag_3Rw = 0
flag_3Lw = 0
flag_3Uw = 0
flag_3Dw = 0
flag_3Fw = 0
flag_3Bw = 0

flag_7_event = 0

tempos = []
mo_3  = []
ao_5  = []
ao_12 = []
scrambles = []
datas = []

precisionTimer = 2
holdSpace = 550

best_mo3  = 9999
best_ao5  = 9999
best_ao12 = 9999

media_3  = 9999
media_5  = 9999
media_12 = 9999

global_best_solve = 9999
global_worst_solve = 0

index_best_mo3  = 0
index_best_ao5  = 0
index_best_ao12 = 0

countdown = 15
run_inspecton = False


our_canvas=tk.Canvas(root,width=450,height=350,bg="white")
our_canvas.pack(side = tk.RIGHT,anchor = tk.S)

#faces



Br_2 = np.array([[1,1],                 
                 [1,1]])

Lr_2 = np.array([[2,2],                 
                 [2,2]]) 

Vd_2 = np.array([[3,3],                 
                 [3,3]])

Vm_2 = np.array([[4,4],                 
                 [4,4]])

Az_2 = np.array([[5,5],                 
                 [5,5]])

Am_2 = np.array([[6,6],                 
                 [6,6]])

Buffer_2 = np.array([[0,0],
                     [0,0],
                     [0,0],
                     [0,0]])


Br_3 = np.array([[1,1,1],
                 [1,1,1],
                 [1,1,1]])

Lr_3 = np.array([[2,2,2],
                 [2,2,2],
                 [2,2,2]]) 

Vd_3 = np.array([[3,3,3],
                 [3,3,3],
                 [3,3,3]])

Vm_3 = np.array([[4,4,4],
                 [4,4,4],
                 [4,4,4]])

Az_3 = np.array([[5,5,5],
                 [5,5,5],
                 [5,5,5]])

Am_3 = np.array([[6,6,6],
                 [6,6,6],
                 [6,6,6]])

Buffer_3 = np.array([[0,0,0],
                     [0,0,0],
                     [0,0,0],
                     [0,0,0]])

Br_4 = np.array([[1,1,1,1],
                 [1,1,1,1],
                 [1,1,1,1],
                 [1,1,1,1]])

Lr_4 = np.array([[2,2,2,2],
                 [2,2,2,2],
                 [2,2,2,2],
                 [2,2,2,2]]) 
 
Vd_4 = np.array([[3,3,3,3],
                 [3,3,3,3],
                 [3,3,3,3],
                 [3,3,3,3]])

Vm_4 = np.array([[4,4,4,4],
                 [4,4,4,4],
                 [4,4,4,4],
                 [4,4,4,4]])

Az_4 = np.array([[5,5,5,5],
                 [5,5,5,5],
                 [5,5,5,5],
                 [5,5,5,5]])

Am_4 = np.array([[6,6,6,6],
                 [6,6,6,6],
                 [6,6,6,6],
                 [6,6,6,6]])

Buffer_4 = np.array([[0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0]])           


Br_5 = np.array([[1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1],
                 [1,1,1,1,1]])

Lr_5 = np.array([[2,2,2,2,2],
                 [2,2,2,2,2],
                 [2,2,2,2,2],
                 [2,2,2,2,2],
                 [2,2,2,2,2]]) 
 
Vd_5 = np.array([[3,3,3,3,3],
                 [3,3,3,3,3],
                 [3,3,3,3,3],
                 [3,3,3,3,3],
                 [3,3,3,3,3]])

Vm_5 = np.array([[4,4,4,4,4],
                 [4,4,4,4,4],
                 [4,4,4,4,4],
                 [4,4,4,4,4],
                 [4,4,4,4,4]])

Az_5 = np.array([[5,5,5,5,5],
                 [5,5,5,5,5],
                 [5,5,5,5,5],
                 [5,5,5,5,5],
                 [5,5,5,5,5]])

Am_5 = np.array([[6,6,6,6,6],
                 [6,6,6,6,6],
                 [6,6,6,6,6],
                 [6,6,6,6,6],
                 [6,6,6,6,6]])

Buffer_5 = np.array([[0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]])  


Br_6 = np.array([[1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1],
                 [1,1,1,1,1,1]])

Lr_6 = np.array([[2,2,2,2,2,2],
                 [2,2,2,2,2,2],
                 [2,2,2,2,2,2],
                 [2,2,2,2,2,2],
                 [2,2,2,2,2,2],
                 [2,2,2,2,2,2]]) 
 
Vd_6 = np.array([[3,3,3,3,3,3],
                 [3,3,3,3,3,3],
                 [3,3,3,3,3,3],
                 [3,3,3,3,3,3],
                 [3,3,3,3,3,3],
                 [3,3,3,3,3,3]])

Vm_6 = np.array([[4,4,4,4,4,4],
                 [4,4,4,4,4,4],
                 [4,4,4,4,4,4],
                 [4,4,4,4,4,4],
                 [4,4,4,4,4,4],
                 [4,4,4,4,4,4]])

Az_6 = np.array([[5,5,5,5,5,5],
                 [5,5,5,5,5,5],
                 [5,5,5,5,5,5],
                 [5,5,5,5,5,5],
                 [5,5,5,5,5,5],
                 [5,5,5,5,5,5]])

Am_6 = np.array([[6,6,6,6,6,6],
                 [6,6,6,6,6,6],
                 [6,6,6,6,6,6],
                 [6,6,6,6,6,6],
                 [6,6,6,6,6,6],
                 [6,6,6,6,6,6]])
         
Buffer_6 = np.array([[0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0],
                     [0,0,0,0,0,0]]) 


Br_7 = np.array([[1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1]])

                


Lr_7 = np.array([[2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2],
                 [2,2,2,2,2,2,2]]) 
 
Vd_7 = np.array([[3,3,3,3,3,3,3],
                 [3,3,3,3,3,3,3],
                 [3,3,3,3,3,3,3],
                 [3,3,3,3,3,3,3],
                 [3,3,3,3,3,3,3],
                 [3,3,3,3,3,3,3],
                 [3,3,3,3,3,3,3]])

Vm_7 = np.array([[4,4,4,4,4,4,4],
                 [4,4,4,4,4,4,4],
                 [4,4,4,4,4,4,4],
                 [4,4,4,4,4,4,4],
                 [4,4,4,4,4,4,4],
                 [4,4,4,4,4,4,4],
                 [4,4,4,4,4,4,4]])

Az_7 = np.array([[5,5,5,5,5,5,5],
                 [5,5,5,5,5,5,5],
                 [5,5,5,5,5,5,5],
                 [5,5,5,5,5,5,5],
                 [5,5,5,5,5,5,5],
                 [5,5,5,5,5,5,5],
                 [5,5,5,5,5,5,5]])

Am_7 = np.array([[6,6,6,6,6,6,6],
                 [6,6,6,6,6,6,6],
                 [6,6,6,6,6,6,6],
                 [6,6,6,6,6,6,6],
                 [6,6,6,6,6,6,6],
                 [6,6,6,6,6,6,6],
                 [6,6,6,6,6,6,6]])

Buffer_7 = np.array([[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0]]) 


Vm_pyra = np.array([[1,1,1,1,1],                 
                    [0,1,1,1,0],
                    [0,0,1,0,0]])
 
Vd_pyra = np.array([[0,0,2,0,0],                 
                    [0,2,2,2,0],
                    [2,2,2,2,2]])

Az_pyra = np.array([[3,3,3,3,3],                 
                    [0,3,3,3,0],
                    [0,0,3,0,0]])

Am_pyra = np.array([[4,4,4,4,4],                 
                    [0,4,4,4,0],
                    [0,0,4,0,0]])

Buffer_pyra = np.array([[0,0,0,0,0],
                        [0,0,0,0,0],                        
                        [0,0,0,0,0]])  
#-------------------------------------------------------------------------------------------
 

Br_color_2 = np.array([["white","white"],                       
                       ["white","white"]])

Lr_color_2 = np.array([["orange","orange"],                       
                       ["orange","orange"]]) 

Vd_color_2 = np.array([["green","green"],                       
                       ["green","green"]])

Vm_color_2 = np.array([["red","red"],                       
                       ["red","red"]])

Az_color_2 = np.array([["blue","blue"],                       
                       ["blue","blue"]])

Am_color_2 = np.array([["yellow","yellow"],                       
                       ["yellow","yellow"]])

# ------------------------------------------------------

Br_color_3 = np.array([["white","white","white"],
                       ["white","white","white"],
                       ["white","white","white"]])

Lr_color_3 = np.array([["orange","orange","orange"],
                       ["orange","orange","orange"],
                       ["orange","orange","orange"]]) 

Vd_color_3 = np.array([["green","green","green"],
                       ["green","green","green"],
                       ["green","green","green"]])

Vm_color_3 = np.array([["red","red","red"],
                       ["red","red","red"],
                       ["red","red","red"]])

Az_color_3 = np.array([["blue","blue","blue"],
                       ["blue","blue","blue"],
                       ["blue","blue","blue"]])

Am_color_3 = np.array([["yellow","yellow","yellow"],
                       ["yellow","yellow","yellow"],
                       ["yellow","yellow","yellow"]])


# ------------------------------------------------------

Br_color_4 = np.array([["white","white","white","white"],
                       ["white","white","white","white"],
                       ["white","white","white","white"],
                       ["white","white","white","white"]])

Lr_color_4 = np.array([["orange","orange","orange","orange"],
                       ["orange","orange","orange","orange"],
                       ["orange","orange","orange","orange"],
                       ["orange","orange","orange","orange"]]) 

Vd_color_4 = np.array([["green","green","green","green"],
                       ["green","green","green","green"],
                       ["green","green","green","green"],
                       ["green","green","green","green"]])

Vm_color_4 = np.array([["red","red","red","red"],
                       ["red","red","red","red"],
                       ["red","red","red","red"],
                       ["red","red","red","red"]])

Az_color_4 = np.array([["blue","blue","blue","blue"],
                       ["blue","blue","blue","blue"],
                       ["blue","blue","blue","blue"],
                       ["blue","blue","blue","blue"]])

Am_color_4 = np.array([["yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow"]])

# ------------------------------------------------------------

Br_color_5 = np.array([["white","white","white","white","white"],
                       ["white","white","white","white","white"],
                       ["white","white","white","white","white"],
                       ["white","white","white","white","white"],
                       ["white","white","white","white","white"]])

Lr_color_5 = np.array([["orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange"]]) 

Vd_color_5 = np.array([["green","green","green","green","green"],
                       ["green","green","green","green","green"],
                       ["green","green","green","green","green"],
                       ["green","green","green","green","green"],
                       ["green","green","green","green","green"]])

Vm_color_5 = np.array([["red","red","red","red","red"],
                       ["red","red","red","red","red"],
                       ["red","red","red","red","red"],
                       ["red","red","red","red","red"],
                       ["red","red","red","red","red"]])

Az_color_5 = np.array([["blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue"]])

Am_color_5 = np.array([["yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow"]])
                       

#-------------------------------------------------------------------

Br_color_6 = np.array([["white","white","white","white","white","white"],
                       ["white","white","white","white","white","white"],
                       ["white","white","white","white","white","white"],
                       ["white","white","white","white","white","white"],
                       ["white","white","white","white","white","white"],
                       ["white","white","white","white","white","white"]])

Lr_color_6 = np.array([["orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange"]]) 

Vd_color_6 = np.array([["green","green","green","green","green","green"],
                       ["green","green","green","green","green","green"],
                       ["green","green","green","green","green","green"],
                       ["green","green","green","green","green","green"],
                       ["green","green","green","green","green","green"],
                       ["green","green","green","green","green","green"]])

Vm_color_6 = np.array([["red","red","red","red","red","red"],
                       ["red","red","red","red","red","red"],
                       ["red","red","red","red","red","red"],
                       ["red","red","red","red","red","red"],
                       ["red","red","red","red","red","red"],
                       ["red","red","red","red","red","red"]])

Az_color_6 = np.array([["blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue"]])

Am_color_6 = np.array([["yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow"]])


# -----------------------------------------------------------------------

Br_color_7 = np.array([["white","white","white","white","white","white","white"],
                       ["white","white","white","white","white","white","white"],
                       ["white","white","white","white","white","white","white"],
                       ["white","white","white","white","white","white","white"],
                       ["white","white","white","white","white","white","white"],
                       ["white","white","white","white","white","white","white"],
                       ["white","white","white","white","white","white","white"]])

Lr_color_7 = np.array([["orange","orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange","orange"],
                       ["orange","orange","orange","orange","orange","orange","orange"]]) 

Vd_color_7 = np.array([["green","green","green","green","green","green","green"],
                       ["green","green","green","green","green","green","green"],
                       ["green","green","green","green","green","green","green"],
                       ["green","green","green","green","green","green","green"],
                       ["green","green","green","green","green","green","green"],
                       ["green","green","green","green","green","green","green"],
                       ["green","green","green","green","green","green","green"]])

Vm_color_7 = np.array([["red","red","red","red","red","red","red"],
                       ["red","red","red","red","red","red","red"],
                       ["red","red","red","red","red","red","red"],
                       ["red","red","red","red","red","red","red"],
                       ["red","red","red","red","red","red","red"],
                       ["red","red","red","red","red","red","red"],
                       ["red","red","red","red","red","red","red"]])

Az_color_7 = np.array([["blue","blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue","blue","blue"]])

Am_color_7 = np.array([["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow","yellow","yellow"]])

# -----------------------------------------------------------------------

Vd_color_pyra = np.array([["green","green","green","green","green"],
                       ["green","green","green","green","green"],                       
                       ["green","green","green","green","green"]])

Vm_color_pyra = np.array([["red","red","red","red","red"],
                       ["red","red","red","red","red"],                       
                       ["red","red","red","red","red"]])

Az_color_pyra = np.array([["blue","blue","blue","blue","blue"],
                       ["blue","blue","blue","blue","blue"],                       
                       ["blue","blue","blue","blue","blue"]])

Am_color_pyra = np.array([["yellow","yellow","yellow","yellow","yellow"],
                       ["yellow","yellow","yellow","yellow","yellow"],                       
                       ["yellow","yellow","yellow","yellow","yellow"]])

def trunc(n, decimals=0):
    # print(n)
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def time_convert(time):
    global precisionTimer
    if time < 60:
        presult = time
    else:
        m, s = divmod(time, 60)
        m = int(m)
        s = trunc(s,precisionTimer)
        if s >=10:
            presult = str(m) + ":" + str(s)
        else:
            presult = str(m) + ":0" + str(s)    
    
    return presult

def best_worst(lista,type):
    # 1 - global
    # 2 - local
    
    if type == "global":
        global global_best_solve
        global global_worst_solve        
        
        global_best_solve  = min(lista)        
        global_worst_solve = max(lista)

        return global_best_solve, global_worst_solve
        
    if type == "local":
        local_best_solve = 9999
        local_worst_solve = 0

        local_best_solve  = min(lista)        
        local_worst_solve = max(lista)        
    
        return local_best_solve, local_worst_solve
 
def average():
    return sum(tempos)/len(tempos) 

def mo3(vf):
    
    list_3 = tempos[vf-3:vf]
    print(list_3)
    average = sum(list_3)/len(list_3) 
    return average    

def ao5(vf):
    list_5 = tempos[vf-5:vf]
    
    b,w = best_worst(list_5,"local")
    print(b,w)
    average = (sum(list_5)-b-w)/3
    return average    

def ao12(vf):
    list_12 = tempos[vf-12:vf]
    b,w = best_worst(list_12,"local")
    average = (sum(list_12)-b-w)/10
    return average    

def estatistica(index):
    global global_best_solve
    global global_worst_solve
    global best_mo3
    global best_ao5
    global best_ao12
    global media_3
    global media_5
    global media_12
    global precisionTimer
    global index_best_mo3
    global index_best_ao5 
    global index_best_ao12

    
    # global tempos

    media = average()
    media_3  = mo3(index)  if index >= 3  else media_3
    media_5  = ao5(index)  if index >= 5  else media_5
    media_12 = ao12(index) if index >= 12 else media_12

    # media_3  = mo3(index)  if len(tempos) >= 3  or index > 3  else media_3
    # media_5  = ao5(index)  if len(tempos) >= 5  or index > 5  else media_5
    # media_12 = ao12(index) if len(tempos) >= 12 or index > 12 else media_12
 
    global_best_solve,global_worst_solve = best_worst(tempos,"global")
    
    best_mo3 = media_3 if media_3 < best_mo3 else best_mo3

    best_ao5 = media_5 if media_5 < best_ao5 else best_ao5

    best_ao12 = media_12 if media_12 < best_ao12 else best_ao12

    index_best_mo3  = index if media_3 < best_mo3 else index_best_mo3

    index_best_ao5  = index if media_5 < best_ao5 else index_best_ao5

    index_best_ao12  = index if media_12 < best_ao12 else index_best_ao12

    tempos[index-1] = trunc(tempos[index-1],precisionTimer)
    global_best_solve = trunc(global_best_solve,precisionTimer)
    global_worst_solve = trunc(global_worst_solve,precisionTimer)
    media = trunc(media,precisionTimer)
    media_3 = trunc(media_3,precisionTimer)
    media_5 = trunc(media_5,precisionTimer)
    media_12 = trunc(media_12,precisionTimer)
    best_mo3 = trunc(best_mo3,precisionTimer)
    best_ao5 = trunc(best_ao5,precisionTimer)
    best_ao12 = trunc(best_ao12,precisionTimer)

    ptempo = time_convert(tempos[index-1])
    pglobal_best_solve = time_convert(global_best_solve)
    pglobal_worst_solve = time_convert(global_worst_solve)
    pmedia = time_convert(media)
    pmedia_3 = time_convert(media_3)
    pmedia_5 = time_convert(media_5)
    pmedia_12 = time_convert(media_12)  
    pbest_mo3 = time_convert(best_mo3) 
    pbest_ao5 = time_convert(best_ao5) 
    pbest_ao12 = time_convert(best_ao12)    

    pmedia_3  = pmedia_3 if index >= 3 else 0
    pmedia_5  = pmedia_5 if index >= 5 else 0
    pmedia_12 = pmedia_12 if index >= 12 else 0

    pbest_mo3  = pbest_mo3 if index >= 3 else 0
    pbest_ao5  = pbest_ao5 if index >= 5 else 0
    pbest_ao12 = pbest_ao12 if index >= 12 else 0

    
    # tb_stat.insert(tk.END,"n° solves: " + str(len(tempos)))   
    # tb_stat.insert(tk.END,"pior:" + str(pglobal_worst_solve))
    # tb_stat.insert(tk.END,"media: " + str(pmedia))
   

    # tb_stat.delete(1)    
    for i in tb_stat.get_children():
        tb_stat.delete(i)

    root.update()

    tb_stat.insert(parent='',index='end',iid=0,text='',
    values=('time',str(ptempo),str(pglobal_best_solve)))

    if index >=3:
        tb_stat.insert(parent='',index='end',iid=1,text='',
        values=('mo3',str(pmedia_3),str(pbest_mo3)))
    
    if index >=5:
        tb_stat.insert(parent='',index='end',iid=2,text='',
        values=('ao5',str(pmedia_5),str(pbest_ao5)))
    
    if index >=12:
        tb_stat.insert(parent='',index='end',iid=3,text='',
        values=('ao12',str(pmedia_12),str(pbest_ao12)))

    tb_times.insert(parent='',index='end',iid=index,text='',
    values=(str(index),str(ptempo),str(pmedia_3),str(pmedia_5),str(pmedia_12)))
    
    tb_times.yview_moveto(1)

    if media_3 != 9999:
        mo_3.append(media_3)
    else:
        mo_3.append(None)
    
    if media_5 != 9999:
        ao_5.append(media_5)
    else:
        ao_5.append(None)
    
    if media_12 != 9999:
        ao_12.append(media_12)
    else:
        ao_12.append(None)
    
   

    
        


    
    





def define_flags(n_move):

    global flag_R
    global flag_L
    global flag_U
    global flag_D
    global flag_F
    global flag_B
    
    global flag_Rw
    global flag_Lw
    global flag_Uw
    global flag_Dw
    global flag_Fw
    global flag_Bw
    
    global flag_3Rw
    global flag_3Lw
    global flag_3Uw
    global flag_3Dw
    global flag_3Fw
    global flag_3Bw
    
    
    if (n_move == 1 or n_move == 2 or n_move == 3):
        flag_R = 1            
        flag_U = 0
        flag_D = 0
        flag_F = 0
        flag_B = 0

        flag_Uw = 0
        flag_Dw = 0
        flag_Fw = 0
        flag_Bw = 0

        flag_3Uw = 0
        flag_3Dw = 0
        flag_3Fw = 0
        flag_3Bw = 0
                
    elif (n_move == 4 or n_move == 5 or n_move == 6):
        flag_L = 1            
        flag_U = 0
        flag_D = 0
        flag_F = 0
        flag_B = 0

        flag_Uw = 0
        flag_Dw = 0
        flag_Fw = 0
        flag_Bw = 0

        flag_3Uw = 0
        flag_3Dw = 0
        flag_3Fw = 0
        flag_3Bw = 0
                
    elif (n_move == 7 or n_move == 8 or n_move == 9):
        flag_U = 1            
        flag_R = 0
        flag_L = 0
        flag_F = 0
        flag_B = 0

        flag_Rw = 0
        flag_Lw = 0
        flag_Fw = 0
        flag_Bw = 0

        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Fw = 0
        flag_3Bw = 0
                
    elif (n_move == 10 or n_move == 11 or n_move == 12):
        flag_D = 1            
        flag_R = 0
        flag_L = 0
        flag_F = 0
        flag_B = 0

        flag_Rw = 0
        flag_Lw = 0
        flag_Fw = 0
        flag_Bw = 0

        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Fw = 0
        flag_3Bw = 0

    elif (n_move == 13 or n_move == 14 or n_move == 15):
        flag_F = 1            
        flag_R = 0
        flag_L = 0
        flag_D = 0
        flag_U = 0

        flag_Rw = 0
        flag_Lw = 0
        flag_Dw = 0
        flag_Uw = 0

        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Dw = 0
        flag_3Uw = 0

    elif (n_move == 16 or n_move == 17 or n_move == 18):
        flag_B = 1            
        flag_R = 0
        flag_L = 0
        flag_D = 0
        flag_U = 0

        flag_Rw = 0
        flag_Lw = 0
        flag_Dw = 0
        flag_Uw = 0

        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Dw = 0
        flag_3Uw = 0

    elif (n_move == 19 or n_move == 20 or n_move == 21):
        flag_Rw = 1            
        flag_Uw = 0
        flag_Dw = 0
        flag_Fw = 0
        flag_Bw = 0

        flag_U = 0
        flag_D = 0
        flag_F = 0
        flag_B = 0

        flag_3Uw = 0
        flag_3Dw = 0
        flag_3Fw = 0
        flag_3Bw = 0

    elif (n_move == 22 or n_move == 23 or n_move == 24):
        flag_Lw = 1            
        flag_Uw = 0
        flag_Dw = 0
        flag_Fw = 0
        flag_Bw = 0

        flag_U = 0
        flag_D = 0
        flag_F = 0
        flag_B = 0

        flag_3Uw = 0
        flag_3Dw = 0
        flag_3Fw = 0
        flag_3Bw = 0

    elif (n_move == 25 or n_move == 26 or n_move == 27):
        flag_Uw = 1            
        flag_Rw = 0
        flag_Lw = 0
        flag_Fw = 0
        flag_Bw = 0

        flag_R = 0
        flag_L = 0
        flag_F = 0
        flag_B = 0

        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Fw = 0
        flag_3Bw = 0

    elif (n_move == 28 or n_move == 29 or n_move == 30):
        flag_Dw = 1            
        flag_Rw = 0
        flag_Lw = 0
        flag_Fw = 0
        flag_Bw = 0

        flag_R = 0
        flag_L = 0
        flag_F = 0
        flag_B = 0

        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Fw = 0
        flag_3Bw = 0

    elif (n_move == 31 or n_move == 32 or n_move == 33):
        flag_Fw = 1            
        flag_Rw = 0
        flag_Lw = 0
        flag_Dw = 0
        flag_Uw = 0

        flag_R = 0
        flag_L = 0
        flag_D = 0
        flag_U = 0

        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Dw = 0
        flag_3Uw = 0

    elif (n_move == 34 or n_move == 35 or n_move == 36):
        flag_Bw = 1            
        flag_Rw = 0
        flag_Lw = 0
        flag_Dw = 0
        flag_Uw = 0

        flag_R = 0
        flag_L = 0
        flag_D = 0
        flag_U = 0

        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Dw = 0
        flag_3Uw = 0

    elif (n_move == 37 or n_move == 38 or n_move == 39):
        flag_3Rw = 1            
        flag_3Uw = 0
        flag_3Dw = 0
        flag_3Fw = 0
        flag_3Bw = 0

        flag_U = 0
        flag_D = 0
        flag_F = 0
        flag_B = 0

        flag_Uw = 0
        flag_Dw = 0
        flag_Fw = 0
        flag_Bw = 0

    elif (n_move == 40 or n_move == 41 or n_move == 42):
        flag_3Lw = 1            
        flag_3Uw = 0
        flag_3Dw = 0
        flag_3Fw = 0
        flag_3Bw = 0

        flag_U = 0
        flag_D = 0
        flag_F = 0
        flag_B = 0

        flag_Uw = 0
        flag_Dw = 0
        flag_Fw = 0
        flag_Bw = 0

    elif (n_move == 43 or n_move == 44 or n_move == 45):
        flag_3Uw = 1            
        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Fw = 0
        flag_3Bw = 0

        flag_R = 0
        flag_L = 0
        flag_F = 0
        flag_B = 0

        flag_Rw = 0
        flag_Lw = 0
        flag_Fw = 0
        flag_Bw = 0

    elif (n_move == 46 or n_move == 47 or n_move == 48):
        flag_3Dw = 1            
        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Fw = 0
        flag_3Bw = 0

        flag_R = 0
        flag_L = 0
        flag_F = 0
        flag_B = 0

        flag_Rw = 0
        flag_Lw = 0
        flag_Fw = 0
        flag_Bw = 0

    elif (n_move == 49 or n_move == 50 or n_move == 51):
        flag_3Fw = 1            
        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Dw = 0
        flag_3Uw = 0

        flag_R = 0
        flag_L = 0
        flag_D = 0
        flag_U = 0

        flag_Rw = 0
        flag_Lw = 0
        flag_Dw = 0
        flag_Uw = 0

    elif (n_move == 52 or n_move == 53 or n_move == 54):
        flag_3Bw = 1            
        flag_3Rw = 0
        flag_3Lw = 0
        flag_3Dw = 0
        flag_3Uw = 0

        flag_R = 0
        flag_L = 0
        flag_D = 0
        flag_U = 0

        flag_Rw = 0
        flag_Lw = 0
        flag_Dw = 0
        flag_Uw = 0

def reset_flags():
        
    global flag_R
    global flag_L
    global flag_U
    global flag_D
    global flag_F
    global flag_B

    global flag_Rw
    global flag_Lw
    global flag_Uw
    global flag_Dw
    global flag_Fw
    global flag_Bw

    global flag_3Rw
    global flag_3Lw
    global flag_3Uw
    global flag_3Dw
    global flag_3Fw
    global flag_3Bw

    flag_R = 0
    flag_L = 0
    flag_U = 0
    flag_D = 0
    flag_F = 0
    flag_B = 0

    flag_Rw = 0
    flag_Lw = 0
    flag_Uw = 0
    flag_Dw = 0
    flag_Fw = 0
    flag_Bw = 0

    flag_3Rw = 0
    flag_3Lw = 0
    flag_3Uw = 0
    flag_3Dw = 0
    flag_3Fw = 0
    flag_3Bw = 0

def reset_draw():

    global Br_2
    global Lr_2
    global Vd_2
    global Vm_2
    global Az_2
    global Am_2

    global Br_3
    global Lr_3
    global Vd_3
    global Vm_3
    global Az_3
    global Am_3

    global Br_4
    global Lr_4
    global Vd_4
    global Vm_4
    global Az_4
    global Am_4

    global Br_5
    global Lr_5
    global Vd_5
    global Vm_5
    global Az_5
    global Am_5

    global Br_6
    global Lr_6
    global Vd_6
    global Vm_6
    global Az_6
    global Am_6

    global Br_7
    global Lr_7
    global Vd_7
    global Vm_7
    global Az_7
    global Am_7  

    global Vm_pyra  
    global Vd_pyra 
    global Az_pyra 
    global Am_pyra

    
    Br_2 = np.array([[1,1],                 
                    [1,1]])

    Lr_2 = np.array([[2,2],                 
                    [2,2]]) 

    Vd_2 = np.array([[3,3],                 
                    [3,3]])

    Vm_2 = np.array([[4,4],                 
                    [4,4]])

    Az_2 = np.array([[5,5],                 
                    [5,5]])

    Am_2 = np.array([[6,6],                 
                    [6,6]]) 


    Br_3 = np.array([[1,1,1],
                     [1,1,1],
                     [1,1,1]])

    Lr_3 = np.array([[2,2,2],
                     [2,2,2],
                     [2,2,2]]) 

    Vd_3 = np.array([[3,3,3],
                     [3,3,3],
                     [3,3,3]])

    Vm_3 = np.array([[4,4,4],
                     [4,4,4],
                     [4,4,4]])

    Az_3 = np.array([[5,5,5],
                     [5,5,5],
                     [5,5,5]])

    Am_3 = np.array([[6,6,6],
                     [6,6,6],
                     [6,6,6]])

    Br_4 = np.array([[1,1,1,1],
                     [1,1,1,1],
                     [1,1,1,1],
                     [1,1,1,1]])

    Lr_4 = np.array([[2,2,2,2],
                     [2,2,2,2],
                     [2,2,2,2],
                     [2,2,2,2]]) 
 
    Vd_4 = np.array([[3,3,3,3],
                     [3,3,3,3],
                     [3,3,3,3],
                     [3,3,3,3]])

    Vm_4 = np.array([[4,4,4,4],
                     [4,4,4,4],
                     [4,4,4,4],
                     [4,4,4,4]])

    Az_4 = np.array([[5,5,5,5],
                     [5,5,5,5],
                     [5,5,5,5],
                     [5,5,5,5]])

    Am_4 = np.array([[6,6,6,6],
                     [6,6,6,6],
                     [6,6,6,6],
                     [6,6,6,6]])
            


    Br_5 = np.array([[1,1,1,1,1],
                     [1,1,1,1,1],
                     [1,1,1,1,1],
                     [1,1,1,1,1],
                     [1,1,1,1,1]])

    Lr_5 = np.array([[2,2,2,2,2],
                     [2,2,2,2,2],
                     [2,2,2,2,2],
                     [2,2,2,2,2],
                     [2,2,2,2,2]]) 
 
    Vd_5 = np.array([[3,3,3,3,3],
                     [3,3,3,3,3],
                     [3,3,3,3,3],
                     [3,3,3,3,3],
                     [3,3,3,3,3]])

    Vm_5 = np.array([[4,4,4,4,4],
                     [4,4,4,4,4],
                     [4,4,4,4,4],
                     [4,4,4,4,4],
                     [4,4,4,4,4]])

    Az_5 = np.array([[5,5,5,5,5],
                     [5,5,5,5,5],
                     [5,5,5,5,5],
                     [5,5,5,5,5],
                     [5,5,5,5,5]])

    Am_5 = np.array([[6,6,6,6,6],
                     [6,6,6,6,6],
                     [6,6,6,6,6],
                     [6,6,6,6,6],
                     [6,6,6,6,6]])

    Buffer_5 = np.array([[0,0,0,0,0],
                         [0,0,0,0,0],
                         [0,0,0,0,0],
                         [0,0,0,0,0]])  


    Br_6 = np.array([[1,1,1,1,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1]])

    Lr_6 = np.array([[2,2,2,2,2,2],
                     [2,2,2,2,2,2],
                     [2,2,2,2,2,2],
                     [2,2,2,2,2,2],
                     [2,2,2,2,2,2],
                     [2,2,2,2,2,2]]) 
 
    Vd_6 = np.array([[3,3,3,3,3,3],
                     [3,3,3,3,3,3],
                     [3,3,3,3,3,3],
                     [3,3,3,3,3,3],
                     [3,3,3,3,3,3],
                     [3,3,3,3,3,3]])

    Vm_6 = np.array([[4,4,4,4,4,4],
                     [4,4,4,4,4,4],
                     [4,4,4,4,4,4],
                     [4,4,4,4,4,4],
                     [4,4,4,4,4,4],
                     [4,4,4,4,4,4]])

    Az_6 = np.array([[5,5,5,5,5,5],
                     [5,5,5,5,5,5],
                     [5,5,5,5,5,5],
                     [5,5,5,5,5,5],
                     [5,5,5,5,5,5],
                     [5,5,5,5,5,5]])

    Am_6 = np.array([[6,6,6,6,6,6],
                     [6,6,6,6,6,6],
                     [6,6,6,6,6,6],
                     [6,6,6,6,6,6],
                     [6,6,6,6,6,6],
                     [6,6,6,6,6,6]])



    Br_7 = np.array([[1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1]])

    Lr_7 = np.array([[2,2,2,2,2,2,2],
                     [2,2,2,2,2,2,2],
                     [2,2,2,2,2,2,2],
                     [2,2,2,2,2,2,2],
                     [2,2,2,2,2,2,2],
                     [2,2,2,2,2,2,2],
                     [2,2,2,2,2,2,2]]) 
 
    Vd_7 = np.array([[3,3,3,3,3,3,3],
                     [3,3,3,3,3,3,3],
                     [3,3,3,3,3,3,3],
                     [3,3,3,3,3,3,3],
                     [3,3,3,3,3,3,3],
                     [3,3,3,3,3,3,3],
                     [3,3,3,3,3,3,3]])

    Vm_7 = np.array([[4,4,4,4,4,4,4],
                     [4,4,4,4,4,4,4],
                     [4,4,4,4,4,4,4],
                     [4,4,4,4,4,4,4],
                     [4,4,4,4,4,4,4],
                     [4,4,4,4,4,4,4],
                     [4,4,4,4,4,4,4]])

    Az_7 = np.array([[5,5,5,5,5,5,5],
                     [5,5,5,5,5,5,5],
                     [5,5,5,5,5,5,5],
                     [5,5,5,5,5,5,5],
                     [5,5,5,5,5,5,5],
                     [5,5,5,5,5,5,5],
                     [5,5,5,5,5,5,5]])

    Am_7 = np.array([[6,6,6,6,6,6,6],
                     [6,6,6,6,6,6,6],
                     [6,6,6,6,6,6,6],
                     [6,6,6,6,6,6,6],
                     [6,6,6,6,6,6,6],
                     [6,6,6,6,6,6,6],
                     [6,6,6,6,6,6,6]])
    
    Vm_pyra = np.array([[1,1,1,1,1],                 
                        [0,1,1,1,0],
                        [0,0,1,0,0]])
 
    Vd_pyra = np.array([[0,0,2,0,0],                 
                        [0,2,2,2,0],
                        [2,2,2,2,2]])

    Az_pyra = np.array([[3,3,3,3,3],                 
                        [0,3,3,3,0],
                        [0,0,3,0,0]])

    Am_pyra = np.array([[4,4,4,4,4],                 
                        [0,4,4,4,0],
                        [0,0,4,0,0]])
    

    
def turn_draw(cube,turn):

    global Br_2  
    global Lr_2  
    global Vd_2  
    global Vm_2  
    global Az_2  
    global Am_2  
    global Buffer_2

    global Br_3  
    global Lr_3  
    global Vd_3  
    global Vm_3  
    global Az_3  
    global Am_3  
    global Buffer_3

    global Br_4
    global Lr_4
    global Vd_4
    global Vm_4
    global Az_4
    global Am_4
    global Buffer_4

    global Br_5
    global Lr_5
    global Vd_5
    global Vm_5
    global Az_5
    global Am_5
    global Buffer_5

    global Br_6
    global Lr_6
    global Vd_6
    global Vm_6
    global Az_6
    global Am_6
    global Buffer_6

    global Br_7
    global Lr_7
    global Vd_7
    global Vm_7
    global Az_7
    global Am_7
    global Buffer_7

    if cube == "2x2":
        if turn == "R":
            Buffer_2[0] = Vd_2[:,1]
            Buffer_2[1] = np.flip(Br_2[:,1],0)
            Buffer_2[2] = np.flip(Az_2[:,0],0)
            Buffer_2[3] = Am_2[:,1]            

            Br_2[:,1] = Buffer_2[0]
            Az_2[:,0] = Buffer_2[1]
            Am_2[:,1] = Buffer_2[2]
            Vd_2[:,1] = Buffer_2[3]

            Vm_2 = np.rot90(Vm_2,1,(1,0))
        elif turn == "R'":

            Buffer_2[0] = Vd_2[:,1]
            Buffer_2[1] = np.flip(Br_2[:,1],0)
            Buffer_2[2] = np.flip(Az_2[:,0],0)
            Buffer_2[3] = Am_2[:,1]            

            Br_2[:,1] = Buffer_2[0]
            Az_2[:,0] = Buffer_2[1]
            Am_2[:,1] = Buffer_2[2]
            Vd_2[:,1] = Buffer_2[3]
            

            Buffer_2[0] = Vd_2[:,1]
            Buffer_2[1] = np.flip(Br_2[:,1],0)
            Buffer_2[2] = np.flip(Az_2[:,0],0)
            Buffer_2[3] = Am_2[:,1]            

            Br_2[:,1] = Buffer_2[0]
            Az_2[:,0] = Buffer_2[1]
            Am_2[:,1] = Buffer_2[2]
            Vd_2[:,1] = Buffer_2[3]
            

            Buffer_2[0] = Vd_2[:,1]
            Buffer_2[1] = np.flip(Br_2[:,1],0)
            Buffer_2[2] = np.flip(Az_2[:,0],0)
            Buffer_2[3] = Am_2[:,1]            

            Br_2[:,1] = Buffer_2[0]
            Az_2[:,0] = Buffer_2[1]
            Am_2[:,1] = Buffer_2[2]
            Vd_2[:,1] = Buffer_2[3]           
            

            Vm_2 = np.rot90(Vm_2,-1,(1,0))
        elif turn == "R2":

            Buffer_2[0] = Vd_2[:,1]
            Buffer_2[1] = np.flip(Br_2[:,1],0)
            Buffer_2[2] = np.flip(Az_2[:,0],0)
            Buffer_2[3] = Am_2[:,1]            

            Br_2[:,1] = Buffer_2[0]
            Az_2[:,0] = Buffer_2[1]
            Am_2[:,1] = Buffer_2[2]
            Vd_2[:,1] = Buffer_2[3]           

            Buffer_2[0] = Vd_2[:,1]
            Buffer_2[1] = np.flip(Br_2[:,1],0)
            Buffer_2[2] = np.flip(Az_2[:,0],0)
            Buffer_2[3] = Am_2[:,1]            

            Br_2[:,1] = Buffer_2[0]
            Az_2[:,0] = Buffer_2[1]
            Am_2[:,1] = Buffer_2[2]
            Vd_2[:,1] = Buffer_2[3]      
            
            Vm_2 = np.rot90(Vm_2,2,(1,0))
        
        elif turn == "U":
            Buffer_2[0] = Vd_2[0]
            Buffer_2[1] = Lr_2[0]
            Buffer_2[2] = Az_2[0]
            Buffer_2[3] = Vm_2[0]

            Lr_2[0] = Buffer_2[0]
            Az_2[0] = Buffer_2[1]
            Vm_2[0] = Buffer_2[2]
            Vd_2[0] = Buffer_2[3]

            Br_2 = np.rot90(Br_2,1,(1,0))
        elif turn == "U'":
            Buffer_2[0] = Vd_2[0]
            Buffer_2[1] = Lr_2[0]
            Buffer_2[2] = Az_2[0]
            Buffer_2[3] = Vm_2[0]

            Lr_2[0] = Buffer_2[0]
            Az_2[0] = Buffer_2[1]
            Vm_2[0] = Buffer_2[2]
            Vd_2[0] = Buffer_2[3]
            Buffer_2[0] = Vd_2[0]
            Buffer_2[1] = Lr_2[0]
            Buffer_2[2] = Az_2[0]
            Buffer_2[3] = Vm_2[0]

            Lr_2[0] = Buffer_2[0]
            Az_2[0] = Buffer_2[1]
            Vm_2[0] = Buffer_2[2]
            Vd_2[0] = Buffer_2[3]
            Buffer_2[0] = Vd_2[0]
            Buffer_2[1] = Lr_2[0]
            Buffer_2[2] = Az_2[0]
            Buffer_2[3] = Vm_2[0]

            Lr_2[0] = Buffer_2[0]
            Az_2[0] = Buffer_2[1]
            Vm_2[0] = Buffer_2[2]
            Vd_2[0] = Buffer_2[3]

            Br_2 = np.rot90(Br_2,-1,(1,0))
        elif turn == "U2":
            Buffer_2[0] = Vd_2[0]
            Buffer_2[1] = Lr_2[0]
            Buffer_2[2] = Az_2[0]
            Buffer_2[3] = Vm_2[0]

            Lr_2[0] = Buffer_2[0]
            Az_2[0] = Buffer_2[1]
            Vm_2[0] = Buffer_2[2]
            Vd_2[0] = Buffer_2[3]
            Buffer_2[0] = Vd_2[0]
            Buffer_2[1] = Lr_2[0]
            Buffer_2[2] = Az_2[0]
            Buffer_2[3] = Vm_2[0]

            Lr_2[0] = Buffer_2[0]
            Az_2[0] = Buffer_2[1]
            Vm_2[0] = Buffer_2[2]
            Vd_2[0] = Buffer_2[3]

            Br_2 = np.rot90(Br_2,2,(1,0))
        
        elif turn == "F":
            Buffer_2[0] = Br_2[1]
            Buffer_2[1] = np.flip(Vm_2[:,0],0)
            Buffer_2[2] = Am_2[0]
            Buffer_2[3] = np.flip(Lr_2[:,1],0)

            Vm_2[:,0] = Buffer_2[0]
            Am_2[0]   = Buffer_2[1]
            Lr_2[:,1] = Buffer_2[2]
            Br_2[1]   = Buffer_2[3]

            Vd_2 = np.rot90(Vd_2,1,(1,0))
        elif turn == "F'":

            Buffer_2[0] = Br_2[1]
            Buffer_2[1] = np.flip(Vm_2[:,0],0)
            Buffer_2[2] = Am_2[0]
            Buffer_2[3] = np.flip(Lr_2[:,1],0)

            Vm_2[:,0] = Buffer_2[0]
            Am_2[0]   = Buffer_2[1]
            Lr_2[:,1] = Buffer_2[2]
            Br_2[1]   = Buffer_2[3]

            Buffer_2[0] = Br_2[1]
            Buffer_2[1] = np.flip(Vm_2[:,0],0)
            Buffer_2[2] = Am_2[0]
            Buffer_2[3] = np.flip(Lr_2[:,1],0)

            Vm_2[:,0] = Buffer_2[0]
            Am_2[0]   = Buffer_2[1]
            Lr_2[:,1] = Buffer_2[2]
            Br_2[1]   = Buffer_2[3]

            Buffer_2[0] = Br_2[1]
            Buffer_2[1] = np.flip(Vm_2[:,0],0)
            Buffer_2[2] = Am_2[0]
            Buffer_2[3] = np.flip(Lr_2[:,1],0)

            Vm_2[:,0] = Buffer_2[0]
            Am_2[0]   = Buffer_2[1]
            Lr_2[:,1] = Buffer_2[2]
            Br_2[1]   = Buffer_2[3]
            

            Vd_2 = np.rot90(Vd_2,-1,(1,0))
        elif turn == "F2":

            Buffer_2[0] = Br_2[1]
            Buffer_2[1] = np.flip(Vm_2[:,0],0)
            Buffer_2[2] = Am_2[0]
            Buffer_2[3] = np.flip(Lr_2[:,1],0)

            Vm_2[:,0] = Buffer_2[0]
            Am_2[0]   = Buffer_2[1]
            Lr_2[:,1] = Buffer_2[2]
            Br_2[1]   = Buffer_2[3]

            Buffer_2[0] = Br_2[1]
            Buffer_2[1] = np.flip(Vm_2[:,0],0)
            Buffer_2[2] = Am_2[0]
            Buffer_2[3] = np.flip(Lr_2[:,1],0)

            Vm_2[:,0] = Buffer_2[0]
            Am_2[0]   = Buffer_2[1]
            Lr_2[:,1] = Buffer_2[2]
            Br_2[1]   = Buffer_2[3]            

            Vd_2 = np.rot90(Vd_2,2,(1,0))
        

    elif cube == "3x3":

        if turn == "R":
            Buffer_3[0] = Vd_3[:,2]
            Buffer_3[1] = np.flip(Br_3[:,2],0)
            Buffer_3[2] = np.flip(Az_3[:,0],0)
            Buffer_3[3] = Am_3[:,2]            

            Br_3[:,2] = Buffer_3[0]
            Az_3[:,0] = Buffer_3[1]
            Am_3[:,2] = Buffer_3[2]
            Vd_3[:,2] = Buffer_3[3]
            Vm_3 = np.rot90(Vm_3,1,(1,0))
        elif turn == "R'":
            Buffer_3[0] = Vd_3[:,2]
            Buffer_3[1] = np.flip(Br_3[:,2],0)
            Buffer_3[2] = np.flip(Az_3[:,0],0)
            Buffer_3[3] = Am_3[:,2]

            Br_3[:,2] = Buffer_3[0]
            Az_3[:,0] = Buffer_3[1]
            Am_3[:,2] = Buffer_3[2]
            Vd_3[:,2] = Buffer_3[3]
            Buffer_3[0] = Vd_3[:,2]
            Buffer_3[1] = np.flip(Br_3[:,2],0)
            Buffer_3[2] = np.flip(Az_3[:,0],0)
            Buffer_3[3] = Am_3[:,2]

            Br_3[:,2] = Buffer_3[0]
            Az_3[:,0] = Buffer_3[1]
            Am_3[:,2] = Buffer_3[2]
            Vd_3[:,2] = Buffer_3[3]
            Buffer_3[0] = Vd_3[:,2]
            Buffer_3[1] = np.flip(Br_3[:,2],0)
            Buffer_3[2] = np.flip(Az_3[:,0],0)
            Buffer_3[3] = Am_3[:,2]

            Br_3[:,2] = Buffer_3[0]
            Az_3[:,0] = Buffer_3[1]
            Am_3[:,2] = Buffer_3[2]
            Vd_3[:,2] = Buffer_3[3]

            Vm_3 = np.rot90(Vm_3,-1,(1,0))
        elif turn == "R2":
            Buffer_3[0] = Vd_3[:,2]
            Buffer_3[1] = np.flip(Br_3[:,2],0)
            Buffer_3[2] = np.flip(Az_3[:,0],0)
            Buffer_3[3] = Am_3[:,2]

            Br_3[:,2] = Buffer_3[0]
            Az_3[:,0] = Buffer_3[1]
            Am_3[:,2] = Buffer_3[2]
            Vd_3[:,2] = Buffer_3[3]

            Buffer_3[0] = Vd_3[:,2]
            Buffer_3[1] = np.flip(Br_3[:,2],0)
            Buffer_3[2] = np.flip(Az_3[:,0],0)
            Buffer_3[3] = Am_3[:,2]

            Br_3[:,2] = Buffer_3[0]
            Az_3[:,0] = Buffer_3[1]
            Am_3[:,2] = Buffer_3[2]
            Vd_3[:,2] = Buffer_3[3]

            Vm_3 = np.rot90(Vm_3,2,(1,0))
        elif turn == "L":
            Buffer_3[0] = Vd_3[:,0]
            Buffer_3[1] = np.flip(Am_3[:,0],0)
            Buffer_3[2] = np.flip(Az_3[:,2],0)
            Buffer_3[3] = Br_3[:,0]

            Am_3[:,0] = Buffer_3[0]
            Az_3[:,2] = Buffer_3[1]
            Br_3[:,0] = Buffer_3[2]
            Vd_3[:,0] = Buffer_3[3]

            Lr_3 = np.rot90(Lr_3,1,(1,0))
        elif turn == "L'":
            Buffer_3[0] = Vd_3[:,0]
            Buffer_3[1] = np.flip(Am_3[:,0],0)
            Buffer_3[2] = np.flip(Az_3[:,2],0)
            Buffer_3[3] = Br_3[:,0]

            Am_3[:,0] = Buffer_3[0]
            Az_3[:,2] = Buffer_3[1]
            Br_3[:,0] = Buffer_3[2]
            Vd_3[:,0] = Buffer_3[3]
            Buffer_3[0] = Vd_3[:,0]
            Buffer_3[1] = np.flip(Am_3[:,0],0)
            Buffer_3[2] = np.flip(Az_3[:,2],0)
            Buffer_3[3] = Br_3[:,0]

            Am_3[:,0] = Buffer_3[0]
            Az_3[:,2] = Buffer_3[1]
            Br_3[:,0] = Buffer_3[2]
            Vd_3[:,0] = Buffer_3[3]
            Buffer_3[0] = Vd_3[:,0]
            Buffer_3[1] = np.flip(Am_3[:,0],0)
            Buffer_3[2] = np.flip(Az_3[:,2],0)
            Buffer_3[3] = Br_3[:,0]

            Am_3[:,0] = Buffer_3[0]
            Az_3[:,2] = Buffer_3[1]
            Br_3[:,0] = Buffer_3[2]
            Vd_3[:,0] = Buffer_3[3]

            Lr_3 = np.rot90(Lr_3,-1,(1,0))
        elif turn == "L2":
            Buffer_3[0] = Vd_3[:,0]
            Buffer_3[1] = np.flip(Am_3[:,0],0)
            Buffer_3[2] = np.flip(Az_3[:,2],0)
            Buffer_3[3] = Br_3[:,0]

            Am_3[:,0] = Buffer_3[0]
            Az_3[:,2] = Buffer_3[1]
            Br_3[:,0] = Buffer_3[2]
            Vd_3[:,0] = Buffer_3[3]
            Buffer_3[0] = Vd_3[:,0]
            Buffer_3[1] = np.flip(Am_3[:,0],0)
            Buffer_3[2] = np.flip(Az_3[:,2],0)
            Buffer_3[3] = Br_3[:,0]

            Am_3[:,0] = Buffer_3[0]
            Az_3[:,2] = Buffer_3[1]
            Br_3[:,0] = Buffer_3[2]
            Vd_3[:,0] = Buffer_3[3]

            Lr_3 = np.rot90(Lr_3,2,(1,0))
        elif turn == "U":
            Buffer_3[0] = Vd_3[0]
            Buffer_3[1] = Lr_3[0]
            Buffer_3[2] = Az_3[0]
            Buffer_3[3] = Vm_3[0]

            Lr_3[0] = Buffer_3[0]
            Az_3[0] = Buffer_3[1]
            Vm_3[0] = Buffer_3[2]
            Vd_3[0] = Buffer_3[3]

            Br_3 = np.rot90(Br_3,1,(1,0))
        elif turn == "U'":
            Buffer_3[0] = Vd_3[0]
            Buffer_3[1] = Lr_3[0]
            Buffer_3[2] = Az_3[0]
            Buffer_3[3] = Vm_3[0]

            Lr_3[0] = Buffer_3[0]
            Az_3[0] = Buffer_3[1]
            Vm_3[0] = Buffer_3[2]
            Vd_3[0] = Buffer_3[3]
            Buffer_3[0] = Vd_3[0]
            Buffer_3[1] = Lr_3[0]
            Buffer_3[2] = Az_3[0]
            Buffer_3[3] = Vm_3[0]

            Lr_3[0] = Buffer_3[0]
            Az_3[0] = Buffer_3[1]
            Vm_3[0] = Buffer_3[2]
            Vd_3[0] = Buffer_3[3]
            Buffer_3[0] = Vd_3[0]
            Buffer_3[1] = Lr_3[0]
            Buffer_3[2] = Az_3[0]
            Buffer_3[3] = Vm_3[0]

            Lr_3[0] = Buffer_3[0]
            Az_3[0] = Buffer_3[1]
            Vm_3[0] = Buffer_3[2]
            Vd_3[0] = Buffer_3[3]

            Br_3 = np.rot90(Br_3,-1,(1,0))
        elif turn == "U2":
            Buffer_3[0] = Vd_3[0]
            Buffer_3[1] = Lr_3[0]
            Buffer_3[2] = Az_3[0]
            Buffer_3[3] = Vm_3[0]

            Lr_3[0] = Buffer_3[0]
            Az_3[0] = Buffer_3[1]
            Vm_3[0] = Buffer_3[2]
            Vd_3[0] = Buffer_3[3]
            Buffer_3[0] = Vd_3[0]
            Buffer_3[1] = Lr_3[0]
            Buffer_3[2] = Az_3[0]
            Buffer_3[3] = Vm_3[0]

            Lr_3[0] = Buffer_3[0]
            Az_3[0] = Buffer_3[1]
            Vm_3[0] = Buffer_3[2]
            Vd_3[0] = Buffer_3[3]

            Br_3 = np.rot90(Br_3,2,(1,0))
        elif turn == "D":
            Buffer_3[0] = Vd_3[2]
            Buffer_3[1] = Vm_3[2]
            Buffer_3[2] = Az_3[2]
            Buffer_3[3] = Lr_3[2]

            Vm_3[2] = Buffer_3[0]
            Az_3[2] = Buffer_3[1]
            Lr_3[2] = Buffer_3[2]
            Vd_3[2] = Buffer_3[3]

            Am_3 = np.rot90(Am_3,1,(1,0))
        elif turn == "D'":
            Buffer_3[0] = Vd_3[2]
            Buffer_3[1] = Vm_3[2]
            Buffer_3[2] = Az_3[2]
            Buffer_3[3] = Lr_3[2]

            Vm_3[2] = Buffer_3[0]
            Az_3[2] = Buffer_3[1]
            Lr_3[2] = Buffer_3[2]
            Vd_3[2] = Buffer_3[3]
            Buffer_3[0] = Vd_3[2]
            Buffer_3[1] = Vm_3[2]
            Buffer_3[2] = Az_3[2]
            Buffer_3[3] = Lr_3[2]

            Vm_3[2] = Buffer_3[0]
            Az_3[2] = Buffer_3[1]
            Lr_3[2] = Buffer_3[2]
            Vd_3[2] = Buffer_3[3]
            Buffer_3[0] = Vd_3[2]
            Buffer_3[1] = Vm_3[2]
            Buffer_3[2] = Az_3[2]
            Buffer_3[3] = Lr_3[2]

            Vm_3[2] = Buffer_3[0]
            Az_3[2] = Buffer_3[1]
            Lr_3[2] = Buffer_3[2]
            Vd_3[2] = Buffer_3[3]

            Am_3 = np.rot90(Am_3,-1,(1,0))
        elif turn == "D2":
            Buffer_3[0] = Vd_3[2]
            Buffer_3[1] = Vm_3[2]
            Buffer_3[2] = Az_3[2]
            Buffer_3[3] = Lr_3[2]

            Vm_3[2] = Buffer_3[0]
            Az_3[2] = Buffer_3[1]
            Lr_3[2] = Buffer_3[2]
            Vd_3[2] = Buffer_3[3]
            Buffer_3[0] = Vd_3[2]
            Buffer_3[1] = Vm_3[2]
            Buffer_3[2] = Az_3[2]
            Buffer_3[3] = Lr_3[2]

            Vm_3[2] = Buffer_3[0]
            Az_3[2] = Buffer_3[1]
            Lr_3[2] = Buffer_3[2]
            Vd_3[2] = Buffer_3[3]

            Am_3 = np.rot90(Am_3,2,(1,0))
        elif turn == "F":
            Buffer_3[0] = Br_3[2]
            Buffer_3[1] = np.flip(Vm_3[:,0],0)
            Buffer_3[2] = Am_3[0]
            Buffer_3[3] = np.flip(Lr_3[:,2],0)

            Vm_3[:,0] = Buffer_3[0]
            Am_3[0]   = Buffer_3[1]
            Lr_3[:,2] = Buffer_3[2]
            Br_3[2]   = Buffer_3[3]

            Vd_3 = np.rot90(Vd_3,1,(1,0))
        elif turn == "F'":
            Buffer_3[0] = Br_3[2]
            Buffer_3[1] = np.flip(Vm_3[:,0],0)
            Buffer_3[2] = Am_3[0]
            Buffer_3[3] = np.flip(Lr_3[:,2],0)

            Vm_3[:,0] = Buffer_3[0]
            Am_3[0]   = Buffer_3[1]
            Lr_3[:,2] = Buffer_3[2]
            Br_3[2]   = Buffer_3[3]
            Buffer_3[0] = Br_3[2]
            Buffer_3[1] = np.flip(Vm_3[:,0],0)
            Buffer_3[2] = Am_3[0]
            Buffer_3[3] = np.flip(Lr_3[:,2],0)

            Vm_3[:,0] = Buffer_3[0]
            Am_3[0]   = Buffer_3[1]
            Lr_3[:,2] = Buffer_3[2]
            Br_3[2]   = Buffer_3[3]
            Buffer_3[0] = Br_3[2]
            Buffer_3[1] = np.flip(Vm_3[:,0],0)
            Buffer_3[2] = Am_3[0]
            Buffer_3[3] = np.flip(Lr_3[:,2],0)

            Vm_3[:,0] = Buffer_3[0]
            Am_3[0]   = Buffer_3[1]
            Lr_3[:,2] = Buffer_3[2]
            Br_3[2]   = Buffer_3[3]

            Vd_3 = np.rot90(Vd_3,-1,(1,0))
        elif turn == "F2":
            Buffer_3[0] = Br_3[2]
            Buffer_3[1] = np.flip(Vm_3[:,0],0)
            Buffer_3[2] = Am_3[0]
            Buffer_3[3] = np.flip(Lr_3[:,2],0)

            Vm_3[:,0] = Buffer_3[0]
            Am_3[0]   = Buffer_3[1]
            Lr_3[:,2] = Buffer_3[2]
            Br_3[2]   = Buffer_3[3]
            Buffer_3[0] = Br_3[2]
            Buffer_3[1] = np.flip(Vm_3[:,0],0)
            Buffer_3[2] = Am_3[0]
            Buffer_3[3] = np.flip(Lr_3[:,2],0)

            Vm_3[:,0] = Buffer_3[0]
            Am_3[0]   = Buffer_3[1]
            Lr_3[:,2] = Buffer_3[2]
            Br_3[2]   = Buffer_3[3]

            Vd_3 = np.rot90(Vd_3,2,(1,0))
        elif turn == "B":
            Buffer_3[0] = np.flip(Br_3[0],0)
            Buffer_3[1] = Lr_3[:,0]
            Buffer_3[2] = np.flip(Am_3[2],0)
            Buffer_3[3] = Vm_3[:,2]

            Lr_3[:,0] = Buffer_3[0]
            Am_3[2]   = Buffer_3[1]
            Vm_3[:,2] = Buffer_3[2]
            Br_3[0]   = Buffer_3[3]

            Az_3 = np.rot90(Az_3,1,(1,0))

        elif turn == "B'":
            Buffer_3[0] = np.flip(Br_3[0],0)
            Buffer_3[1] = Lr_3[:,0]
            Buffer_3[2] = np.flip(Am_3[2],0)
            Buffer_3[3] = Vm_3[:,2]

            Lr_3[:,0] = Buffer_3[0]
            Am_3[2]   = Buffer_3[1]
            Vm_3[:,2] = Buffer_3[2]
            Br_3[0]   = Buffer_3[3]
            Buffer_3[0] = np.flip(Br_3[0],0)
            Buffer_3[1] = Lr_3[:,0]
            Buffer_3[2] = np.flip(Am_3[2],0)
            Buffer_3[3] = Vm_3[:,2]

            Lr_3[:,0] = Buffer_3[0]
            Am_3[2]   = Buffer_3[1]
            Vm_3[:,2] = Buffer_3[2]
            Br_3[0]   = Buffer_3[3]
            Buffer_3[0] = np.flip(Br_3[0],0)
            Buffer_3[1] = Lr_3[:,0]
            Buffer_3[2] = np.flip(Am_3[2],0)
            Buffer_3[3] = Vm_3[:,2]

            Lr_3[:,0] = Buffer_3[0]
            Am_3[2]   = Buffer_3[1]
            Vm_3[:,2] = Buffer_3[2]
            Br_3[0]   = Buffer_3[3]

            Az_3 = np.rot90(Az_3,-1,(1,0))
        elif turn == "B2":
            Buffer_3[0] = np.flip(Br_3[0],0)
            Buffer_3[1] = Lr_3[:,0]
            Buffer_3[2] = np.flip(Am_3[2],0)
            Buffer_3[3] = Vm_3[:,2]

            Lr_3[:,0] = Buffer_3[0]
            Am_3[2]   = Buffer_3[1]
            Vm_3[:,2] = Buffer_3[2]
            Br_3[0]   = Buffer_3[3]
            Buffer_3[0] = np.flip(Br_3[0],0)
            Buffer_3[1] = Lr_3[:,0]
            Buffer_3[2] = np.flip(Am_3[2],0)
            Buffer_3[3] = Vm_3[:,2]

            Lr_3[:,0] = Buffer_3[0]
            Am_3[2]   = Buffer_3[1]
            Vm_3[:,2] = Buffer_3[2]
            Br_3[0]   = Buffer_3[3]

            Az_3 = np.rot90(Az_3,2,(1,0))
        
    
    elif cube == "4x4":

        if turn == "R":
            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]           

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]
            
            Vm_4 = np.rot90(Vm_4,1,(1,0))

        elif turn == "R'":
            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]
            
            Vm_4 = np.rot90(Vm_4,-1,(1,0))
        elif turn == "R2":
            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]

            Vm_4 = np.rot90(Vm_4,2,(1,0))
        elif turn == "L":
            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Lr_4 = np.rot90(Lr_4,1,(1,0))
        elif turn == "L'":

            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]            

            Lr_4 = np.rot90(Lr_4,-1,(1,0))
        elif turn == "L2":
            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Lr_4 = np.rot90(Lr_4,2,(1,0))
        elif turn == "U":
            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]

            Br_4 = np.rot90(Br_4,1,(1,0))
        elif turn == "U'":
            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]
            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]
            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]

            Br_4 = np.rot90(Br_4,-1,(1,0))
        elif turn == "U2":
            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]
            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]

            Br_4 = np.rot90(Br_4,2,(1,0))
        elif turn == "D":
            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Am_4 = np.rot90(Am_4,1,(1,0))
        elif turn == "D'":
            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Am_4 = np.rot90(Am_4,-1,(1,0))
        elif turn == "D2":

            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]
            

            Am_4 = np.rot90(Am_4,2,(1,0))
        elif turn == "F":
            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]

            Vd_4 = np.rot90(Vd_4,1,(1,0))
        elif turn == "F'":
            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]

            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]

            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]
            

            Vd_4 = np.rot90(Vd_4,-1,(1,0))
        elif turn == "F2":

            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]

            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]
           

            Vd_4 = np.rot90(Vd_4,2,(1,0))
        elif turn == "B":
            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]

            Az_4 = np.rot90(Az_4,1,(1,0))

        elif turn == "B'":
            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]
            
            Az_4 = np.rot90(Az_4,-1,(1,0))
        elif turn == "B2":
            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]
            

            Az_4 = np.rot90(Az_4,2,(1,0))

        if turn == "Rw":
            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]           

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,2]
            Buffer_4[1] = np.flip(Br_4[:,2],0)
            Buffer_4[2] = np.flip(Az_4[:,1],0)
            Buffer_4[3] = Am_4[:,2]           

            Br_4[:,2] = Buffer_4[0]
            Az_4[:,1] = Buffer_4[1]
            Am_4[:,2] = Buffer_4[2]
            Vd_4[:,2] = Buffer_4[3]
            
            Vm_4 = np.rot90(Vm_4,1,(1,0))

        elif turn == "Rw'":
            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]           

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,2]
            Buffer_4[1] = np.flip(Br_4[:,2],0)
            Buffer_4[2] = np.flip(Az_4[:,1],0)
            Buffer_4[3] = Am_4[:,2]           

            Br_4[:,2] = Buffer_4[0]
            Az_4[:,1] = Buffer_4[1]
            Am_4[:,2] = Buffer_4[2]
            Vd_4[:,2] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]           

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,2]
            Buffer_4[1] = np.flip(Br_4[:,2],0)
            Buffer_4[2] = np.flip(Az_4[:,1],0)
            Buffer_4[3] = Am_4[:,2]           

            Br_4[:,2] = Buffer_4[0]
            Az_4[:,1] = Buffer_4[1]
            Am_4[:,2] = Buffer_4[2]
            Vd_4[:,2] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]           

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,2]
            Buffer_4[1] = np.flip(Br_4[:,2],0)
            Buffer_4[2] = np.flip(Az_4[:,1],0)
            Buffer_4[3] = Am_4[:,2]           

            Br_4[:,2] = Buffer_4[0]
            Az_4[:,1] = Buffer_4[1]
            Am_4[:,2] = Buffer_4[2]
            Vd_4[:,2] = Buffer_4[3]
            
            Vm_4 = np.rot90(Vm_4,-1,(1,0))
        elif turn == "Rw2":

            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]           

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,2]
            Buffer_4[1] = np.flip(Br_4[:,2],0)
            Buffer_4[2] = np.flip(Az_4[:,1],0)
            Buffer_4[3] = Am_4[:,2]           

            Br_4[:,2] = Buffer_4[0]
            Az_4[:,1] = Buffer_4[1]
            Am_4[:,2] = Buffer_4[2]
            Vd_4[:,2] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,3]
            Buffer_4[1] = np.flip(Br_4[:,3],0)
            Buffer_4[2] = np.flip(Az_4[:,0],0)
            Buffer_4[3] = Am_4[:,3]           

            Br_4[:,3] = Buffer_4[0]
            Az_4[:,0] = Buffer_4[1]
            Am_4[:,3] = Buffer_4[2]
            Vd_4[:,3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,2]
            Buffer_4[1] = np.flip(Br_4[:,2],0)
            Buffer_4[2] = np.flip(Az_4[:,1],0)
            Buffer_4[3] = Am_4[:,2]           

            Br_4[:,2] = Buffer_4[0]
            Az_4[:,1] = Buffer_4[1]
            Am_4[:,2] = Buffer_4[2]
            Vd_4[:,2] = Buffer_4[3]
            

            

            Vm_4 = np.rot90(Vm_4,2,(1,0))

        elif turn == "Lw":
            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,1]
            Buffer_4[1] = np.flip(Am_4[:,1],0)
            Buffer_4[2] = np.flip(Az_4[:,2],0)
            Buffer_4[3] = Br_4[:,1]

            Am_4[:,1] = Buffer_4[0]
            Az_4[:,2] = Buffer_4[1]
            Br_4[:,1] = Buffer_4[2]
            Vd_4[:,1] = Buffer_4[3]

            Lr_4 = np.rot90(Lr_4,1,(1,0))
        elif turn == "Lw'":

            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,1]
            Buffer_4[1] = np.flip(Am_4[:,1],0)
            Buffer_4[2] = np.flip(Az_4[:,2],0)
            Buffer_4[3] = Br_4[:,1]

            Am_4[:,1] = Buffer_4[0]
            Az_4[:,2] = Buffer_4[1]
            Br_4[:,1] = Buffer_4[2]
            Vd_4[:,1] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,1]
            Buffer_4[1] = np.flip(Am_4[:,1],0)
            Buffer_4[2] = np.flip(Az_4[:,2],0)
            Buffer_4[3] = Br_4[:,1]

            Am_4[:,1] = Buffer_4[0]
            Az_4[:,2] = Buffer_4[1]
            Br_4[:,1] = Buffer_4[2]
            Vd_4[:,1] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,1]
            Buffer_4[1] = np.flip(Am_4[:,1],0)
            Buffer_4[2] = np.flip(Az_4[:,2],0)
            Buffer_4[3] = Br_4[:,1]

            Am_4[:,1] = Buffer_4[0]
            Az_4[:,2] = Buffer_4[1]
            Br_4[:,1] = Buffer_4[2]
            Vd_4[:,1] = Buffer_4[3]

                  

            Lr_4 = np.rot90(Lr_4,-1,(1,0))
        elif turn == "Lw2":

            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,1]
            Buffer_4[1] = np.flip(Am_4[:,1],0)
            Buffer_4[2] = np.flip(Az_4[:,2],0)
            Buffer_4[3] = Br_4[:,1]

            Am_4[:,1] = Buffer_4[0]
            Az_4[:,2] = Buffer_4[1]
            Br_4[:,1] = Buffer_4[2]
            Vd_4[:,1] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,0]
            Buffer_4[1] = np.flip(Am_4[:,0],0)
            Buffer_4[2] = np.flip(Az_4[:,3],0)
            Buffer_4[3] = Br_4[:,0]

            Am_4[:,0] = Buffer_4[0]
            Az_4[:,3] = Buffer_4[1]
            Br_4[:,0] = Buffer_4[2]
            Vd_4[:,0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[:,1]
            Buffer_4[1] = np.flip(Am_4[:,1],0)
            Buffer_4[2] = np.flip(Az_4[:,2],0)
            Buffer_4[3] = Br_4[:,1]

            Am_4[:,1] = Buffer_4[0]
            Az_4[:,2] = Buffer_4[1]
            Br_4[:,1] = Buffer_4[2]
            Vd_4[:,1] = Buffer_4[3]
           

            Lr_4 = np.rot90(Lr_4,2,(1,0))
        elif turn == "Uw":
            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[1]
            Buffer_4[1] = Lr_4[1]
            Buffer_4[2] = Az_4[1]
            Buffer_4[3] = Vm_4[1]

            Lr_4[1] = Buffer_4[0]
            Az_4[1] = Buffer_4[1]
            Vm_4[1] = Buffer_4[2]
            Vd_4[1] = Buffer_4[3]

            Br_4 = np.rot90(Br_4,1,(1,0))
        elif turn == "Uw'":

            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[1]
            Buffer_4[1] = Lr_4[1]
            Buffer_4[2] = Az_4[1]
            Buffer_4[3] = Vm_4[1]

            Lr_4[1] = Buffer_4[0]
            Az_4[1] = Buffer_4[1]
            Vm_4[1] = Buffer_4[2]
            Vd_4[1] = Buffer_4[3]

            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[1]
            Buffer_4[1] = Lr_4[1]
            Buffer_4[2] = Az_4[1]
            Buffer_4[3] = Vm_4[1]

            Lr_4[1] = Buffer_4[0]
            Az_4[1] = Buffer_4[1]
            Vm_4[1] = Buffer_4[2]
            Vd_4[1] = Buffer_4[3]

            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[1]
            Buffer_4[1] = Lr_4[1]
            Buffer_4[2] = Az_4[1]
            Buffer_4[3] = Vm_4[1]

            Lr_4[1] = Buffer_4[0]
            Az_4[1] = Buffer_4[1]
            Vm_4[1] = Buffer_4[2]
            Vd_4[1] = Buffer_4[3]            

            Br_4 = np.rot90(Br_4,-1,(1,0))
        elif turn == "Uw2":

            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[1]
            Buffer_4[1] = Lr_4[1]
            Buffer_4[2] = Az_4[1]
            Buffer_4[3] = Vm_4[1]

            Lr_4[1] = Buffer_4[0]
            Az_4[1] = Buffer_4[1]
            Vm_4[1] = Buffer_4[2]
            Vd_4[1] = Buffer_4[3]

            Buffer_4[0] = Vd_4[0]
            Buffer_4[1] = Lr_4[0]
            Buffer_4[2] = Az_4[0]
            Buffer_4[3] = Vm_4[0]

            Lr_4[0] = Buffer_4[0]
            Az_4[0] = Buffer_4[1]
            Vm_4[0] = Buffer_4[2]
            Vd_4[0] = Buffer_4[3]

            Buffer_4[0] = Vd_4[1]
            Buffer_4[1] = Lr_4[1]
            Buffer_4[2] = Az_4[1]
            Buffer_4[3] = Vm_4[1]

            Lr_4[1] = Buffer_4[0]
            Az_4[1] = Buffer_4[1]
            Vm_4[1] = Buffer_4[2]
            Vd_4[1] = Buffer_4[3]            

            Br_4 = np.rot90(Br_4,2,(1,0))
        elif turn == "Dw":
            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[2]
            Buffer_4[1] = Vm_4[2]
            Buffer_4[2] = Az_4[2]
            Buffer_4[3] = Lr_4[2]

            Vm_4[2] = Buffer_4[0]
            Az_4[2] = Buffer_4[1]
            Lr_4[2] = Buffer_4[2]
            Vd_4[2] = Buffer_4[3]

            Am_4 = np.rot90(Am_4,1,(1,0))
        elif turn == "Dw'":

            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[2]
            Buffer_4[1] = Vm_4[2]
            Buffer_4[2] = Az_4[2]
            Buffer_4[3] = Lr_4[2]

            Vm_4[2] = Buffer_4[0]
            Az_4[2] = Buffer_4[1]
            Lr_4[2] = Buffer_4[2]
            Vd_4[2] = Buffer_4[3]

            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[2]
            Buffer_4[1] = Vm_4[2]
            Buffer_4[2] = Az_4[2]
            Buffer_4[3] = Lr_4[2]

            Vm_4[2] = Buffer_4[0]
            Az_4[2] = Buffer_4[1]
            Lr_4[2] = Buffer_4[2]
            Vd_4[2] = Buffer_4[3]

            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[2]
            Buffer_4[1] = Vm_4[2]
            Buffer_4[2] = Az_4[2]
            Buffer_4[3] = Lr_4[2]

            Vm_4[2] = Buffer_4[0]
            Az_4[2] = Buffer_4[1]
            Lr_4[2] = Buffer_4[2]
            Vd_4[2] = Buffer_4[3]
            

            Am_4 = np.rot90(Am_4,-1,(1,0))
        elif turn == "Dw2":

            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[2]
            Buffer_4[1] = Vm_4[2]
            Buffer_4[2] = Az_4[2]
            Buffer_4[3] = Lr_4[2]

            Vm_4[2] = Buffer_4[0]
            Az_4[2] = Buffer_4[1]
            Lr_4[2] = Buffer_4[2]
            Vd_4[2] = Buffer_4[3]

            Buffer_4[0] = Vd_4[3]
            Buffer_4[1] = Vm_4[3]
            Buffer_4[2] = Az_4[3]
            Buffer_4[3] = Lr_4[3]

            Vm_4[3] = Buffer_4[0]
            Az_4[3] = Buffer_4[1]
            Lr_4[3] = Buffer_4[2]
            Vd_4[3] = Buffer_4[3]

            Buffer_4[0] = Vd_4[2]
            Buffer_4[1] = Vm_4[2]
            Buffer_4[2] = Az_4[2]
            Buffer_4[3] = Lr_4[2]

            Vm_4[2] = Buffer_4[0]
            Az_4[2] = Buffer_4[1]
            Lr_4[2] = Buffer_4[2]
            Vd_4[2] = Buffer_4[3]
            

            Am_4 = np.rot90(Am_4,2,(1,0))
        elif turn == "Fw":
            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]

            Buffer_4[0] = Br_4[2]
            Buffer_4[1] = np.flip(Vm_4[:,1],0)
            Buffer_4[2] = Am_4[1]
            Buffer_4[3] = np.flip(Lr_4[:,2],0)

            Vm_4[:,1] = Buffer_4[0]
            Am_4[1]   = Buffer_4[1]
            Lr_4[:,2] = Buffer_4[2]
            Br_4[2]   = Buffer_4[3]

            Vd_4 = np.rot90(Vd_4,1,(1,0))
        elif turn == "Fw'":
            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]

            Buffer_4[0] = Br_4[2]
            Buffer_4[1] = np.flip(Vm_4[:,1],0)
            Buffer_4[2] = Am_4[1]
            Buffer_4[3] = np.flip(Lr_4[:,2],0)

            Vm_4[:,1] = Buffer_4[0]
            Am_4[1]   = Buffer_4[1]
            Lr_4[:,2] = Buffer_4[2]
            Br_4[2]   = Buffer_4[3]

            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]

            Buffer_4[0] = Br_4[2]
            Buffer_4[1] = np.flip(Vm_4[:,1],0)
            Buffer_4[2] = Am_4[1]
            Buffer_4[3] = np.flip(Lr_4[:,2],0)

            Vm_4[:,1] = Buffer_4[0]
            Am_4[1]   = Buffer_4[1]
            Lr_4[:,2] = Buffer_4[2]
            Br_4[2]   = Buffer_4[3]

            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]

            Buffer_4[0] = Br_4[2]
            Buffer_4[1] = np.flip(Vm_4[:,1],0)
            Buffer_4[2] = Am_4[1]
            Buffer_4[3] = np.flip(Lr_4[:,2],0)

            Vm_4[:,1] = Buffer_4[0]
            Am_4[1]   = Buffer_4[1]
            Lr_4[:,2] = Buffer_4[2]
            Br_4[2]   = Buffer_4[3]
           
            

            Vd_4 = np.rot90(Vd_4,-1,(1,0))
        elif turn == "Fw2":
            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]

            Buffer_4[0] = Br_4[2]
            Buffer_4[1] = np.flip(Vm_4[:,1],0)
            Buffer_4[2] = Am_4[1]
            Buffer_4[3] = np.flip(Lr_4[:,2],0)

            Vm_4[:,1] = Buffer_4[0]
            Am_4[1]   = Buffer_4[1]
            Lr_4[:,2] = Buffer_4[2]
            Br_4[2]   = Buffer_4[3]

            Buffer_4[0] = Br_4[3]
            Buffer_4[1] = np.flip(Vm_4[:,0],0)
            Buffer_4[2] = Am_4[0]
            Buffer_4[3] = np.flip(Lr_4[:,3],0)

            Vm_4[:,0] = Buffer_4[0]
            Am_4[0]   = Buffer_4[1]
            Lr_4[:,3] = Buffer_4[2]
            Br_4[3]   = Buffer_4[3]

            Buffer_4[0] = Br_4[2]
            Buffer_4[1] = np.flip(Vm_4[:,1],0)
            Buffer_4[2] = Am_4[1]
            Buffer_4[3] = np.flip(Lr_4[:,2],0)

            Vm_4[:,1] = Buffer_4[0]
            Am_4[1]   = Buffer_4[1]
            Lr_4[:,2] = Buffer_4[2]
            Br_4[2]   = Buffer_4[3]
                    
           

            Vd_4 = np.rot90(Vd_4,2,(1,0))

        elif turn == "Bw":
            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[1],0)
            Buffer_4[1] = Lr_4[:,1]
            Buffer_4[2] = np.flip(Am_4[2],0)
            Buffer_4[3] = Vm_4[:,2]

            Lr_4[:,1] = Buffer_4[0]
            Am_4[2]   = Buffer_4[1]
            Vm_4[:,2] = Buffer_4[2]
            Br_4[1]   = Buffer_4[3]

            Az_4 = np.rot90(Az_4,1,(1,0))

        elif turn == "Bw'":
            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[1],0)
            Buffer_4[1] = Lr_4[:,1]
            Buffer_4[2] = np.flip(Am_4[2],0)
            Buffer_4[3] = Vm_4[:,2]

            Lr_4[:,1] = Buffer_4[0]
            Am_4[2]   = Buffer_4[1]
            Vm_4[:,2] = Buffer_4[2]
            Br_4[1]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[1],0)
            Buffer_4[1] = Lr_4[:,1]
            Buffer_4[2] = np.flip(Am_4[2],0)
            Buffer_4[3] = Vm_4[:,2]

            Lr_4[:,1] = Buffer_4[0]
            Am_4[2]   = Buffer_4[1]
            Vm_4[:,2] = Buffer_4[2]
            Br_4[1]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[1],0)
            Buffer_4[1] = Lr_4[:,1]
            Buffer_4[2] = np.flip(Am_4[2],0)
            Buffer_4[3] = Vm_4[:,2]

            Lr_4[:,1] = Buffer_4[0]
            Am_4[2]   = Buffer_4[1]
            Vm_4[:,2] = Buffer_4[2]
            Br_4[1]   = Buffer_4[3]            
            
            Az_4 = np.rot90(Az_4,-1,(1,0))
        elif turn == "Bw2":
            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[1],0)
            Buffer_4[1] = Lr_4[:,1]
            Buffer_4[2] = np.flip(Am_4[2],0)
            Buffer_4[3] = Vm_4[:,2]

            Lr_4[:,1] = Buffer_4[0]
            Am_4[2]   = Buffer_4[1]
            Vm_4[:,2] = Buffer_4[2]
            Br_4[1]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[0],0)
            Buffer_4[1] = Lr_4[:,0]
            Buffer_4[2] = np.flip(Am_4[3],0)
            Buffer_4[3] = Vm_4[:,3]

            Lr_4[:,0] = Buffer_4[0]
            Am_4[3]   = Buffer_4[1]
            Vm_4[:,3] = Buffer_4[2]
            Br_4[0]   = Buffer_4[3]

            Buffer_4[0] = np.flip(Br_4[1],0)
            Buffer_4[1] = Lr_4[:,1]
            Buffer_4[2] = np.flip(Am_4[2],0)
            Buffer_4[3] = Vm_4[:,2]

            Lr_4[:,1] = Buffer_4[0]
            Am_4[2]   = Buffer_4[1]
            Vm_4[:,2] = Buffer_4[2]
            Br_4[1]   = Buffer_4[3]
                      

            Az_4 = np.rot90(Az_4,2,(1,0))

        
    elif cube == "5x5":
         
        if turn == "R":
            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]
            
            Vm_5 = np.rot90(Vm_5,1,(1,0))

        elif turn == "R'":

            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]
            
            
            Vm_5 = np.rot90(Vm_5,-1,(1,0))
        elif turn == "R2":

            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]
            

            Vm_5 = np.rot90(Vm_5,2,(1,0))
        elif turn == "L":
            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

            Lr_5 = np.rot90(Lr_5,1,(1,0))
        elif turn == "L'":

            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

                       

            Lr_5 = np.rot90(Lr_5,-1,(1,0))
        elif turn == "L2":

            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]
           

            Lr_5 = np.rot90(Lr_5,2,(1,0))
        elif turn == "U":
            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]

            Br_5 = np.rot90(Br_5,1,(1,0))
        elif turn == "U'":
            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]
            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]
            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]

            Br_5 = np.rot90(Br_5,-1,(1,0))
        elif turn == "U2":
            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]
            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]

            Br_5 = np.rot90(Br_5,2,(1,0))
        elif turn == "D":
            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            Am_5 = np.rot90(Am_5,1,(1,0))
        elif turn == "D'":

            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]
            

            Am_5 = np.rot90(Am_5,-1,(1,0))
        elif turn == "D2":

            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            
            

            Am_5 = np.rot90(Am_5,2,(1,0))
        elif turn == "F":
            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]

            Vd_5 = np.rot90(Vd_5,1,(1,0))
        elif turn == "F'":

            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]

            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]

            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]
            
            

            Vd_5 = np.rot90(Vd_5,-1,(1,0))
        elif turn == "F2":

            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]

            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]
           

            Vd_5 = np.rot90(Vd_5,2,(1,0))
        elif turn == "B":
            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]

            Az_5 = np.rot90(Az_5,1,(1,0))

        elif turn == "B'":

            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]
            
            
            Az_5 = np.rot90(Az_5,-1,(1,0))
        elif turn == "B2":

            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]
            
            

            Az_5 = np.rot90(Az_5,2,(1,0))

        elif turn == "Rw":
            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,3]
            Buffer_5[1] = np.flip(Br_5[:,3],0)
            Buffer_5[2] = np.flip(Az_5[:,1],0)
            Buffer_5[3] = Am_5[:,3]           

            Br_5[:,3] = Buffer_5[0]
            Az_5[:,1] = Buffer_5[1]
            Am_5[:,3] = Buffer_5[2]
            Vd_5[:,3] = Buffer_5[3]
            
            Vm_5 = np.rot90(Vm_5,1,(1,0))

        elif turn == "Rw'":

            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,3]
            Buffer_5[1] = np.flip(Br_5[:,3],0)
            Buffer_5[2] = np.flip(Az_5[:,1],0)
            Buffer_5[3] = Am_5[:,3]           

            Br_5[:,3] = Buffer_5[0]
            Az_5[:,1] = Buffer_5[1]
            Am_5[:,3] = Buffer_5[2]
            Vd_5[:,3] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,3]
            Buffer_5[1] = np.flip(Br_5[:,3],0)
            Buffer_5[2] = np.flip(Az_5[:,1],0)
            Buffer_5[3] = Am_5[:,3]           

            Br_5[:,3] = Buffer_5[0]
            Az_5[:,1] = Buffer_5[1]
            Am_5[:,3] = Buffer_5[2]
            Vd_5[:,3] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,3]
            Buffer_5[1] = np.flip(Br_5[:,3],0)
            Buffer_5[2] = np.flip(Az_5[:,1],0)
            Buffer_5[3] = Am_5[:,3]           

            Br_5[:,3] = Buffer_5[0]
            Az_5[:,1] = Buffer_5[1]
            Am_5[:,3] = Buffer_5[2]
            Vd_5[:,3] = Buffer_5[3]
           
            
            Vm_5 = np.rot90(Vm_5,-1,(1,0))
        elif turn == "Rw2":

            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,3]
            Buffer_5[1] = np.flip(Br_5[:,3],0)
            Buffer_5[2] = np.flip(Az_5[:,1],0)
            Buffer_5[3] = Am_5[:,3]           

            Br_5[:,3] = Buffer_5[0]
            Az_5[:,1] = Buffer_5[1]
            Am_5[:,3] = Buffer_5[2]
            Vd_5[:,3] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,4]
            Buffer_5[1] = np.flip(Br_5[:,4],0)
            Buffer_5[2] = np.flip(Az_5[:,0],0)
            Buffer_5[3] = Am_5[:,4]           

            Br_5[:,4] = Buffer_5[0]
            Az_5[:,0] = Buffer_5[1]
            Am_5[:,4] = Buffer_5[2]
            Vd_5[:,4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,3]
            Buffer_5[1] = np.flip(Br_5[:,3],0)
            Buffer_5[2] = np.flip(Az_5[:,1],0)
            Buffer_5[3] = Am_5[:,3]           

            Br_5[:,3] = Buffer_5[0]
            Az_5[:,1] = Buffer_5[1]
            Am_5[:,3] = Buffer_5[2]
            Vd_5[:,3] = Buffer_5[3]            

            Vm_5 = np.rot90(Vm_5,2,(1,0))

        elif turn == "Lw":
            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,1]
            Buffer_5[1] = np.flip(Am_5[:,1],0)
            Buffer_5[2] = np.flip(Az_5[:,3],0)
            Buffer_5[3] = Br_5[:,1]

            Am_5[:,1] = Buffer_5[0]
            Az_5[:,3] = Buffer_5[1]
            Br_5[:,1] = Buffer_5[2]
            Vd_5[:,1] = Buffer_5[3]

            Lr_5 = np.rot90(Lr_5,1,(1,0))
        elif turn == "Lw'":

            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,1]
            Buffer_5[1] = np.flip(Am_5[:,1],0)
            Buffer_5[2] = np.flip(Az_5[:,3],0)
            Buffer_5[3] = Br_5[:,1]

            Am_5[:,1] = Buffer_5[0]
            Az_5[:,3] = Buffer_5[1]
            Br_5[:,1] = Buffer_5[2]
            Vd_5[:,1] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,1]
            Buffer_5[1] = np.flip(Am_5[:,1],0)
            Buffer_5[2] = np.flip(Az_5[:,3],0)
            Buffer_5[3] = Br_5[:,1]

            Am_5[:,1] = Buffer_5[0]
            Az_5[:,3] = Buffer_5[1]
            Br_5[:,1] = Buffer_5[2]
            Vd_5[:,1] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,1]
            Buffer_5[1] = np.flip(Am_5[:,1],0)
            Buffer_5[2] = np.flip(Az_5[:,3],0)
            Buffer_5[3] = Br_5[:,1]

            Am_5[:,1] = Buffer_5[0]
            Az_5[:,3] = Buffer_5[1]
            Br_5[:,1] = Buffer_5[2]
            Vd_5[:,1] = Buffer_5[3]                  

            Lr_5 = np.rot90(Lr_5,-1,(1,0))
        elif turn == "Lw2":
            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,1]
            Buffer_5[1] = np.flip(Am_5[:,1],0)
            Buffer_5[2] = np.flip(Az_5[:,3],0)
            Buffer_5[3] = Br_5[:,1]

            Am_5[:,1] = Buffer_5[0]
            Az_5[:,3] = Buffer_5[1]
            Br_5[:,1] = Buffer_5[2]
            Vd_5[:,1] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,0]
            Buffer_5[1] = np.flip(Am_5[:,0],0)
            Buffer_5[2] = np.flip(Az_5[:,4],0)
            Buffer_5[3] = Br_5[:,0]

            Am_5[:,0] = Buffer_5[0]
            Az_5[:,4] = Buffer_5[1]
            Br_5[:,0] = Buffer_5[2]
            Vd_5[:,0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[:,1]
            Buffer_5[1] = np.flip(Am_5[:,1],0)
            Buffer_5[2] = np.flip(Az_5[:,3],0)
            Buffer_5[3] = Br_5[:,1]

            Am_5[:,1] = Buffer_5[0]
            Az_5[:,3] = Buffer_5[1]
            Br_5[:,1] = Buffer_5[2]
            Vd_5[:,1] = Buffer_5[3]          

            Lr_5 = np.rot90(Lr_5,2,(1,0))
        elif turn == "Uw":
            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[1]
            Buffer_5[1] = Lr_5[1]
            Buffer_5[2] = Az_5[1]
            Buffer_5[3] = Vm_5[1]

            Lr_5[1] = Buffer_5[0]
            Az_5[1] = Buffer_5[1]
            Vm_5[1] = Buffer_5[2]
            Vd_5[1] = Buffer_5[3]

            Br_5 = np.rot90(Br_5,1,(1,0))
        elif turn == "Uw'":

            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[1]
            Buffer_5[1] = Lr_5[1]
            Buffer_5[2] = Az_5[1]
            Buffer_5[3] = Vm_5[1]

            Lr_5[1] = Buffer_5[0]
            Az_5[1] = Buffer_5[1]
            Vm_5[1] = Buffer_5[2]
            Vd_5[1] = Buffer_5[3]

            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[1]
            Buffer_5[1] = Lr_5[1]
            Buffer_5[2] = Az_5[1]
            Buffer_5[3] = Vm_5[1]

            Lr_5[1] = Buffer_5[0]
            Az_5[1] = Buffer_5[1]
            Vm_5[1] = Buffer_5[2]
            Vd_5[1] = Buffer_5[3]

            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[1]
            Buffer_5[1] = Lr_5[1]
            Buffer_5[2] = Az_5[1]
            Buffer_5[3] = Vm_5[1]

            Lr_5[1] = Buffer_5[0]
            Az_5[1] = Buffer_5[1]
            Vm_5[1] = Buffer_5[2]
            Vd_5[1] = Buffer_5[3]            

            Br_5 = np.rot90(Br_5,-1,(1,0))
        elif turn == "Uw2":

            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[1]
            Buffer_5[1] = Lr_5[1]
            Buffer_5[2] = Az_5[1]
            Buffer_5[3] = Vm_5[1]

            Lr_5[1] = Buffer_5[0]
            Az_5[1] = Buffer_5[1]
            Vm_5[1] = Buffer_5[2]
            Vd_5[1] = Buffer_5[3]

            Buffer_5[0] = Vd_5[0]
            Buffer_5[1] = Lr_5[0]
            Buffer_5[2] = Az_5[0]
            Buffer_5[3] = Vm_5[0]

            Lr_5[0] = Buffer_5[0]
            Az_5[0] = Buffer_5[1]
            Vm_5[0] = Buffer_5[2]
            Vd_5[0] = Buffer_5[3]

            Buffer_5[0] = Vd_5[1]
            Buffer_5[1] = Lr_5[1]
            Buffer_5[2] = Az_5[1]
            Buffer_5[3] = Vm_5[1]

            Lr_5[1] = Buffer_5[0]
            Az_5[1] = Buffer_5[1]
            Vm_5[1] = Buffer_5[2]
            Vd_5[1] = Buffer_5[3]            

            Br_5 = np.rot90(Br_5,2,(1,0))
        elif turn == "Dw":
            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[3]
            Buffer_5[1] = Vm_5[3]
            Buffer_5[2] = Az_5[3]
            Buffer_5[3] = Lr_5[3]

            Vm_5[3] = Buffer_5[0]
            Az_5[3] = Buffer_5[1]
            Lr_5[3] = Buffer_5[2]
            Vd_5[3] = Buffer_5[3]

            Am_5 = np.rot90(Am_5,1,(1,0))
        elif turn == "Dw'":

            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[3]
            Buffer_5[1] = Vm_5[3]
            Buffer_5[2] = Az_5[3]
            Buffer_5[3] = Lr_5[3]

            Vm_5[3] = Buffer_5[0]
            Az_5[3] = Buffer_5[1]
            Lr_5[3] = Buffer_5[2]
            Vd_5[3] = Buffer_5[3]

            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[3]
            Buffer_5[1] = Vm_5[3]
            Buffer_5[2] = Az_5[3]
            Buffer_5[3] = Lr_5[3]

            Vm_5[3] = Buffer_5[0]
            Az_5[3] = Buffer_5[1]
            Lr_5[3] = Buffer_5[2]
            Vd_5[3] = Buffer_5[3]

            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[3]
            Buffer_5[1] = Vm_5[3]
            Buffer_5[2] = Az_5[3]
            Buffer_5[3] = Lr_5[3]

            Vm_5[3] = Buffer_5[0]
            Az_5[3] = Buffer_5[1]
            Lr_5[3] = Buffer_5[2]
            Vd_5[3] = Buffer_5[3]         
            

            Am_5 = np.rot90(Am_5,-1,(1,0))
        elif turn == "Dw2":

            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[3]
            Buffer_5[1] = Vm_5[3]
            Buffer_5[2] = Az_5[3]
            Buffer_5[3] = Lr_5[3]

            Vm_5[3] = Buffer_5[0]
            Az_5[3] = Buffer_5[1]
            Lr_5[3] = Buffer_5[2]
            Vd_5[3] = Buffer_5[3]

            Buffer_5[0] = Vd_5[4]
            Buffer_5[1] = Vm_5[4]
            Buffer_5[2] = Az_5[4]
            Buffer_5[3] = Lr_5[4]

            Vm_5[4] = Buffer_5[0]
            Az_5[4] = Buffer_5[1]
            Lr_5[4] = Buffer_5[2]
            Vd_5[4] = Buffer_5[3]

            Buffer_5[0] = Vd_5[3]
            Buffer_5[1] = Vm_5[3]
            Buffer_5[2] = Az_5[3]
            Buffer_5[3] = Lr_5[3]

            Vm_5[3] = Buffer_5[0]
            Az_5[3] = Buffer_5[1]
            Lr_5[3] = Buffer_5[2]
            Vd_5[3] = Buffer_5[3]            

            Am_5 = np.rot90(Am_5,2,(1,0))
        elif turn == "Fw":
            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]

            Buffer_5[0] = Br_5[3]
            Buffer_5[1] = np.flip(Vm_5[:,1],0)
            Buffer_5[2] = Am_5[1]
            Buffer_5[3] = np.flip(Lr_5[:,3],0)

            Vm_5[:,1] = Buffer_5[0]
            Am_5[1]   = Buffer_5[1]
            Lr_5[:,3] = Buffer_5[2]
            Br_5[3]   = Buffer_5[3]

            Vd_5 = np.rot90(Vd_5,1,(1,0))
        elif turn == "Fw'":     

            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]

            Buffer_5[0] = Br_5[3]
            Buffer_5[1] = np.flip(Vm_5[:,1],0)
            Buffer_5[2] = Am_5[1]
            Buffer_5[3] = np.flip(Lr_5[:,3],0)

            Vm_5[:,1] = Buffer_5[0]
            Am_5[1]   = Buffer_5[1]
            Lr_5[:,3] = Buffer_5[2]
            Br_5[3]   = Buffer_5[3]

            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]

            Buffer_5[0] = Br_5[3]
            Buffer_5[1] = np.flip(Vm_5[:,1],0)
            Buffer_5[2] = Am_5[1]
            Buffer_5[3] = np.flip(Lr_5[:,3],0)

            Vm_5[:,1] = Buffer_5[0]
            Am_5[1]   = Buffer_5[1]
            Lr_5[:,3] = Buffer_5[2]
            Br_5[3]   = Buffer_5[3]

            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]

            Buffer_5[0] = Br_5[3]
            Buffer_5[1] = np.flip(Vm_5[:,1],0)
            Buffer_5[2] = Am_5[1]
            Buffer_5[3] = np.flip(Lr_5[:,3],0)

            Vm_5[:,1] = Buffer_5[0]
            Am_5[1]   = Buffer_5[1]
            Lr_5[:,3] = Buffer_5[2]
            Br_5[3]   = Buffer_5[3]
           
            

            Vd_5 = np.rot90(Vd_5,-1,(1,0))
        elif turn == "Fw2":

            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]

            Buffer_5[0] = Br_5[3]
            Buffer_5[1] = np.flip(Vm_5[:,1],0)
            Buffer_5[2] = Am_5[1]
            Buffer_5[3] = np.flip(Lr_5[:,3],0)

            Vm_5[:,1] = Buffer_5[0]
            Am_5[1]   = Buffer_5[1]
            Lr_5[:,3] = Buffer_5[2]
            Br_5[3]   = Buffer_5[3]

            Buffer_5[0] = Br_5[4]
            Buffer_5[1] = np.flip(Vm_5[:,0],0)
            Buffer_5[2] = Am_5[0]
            Buffer_5[3] = np.flip(Lr_5[:,4],0)

            Vm_5[:,0] = Buffer_5[0]
            Am_5[0]   = Buffer_5[1]
            Lr_5[:,4] = Buffer_5[2]
            Br_5[4]   = Buffer_5[3]

            Buffer_5[0] = Br_5[3]
            Buffer_5[1] = np.flip(Vm_5[:,1],0)
            Buffer_5[2] = Am_5[1]
            Buffer_5[3] = np.flip(Lr_5[:,3],0)

            Vm_5[:,1] = Buffer_5[0]
            Am_5[1]   = Buffer_5[1]
            Lr_5[:,3] = Buffer_5[2]
            Br_5[3]   = Buffer_5[3]    
                              
            Vd_5 = np.rot90(Vd_5,2,(1,0))

        elif turn == "Bw":
            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[1],0)
            Buffer_5[1] = Lr_5[:,1]
            Buffer_5[2] = np.flip(Am_5[3],0)
            Buffer_5[3] = Vm_5[:,3]

            Lr_5[:,1] = Buffer_5[0]
            Am_5[3]   = Buffer_5[1]
            Vm_5[:,3] = Buffer_5[2]
            Br_5[1]   = Buffer_5[3]

            Az_5 = np.rot90(Az_5,1,(1,0))

        elif turn == "Bw'":
            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[1],0)
            Buffer_5[1] = Lr_5[:,1]
            Buffer_5[2] = np.flip(Am_5[3],0)
            Buffer_5[3] = Vm_5[:,3]

            Lr_5[:,1] = Buffer_5[0]
            Am_5[3]   = Buffer_5[1]
            Vm_5[:,3] = Buffer_5[2]
            Br_5[1]   = Buffer_5[3]    

            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[1],0)
            Buffer_5[1] = Lr_5[:,1]
            Buffer_5[2] = np.flip(Am_5[3],0)
            Buffer_5[3] = Vm_5[:,3]

            Lr_5[:,1] = Buffer_5[0]
            Am_5[3]   = Buffer_5[1]
            Vm_5[:,3] = Buffer_5[2]
            Br_5[1]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[1],0)
            Buffer_5[1] = Lr_5[:,1]
            Buffer_5[2] = np.flip(Am_5[3],0)
            Buffer_5[3] = Vm_5[:,3]

            Lr_5[:,1] = Buffer_5[0]
            Am_5[3]   = Buffer_5[1]
            Vm_5[:,3] = Buffer_5[2]
            Br_5[1]   = Buffer_5[3]     
            
            Az_5 = np.rot90(Az_5,-1,(1,0))
        elif turn == "Bw2":

            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[1],0)
            Buffer_5[1] = Lr_5[:,1]
            Buffer_5[2] = np.flip(Am_5[3],0)
            Buffer_5[3] = Vm_5[:,3]

            Lr_5[:,1] = Buffer_5[0]
            Am_5[3]   = Buffer_5[1]
            Vm_5[:,3] = Buffer_5[2]
            Br_5[1]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[0],0)
            Buffer_5[1] = Lr_5[:,0]
            Buffer_5[2] = np.flip(Am_5[4],0)
            Buffer_5[3] = Vm_5[:,4]

            Lr_5[:,0] = Buffer_5[0]
            Am_5[4]   = Buffer_5[1]
            Vm_5[:,4] = Buffer_5[2]
            Br_5[0]   = Buffer_5[3]

            Buffer_5[0] = np.flip(Br_5[1],0)
            Buffer_5[1] = Lr_5[:,1]
            Buffer_5[2] = np.flip(Am_5[3],0)
            Buffer_5[3] = Vm_5[:,3]

            Lr_5[:,1] = Buffer_5[0]
            Am_5[3]   = Buffer_5[1]
            Vm_5[:,3] = Buffer_5[2]
            Br_5[1]   = Buffer_5[3]
           
                      

            Az_5 = np.rot90(Az_5,2,(1,0))

        
    elif cube == "6x6":
        
        if turn == "R":
            
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]
            
            
            Vm_6 = np.rot90(Vm_6,1,(1,0))

        elif turn == "R'":
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Vm_6 = np.rot90(Vm_6,-1,(1,0))
                   
            
            
            
        elif turn == "R2":
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]        

            Vm_6 = np.rot90(Vm_6,2,(1,0))
           
        elif turn == "L":
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Lr_6 = np.rot90(Lr_6,1,(1,0))
        elif turn == "L'":
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]                   

            Lr_6 = np.rot90(Lr_6,-1,(1,0))
        elif turn == "L2":
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]        
           

            Lr_6 = np.rot90(Lr_6,2,(1,0))
        elif turn == "U":
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Br_6 = np.rot90(Br_6,1,(1,0))
        elif turn == "U'":
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Br_6 = np.rot90(Br_6,-1,(1,0))
        elif turn == "U2":
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Br_6 = np.rot90(Br_6,2,(1,0))
        elif turn == "D":
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Am_6 = np.rot90(Am_6,1,(1,0))
        elif turn == "D'":

            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]
            

            Am_6 = np.rot90(Am_6,-1,(1,0))
        elif turn == "D2":

            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]           
            

            Am_6 = np.rot90(Am_6,2,(1,0))
        elif turn == "F":
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Vd_6 = np.rot90(Vd_6,1,(1,0))
        elif turn == "F'":

            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]
            
            

            Vd_6 = np.rot90(Vd_6,-1,(1,0))
        elif turn == "F2":

            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]
           

            Vd_6 = np.rot90(Vd_6,2,(1,0))
        elif turn == "B":
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Az_6 = np.rot90(Az_6,1,(1,0))

        elif turn == "B'":

            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]
            
            
            Az_6 = np.rot90(Az_6,-1,(1,0))
        elif turn == "B2":

            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]
            
            

            Az_6 = np.rot90(Az_6,2,(1,0))

        elif turn == "Rw":
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]
            
            Vm_6 = np.rot90(Vm_6,1,(1,0))

        elif turn == "Rw'":

            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]

           
            
            Vm_6 = np.rot90(Vm_6,-1,(1,0))
        elif turn == "Rw2":

            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]      

            Vm_6 = np.rot90(Vm_6,2,(1,0))

        elif turn == "Lw":
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]

            Lr_6 = np.rot90(Lr_6,1,(1,0))
        elif turn == "Lw'":

            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]              

            Lr_6 = np.rot90(Lr_6,-1,(1,0))
        elif turn == "Lw2":
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]    

            Lr_6 = np.rot90(Lr_6,2,(1,0))
        elif turn == "Uw":
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]

            Br_6 = np.rot90(Br_6,1,(1,0))
        elif turn == "Uw'":

            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]           

            Br_6 = np.rot90(Br_6,-1,(1,0))
        elif turn == "Uw2":

            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]           

            Br_6 = np.rot90(Br_6,2,(1,0))
        elif turn == "Dw":
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]

            Am_6 = np.rot90(Am_6,1,(1,0))
        elif turn == "Dw'":

            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]      
            

            Am_6 = np.rot90(Am_6,-1,(1,0))
        elif turn == "Dw2":

            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]         

            Am_6 = np.rot90(Am_6,2,(1,0))
        elif turn == "Fw":
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]

            Vd_6 = np.rot90(Vd_6,1,(1,0))
        elif turn == "Fw'":     

            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]
           
            

            Vd_6 = np.rot90(Vd_6,-1,(1,0))
        elif turn == "Fw2":

            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]
                              
            Vd_6 = np.rot90(Vd_6,2,(1,0))

        elif turn == "Bw":
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]

            Az_6 = np.rot90(Az_6,1,(1,0))

        elif turn == "Bw'":
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]  
            
            Az_6 = np.rot90(Az_6,-1,(1,0))
        elif turn == "Bw2":

            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]        
                      

            Az_6 = np.rot90(Az_6,2,(1,0))
        
        elif turn == "3Rw":
        
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,3]
            Buffer_6[1] = np.flip(Br_6[:,3],0)
            Buffer_6[2] = np.flip(Az_6[:,2],0)
            Buffer_6[3] = Am_6[:,3]           

            Br_6[:,3] = Buffer_6[0]
            Az_6[:,2] = Buffer_6[1]
            Am_6[:,3] = Buffer_6[2]
            Vd_6[:,3] = Buffer_6[3]
            
            Vm_6 = np.rot90(Vm_6,1,(1,0))

        elif turn == "3Rw'":

            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,3]
            Buffer_6[1] = np.flip(Br_6[:,3],0)
            Buffer_6[2] = np.flip(Az_6[:,2],0)
            Buffer_6[3] = Am_6[:,3]           

            Br_6[:,3] = Buffer_6[0]
            Az_6[:,2] = Buffer_6[1]
            Am_6[:,3] = Buffer_6[2]
            Vd_6[:,3] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,3]
            Buffer_6[1] = np.flip(Br_6[:,3],0)
            Buffer_6[2] = np.flip(Az_6[:,2],0)
            Buffer_6[3] = Am_6[:,3]           

            Br_6[:,3] = Buffer_6[0]
            Az_6[:,2] = Buffer_6[1]
            Am_6[:,3] = Buffer_6[2]
            Vd_6[:,3] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,3]
            Buffer_6[1] = np.flip(Br_6[:,3],0)
            Buffer_6[2] = np.flip(Az_6[:,2],0)
            Buffer_6[3] = Am_6[:,3]           

            Br_6[:,3] = Buffer_6[0]
            Az_6[:,2] = Buffer_6[1]
            Am_6[:,3] = Buffer_6[2]
            Vd_6[:,3] = Buffer_6[3]
           
            
            Vm_6 = np.rot90(Vm_6,-1,(1,0))
        elif turn == "3Rw2":

            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,3]
            Buffer_6[1] = np.flip(Br_6[:,3],0)
            Buffer_6[2] = np.flip(Az_6[:,2],0)
            Buffer_6[3] = Am_6[:,3]           

            Br_6[:,3] = Buffer_6[0]
            Az_6[:,2] = Buffer_6[1]
            Am_6[:,3] = Buffer_6[2]
            Vd_6[:,3] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,5]
            Buffer_6[1] = np.flip(Br_6[:,5],0)
            Buffer_6[2] = np.flip(Az_6[:,0],0)
            Buffer_6[3] = Am_6[:,5]           

            Br_6[:,5] = Buffer_6[0]
            Az_6[:,0] = Buffer_6[1]
            Am_6[:,5] = Buffer_6[2]
            Vd_6[:,5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,4]
            Buffer_6[1] = np.flip(Br_6[:,4],0)
            Buffer_6[2] = np.flip(Az_6[:,1],0)
            Buffer_6[3] = Am_6[:,4]           

            Br_6[:,4] = Buffer_6[0]
            Az_6[:,1] = Buffer_6[1]
            Am_6[:,4] = Buffer_6[2]
            Vd_6[:,4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,3]
            Buffer_6[1] = np.flip(Br_6[:,3],0)
            Buffer_6[2] = np.flip(Az_6[:,2],0)
            Buffer_6[3] = Am_6[:,3]           

            Br_6[:,3] = Buffer_6[0]
            Az_6[:,2] = Buffer_6[1]
            Am_6[:,3] = Buffer_6[2]
            Vd_6[:,3] = Buffer_6[3]

            Vm_6 = np.rot90(Vm_6,2,(1,0))

        elif turn == "3Lw":
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,2]
            Buffer_6[1] = np.flip(Am_6[:,2],0)
            Buffer_6[2] = np.flip(Az_6[:,3],0)
            Buffer_6[3] = Br_6[:,2]

            Am_6[:,2] = Buffer_6[0]
            Az_6[:,3] = Buffer_6[1]
            Br_6[:,2] = Buffer_6[2]
            Vd_6[:,2] = Buffer_6[3]

            Lr_6 = np.rot90(Lr_6,1,(1,0))
        elif turn == "3Lw'":

            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,2]
            Buffer_6[1] = np.flip(Am_6[:,2],0)
            Buffer_6[2] = np.flip(Az_6[:,3],0)
            Buffer_6[3] = Br_6[:,2]

            Am_6[:,2] = Buffer_6[0]
            Az_6[:,3] = Buffer_6[1]
            Br_6[:,2] = Buffer_6[2]
            Vd_6[:,2] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,2]
            Buffer_6[1] = np.flip(Am_6[:,2],0)
            Buffer_6[2] = np.flip(Az_6[:,3],0)
            Buffer_6[3] = Br_6[:,2]

            Am_6[:,2] = Buffer_6[0]
            Az_6[:,3] = Buffer_6[1]
            Br_6[:,2] = Buffer_6[2]
            Vd_6[:,2] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,2]
            Buffer_6[1] = np.flip(Am_6[:,2],0)
            Buffer_6[2] = np.flip(Az_6[:,3],0)
            Buffer_6[3] = Br_6[:,2]

            Am_6[:,2] = Buffer_6[0]
            Az_6[:,3] = Buffer_6[1]
            Br_6[:,2] = Buffer_6[2]
            Vd_6[:,2] = Buffer_6[3]           

            Lr_6 = np.rot90(Lr_6,-1,(1,0))
        elif turn == "3Lw2":
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,2]
            Buffer_6[1] = np.flip(Am_6[:,2],0)
            Buffer_6[2] = np.flip(Az_6[:,3],0)
            Buffer_6[3] = Br_6[:,2]

            Am_6[:,2] = Buffer_6[0]
            Az_6[:,3] = Buffer_6[1]
            Br_6[:,2] = Buffer_6[2]
            Vd_6[:,2] = Buffer_6[3]
            Buffer_6[0] = Vd_6[:,0]
            Buffer_6[1] = np.flip(Am_6[:,0],0)
            Buffer_6[2] = np.flip(Az_6[:,5],0)
            Buffer_6[3] = Br_6[:,0]

            Am_6[:,0] = Buffer_6[0]
            Az_6[:,5] = Buffer_6[1]
            Br_6[:,0] = Buffer_6[2]
            Vd_6[:,0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,1]
            Buffer_6[1] = np.flip(Am_6[:,1],0)
            Buffer_6[2] = np.flip(Az_6[:,4],0)
            Buffer_6[3] = Br_6[:,1]

            Am_6[:,1] = Buffer_6[0]
            Az_6[:,4] = Buffer_6[1]
            Br_6[:,1] = Buffer_6[2]
            Vd_6[:,1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[:,2]
            Buffer_6[1] = np.flip(Am_6[:,2],0)
            Buffer_6[2] = np.flip(Az_6[:,3],0)
            Buffer_6[3] = Br_6[:,2]

            Am_6[:,2] = Buffer_6[0]
            Az_6[:,3] = Buffer_6[1]
            Br_6[:,2] = Buffer_6[2]
            Vd_6[:,2] = Buffer_6[3]  

            Lr_6 = np.rot90(Lr_6,2,(1,0))
        elif turn == "3Uw":
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[2]
            Buffer_6[1] = Lr_6[2]
            Buffer_6[2] = Az_6[2]
            Buffer_6[3] = Vm_6[2]

            Lr_6[2] = Buffer_6[0]
            Az_6[2] = Buffer_6[1]
            Vm_6[2] = Buffer_6[2]
            Vd_6[2] = Buffer_6[3]

            Br_6 = np.rot90(Br_6,1,(1,0))
        elif turn == "3Uw'":

            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[2]
            Buffer_6[1] = Lr_6[2]
            Buffer_6[2] = Az_6[2]
            Buffer_6[3] = Vm_6[2]

            Lr_6[2] = Buffer_6[0]
            Az_6[2] = Buffer_6[1]
            Vm_6[2] = Buffer_6[2]
            Vd_6[2] = Buffer_6[3]
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[2]
            Buffer_6[1] = Lr_6[2]
            Buffer_6[2] = Az_6[2]
            Buffer_6[3] = Vm_6[2]

            Lr_6[2] = Buffer_6[0]
            Az_6[2] = Buffer_6[1]
            Vm_6[2] = Buffer_6[2]
            Vd_6[2] = Buffer_6[3]
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[2]
            Buffer_6[1] = Lr_6[2]
            Buffer_6[2] = Az_6[2]
            Buffer_6[3] = Vm_6[2]

            Lr_6[2] = Buffer_6[0]
            Az_6[2] = Buffer_6[1]
            Vm_6[2] = Buffer_6[2]
            Vd_6[2] = Buffer_6[3]         

            Br_6 = np.rot90(Br_6,-1,(1,0))
        elif turn == "3Uw2":

            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[2]
            Buffer_6[1] = Lr_6[2]
            Buffer_6[2] = Az_6[2]
            Buffer_6[3] = Vm_6[2]

            Lr_6[2] = Buffer_6[0]
            Az_6[2] = Buffer_6[1]
            Vm_6[2] = Buffer_6[2]
            Vd_6[2] = Buffer_6[3]
            Buffer_6[0] = Vd_6[0]
            Buffer_6[1] = Lr_6[0]
            Buffer_6[2] = Az_6[0]
            Buffer_6[3] = Vm_6[0]

            Lr_6[0] = Buffer_6[0]
            Az_6[0] = Buffer_6[1]
            Vm_6[0] = Buffer_6[2]
            Vd_6[0] = Buffer_6[3]

            Buffer_6[0] = Vd_6[1]
            Buffer_6[1] = Lr_6[1]
            Buffer_6[2] = Az_6[1]
            Buffer_6[3] = Vm_6[1]

            Lr_6[1] = Buffer_6[0]
            Az_6[1] = Buffer_6[1]
            Vm_6[1] = Buffer_6[2]
            Vd_6[1] = Buffer_6[3]

            Buffer_6[0] = Vd_6[2]
            Buffer_6[1] = Lr_6[2]
            Buffer_6[2] = Az_6[2]
            Buffer_6[3] = Vm_6[2]

            Lr_6[2] = Buffer_6[0]
            Az_6[2] = Buffer_6[1]
            Vm_6[2] = Buffer_6[2]
            Vd_6[2] = Buffer_6[3]        

            Br_6 = np.rot90(Br_6,2,(1,0))
        elif turn == "3Dw":
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[3]
            Buffer_6[1] = Vm_6[3]
            Buffer_6[2] = Az_6[3]
            Buffer_6[3] = Lr_6[3]

            Vm_6[3] = Buffer_6[0]
            Az_6[3] = Buffer_6[1]
            Lr_6[3] = Buffer_6[2]
            Vd_6[3] = Buffer_6[3]

            Am_6 = np.rot90(Am_6,1,(1,0))
        elif turn == "3Dw'":

            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[3]
            Buffer_6[1] = Vm_6[3]
            Buffer_6[2] = Az_6[3]
            Buffer_6[3] = Lr_6[3]

            Vm_6[3] = Buffer_6[0]
            Az_6[3] = Buffer_6[1]
            Lr_6[3] = Buffer_6[2]
            Vd_6[3] = Buffer_6[3]
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[3]
            Buffer_6[1] = Vm_6[3]
            Buffer_6[2] = Az_6[3]
            Buffer_6[3] = Lr_6[3]

            Vm_6[3] = Buffer_6[0]
            Az_6[3] = Buffer_6[1]
            Lr_6[3] = Buffer_6[2]
            Vd_6[3] = Buffer_6[3]
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[3]
            Buffer_6[1] = Vm_6[3]
            Buffer_6[2] = Az_6[3]
            Buffer_6[3] = Lr_6[3]

            Vm_6[3] = Buffer_6[0]
            Az_6[3] = Buffer_6[1]
            Lr_6[3] = Buffer_6[2]
            Vd_6[3] = Buffer_6[3]    
            

            Am_6 = np.rot90(Am_6,-1,(1,0))
        elif turn == "3Dw2":

            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[3]
            Buffer_6[1] = Vm_6[3]
            Buffer_6[2] = Az_6[3]
            Buffer_6[3] = Lr_6[3]

            Vm_6[3] = Buffer_6[0]
            Az_6[3] = Buffer_6[1]
            Lr_6[3] = Buffer_6[2]
            Vd_6[3] = Buffer_6[3]
            Buffer_6[0] = Vd_6[5]
            Buffer_6[1] = Vm_6[5]
            Buffer_6[2] = Az_6[5]
            Buffer_6[3] = Lr_6[5]

            Vm_6[5] = Buffer_6[0]
            Az_6[5] = Buffer_6[1]
            Lr_6[5] = Buffer_6[2]
            Vd_6[5] = Buffer_6[3]

            Buffer_6[0] = Vd_6[4]
            Buffer_6[1] = Vm_6[4]
            Buffer_6[2] = Az_6[4]
            Buffer_6[3] = Lr_6[4]

            Vm_6[4] = Buffer_6[0]
            Az_6[4] = Buffer_6[1]
            Lr_6[4] = Buffer_6[2]
            Vd_6[4] = Buffer_6[3]

            Buffer_6[0] = Vd_6[3]
            Buffer_6[1] = Vm_6[3]
            Buffer_6[2] = Az_6[3]
            Buffer_6[3] = Lr_6[3]

            Vm_6[3] = Buffer_6[0]
            Az_6[3] = Buffer_6[1]
            Lr_6[3] = Buffer_6[2]
            Vd_6[3] = Buffer_6[3]    

            Am_6 = np.rot90(Am_6,2,(1,0))
        elif turn == "3Fw":
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]

            Buffer_6[0] = Br_6[3]
            Buffer_6[1] = np.flip(Vm_6[:,2],0)
            Buffer_6[2] = Am_6[2]
            Buffer_6[3] = np.flip(Lr_6[:,3],0)

            Vm_6[:,2] = Buffer_6[0]
            Am_6[2]   = Buffer_6[1]
            Lr_6[:,3] = Buffer_6[2]
            Br_6[3]   = Buffer_6[3]

            Vd_6 = np.rot90(Vd_6,1,(1,0))
        elif turn == "3Fw'":     

            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]

            Buffer_6[0] = Br_6[3]
            Buffer_6[1] = np.flip(Vm_6[:,2],0)
            Buffer_6[2] = Am_6[2]
            Buffer_6[3] = np.flip(Lr_6[:,3],0)

            Vm_6[:,2] = Buffer_6[0]
            Am_6[2]   = Buffer_6[1]
            Lr_6[:,3] = Buffer_6[2]
            Br_6[3]   = Buffer_6[3]
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]

            Buffer_6[0] = Br_6[3]
            Buffer_6[1] = np.flip(Vm_6[:,2],0)
            Buffer_6[2] = Am_6[2]
            Buffer_6[3] = np.flip(Lr_6[:,3],0)

            Vm_6[:,2] = Buffer_6[0]
            Am_6[2]   = Buffer_6[1]
            Lr_6[:,3] = Buffer_6[2]
            Br_6[3]   = Buffer_6[3]
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]

            Buffer_6[0] = Br_6[3]
            Buffer_6[1] = np.flip(Vm_6[:,2],0)
            Buffer_6[2] = Am_6[2]
            Buffer_6[3] = np.flip(Lr_6[:,3],0)

            Vm_6[:,2] = Buffer_6[0]
            Am_6[2]   = Buffer_6[1]
            Lr_6[:,3] = Buffer_6[2]
            Br_6[3]   = Buffer_6[3]
           
            

            Vd_6 = np.rot90(Vd_6,-1,(1,0))
        elif turn == "3Fw2":

            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]

            Buffer_6[0] = Br_6[3]
            Buffer_6[1] = np.flip(Vm_6[:,2],0)
            Buffer_6[2] = Am_6[2]
            Buffer_6[3] = np.flip(Lr_6[:,3],0)

            Vm_6[:,2] = Buffer_6[0]
            Am_6[2]   = Buffer_6[1]
            Lr_6[:,3] = Buffer_6[2]
            Br_6[3]   = Buffer_6[3]
            Buffer_6[0] = Br_6[5]
            Buffer_6[1] = np.flip(Vm_6[:,0],0)
            Buffer_6[2] = Am_6[0]
            Buffer_6[3] = np.flip(Lr_6[:,5],0)

            Vm_6[:,0] = Buffer_6[0]
            Am_6[0]   = Buffer_6[1]
            Lr_6[:,5] = Buffer_6[2]
            Br_6[5]   = Buffer_6[3]

            Buffer_6[0] = Br_6[4]
            Buffer_6[1] = np.flip(Vm_6[:,1],0)
            Buffer_6[2] = Am_6[1]
            Buffer_6[3] = np.flip(Lr_6[:,4],0)

            Vm_6[:,1] = Buffer_6[0]
            Am_6[1]   = Buffer_6[1]
            Lr_6[:,4] = Buffer_6[2]
            Br_6[4]   = Buffer_6[3]

            Buffer_6[0] = Br_6[3]
            Buffer_6[1] = np.flip(Vm_6[:,2],0)
            Buffer_6[2] = Am_6[2]
            Buffer_6[3] = np.flip(Lr_6[:,3],0)

            Vm_6[:,2] = Buffer_6[0]
            Am_6[2]   = Buffer_6[1]
            Lr_6[:,3] = Buffer_6[2]
            Br_6[3]   = Buffer_6[3]
                              
            Vd_6 = np.rot90(Vd_6,2,(1,0))

        elif turn == "3Bw":
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[2],0)
            Buffer_6[1] = Lr_6[:,2]
            Buffer_6[2] = np.flip(Am_6[3],0)
            Buffer_6[3] = Vm_6[:,3]

            Lr_6[:,2] = Buffer_6[0]
            Am_6[3]   = Buffer_6[1]
            Vm_6[:,3] = Buffer_6[2]
            Br_6[2]   = Buffer_6[3]

            Az_6 = np.rot90(Az_6,1,(1,0))

        elif turn == "3Bw'":
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[2],0)
            Buffer_6[1] = Lr_6[:,2]
            Buffer_6[2] = np.flip(Am_6[3],0)
            Buffer_6[3] = Vm_6[:,3]

            Lr_6[:,2] = Buffer_6[0]
            Am_6[3]   = Buffer_6[1]
            Vm_6[:,3] = Buffer_6[2]
            Br_6[2]   = Buffer_6[3]
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[2],0)
            Buffer_6[1] = Lr_6[:,2]
            Buffer_6[2] = np.flip(Am_6[3],0)
            Buffer_6[3] = Vm_6[:,3]

            Lr_6[:,2] = Buffer_6[0]
            Am_6[3]   = Buffer_6[1]
            Vm_6[:,3] = Buffer_6[2]
            Br_6[2]   = Buffer_6[3]
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[2],0)
            Buffer_6[1] = Lr_6[:,2]
            Buffer_6[2] = np.flip(Am_6[3],0)
            Buffer_6[3] = Vm_6[:,3]

            Lr_6[:,2] = Buffer_6[0]
            Am_6[3]   = Buffer_6[1]
            Vm_6[:,3] = Buffer_6[2]
            Br_6[2]   = Buffer_6[3]
            
            Az_6 = np.rot90(Az_6,-1,(1,0))
        elif turn == "3Bw2":

            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[2],0)
            Buffer_6[1] = Lr_6[:,2]
            Buffer_6[2] = np.flip(Am_6[3],0)
            Buffer_6[3] = Vm_6[:,3]

            Lr_6[:,2] = Buffer_6[0]
            Am_6[3]   = Buffer_6[1]
            Vm_6[:,3] = Buffer_6[2]
            Br_6[2]   = Buffer_6[3]
            Buffer_6[0] = np.flip(Br_6[0],0)
            Buffer_6[1] = Lr_6[:,0]
            Buffer_6[2] = np.flip(Am_6[5],0)
            Buffer_6[3] = Vm_6[:,5]

            Lr_6[:,0] = Buffer_6[0]
            Am_6[5]   = Buffer_6[1]
            Vm_6[:,5] = Buffer_6[2]
            Br_6[0]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[1],0)
            Buffer_6[1] = Lr_6[:,1]
            Buffer_6[2] = np.flip(Am_6[4],0)
            Buffer_6[3] = Vm_6[:,4]

            Lr_6[:,1] = Buffer_6[0]
            Am_6[4]   = Buffer_6[1]
            Vm_6[:,4] = Buffer_6[2]
            Br_6[1]   = Buffer_6[3]

            Buffer_6[0] = np.flip(Br_6[2],0)
            Buffer_6[1] = Lr_6[:,2]
            Buffer_6[2] = np.flip(Am_6[3],0)
            Buffer_6[3] = Vm_6[:,3]

            Lr_6[:,2] = Buffer_6[0]
            Am_6[3]   = Buffer_6[1]
            Vm_6[:,3] = Buffer_6[2]
            Br_6[2]   = Buffer_6[3]                      

            Az_6 = np.rot90(Az_6,2,(1,0))

  
        
    elif cube == "7x7":
        if turn == "R":
            
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]
            
            
            Vm_7 = np.rot90(Vm_7,1,(1,0))

        elif turn == "R'":
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Vm_7 = np.rot90(Vm_7,-1,(1,0))
                   
            
            
            
        elif turn == "R2":
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]   

            Vm_7 = np.rot90(Vm_7,2,(1,0))
           
        elif turn == "L":
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Lr_7 = np.rot90(Lr_7,1,(1,0))
        elif turn == "L'":
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]            

            Lr_7 = np.rot90(Lr_7,-1,(1,0))
        elif turn == "L2":
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]    
           

            Lr_7 = np.rot90(Lr_7,2,(1,0))
        elif turn == "U":
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Br_7 = np.rot90(Br_7,1,(1,0))
        elif turn == "U'":
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Br_7 = np.rot90(Br_7,-1,(1,0))
        elif turn == "U2":
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Br_7 = np.rot90(Br_7,2,(1,0))
        elif turn == "D":
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Am_7 = np.rot90(Am_7,1,(1,0))
        elif turn == "D'":

            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]
            

            Am_7 = np.rot90(Am_7,-1,(1,0))
        elif turn == "D2":

            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]     
            

            Am_7 = np.rot90(Am_7,2,(1,0))
        elif turn == "F":
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Vd_7 = np.rot90(Vd_7,1,(1,0))
        elif turn == "F'":

            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]
            
            

            Vd_7 = np.rot90(Vd_7,-1,(1,0))
        elif turn == "F2":

            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]
           

            Vd_7 = np.rot90(Vd_7,2,(1,0))
        elif turn == "B":
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Az_7 = np.rot90(Az_7,1,(1,0))

        elif turn == "B'":

            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]
            
            
            Az_7 = np.rot90(Az_7,-1,(1,0))
        elif turn == "B2":

            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]
            
            

            Az_7 = np.rot90(Az_7,2,(1,0))

        elif turn == "Rw":
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]
            
            Vm_7 = np.rot90(Vm_7,1,(1,0))

        elif turn == "Rw'":

            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]

           
            
            Vm_7 = np.rot90(Vm_7,-1,(1,0))
        elif turn == "Rw2":

            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]    

            Vm_7 = np.rot90(Vm_7,2,(1,0))

        elif turn == "Lw":
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]

            Lr_7 = np.rot90(Lr_7,1,(1,0))
        elif turn == "Lw'":

            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]


            Lr_7 = np.rot90(Lr_7,-1,(1,0))
        elif turn == "Lw2":
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]


            Lr_7 = np.rot90(Lr_7,2,(1,0))
        elif turn == "Uw":
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]

            Br_7 = np.rot90(Br_7,1,(1,0))
        elif turn == "Uw'":

            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]           

            Br_7 = np.rot90(Br_7,-1,(1,0))
        elif turn == "Uw2":

            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]           

            Br_7 = np.rot90(Br_7,2,(1,0))
        elif turn == "Dw":
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]

            Am_7 = np.rot90(Am_7,1,(1,0))
        elif turn == "Dw'":

            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]     
            

            Am_7 = np.rot90(Am_7,-1,(1,0))
        elif turn == "Dw2":

            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]       

            Am_7 = np.rot90(Am_7,2,(1,0))
        elif turn == "Fw":
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]

            Vd_7 = np.rot90(Vd_7,1,(1,0))
        elif turn == "Fw'":     

            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]
           
            

            Vd_7 = np.rot90(Vd_7,-1,(1,0))
        elif turn == "Fw2":

            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]
                              
            Vd_7 = np.rot90(Vd_7,2,(1,0))

        elif turn == "Bw":
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]

            Az_7 = np.rot90(Az_7,1,(1,0))

        elif turn == "Bw'":
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]
            
            Az_7 = np.rot90(Az_7,-1,(1,0))
        elif turn == "Bw2":

            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]      
                      

            Az_7 = np.rot90(Az_7,2,(1,0))
        
        elif turn == "3Rw":
        
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,4]
            Buffer_7[1] = np.flip(Br_7[:,4],0)
            Buffer_7[2] = np.flip(Az_7[:,2],0)
            Buffer_7[3] = Am_7[:,4]           

            Br_7[:,4] = Buffer_7[0]
            Az_7[:,2] = Buffer_7[1]
            Am_7[:,4] = Buffer_7[2]
            Vd_7[:,4] = Buffer_7[3]
            
            Vm_7 = np.rot90(Vm_7,1,(1,0))

        elif turn == "3Rw'":

            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,4]
            Buffer_7[1] = np.flip(Br_7[:,4],0)
            Buffer_7[2] = np.flip(Az_7[:,2],0)
            Buffer_7[3] = Am_7[:,4]           

            Br_7[:,4] = Buffer_7[0]
            Az_7[:,2] = Buffer_7[1]
            Am_7[:,4] = Buffer_7[2]
            Vd_7[:,4] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,4]
            Buffer_7[1] = np.flip(Br_7[:,4],0)
            Buffer_7[2] = np.flip(Az_7[:,2],0)
            Buffer_7[3] = Am_7[:,4]           

            Br_7[:,4] = Buffer_7[0]
            Az_7[:,2] = Buffer_7[1]
            Am_7[:,4] = Buffer_7[2]
            Vd_7[:,4] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,4]
            Buffer_7[1] = np.flip(Br_7[:,4],0)
            Buffer_7[2] = np.flip(Az_7[:,2],0)
            Buffer_7[3] = Am_7[:,4]           

            Br_7[:,4] = Buffer_7[0]
            Az_7[:,2] = Buffer_7[1]
            Am_7[:,4] = Buffer_7[2]
            Vd_7[:,4] = Buffer_7[3]
           
            
            Vm_7 = np.rot90(Vm_7,-1,(1,0))
        elif turn == "3Rw2":

            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,4]
            Buffer_7[1] = np.flip(Br_7[:,4],0)
            Buffer_7[2] = np.flip(Az_7[:,2],0)
            Buffer_7[3] = Am_7[:,4]           

            Br_7[:,4] = Buffer_7[0]
            Az_7[:,2] = Buffer_7[1]
            Am_7[:,4] = Buffer_7[2]
            Vd_7[:,4] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,6]
            Buffer_7[1] = np.flip(Br_7[:,6],0)
            Buffer_7[2] = np.flip(Az_7[:,0],0)
            Buffer_7[3] = Am_7[:,6]           

            Br_7[:,6] = Buffer_7[0]
            Az_7[:,0] = Buffer_7[1]
            Am_7[:,6] = Buffer_7[2]
            Vd_7[:,6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,5]
            Buffer_7[1] = np.flip(Br_7[:,5],0)
            Buffer_7[2] = np.flip(Az_7[:,1],0)
            Buffer_7[3] = Am_7[:,5]           

            Br_7[:,5] = Buffer_7[0]
            Az_7[:,1] = Buffer_7[1]
            Am_7[:,5] = Buffer_7[2]
            Vd_7[:,5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,4]
            Buffer_7[1] = np.flip(Br_7[:,4],0)
            Buffer_7[2] = np.flip(Az_7[:,2],0)
            Buffer_7[3] = Am_7[:,4]           

            Br_7[:,4] = Buffer_7[0]
            Az_7[:,2] = Buffer_7[1]
            Am_7[:,4] = Buffer_7[2]
            Vd_7[:,4] = Buffer_7[3]

            Vm_7 = np.rot90(Vm_7,2,(1,0))

        elif turn == "3Lw":
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,2]
            Buffer_7[1] = np.flip(Am_7[:,2],0)
            Buffer_7[2] = np.flip(Az_7[:,4],0)
            Buffer_7[3] = Br_7[:,2]

            Am_7[:,2] = Buffer_7[0]
            Az_7[:,4] = Buffer_7[1]
            Br_7[:,2] = Buffer_7[2]
            Vd_7[:,2] = Buffer_7[3]

            Lr_7 = np.rot90(Lr_7,1,(1,0))
        elif turn == "3Lw'":

            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,2]
            Buffer_7[1] = np.flip(Am_7[:,2],0)
            Buffer_7[2] = np.flip(Az_7[:,4],0)
            Buffer_7[3] = Br_7[:,2]

            Am_7[:,2] = Buffer_7[0]
            Az_7[:,4] = Buffer_7[1]
            Br_7[:,2] = Buffer_7[2]
            Vd_7[:,2] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,2]
            Buffer_7[1] = np.flip(Am_7[:,2],0)
            Buffer_7[2] = np.flip(Az_7[:,4],0)
            Buffer_7[3] = Br_7[:,2]

            Am_7[:,2] = Buffer_7[0]
            Az_7[:,4] = Buffer_7[1]
            Br_7[:,2] = Buffer_7[2]
            Vd_7[:,2] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,2]
            Buffer_7[1] = np.flip(Am_7[:,2],0)
            Buffer_7[2] = np.flip(Az_7[:,4],0)
            Buffer_7[3] = Br_7[:,2]

            Am_7[:,2] = Buffer_7[0]
            Az_7[:,4] = Buffer_7[1]
            Br_7[:,2] = Buffer_7[2]
            Vd_7[:,2] = Buffer_7[3]       

            Lr_7 = np.rot90(Lr_7,-1,(1,0))
        elif turn == "3Lw2":
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,2]
            Buffer_7[1] = np.flip(Am_7[:,2],0)
            Buffer_7[2] = np.flip(Az_7[:,4],0)
            Buffer_7[3] = Br_7[:,2]

            Am_7[:,2] = Buffer_7[0]
            Az_7[:,4] = Buffer_7[1]
            Br_7[:,2] = Buffer_7[2]
            Vd_7[:,2] = Buffer_7[3]
            Buffer_7[0] = Vd_7[:,0]
            Buffer_7[1] = np.flip(Am_7[:,0],0)
            Buffer_7[2] = np.flip(Az_7[:,6],0)
            Buffer_7[3] = Br_7[:,0]

            Am_7[:,0] = Buffer_7[0]
            Az_7[:,6] = Buffer_7[1]
            Br_7[:,0] = Buffer_7[2]
            Vd_7[:,0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,1]
            Buffer_7[1] = np.flip(Am_7[:,1],0)
            Buffer_7[2] = np.flip(Az_7[:,5],0)
            Buffer_7[3] = Br_7[:,1]

            Am_7[:,1] = Buffer_7[0]
            Az_7[:,5] = Buffer_7[1]
            Br_7[:,1] = Buffer_7[2]
            Vd_7[:,1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[:,2]
            Buffer_7[1] = np.flip(Am_7[:,2],0)
            Buffer_7[2] = np.flip(Az_7[:,4],0)
            Buffer_7[3] = Br_7[:,2]

            Am_7[:,2] = Buffer_7[0]
            Az_7[:,4] = Buffer_7[1]
            Br_7[:,2] = Buffer_7[2]
            Vd_7[:,2] = Buffer_7[3]

            Lr_7 = np.rot90(Lr_7,2,(1,0))
        elif turn == "3Uw":
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[2]
            Buffer_7[1] = Lr_7[2]
            Buffer_7[2] = Az_7[2]
            Buffer_7[3] = Vm_7[2]

            Lr_7[2] = Buffer_7[0]
            Az_7[2] = Buffer_7[1]
            Vm_7[2] = Buffer_7[2]
            Vd_7[2] = Buffer_7[3]

            Br_7 = np.rot90(Br_7,1,(1,0))
        elif turn == "3Uw'":

            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[2]
            Buffer_7[1] = Lr_7[2]
            Buffer_7[2] = Az_7[2]
            Buffer_7[3] = Vm_7[2]

            Lr_7[2] = Buffer_7[0]
            Az_7[2] = Buffer_7[1]
            Vm_7[2] = Buffer_7[2]
            Vd_7[2] = Buffer_7[3]
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[2]
            Buffer_7[1] = Lr_7[2]
            Buffer_7[2] = Az_7[2]
            Buffer_7[3] = Vm_7[2]

            Lr_7[2] = Buffer_7[0]
            Az_7[2] = Buffer_7[1]
            Vm_7[2] = Buffer_7[2]
            Vd_7[2] = Buffer_7[3]
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[2]
            Buffer_7[1] = Lr_7[2]
            Buffer_7[2] = Az_7[2]
            Buffer_7[3] = Vm_7[2]

            Lr_7[2] = Buffer_7[0]
            Az_7[2] = Buffer_7[1]
            Vm_7[2] = Buffer_7[2]
            Vd_7[2] = Buffer_7[3]         

            Br_7 = np.rot90(Br_7,-1,(1,0))
        elif turn == "3Uw2":

            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[2]
            Buffer_7[1] = Lr_7[2]
            Buffer_7[2] = Az_7[2]
            Buffer_7[3] = Vm_7[2]

            Lr_7[2] = Buffer_7[0]
            Az_7[2] = Buffer_7[1]
            Vm_7[2] = Buffer_7[2]
            Vd_7[2] = Buffer_7[3]
            Buffer_7[0] = Vd_7[0]
            Buffer_7[1] = Lr_7[0]
            Buffer_7[2] = Az_7[0]
            Buffer_7[3] = Vm_7[0]

            Lr_7[0] = Buffer_7[0]
            Az_7[0] = Buffer_7[1]
            Vm_7[0] = Buffer_7[2]
            Vd_7[0] = Buffer_7[3]

            Buffer_7[0] = Vd_7[1]
            Buffer_7[1] = Lr_7[1]
            Buffer_7[2] = Az_7[1]
            Buffer_7[3] = Vm_7[1]

            Lr_7[1] = Buffer_7[0]
            Az_7[1] = Buffer_7[1]
            Vm_7[1] = Buffer_7[2]
            Vd_7[1] = Buffer_7[3]

            Buffer_7[0] = Vd_7[2]
            Buffer_7[1] = Lr_7[2]
            Buffer_7[2] = Az_7[2]
            Buffer_7[3] = Vm_7[2]

            Lr_7[2] = Buffer_7[0]
            Az_7[2] = Buffer_7[1]
            Vm_7[2] = Buffer_7[2]
            Vd_7[2] = Buffer_7[3]        

            Br_7 = np.rot90(Br_7,2,(1,0))
        elif turn == "3Dw":
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[4]
            Buffer_7[1] = Vm_7[4]
            Buffer_7[2] = Az_7[4]
            Buffer_7[3] = Lr_7[4]

            Vm_7[4] = Buffer_7[0]
            Az_7[4] = Buffer_7[1]
            Lr_7[4] = Buffer_7[2]
            Vd_7[4] = Buffer_7[3]

            Am_7 = np.rot90(Am_7,1,(1,0))
        elif turn == "3Dw'":

            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[4]
            Buffer_7[1] = Vm_7[4]
            Buffer_7[2] = Az_7[4]
            Buffer_7[3] = Lr_7[4]

            Vm_7[4] = Buffer_7[0]
            Az_7[4] = Buffer_7[1]
            Lr_7[4] = Buffer_7[2]
            Vd_7[4] = Buffer_7[3]
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[4]
            Buffer_7[1] = Vm_7[4]
            Buffer_7[2] = Az_7[4]
            Buffer_7[3] = Lr_7[4]

            Vm_7[4] = Buffer_7[0]
            Az_7[4] = Buffer_7[1]
            Lr_7[4] = Buffer_7[2]
            Vd_7[4] = Buffer_7[3]
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[4]
            Buffer_7[1] = Vm_7[4]
            Buffer_7[2] = Az_7[4]
            Buffer_7[3] = Lr_7[4]

            Vm_7[4] = Buffer_7[0]
            Az_7[4] = Buffer_7[1]
            Lr_7[4] = Buffer_7[2]
            Vd_7[4] = Buffer_7[3] 
            

            Am_7 = np.rot90(Am_7,-1,(1,0))
        elif turn == "3Dw2":

            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[4]
            Buffer_7[1] = Vm_7[4]
            Buffer_7[2] = Az_7[4]
            Buffer_7[3] = Lr_7[4]

            Vm_7[4] = Buffer_7[0]
            Az_7[4] = Buffer_7[1]
            Lr_7[4] = Buffer_7[2]
            Vd_7[4] = Buffer_7[3]
            Buffer_7[0] = Vd_7[6]
            Buffer_7[1] = Vm_7[6]
            Buffer_7[2] = Az_7[6]
            Buffer_7[3] = Lr_7[6]

            Vm_7[6] = Buffer_7[0]
            Az_7[6] = Buffer_7[1]
            Lr_7[6] = Buffer_7[2]
            Vd_7[6] = Buffer_7[3]

            Buffer_7[0] = Vd_7[5]
            Buffer_7[1] = Vm_7[5]
            Buffer_7[2] = Az_7[5]
            Buffer_7[3] = Lr_7[5]

            Vm_7[5] = Buffer_7[0]
            Az_7[5] = Buffer_7[1]
            Lr_7[5] = Buffer_7[2]
            Vd_7[5] = Buffer_7[3]

            Buffer_7[0] = Vd_7[4]
            Buffer_7[1] = Vm_7[4]
            Buffer_7[2] = Az_7[4]
            Buffer_7[3] = Lr_7[4]

            Vm_7[4] = Buffer_7[0]
            Az_7[4] = Buffer_7[1]
            Lr_7[4] = Buffer_7[2]
            Vd_7[4] = Buffer_7[3] 

            Am_7 = np.rot90(Am_7,2,(1,0))
        elif turn == "3Fw":
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]

            Buffer_7[0] = Br_7[4]
            Buffer_7[1] = np.flip(Vm_7[:,2],0)
            Buffer_7[2] = Am_7[2]
            Buffer_7[3] = np.flip(Lr_7[:,4],0)

            Vm_7[:,2] = Buffer_7[0]
            Am_7[2]   = Buffer_7[1]
            Lr_7[:,4] = Buffer_7[2]
            Br_7[4]   = Buffer_7[3]

            Vd_7 = np.rot90(Vd_7,1,(1,0))
        elif turn == "3Fw'":     

            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]

            Buffer_7[0] = Br_7[4]
            Buffer_7[1] = np.flip(Vm_7[:,2],0)
            Buffer_7[2] = Am_7[2]
            Buffer_7[3] = np.flip(Lr_7[:,4],0)

            Vm_7[:,2] = Buffer_7[0]
            Am_7[2]   = Buffer_7[1]
            Lr_7[:,4] = Buffer_7[2]
            Br_7[4]   = Buffer_7[3]
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]

            Buffer_7[0] = Br_7[4]
            Buffer_7[1] = np.flip(Vm_7[:,2],0)
            Buffer_7[2] = Am_7[2]
            Buffer_7[3] = np.flip(Lr_7[:,4],0)

            Vm_7[:,2] = Buffer_7[0]
            Am_7[2]   = Buffer_7[1]
            Lr_7[:,4] = Buffer_7[2]
            Br_7[4]   = Buffer_7[3]
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]

            Buffer_7[0] = Br_7[4]
            Buffer_7[1] = np.flip(Vm_7[:,2],0)
            Buffer_7[2] = Am_7[2]
            Buffer_7[3] = np.flip(Lr_7[:,4],0)

            Vm_7[:,2] = Buffer_7[0]
            Am_7[2]   = Buffer_7[1]
            Lr_7[:,4] = Buffer_7[2]
            Br_7[4]   = Buffer_7[3]
           
            

            Vd_7 = np.rot90(Vd_7,-1,(1,0))
        elif turn == "3Fw2":

            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]

            Buffer_7[0] = Br_7[4]
            Buffer_7[1] = np.flip(Vm_7[:,2],0)
            Buffer_7[2] = Am_7[2]
            Buffer_7[3] = np.flip(Lr_7[:,4],0)

            Vm_7[:,2] = Buffer_7[0]
            Am_7[2]   = Buffer_7[1]
            Lr_7[:,4] = Buffer_7[2]
            Br_7[4]   = Buffer_7[3]
            Buffer_7[0] = Br_7[6]
            Buffer_7[1] = np.flip(Vm_7[:,0],0)
            Buffer_7[2] = Am_7[0]
            Buffer_7[3] = np.flip(Lr_7[:,6],0)

            Vm_7[:,0] = Buffer_7[0]
            Am_7[0]   = Buffer_7[1]
            Lr_7[:,6] = Buffer_7[2]
            Br_7[6]   = Buffer_7[3]

            Buffer_7[0] = Br_7[5]
            Buffer_7[1] = np.flip(Vm_7[:,1],0)
            Buffer_7[2] = Am_7[1]
            Buffer_7[3] = np.flip(Lr_7[:,5],0)

            Vm_7[:,1] = Buffer_7[0]
            Am_7[1]   = Buffer_7[1]
            Lr_7[:,5] = Buffer_7[2]
            Br_7[5]   = Buffer_7[3]

            Buffer_7[0] = Br_7[4]
            Buffer_7[1] = np.flip(Vm_7[:,2],0)
            Buffer_7[2] = Am_7[2]
            Buffer_7[3] = np.flip(Lr_7[:,4],0)

            Vm_7[:,2] = Buffer_7[0]
            Am_7[2]   = Buffer_7[1]
            Lr_7[:,4] = Buffer_7[2]
            Br_7[4]   = Buffer_7[3]
                              
            Vd_7 = np.rot90(Vd_7,2,(1,0))

        elif turn == "3Bw":
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[2],0)
            Buffer_7[1] = Lr_7[:,2]
            Buffer_7[2] = np.flip(Am_7[4],0)
            Buffer_7[3] = Vm_7[:,4]

            Lr_7[:,2] = Buffer_7[0]
            Am_7[4]   = Buffer_7[1]
            Vm_7[:,4] = Buffer_7[2]
            Br_7[2]   = Buffer_7[3]

            Az_7 = np.rot90(Az_7,1,(1,0))

        elif turn == "3Bw'":
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[2],0)
            Buffer_7[1] = Lr_7[:,2]
            Buffer_7[2] = np.flip(Am_7[4],0)
            Buffer_7[3] = Vm_7[:,4]

            Lr_7[:,2] = Buffer_7[0]
            Am_7[4]   = Buffer_7[1]
            Vm_7[:,4] = Buffer_7[2]
            Br_7[2]   = Buffer_7[3]
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[2],0)
            Buffer_7[1] = Lr_7[:,2]
            Buffer_7[2] = np.flip(Am_7[4],0)
            Buffer_7[3] = Vm_7[:,4]

            Lr_7[:,2] = Buffer_7[0]
            Am_7[4]   = Buffer_7[1]
            Vm_7[:,4] = Buffer_7[2]
            Br_7[2]   = Buffer_7[3]
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[2],0)
            Buffer_7[1] = Lr_7[:,2]
            Buffer_7[2] = np.flip(Am_7[4],0)
            Buffer_7[3] = Vm_7[:,4]

            Lr_7[:,2] = Buffer_7[0]
            Am_7[4]   = Buffer_7[1]
            Vm_7[:,4] = Buffer_7[2]
            Br_7[2]   = Buffer_7[3]
            
            Az_7 = np.rot90(Az_7,-1,(1,0))
        elif turn == "3Bw2":

            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[2],0)
            Buffer_7[1] = Lr_7[:,2]
            Buffer_7[2] = np.flip(Am_7[4],0)
            Buffer_7[3] = Vm_7[:,4]

            Lr_7[:,2] = Buffer_7[0]
            Am_7[4]   = Buffer_7[1]
            Vm_7[:,4] = Buffer_7[2]
            Br_7[2]   = Buffer_7[3]
            Buffer_7[0] = np.flip(Br_7[0],0)
            Buffer_7[1] = Lr_7[:,0]
            Buffer_7[2] = np.flip(Am_7[6],0)
            Buffer_7[3] = Vm_7[:,6]

            Lr_7[:,0] = Buffer_7[0]
            Am_7[6]   = Buffer_7[1]
            Vm_7[:,6] = Buffer_7[2]
            Br_7[0]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[1],0)
            Buffer_7[1] = Lr_7[:,1]
            Buffer_7[2] = np.flip(Am_7[5],0)
            Buffer_7[3] = Vm_7[:,5]

            Lr_7[:,1] = Buffer_7[0]
            Am_7[5]   = Buffer_7[1]
            Vm_7[:,5] = Buffer_7[2]
            Br_7[1]   = Buffer_7[3]

            Buffer_7[0] = np.flip(Br_7[2],0)
            Buffer_7[1] = Lr_7[:,2]
            Buffer_7[2] = np.flip(Am_7[4],0)
            Buffer_7[3] = Vm_7[:,4]

            Lr_7[:,2] = Buffer_7[0]
            Am_7[4]   = Buffer_7[1]
            Vm_7[:,4] = Buffer_7[2]
            Br_7[2]   = Buffer_7[3]                    

            Az_7 = np.rot90(Az_7,2,(1,0))


    elif cube == "pyraminx":
        if turn == "R":
            Buffer_pyra[0][0] = Vd_pyra[1,3]
            Buffer_pyra[0][1] = Vd_pyra[2,2]
            Buffer_pyra[0][2] = Vd_pyra[2,3]
            Buffer_pyra[0][3] = Vd_pyra[2,4]

            Buffer_pyra[1][0] = Az_pyra[1,1]
            Buffer_pyra[1][1] = Az_pyra[1,2]
            Buffer_pyra[1][2] = Az_pyra[1,3]
            Buffer_pyra[1][3] = Az_pyra[2,2]

            Buffer_pyra[2][0] = Am_pyra[0,2]
            Buffer_pyra[2][1] = Am_pyra[0,3]
            Buffer_pyra[2][2] = Am_pyra[0,4]
            Buffer_pyra[2][3] = Am_pyra[1,3]             

            Az_pyra[1,3] = Buffer_pyra[0][0] 
            Az_pyra[1,1] = Buffer_pyra[0][1] 
            Az_pyra[1,2] = Buffer_pyra[0][2] 
            Az_pyra[2,2] = Buffer_pyra[0][3] 

            Am_pyra[1,3] = Buffer_pyra[1][0] 
            Am_pyra[0,3] = Buffer_pyra[1][1] 
            Am_pyra[0,2] = Buffer_pyra[1][2] 
            Am_pyra[0,4] = Buffer_pyra[1][3] 

            Vd_pyra[1,3] = Buffer_pyra[2][0] 
            Vd_pyra[2,3] = Buffer_pyra[2][1] 
            Vd_pyra[2,4] = Buffer_pyra[2][2] 
            Vd_pyra[2,2] = Buffer_pyra[2][3]
        
        elif turn == "R'":
            Buffer_pyra[0][0] = Vd_pyra[1,3]
            Buffer_pyra[0][1] = Vd_pyra[2,2]
            Buffer_pyra[0][2] = Vd_pyra[2,3]
            Buffer_pyra[0][3] = Vd_pyra[2,4]

            Buffer_pyra[1][0] = Az_pyra[1,1]
            Buffer_pyra[1][1] = Az_pyra[1,2]
            Buffer_pyra[1][2] = Az_pyra[1,3]
            Buffer_pyra[1][3] = Az_pyra[2,2]

            Buffer_pyra[2][0] = Am_pyra[0,2]
            Buffer_pyra[2][1] = Am_pyra[0,3]
            Buffer_pyra[2][2] = Am_pyra[0,4]
            Buffer_pyra[2][3] = Am_pyra[1,3]             

            Az_pyra[1,3] = Buffer_pyra[0][0] 
            Az_pyra[1,1] = Buffer_pyra[0][1] 
            Az_pyra[1,2] = Buffer_pyra[0][2] 
            Az_pyra[2,2] = Buffer_pyra[0][3] 

            Am_pyra[1,3] = Buffer_pyra[1][0] 
            Am_pyra[0,3] = Buffer_pyra[1][1] 
            Am_pyra[0,2] = Buffer_pyra[1][2] 
            Am_pyra[0,4] = Buffer_pyra[1][3] 

            Vd_pyra[1,3] = Buffer_pyra[2][0] 
            Vd_pyra[2,3] = Buffer_pyra[2][1] 
            Vd_pyra[2,4] = Buffer_pyra[2][2] 
            Vd_pyra[2,2] = Buffer_pyra[2][3]

            Buffer_pyra[0][0] = Vd_pyra[1,3]
            Buffer_pyra[0][1] = Vd_pyra[2,2]
            Buffer_pyra[0][2] = Vd_pyra[2,3]
            Buffer_pyra[0][3] = Vd_pyra[2,4]

            Buffer_pyra[1][0] = Az_pyra[1,1]
            Buffer_pyra[1][1] = Az_pyra[1,2]
            Buffer_pyra[1][2] = Az_pyra[1,3]
            Buffer_pyra[1][3] = Az_pyra[2,2]

            Buffer_pyra[2][0] = Am_pyra[0,2]
            Buffer_pyra[2][1] = Am_pyra[0,3]
            Buffer_pyra[2][2] = Am_pyra[0,4]
            Buffer_pyra[2][3] = Am_pyra[1,3]             

            Az_pyra[1,3] = Buffer_pyra[0][0] 
            Az_pyra[1,1] = Buffer_pyra[0][1] 
            Az_pyra[1,2] = Buffer_pyra[0][2] 
            Az_pyra[2,2] = Buffer_pyra[0][3] 

            Am_pyra[1,3] = Buffer_pyra[1][0] 
            Am_pyra[0,3] = Buffer_pyra[1][1] 
            Am_pyra[0,2] = Buffer_pyra[1][2] 
            Am_pyra[0,4] = Buffer_pyra[1][3] 

            Vd_pyra[1,3] = Buffer_pyra[2][0] 
            Vd_pyra[2,3] = Buffer_pyra[2][1] 
            Vd_pyra[2,4] = Buffer_pyra[2][2] 
            Vd_pyra[2,2] = Buffer_pyra[2][3]
           
            
            

        
        elif turn == "L":
            Buffer_pyra[0][0] = Vd_pyra[1,1]
            Buffer_pyra[0][1] = Vd_pyra[2,0]
            Buffer_pyra[0][2] = Vd_pyra[2,1]
            Buffer_pyra[0][3] = Vd_pyra[2,2]            

            Buffer_pyra[1][0] = Am_pyra[0,0]
            Buffer_pyra[1][1] = Am_pyra[0,1]
            Buffer_pyra[1][2] = Am_pyra[0,2]
            Buffer_pyra[1][3] = Am_pyra[1,1]

            Buffer_pyra[2][0] = Vm_pyra[1,1]
            Buffer_pyra[2][1] = Vm_pyra[1,2]
            Buffer_pyra[2][2] = Vm_pyra[1,3]
            Buffer_pyra[2][3] = Vm_pyra[2,2] 


            Am_pyra[0,2] = Buffer_pyra[0][0] 
            Am_pyra[0,0] = Buffer_pyra[0][1] 
            Am_pyra[0,1] = Buffer_pyra[0][2] 
            Am_pyra[1,1] = Buffer_pyra[0][3] 

            Vm_pyra[2,2] = Buffer_pyra[1][0] 
            Vm_pyra[1,2] = Buffer_pyra[1][1] 
            Vm_pyra[1,1] = Buffer_pyra[1][2] 
            Vm_pyra[1,3] = Buffer_pyra[1][3]             

            Vd_pyra[1,1] = Buffer_pyra[2][0] 
            Vd_pyra[2,1] = Buffer_pyra[2][1] 
            Vd_pyra[2,2] = Buffer_pyra[2][2] 
            Vd_pyra[2,0] = Buffer_pyra[2][3]
        
        elif turn == "L'":
            Buffer_pyra[0][0] = Vd_pyra[1,1]
            Buffer_pyra[0][1] = Vd_pyra[2,0]
            Buffer_pyra[0][2] = Vd_pyra[2,1]
            Buffer_pyra[0][3] = Vd_pyra[2,2]            

            Buffer_pyra[1][0] = Am_pyra[0,0]
            Buffer_pyra[1][1] = Am_pyra[0,1]
            Buffer_pyra[1][2] = Am_pyra[0,2]
            Buffer_pyra[1][3] = Am_pyra[1,1]

            Buffer_pyra[2][0] = Vm_pyra[1,1]
            Buffer_pyra[2][1] = Vm_pyra[1,2]
            Buffer_pyra[2][2] = Vm_pyra[1,3]
            Buffer_pyra[2][3] = Vm_pyra[2,2] 


            Am_pyra[0,2] = Buffer_pyra[0][0] 
            Am_pyra[0,0] = Buffer_pyra[0][1] 
            Am_pyra[0,1] = Buffer_pyra[0][2] 
            Am_pyra[1,1] = Buffer_pyra[0][3] 

            Vm_pyra[2,2] = Buffer_pyra[1][0] 
            Vm_pyra[1,2] = Buffer_pyra[1][1] 
            Vm_pyra[1,1] = Buffer_pyra[1][2] 
            Vm_pyra[1,3] = Buffer_pyra[1][3]             

            Vd_pyra[1,1] = Buffer_pyra[2][0] 
            Vd_pyra[2,1] = Buffer_pyra[2][1] 
            Vd_pyra[2,2] = Buffer_pyra[2][2] 
            Vd_pyra[2,0] = Buffer_pyra[2][3]

            Buffer_pyra[0][0] = Vd_pyra[1,1]
            Buffer_pyra[0][1] = Vd_pyra[2,0]
            Buffer_pyra[0][2] = Vd_pyra[2,1]
            Buffer_pyra[0][3] = Vd_pyra[2,2]            

            Buffer_pyra[1][0] = Am_pyra[0,0]
            Buffer_pyra[1][1] = Am_pyra[0,1]
            Buffer_pyra[1][2] = Am_pyra[0,2]
            Buffer_pyra[1][3] = Am_pyra[1,1]

            Buffer_pyra[2][0] = Vm_pyra[1,1]
            Buffer_pyra[2][1] = Vm_pyra[1,2]
            Buffer_pyra[2][2] = Vm_pyra[1,3]
            Buffer_pyra[2][3] = Vm_pyra[2,2] 


            Am_pyra[0,2] = Buffer_pyra[0][0] 
            Am_pyra[0,0] = Buffer_pyra[0][1] 
            Am_pyra[0,1] = Buffer_pyra[0][2] 
            Am_pyra[1,1] = Buffer_pyra[0][3] 

            Vm_pyra[2,2] = Buffer_pyra[1][0] 
            Vm_pyra[1,2] = Buffer_pyra[1][1] 
            Vm_pyra[1,1] = Buffer_pyra[1][2] 
            Vm_pyra[1,3] = Buffer_pyra[1][3]             

            Vd_pyra[1,1] = Buffer_pyra[2][0] 
            Vd_pyra[2,1] = Buffer_pyra[2][1] 
            Vd_pyra[2,2] = Buffer_pyra[2][2] 
            Vd_pyra[2,0] = Buffer_pyra[2][3]
            
            



        elif turn == "U":
            Buffer_pyra[0][0] = Vd_pyra[0,2]
            Buffer_pyra[0][1] = Vd_pyra[1,1]
            Buffer_pyra[0][2] = Vd_pyra[1,2]
            Buffer_pyra[0][3] = Vd_pyra[1,3]                       

            Buffer_pyra[1][0] = Vm_pyra[0,2]
            Buffer_pyra[1][1] = Vm_pyra[0,3]
            Buffer_pyra[1][2] = Vm_pyra[0,4]
            Buffer_pyra[1][3] = Vm_pyra[1,3]           

            Buffer_pyra[2][0] = Az_pyra[0,0]
            Buffer_pyra[2][1] = Az_pyra[0,1]
            Buffer_pyra[2][2] = Az_pyra[0,2]
            Buffer_pyra[2][3] = Az_pyra[1,1]

            Vm_pyra[0,4] = Buffer_pyra[0][0] 
            Vm_pyra[0,2] = Buffer_pyra[0][1] 
            Vm_pyra[0,3] = Buffer_pyra[0][2] 
            Vm_pyra[1,3] = Buffer_pyra[0][3]

            Az_pyra[1,1] = Buffer_pyra[1][0] 
            Az_pyra[0,1] = Buffer_pyra[1][1] 
            Az_pyra[0,0] = Buffer_pyra[1][2] 
            Az_pyra[0,2] = Buffer_pyra[1][3]                          

            Vd_pyra[0,2] = Buffer_pyra[2][0] 
            Vd_pyra[1,2] = Buffer_pyra[2][1] 
            Vd_pyra[1,3] = Buffer_pyra[2][2] 
            Vd_pyra[1,1] = Buffer_pyra[2][3]

        
        elif turn == "U'":
            Buffer_pyra[0][0] = Vd_pyra[0,2]
            Buffer_pyra[0][1] = Vd_pyra[1,1]
            Buffer_pyra[0][2] = Vd_pyra[1,2]
            Buffer_pyra[0][3] = Vd_pyra[1,3]                       

            Buffer_pyra[1][0] = Vm_pyra[0,2]
            Buffer_pyra[1][1] = Vm_pyra[0,3]
            Buffer_pyra[1][2] = Vm_pyra[0,4]
            Buffer_pyra[1][3] = Vm_pyra[1,3]           

            Buffer_pyra[2][0] = Az_pyra[0,0]
            Buffer_pyra[2][1] = Az_pyra[0,1]
            Buffer_pyra[2][2] = Az_pyra[0,2]
            Buffer_pyra[2][3] = Az_pyra[1,1]

            Vm_pyra[0,4] = Buffer_pyra[0][0] 
            Vm_pyra[0,2] = Buffer_pyra[0][1] 
            Vm_pyra[0,3] = Buffer_pyra[0][2] 
            Vm_pyra[1,3] = Buffer_pyra[0][3]

            Az_pyra[1,1] = Buffer_pyra[1][0] 
            Az_pyra[0,1] = Buffer_pyra[1][1] 
            Az_pyra[0,0] = Buffer_pyra[1][2] 
            Az_pyra[0,2] = Buffer_pyra[1][3]                          

            Vd_pyra[0,2] = Buffer_pyra[2][0] 
            Vd_pyra[1,2] = Buffer_pyra[2][1] 
            Vd_pyra[1,3] = Buffer_pyra[2][2] 
            Vd_pyra[1,1] = Buffer_pyra[2][3]

            Buffer_pyra[0][0] = Vd_pyra[0,2]
            Buffer_pyra[0][1] = Vd_pyra[1,1]
            Buffer_pyra[0][2] = Vd_pyra[1,2]
            Buffer_pyra[0][3] = Vd_pyra[1,3]                       

            Buffer_pyra[1][0] = Vm_pyra[0,2]
            Buffer_pyra[1][1] = Vm_pyra[0,3]
            Buffer_pyra[1][2] = Vm_pyra[0,4]
            Buffer_pyra[1][3] = Vm_pyra[1,3]           

            Buffer_pyra[2][0] = Az_pyra[0,0]
            Buffer_pyra[2][1] = Az_pyra[0,1]
            Buffer_pyra[2][2] = Az_pyra[0,2]
            Buffer_pyra[2][3] = Az_pyra[1,1]

            Vm_pyra[0,4] = Buffer_pyra[0][0] 
            Vm_pyra[0,2] = Buffer_pyra[0][1] 
            Vm_pyra[0,3] = Buffer_pyra[0][2] 
            Vm_pyra[1,3] = Buffer_pyra[0][3]

            Az_pyra[1,1] = Buffer_pyra[1][0] 
            Az_pyra[0,1] = Buffer_pyra[1][1] 
            Az_pyra[0,0] = Buffer_pyra[1][2] 
            Az_pyra[0,2] = Buffer_pyra[1][3]                          

            Vd_pyra[0,2] = Buffer_pyra[2][0] 
            Vd_pyra[1,2] = Buffer_pyra[2][1] 
            Vd_pyra[1,3] = Buffer_pyra[2][2] 
            Vd_pyra[1,1] = Buffer_pyra[2][3]
           
           

        
        elif turn == "B":

            Buffer_pyra[0][0] = Az_pyra[0,2]
            Buffer_pyra[0][1] = Az_pyra[0,3]
            Buffer_pyra[0][2] = Az_pyra[0,4]
            Buffer_pyra[0][3] = Az_pyra[1,3]

            Buffer_pyra[1][0] = Vm_pyra[0,0]
            Buffer_pyra[1][1] = Vm_pyra[0,1]
            Buffer_pyra[1][2] = Vm_pyra[0,2]
            Buffer_pyra[1][3] = Vm_pyra[1,1]

            Buffer_pyra[2][0] = Am_pyra[1,1]
            Buffer_pyra[2][1] = Am_pyra[1,2]
            Buffer_pyra[2][2] = Am_pyra[1,3]
            Buffer_pyra[2][3] = Am_pyra[2,2] 

            Vm_pyra[1,1] = Buffer_pyra[0][0] 
            Vm_pyra[0,1] = Buffer_pyra[0][1] 
            Vm_pyra[0,0] = Buffer_pyra[0][2] 
            Vm_pyra[0,2] = Buffer_pyra[0][3]

            Am_pyra[2,2] = Buffer_pyra[1][0] 
            Am_pyra[1,2] = Buffer_pyra[1][1] 
            Am_pyra[1,1] = Buffer_pyra[1][2] 
            Am_pyra[1,3] = Buffer_pyra[1][3]

            Az_pyra[1,3] = Buffer_pyra[2][0] 
            Az_pyra[0,3] = Buffer_pyra[2][1] 
            Az_pyra[0,2] = Buffer_pyra[2][2] 
            Az_pyra[0,4] = Buffer_pyra[2][3] 

        elif turn == "B'":
            Buffer_pyra[0][0] = Az_pyra[0,2]
            Buffer_pyra[0][1] = Az_pyra[0,3]
            Buffer_pyra[0][2] = Az_pyra[0,4]
            Buffer_pyra[0][3] = Az_pyra[1,3]

            Buffer_pyra[1][0] = Vm_pyra[0,0]
            Buffer_pyra[1][1] = Vm_pyra[0,1]
            Buffer_pyra[1][2] = Vm_pyra[0,2]
            Buffer_pyra[1][3] = Vm_pyra[1,1]

            Buffer_pyra[2][0] = Am_pyra[1,1]
            Buffer_pyra[2][1] = Am_pyra[1,2]
            Buffer_pyra[2][2] = Am_pyra[1,3]
            Buffer_pyra[2][3] = Am_pyra[2,2] 

            Vm_pyra[1,1] = Buffer_pyra[0][0] 
            Vm_pyra[0,1] = Buffer_pyra[0][1] 
            Vm_pyra[0,0] = Buffer_pyra[0][2] 
            Vm_pyra[0,2] = Buffer_pyra[0][3]

            Am_pyra[2,2] = Buffer_pyra[1][0] 
            Am_pyra[1,2] = Buffer_pyra[1][1] 
            Am_pyra[1,1] = Buffer_pyra[1][2] 
            Am_pyra[1,3] = Buffer_pyra[1][3]

            Az_pyra[1,3] = Buffer_pyra[2][0] 
            Az_pyra[0,3] = Buffer_pyra[2][1] 
            Az_pyra[0,2] = Buffer_pyra[2][2] 
            Az_pyra[0,4] = Buffer_pyra[2][3] 

            Buffer_pyra[0][0] = Az_pyra[0,2]
            Buffer_pyra[0][1] = Az_pyra[0,3]
            Buffer_pyra[0][2] = Az_pyra[0,4]
            Buffer_pyra[0][3] = Az_pyra[1,3]

            Buffer_pyra[1][0] = Vm_pyra[0,0]
            Buffer_pyra[1][1] = Vm_pyra[0,1]
            Buffer_pyra[1][2] = Vm_pyra[0,2]
            Buffer_pyra[1][3] = Vm_pyra[1,1]

            Buffer_pyra[2][0] = Am_pyra[1,1]
            Buffer_pyra[2][1] = Am_pyra[1,2]
            Buffer_pyra[2][2] = Am_pyra[1,3]
            Buffer_pyra[2][3] = Am_pyra[2,2] 

            Vm_pyra[1,1] = Buffer_pyra[0][0] 
            Vm_pyra[0,1] = Buffer_pyra[0][1] 
            Vm_pyra[0,0] = Buffer_pyra[0][2] 
            Vm_pyra[0,2] = Buffer_pyra[0][3]

            Am_pyra[2,2] = Buffer_pyra[1][0] 
            Am_pyra[1,2] = Buffer_pyra[1][1] 
            Am_pyra[1,1] = Buffer_pyra[1][2] 
            Am_pyra[1,3] = Buffer_pyra[1][3]

            Az_pyra[1,3] = Buffer_pyra[2][0] 
            Az_pyra[0,3] = Buffer_pyra[2][1] 
            Az_pyra[0,2] = Buffer_pyra[2][2] 
            Az_pyra[0,4] = Buffer_pyra[2][3] 
            
           

            
        
        elif turn == "r":
            
            Buffer_pyra[0][3] = Vd_pyra[2,4]            
            Buffer_pyra[1][3] = Az_pyra[2,2]           
            Buffer_pyra[2][2] = Am_pyra[0,4]                
          
            Az_pyra[2,2] = Buffer_pyra[0][3]            
            Am_pyra[0,4] = Buffer_pyra[1][3]          
            Vd_pyra[2,4] = Buffer_pyra[2][2] 
        
        elif turn == "r'":
            
            Buffer_pyra[0][3] = Vd_pyra[2,4]            
            Buffer_pyra[1][3] = Az_pyra[2,2]           
            Buffer_pyra[2][2] = Am_pyra[0,4]                
          
            Az_pyra[2,2] = Buffer_pyra[0][3]            
            Am_pyra[0,4] = Buffer_pyra[1][3]          
            Vd_pyra[2,4] = Buffer_pyra[2][2] 

            Buffer_pyra[0][3] = Vd_pyra[2,4]            
            Buffer_pyra[1][3] = Az_pyra[2,2]           
            Buffer_pyra[2][2] = Am_pyra[0,4]                
          
            Az_pyra[2,2] = Buffer_pyra[0][3]            
            Am_pyra[0,4] = Buffer_pyra[1][3]          
            Vd_pyra[2,4] = Buffer_pyra[2][2] 
        
        elif turn == "l":
           
            Buffer_pyra[0][1] = Vd_pyra[2,0]   
            Buffer_pyra[1][0] = Am_pyra[0,0]  
            Buffer_pyra[2][3] = Vm_pyra[2,2]


            Am_pyra[0,0] = Buffer_pyra[0][1]         
            Vm_pyra[2,2] = Buffer_pyra[1][0]               
            Vd_pyra[2,0] = Buffer_pyra[2][3]
        
        elif turn == "l'":
           
            Buffer_pyra[0][1] = Vd_pyra[2,0]   
            Buffer_pyra[1][0] = Am_pyra[0,0]  
            Buffer_pyra[2][3] = Vm_pyra[2,2]
            
                      
            Am_pyra[0,0] = Buffer_pyra[0][1]         
            Vm_pyra[2,2] = Buffer_pyra[1][0]               
            Vd_pyra[2,0] = Buffer_pyra[2][3]

            Buffer_pyra[0][1] = Vd_pyra[2,0]   
            Buffer_pyra[1][0] = Am_pyra[0,0]  
            Buffer_pyra[2][3] = Vm_pyra[2,2]
            
                      
            Am_pyra[0,0] = Buffer_pyra[0][1]         
            Vm_pyra[2,2] = Buffer_pyra[1][0]               
            Vd_pyra[2,0] = Buffer_pyra[2][3]
        
        elif turn == "u":
            Buffer_pyra[0][0] = Vd_pyra[0,2]                         
            Buffer_pyra[1][2] = Vm_pyra[0,4]               
            Buffer_pyra[2][0] = Az_pyra[0,0]
           

            Vm_pyra[0,4] = Buffer_pyra[0][0]   
            Az_pyra[0,0] = Buffer_pyra[1][2]                                 
            Vd_pyra[0,2] = Buffer_pyra[2][0]

        elif turn == "u'":
            Buffer_pyra[0][0] = Vd_pyra[0,2]                         
            Buffer_pyra[1][2] = Vm_pyra[0,4]               
            Buffer_pyra[2][0] = Az_pyra[0,0]
           

            Vm_pyra[0,4] = Buffer_pyra[0][0]   
            Az_pyra[0,0] = Buffer_pyra[1][2]                                 
            Vd_pyra[0,2] = Buffer_pyra[2][0] 

            Buffer_pyra[0][0] = Vd_pyra[0,2]                         
            Buffer_pyra[1][2] = Vm_pyra[0,4]               
            Buffer_pyra[2][0] = Az_pyra[0,0]
           

            Vm_pyra[0,4] = Buffer_pyra[0][0]   
            Az_pyra[0,0] = Buffer_pyra[1][2]                                 
            Vd_pyra[0,2] = Buffer_pyra[2][0] 
        
        elif turn == "b":  
                        
            Buffer_pyra[0][2] = Az_pyra[0,4]          
            Buffer_pyra[1][0] = Vm_pyra[0,0]     
            Buffer_pyra[2][3] = Am_pyra[2,2]

            Vm_pyra[0,0] = Buffer_pyra[0][2]        
            Am_pyra[2,2] = Buffer_pyra[1][0]      
            Az_pyra[0,4] = Buffer_pyra[2][3]      
            
        
        elif turn == "b'":

            Buffer_pyra[0][2] = Az_pyra[0,4]          
            Buffer_pyra[1][0] = Vm_pyra[0,0]     
            Buffer_pyra[2][3] = Am_pyra[2,2]

            Vm_pyra[0,0] = Buffer_pyra[0][2]        
            Am_pyra[2,2] = Buffer_pyra[1][0]      
            Az_pyra[0,4] = Buffer_pyra[2][3]

            Buffer_pyra[0][2] = Az_pyra[0,4]          
            Buffer_pyra[1][0] = Vm_pyra[0,0]     
            Buffer_pyra[2][3] = Am_pyra[2,2]

            Vm_pyra[0,0] = Buffer_pyra[0][2]        
            Am_pyra[2,2] = Buffer_pyra[1][0]      
            Az_pyra[0,4] = Buffer_pyra[2][3]
            
           
        

       
        

        
         
        
                                  

                                  

                       

            
           


    elif cube == "megaminx":
        pass
    elif cube == "skewb":
        pass
    elif cube == "clock":
        pass


def draw_scramble(cube):  

    global Br_2  
    global Lr_2  
    global Vd_2  
    global Vm_2  
    global Az_2  
    global Am_2  

    global Br_3  
    global Lr_3  
    global Vd_3  
    global Vm_3  
    global Az_3  
    global Am_3    

    global Br_4
    global Lr_4
    global Vd_4
    global Vm_4
    global Az_4
    global Am_4

    global Br_5
    global Lr_5
    global Vd_5
    global Vm_5
    global Az_5
    global Am_5

    global Br_6
    global Lr_6
    global Vd_6
    global Vm_6
    global Az_6
    global Am_6

    global Br_7
    global Lr_7
    global Vd_7
    global Vm_7
    global Az_7
    global Am_7

    global Br_pyra
    global Lr_pyra
    global Vd_pyra
    global Vm_pyra
    global Az_pyra
    global Am_pyra

    global Br_color_2 
    global Lr_color_2 
    global Vd_color_2 
    global Vm_color_2 
    global Az_color_2 
    global Am_color_2    

    global Br_color_3 
    global Lr_color_3 
    global Vd_color_3 
    global Vm_color_3 
    global Az_color_3 
    global Am_color_3 

    global Br_color_4  
    global Lr_color_4    
    global Vd_color_4    
    global Vm_color_4    
    global Az_color_4    
    global Am_color_4

    global Br_color_5  
    global Lr_color_5    
    global Vd_color_5    
    global Vm_color_5    
    global Az_color_5    
    global Am_color_5

    global Br_color_6  
    global Lr_color_6    
    global Vd_color_6    
    global Vm_color_6    
    global Az_color_6    
    global Am_color_6          

    global Br_color_7  
    global Lr_color_7    
    global Vd_color_7    
    global Vm_color_7    
    global Az_color_7    
    global Am_color_7 

    global Br_color_pyra 
    global Lr_color_pyra 
    global Vd_color_pyra 
    global Vm_color_pyra 
    global Az_color_pyra 
    global Am_color_pyra

    our_canvas.delete("all")

   
    if cube == "2x2":

        Br_color_2 = np.where(Br_2 != 1, Br_color_2,"white")
        Lr_color_2 = np.where(Lr_2 != 1, Lr_color_2,"white")
        Vd_color_2 = np.where(Vd_2 != 1, Vd_color_2,"white")
        Vm_color_2 = np.where(Vm_2 != 1, Vm_color_2,"white")
        Az_color_2 = np.where(Az_2 != 1, Az_color_2,"white")    
        Am_color_2 = np.where(Am_2 != 1, Am_color_2,"white")  

        Br_color_2 = np.where(Br_2 != 2, Br_color_2,"orange")
        Lr_color_2 = np.where(Lr_2 != 2, Lr_color_2,"orange")
        Vd_color_2 = np.where(Vd_2 != 2, Vd_color_2,"orange")
        Vm_color_2 = np.where(Vm_2 != 2, Vm_color_2,"orange")
        Az_color_2 = np.where(Az_2 != 2, Az_color_2,"orange")    
        Am_color_2 = np.where(Am_2 != 2, Am_color_2,"orange")   

        Br_color_2 = np.where(Br_2 != 3, Br_color_2,"green")
        Lr_color_2 = np.where(Lr_2 != 3, Lr_color_2,"green")
        Vd_color_2 = np.where(Vd_2 != 3, Vd_color_2,"green")
        Vm_color_2 = np.where(Vm_2 != 3, Vm_color_2,"green")
        Az_color_2 = np.where(Az_2 != 3, Az_color_2,"green")
        Am_color_2 = np.where(Am_2 != 3, Am_color_2,"green")

        Br_color_2 = np.where(Br_2 != 4, Br_color_2,"red")
        Lr_color_2 = np.where(Lr_2 != 4, Lr_color_2,"red")
        Vd_color_2 = np.where(Vd_2 != 4, Vd_color_2,"red")
        Vm_color_2 = np.where(Vm_2 != 4, Vm_color_2,"red")
        Az_color_2 = np.where(Az_2 != 4, Az_color_2,"red")
        Am_color_2 = np.where(Am_2 != 4, Am_color_2,"red")

        Br_color_2 = np.where(Br_2 != 5, Br_color_2,"blue")
        Lr_color_2 = np.where(Lr_2 != 5, Lr_color_2,"blue")
        Vd_color_2 = np.where(Vd_2 != 5, Vd_color_2,"blue")
        Vm_color_2 = np.where(Vm_2 != 5, Vm_color_2,"blue")
        Az_color_2 = np.where(Az_2 != 5, Az_color_2,"blue")
        Am_color_2 = np.where(Am_2 != 5, Am_color_2,"blue")

        Br_color_2 = np.where(Br_2 != 6, Br_color_2,"yellow")
        Lr_color_2 = np.where(Lr_2 != 6, Lr_color_2,"yellow")
        Vd_color_2 = np.where(Vd_2 != 6, Vd_color_2,"yellow")
        Vm_color_2 = np.where(Vm_2 != 6, Vm_color_2,"yellow")
        Az_color_2 = np.where(Az_2 != 6, Az_color_2,"yellow")
        Am_color_2 = np.where(Am_2 != 6, Am_color_2,"yellow")   

        
        #U
        our_canvas.create_rectangle(120,10,165,55, fill=Br_color_2[0][0])    
        our_canvas.create_rectangle(170,10,215,55, fill=Br_color_2[0][1])

        our_canvas.create_rectangle(120,60,165,105, fill=Br_color_2[1][0])
        our_canvas.create_rectangle(170,60,215,105, fill=Br_color_2[1][1])

        #L
        our_canvas.create_rectangle(10,120,55 ,165,fill=Lr_color_2[0][0])
        our_canvas.create_rectangle(60,120,105,165,fill=Lr_color_2[0][1])        

        our_canvas.create_rectangle(10,170,55 ,215,fill=Lr_color_2[1][0])
        our_canvas.create_rectangle(60,170,105,215,fill=Lr_color_2[1][1])     

        #F
        our_canvas.create_rectangle(120,120,165,165,fill=Vd_color_2[0][0])
        our_canvas.create_rectangle(170,120,215,165,fill=Vd_color_2[0][1])        

        our_canvas.create_rectangle(120,170,165,215,fill=Vd_color_2[1][0])
        our_canvas.create_rectangle(170,170,215,215,fill=Vd_color_2[1][1])     


        #R
        our_canvas.create_rectangle(230,120,275,165,fill=Vm_color_2[0][0])
        our_canvas.create_rectangle(280,120,325,165,fill=Vm_color_2[0][1])        

        our_canvas.create_rectangle(230,170,275,215,fill=Vm_color_2[1][0])
        our_canvas.create_rectangle(280,170,325,215,fill=Vm_color_2[1][1])               

        #B
        our_canvas.create_rectangle(340,120,385,165,fill=Az_color_2[0][0])
        our_canvas.create_rectangle(390,120,435,165,fill=Az_color_2[0][1])        

        our_canvas.create_rectangle(340,170,385,215,fill=Az_color_2[1][0])
        our_canvas.create_rectangle(390,170,435,215,fill=Az_color_2[1][1])               

        #D
        our_canvas.create_rectangle(120,230,165,275,fill=Am_color_2[0][0])
        our_canvas.create_rectangle(170,230,215,275,fill=Am_color_2[0][1])        

        our_canvas.create_rectangle(120,280,165,325,fill=Am_color_2[1][0])
        our_canvas.create_rectangle(170,280,215,325,fill=Am_color_2[1][1])           
        

    elif cube == "3x3":

        Br_color_3 = np.where(Br_3 != 1, Br_color_3,"white")
        Lr_color_3 = np.where(Lr_3 != 1, Lr_color_3,"white")
        Vd_color_3 = np.where(Vd_3 != 1, Vd_color_3,"white")
        Vm_color_3 = np.where(Vm_3 != 1, Vm_color_3,"white")
        Az_color_3 = np.where(Az_3 != 1, Az_color_3,"white")    
        Am_color_3 = np.where(Am_3 != 1, Am_color_3,"white")  

        Br_color_3 = np.where(Br_3 != 2, Br_color_3,"orange")
        Lr_color_3 = np.where(Lr_3 != 2, Lr_color_3,"orange")
        Vd_color_3 = np.where(Vd_3 != 2, Vd_color_3,"orange")
        Vm_color_3 = np.where(Vm_3 != 2, Vm_color_3,"orange")
        Az_color_3 = np.where(Az_3 != 2, Az_color_3,"orange")    
        Am_color_3 = np.where(Am_3 != 2, Am_color_3,"orange")   

        Br_color_3 = np.where(Br_3 != 3, Br_color_3,"green")
        Lr_color_3 = np.where(Lr_3 != 3, Lr_color_3,"green")
        Vd_color_3 = np.where(Vd_3 != 3, Vd_color_3,"green")
        Vm_color_3 = np.where(Vm_3 != 3, Vm_color_3,"green")
        Az_color_3 = np.where(Az_3 != 3, Az_color_3,"green")
        Am_color_3 = np.where(Am_3 != 3, Am_color_3,"green")

        Br_color_3 = np.where(Br_3 != 4, Br_color_3,"red")
        Lr_color_3 = np.where(Lr_3 != 4, Lr_color_3,"red")
        Vd_color_3 = np.where(Vd_3 != 4, Vd_color_3,"red")
        Vm_color_3 = np.where(Vm_3 != 4, Vm_color_3,"red")
        Az_color_3 = np.where(Az_3 != 4, Az_color_3,"red")
        Am_color_3 = np.where(Am_3 != 4, Am_color_3,"red")

        Br_color_3 = np.where(Br_3 != 5, Br_color_3,"blue")
        Lr_color_3 = np.where(Lr_3 != 5, Lr_color_3,"blue")
        Vd_color_3 = np.where(Vd_3 != 5, Vd_color_3,"blue")
        Vm_color_3 = np.where(Vm_3 != 5, Vm_color_3,"blue")
        Az_color_3 = np.where(Az_3 != 5, Az_color_3,"blue")
        Am_color_3 = np.where(Am_3 != 5, Am_color_3,"blue")

        Br_color_3 = np.where(Br_3 != 6, Br_color_3,"yellow")
        Lr_color_3 = np.where(Lr_3 != 6, Lr_color_3,"yellow")
        Vd_color_3 = np.where(Vd_3 != 6, Vd_color_3,"yellow")
        Vm_color_3 = np.where(Vm_3 != 6, Vm_color_3,"yellow")
        Az_color_3 = np.where(Az_3 != 6, Az_color_3,"yellow")
        Am_color_3 = np.where(Am_3 != 6, Am_color_3,"yellow")   

        
        #U
        our_canvas.create_rectangle(120,10,150,40, fill=Br_color_3[0][0])    
        our_canvas.create_rectangle(155,10,185,40, fill=Br_color_3[0][1])
        our_canvas.create_rectangle(190,10,220,40, fill=Br_color_3[0][2])
        

        our_canvas.create_rectangle(120,45,150,75, fill=Br_color_3[1][0])
        our_canvas.create_rectangle(155,45,185,75, fill=Br_color_3[1][1])
        our_canvas.create_rectangle(190,45,220,75, fill=Br_color_3[1][2])

        our_canvas.create_rectangle(120,80,150,110,fill=Br_color_3[2][0])
        our_canvas.create_rectangle(155,80,185,110,fill=Br_color_3[2][1])
        our_canvas.create_rectangle(190,80,220,110,fill=Br_color_3[2][2])


        #L
        our_canvas.create_rectangle(10,120,40 ,150,fill=Lr_color_3[0][0])
        our_canvas.create_rectangle(45,120,75 ,150,fill=Lr_color_3[0][1])
        our_canvas.create_rectangle(80,120,110,150,fill=Lr_color_3[0][2])

        our_canvas.create_rectangle(10,155,40 ,185,fill=Lr_color_3[1][0])
        our_canvas.create_rectangle(45,155,75 ,185,fill=Lr_color_3[1][1])
        our_canvas.create_rectangle(80,155,110,185,fill=Lr_color_3[1][2])

        our_canvas.create_rectangle(10,190,40 ,220,fill=Lr_color_3[2][0])
        our_canvas.create_rectangle(45,190,75 ,220,fill=Lr_color_3[2][1])
        our_canvas.create_rectangle(80,190,110,220,fill=Lr_color_3[2][2])


        #F
        our_canvas.create_rectangle(120,120,150,150,fill=Vd_color_3[0][0])
        our_canvas.create_rectangle(155,120,185,150,fill=Vd_color_3[0][1])
        our_canvas.create_rectangle(190,120,220,150,fill=Vd_color_3[0][2])

        our_canvas.create_rectangle(120,155,150,185,fill=Vd_color_3[1][0])
        our_canvas.create_rectangle(155,155,185,185,fill=Vd_color_3[1][1])
        our_canvas.create_rectangle(190,155,220,185,fill=Vd_color_3[1][2])

        our_canvas.create_rectangle(120,190,150,220,fill=Vd_color_3[2][0])
        our_canvas.create_rectangle(155,190,185,220,fill=Vd_color_3[2][1])
        our_canvas.create_rectangle(190,190,220,220,fill=Vd_color_3[2][2])


        #R
        our_canvas.create_rectangle(230,120,260,150,fill=Vm_color_3[0][0])
        our_canvas.create_rectangle(265,120,295,150,fill=Vm_color_3[0][1])
        our_canvas.create_rectangle(300,120,330,150,fill=Vm_color_3[0][2])

        our_canvas.create_rectangle(230,155,260,185,fill=Vm_color_3[1][0])
        our_canvas.create_rectangle(265,155,295,185,fill=Vm_color_3[1][1])
        our_canvas.create_rectangle(300,155,330,185,fill=Vm_color_3[1][2])

        our_canvas.create_rectangle(230,190,260,220,fill=Vm_color_3[2][0])
        our_canvas.create_rectangle(265,190,295,220,fill=Vm_color_3[2][1])
        our_canvas.create_rectangle(300,190,330,220,fill=Vm_color_3[2][2])


        #B
        our_canvas.create_rectangle(340,120,370,150,fill=Az_color_3[0][0])
        our_canvas.create_rectangle(375,120,405,150,fill=Az_color_3[0][1])
        our_canvas.create_rectangle(410,120,440,150,fill=Az_color_3[0][2])

        our_canvas.create_rectangle(340,155,370,185,fill=Az_color_3[1][0])
        our_canvas.create_rectangle(375,155,405,185,fill=Az_color_3[1][1])
        our_canvas.create_rectangle(410,155,440,185,fill=Az_color_3[1][2])

        our_canvas.create_rectangle(340,190,370,220,fill=Az_color_3[2][0])
        our_canvas.create_rectangle(375,190,405,220,fill=Az_color_3[2][1])
        our_canvas.create_rectangle(410,190,440,220,fill=Az_color_3[2][2])

        #D
        our_canvas.create_rectangle(120,230,150,260,fill=Am_color_3[0][0])
        our_canvas.create_rectangle(155,230,185,260,fill=Am_color_3[0][1])
        our_canvas.create_rectangle(190,230,220,260,fill=Am_color_3[0][2])

        our_canvas.create_rectangle(120,265,150,295,fill=Am_color_3[1][0])
        our_canvas.create_rectangle(155,265,185,295,fill=Am_color_3[1][1])
        our_canvas.create_rectangle(190,265,220,295,fill=Am_color_3[1][2])

        our_canvas.create_rectangle(120,300,150,330,fill=Am_color_3[2][0])
        our_canvas.create_rectangle(155,300,185,330,fill=Am_color_3[2][1])
        our_canvas.create_rectangle(190,300,220,330,fill=Am_color_3[2][2])

    elif cube == "4x4":        

        Br_color_4 = np.where(Br_4 != 1, Br_color_4,"white")
        Lr_color_4 = np.where(Lr_4 != 1, Lr_color_4,"white")
        Vd_color_4 = np.where(Vd_4 != 1, Vd_color_4,"white")
        Vm_color_4 = np.where(Vm_4 != 1, Vm_color_4,"white")
        Az_color_4 = np.where(Az_4 != 1, Az_color_4,"white")    
        Am_color_4 = np.where(Am_4 != 1, Am_color_4,"white")  

        Br_color_4 = np.where(Br_4 != 2, Br_color_4,"orange")
        Lr_color_4 = np.where(Lr_4 != 2, Lr_color_4,"orange")
        Vd_color_4 = np.where(Vd_4 != 2, Vd_color_4,"orange")
        Vm_color_4 = np.where(Vm_4 != 2, Vm_color_4,"orange")
        Az_color_4 = np.where(Az_4 != 2, Az_color_4,"orange")    
        Am_color_4 = np.where(Am_4 != 2, Am_color_4,"orange")   

        Br_color_4 = np.where(Br_4 != 3, Br_color_4,"green")
        Lr_color_4 = np.where(Lr_4 != 3, Lr_color_4,"green")
        Vd_color_4 = np.where(Vd_4 != 3, Vd_color_4,"green")
        Vm_color_4 = np.where(Vm_4 != 3, Vm_color_4,"green")
        Az_color_4 = np.where(Az_4 != 3, Az_color_4,"green")
        Am_color_4 = np.where(Am_4 != 3, Am_color_4,"green")

        Br_color_4 = np.where(Br_4 != 4, Br_color_4,"red")
        Lr_color_4 = np.where(Lr_4 != 4, Lr_color_4,"red")
        Vd_color_4 = np.where(Vd_4 != 4, Vd_color_4,"red")
        Vm_color_4 = np.where(Vm_4 != 4, Vm_color_4,"red")
        Az_color_4 = np.where(Az_4 != 4, Az_color_4,"red")
        Am_color_4 = np.where(Am_4 != 4, Am_color_4,"red")

        Br_color_4 = np.where(Br_4 != 5, Br_color_4,"blue")
        Lr_color_4 = np.where(Lr_4 != 5, Lr_color_4,"blue")
        Vd_color_4 = np.where(Vd_4 != 5, Vd_color_4,"blue")
        Vm_color_4 = np.where(Vm_4 != 5, Vm_color_4,"blue")
        Az_color_4 = np.where(Az_4 != 5, Az_color_4,"blue")
        Am_color_4 = np.where(Am_4 != 5, Am_color_4,"blue")

        Br_color_4 = np.where(Br_4 != 6, Br_color_4,"yellow")
        Lr_color_4 = np.where(Lr_4 != 6, Lr_color_4,"yellow")
        Vd_color_4 = np.where(Vd_4 != 6, Vd_color_4,"yellow")
        Vm_color_4 = np.where(Vm_4 != 6, Vm_color_4,"yellow")
        Az_color_4 = np.where(Az_4 != 6, Az_color_4,"yellow")
        Am_color_4 = np.where(Am_4 != 6, Am_color_4,"yellow")   
        

        
        #U
        our_canvas.create_rectangle(115,10,135,30, fill=Br_color_4[0][0])    
        our_canvas.create_rectangle(140,10,160,30, fill=Br_color_4[0][1])
        our_canvas.create_rectangle(165,10,185,30, fill=Br_color_4[0][2])
        our_canvas.create_rectangle(190,10,210,30, fill=Br_color_4[0][3])        

        our_canvas.create_rectangle(115,35,135,55, fill=Br_color_4[1][0])
        our_canvas.create_rectangle(140,35,160,55, fill=Br_color_4[1][1])
        our_canvas.create_rectangle(165,35,185,55, fill=Br_color_4[1][2])
        our_canvas.create_rectangle(190,35,210,55, fill=Br_color_4[1][3])

        our_canvas.create_rectangle(115,60,135,80,fill=Br_color_4[2][0])
        our_canvas.create_rectangle(140,60,160,80,fill=Br_color_4[2][1])
        our_canvas.create_rectangle(165,60,185,80,fill=Br_color_4[2][2])
        our_canvas.create_rectangle(190,60,210,80,fill=Br_color_4[2][3])

        our_canvas.create_rectangle(115,85,135,105,fill=Br_color_4[3][0])
        our_canvas.create_rectangle(140,85,160,105,fill=Br_color_4[3][1])
        our_canvas.create_rectangle(165,85,185,105,fill=Br_color_4[3][2])
        our_canvas.create_rectangle(190,85,210,105,fill=Br_color_4[3][3])

        #L
        our_canvas.create_rectangle(10,115,30 ,135,fill=Lr_color_4[0][0])
        our_canvas.create_rectangle(35,115,55 ,135,fill=Lr_color_4[0][1])
        our_canvas.create_rectangle(60,115,80 ,135,fill=Lr_color_4[0][2])
        our_canvas.create_rectangle(85,115,105,135,fill=Lr_color_4[0][3])

        our_canvas.create_rectangle(10,140,30 ,160,fill=Lr_color_4[1][0])
        our_canvas.create_rectangle(35,140,55 ,160,fill=Lr_color_4[1][1])
        our_canvas.create_rectangle(60,140,80 ,160,fill=Lr_color_4[1][2])
        our_canvas.create_rectangle(85,140,105,160,fill=Lr_color_4[1][3])

        our_canvas.create_rectangle(10,165,30 ,185,fill=Lr_color_4[2][0])
        our_canvas.create_rectangle(35,165,55 ,185,fill=Lr_color_4[2][1])
        our_canvas.create_rectangle(60,165,80 ,185,fill=Lr_color_4[2][2])
        our_canvas.create_rectangle(85,165,105,185,fill=Lr_color_4[2][3])

        our_canvas.create_rectangle(10,190,30 ,210,fill=Lr_color_4[3][0])
        our_canvas.create_rectangle(35,190,55 ,210,fill=Lr_color_4[3][1])
        our_canvas.create_rectangle(60,190,80 ,210,fill=Lr_color_4[3][2])
        our_canvas.create_rectangle(85,190,105,210,fill=Lr_color_4[3][3])


        #F
        our_canvas.create_rectangle(115,115,135,135,fill=Vd_color_4[0][0])
        our_canvas.create_rectangle(140,115,160,135,fill=Vd_color_4[0][1])
        our_canvas.create_rectangle(165,115,185,135,fill=Vd_color_4[0][2])
        our_canvas.create_rectangle(190,115,210,135,fill=Vd_color_4[0][3])

        our_canvas.create_rectangle(115,140,135,160,fill=Vd_color_4[1][0])
        our_canvas.create_rectangle(140,140,160,160,fill=Vd_color_4[1][1])
        our_canvas.create_rectangle(165,140,185,160,fill=Vd_color_4[1][2])
        our_canvas.create_rectangle(190,140,210,160,fill=Vd_color_4[1][3])

        our_canvas.create_rectangle(115,165,135,185,fill=Vd_color_4[2][0])
        our_canvas.create_rectangle(140,165,160,185,fill=Vd_color_4[2][1])
        our_canvas.create_rectangle(165,165,185,185,fill=Vd_color_4[2][2])
        our_canvas.create_rectangle(190,165,210,185,fill=Vd_color_4[2][3])

        our_canvas.create_rectangle(115,190,135,210,fill=Vd_color_4[3][0])
        our_canvas.create_rectangle(140,190,160,210,fill=Vd_color_4[3][1])
        our_canvas.create_rectangle(165,190,185,210,fill=Vd_color_4[3][2])
        our_canvas.create_rectangle(190,190,210,210,fill=Vd_color_4[3][3])



        #R
        our_canvas.create_rectangle(220,115,240,135,fill=Vm_color_4[0][0])
        our_canvas.create_rectangle(245,115,265,135,fill=Vm_color_4[0][1])
        our_canvas.create_rectangle(270,115,290,135,fill=Vm_color_4[0][2])
        our_canvas.create_rectangle(295,115,315,135,fill=Vm_color_4[0][3])

        our_canvas.create_rectangle(220,140,240,160,fill=Vm_color_4[1][0])
        our_canvas.create_rectangle(245,140,265,160,fill=Vm_color_4[1][1])
        our_canvas.create_rectangle(270,140,290,160,fill=Vm_color_4[1][2])
        our_canvas.create_rectangle(295,140,315,160,fill=Vm_color_4[1][3])

        our_canvas.create_rectangle(220,165,240,185,fill=Vm_color_4[2][0])
        our_canvas.create_rectangle(245,165,265,185,fill=Vm_color_4[2][1])
        our_canvas.create_rectangle(270,165,290,185,fill=Vm_color_4[2][2])
        our_canvas.create_rectangle(295,165,315,185,fill=Vm_color_4[2][3])

        our_canvas.create_rectangle(220,190,240,210,fill=Vm_color_4[3][0])
        our_canvas.create_rectangle(245,190,265,210,fill=Vm_color_4[3][1])
        our_canvas.create_rectangle(270,190,290,210,fill=Vm_color_4[3][2])
        our_canvas.create_rectangle(295,190,315,210,fill=Vm_color_4[3][3])


        #B
        our_canvas.create_rectangle(325,115,345,135,fill=Az_color_4[0][0])
        our_canvas.create_rectangle(350,115,370,135,fill=Az_color_4[0][1])
        our_canvas.create_rectangle(375,115,395,135,fill=Az_color_4[0][2])
        our_canvas.create_rectangle(400,115,420,135,fill=Az_color_4[0][3])

        our_canvas.create_rectangle(325,140,345,160,fill=Az_color_4[1][0])
        our_canvas.create_rectangle(350,140,370,160,fill=Az_color_4[1][1])
        our_canvas.create_rectangle(375,140,395,160,fill=Az_color_4[1][2])
        our_canvas.create_rectangle(400,140,420,160,fill=Az_color_4[1][3])

        our_canvas.create_rectangle(325,165,345,185,fill=Az_color_4[2][0])
        our_canvas.create_rectangle(350,165,370,185,fill=Az_color_4[2][1])
        our_canvas.create_rectangle(375,165,395,185,fill=Az_color_4[2][2])
        our_canvas.create_rectangle(400,165,420,185,fill=Az_color_4[2][3])

        our_canvas.create_rectangle(325,190,345,210,fill=Az_color_4[3][0])
        our_canvas.create_rectangle(350,190,370,210,fill=Az_color_4[3][1])
        our_canvas.create_rectangle(375,190,395,210,fill=Az_color_4[3][2])
        our_canvas.create_rectangle(400,190,420,210,fill=Az_color_4[3][3])

        #D
        our_canvas.create_rectangle(115,220,135,240,fill=Am_color_4[0][0])
        our_canvas.create_rectangle(140,220,160,240,fill=Am_color_4[0][1])
        our_canvas.create_rectangle(165,220,185,240,fill=Am_color_4[0][2])
        our_canvas.create_rectangle(190,220,210,240,fill=Am_color_4[0][3])

        our_canvas.create_rectangle(115,245,135,265,fill=Am_color_4[1][0])
        our_canvas.create_rectangle(140,245,160,265,fill=Am_color_4[1][1])
        our_canvas.create_rectangle(165,245,185,265,fill=Am_color_4[1][2])
        our_canvas.create_rectangle(190,245,210,265,fill=Am_color_4[1][3])

        our_canvas.create_rectangle(115,270,135,290,fill=Am_color_4[2][0])
        our_canvas.create_rectangle(140,270,160,290,fill=Am_color_4[2][1])
        our_canvas.create_rectangle(165,270,185,290,fill=Am_color_4[2][2])
        our_canvas.create_rectangle(190,270,210,290,fill=Am_color_4[2][3])

        our_canvas.create_rectangle(115,295,135,315,fill=Am_color_4[3][0])
        our_canvas.create_rectangle(140,295,160,315,fill=Am_color_4[3][1])
        our_canvas.create_rectangle(165,295,185,315,fill=Am_color_4[3][2])
        our_canvas.create_rectangle(190,295,210,315,fill=Am_color_4[3][3])
        
    elif cube == "5x5":
        Br_color_5 = np.where(Br_5 != 1, Br_color_5,"white")
        Lr_color_5 = np.where(Lr_5 != 1, Lr_color_5,"white")
        Vd_color_5 = np.where(Vd_5 != 1, Vd_color_5,"white")
        Vm_color_5 = np.where(Vm_5 != 1, Vm_color_5,"white")
        Az_color_5 = np.where(Az_5 != 1, Az_color_5,"white")    
        Am_color_5 = np.where(Am_5 != 1, Am_color_5,"white")  

        Br_color_5 = np.where(Br_5 != 2, Br_color_5,"orange")
        Lr_color_5 = np.where(Lr_5 != 2, Lr_color_5,"orange")
        Vd_color_5 = np.where(Vd_5 != 2, Vd_color_5,"orange")
        Vm_color_5 = np.where(Vm_5 != 2, Vm_color_5,"orange")
        Az_color_5 = np.where(Az_5 != 2, Az_color_5,"orange")    
        Am_color_5 = np.where(Am_5 != 2, Am_color_5,"orange")   

        Br_color_5 = np.where(Br_5 != 3, Br_color_5,"green")
        Lr_color_5 = np.where(Lr_5 != 3, Lr_color_5,"green")
        Vd_color_5 = np.where(Vd_5 != 3, Vd_color_5,"green")
        Vm_color_5 = np.where(Vm_5 != 3, Vm_color_5,"green")
        Az_color_5 = np.where(Az_5 != 3, Az_color_5,"green")
        Am_color_5 = np.where(Am_5 != 3, Am_color_5,"green")

        Br_color_5 = np.where(Br_5 != 4, Br_color_5,"red")
        Lr_color_5 = np.where(Lr_5 != 4, Lr_color_5,"red")
        Vd_color_5 = np.where(Vd_5 != 4, Vd_color_5,"red")
        Vm_color_5 = np.where(Vm_5 != 4, Vm_color_5,"red")
        Az_color_5 = np.where(Az_5 != 4, Az_color_5,"red")
        Am_color_5 = np.where(Am_5 != 4, Am_color_5,"red")

        Br_color_5 = np.where(Br_5 != 5, Br_color_5,"blue")
        Lr_color_5 = np.where(Lr_5 != 5, Lr_color_5,"blue")
        Vd_color_5 = np.where(Vd_5 != 5, Vd_color_5,"blue")
        Vm_color_5 = np.where(Vm_5 != 5, Vm_color_5,"blue")
        Az_color_5 = np.where(Az_5 != 5, Az_color_5,"blue")
        Am_color_5 = np.where(Am_5 != 5, Am_color_5,"blue")

        Br_color_5 = np.where(Br_5 != 6, Br_color_5,"yellow")
        Lr_color_5 = np.where(Lr_5 != 6, Lr_color_5,"yellow")
        Vd_color_5 = np.where(Vd_5 != 6, Vd_color_5,"yellow")
        Vm_color_5 = np.where(Vm_5 != 6, Vm_color_5,"yellow")
        Az_color_5 = np.where(Az_5 != 6, Az_color_5,"yellow")
        Am_color_5 = np.where(Am_5 != 6, Am_color_5,"yellow")  


        #U
        our_canvas.create_rectangle(120,10,138,28,fill=Br_color_5[0][0])    
        our_canvas.create_rectangle(141,10,159,28,fill=Br_color_5[0][1])
        our_canvas.create_rectangle(162,10,180,28,fill=Br_color_5[0][2])
        our_canvas.create_rectangle(183,10,201,28,fill=Br_color_5[0][3])        
        our_canvas.create_rectangle(204,10,222,28,fill=Br_color_5[0][4])        

        our_canvas.create_rectangle(120,31,138,49,fill=Br_color_5[1][0])
        our_canvas.create_rectangle(141,31,159,49,fill=Br_color_5[1][1])
        our_canvas.create_rectangle(162,31,180,49,fill=Br_color_5[1][2])
        our_canvas.create_rectangle(183,31,201,49,fill=Br_color_5[1][3])
        our_canvas.create_rectangle(204,31,222,49,fill=Br_color_5[1][4])

        our_canvas.create_rectangle(120,52,138,70,fill=Br_color_5[2][0])
        our_canvas.create_rectangle(141,52,159,70,fill=Br_color_5[2][1])
        our_canvas.create_rectangle(162,52,180,70,fill=Br_color_5[2][2])
        our_canvas.create_rectangle(183,52,201,70,fill=Br_color_5[2][3])
        our_canvas.create_rectangle(204,52,222,70,fill=Br_color_5[2][4])

        our_canvas.create_rectangle(120,73,138,91,fill=Br_color_5[3][0])
        our_canvas.create_rectangle(141,73,159,91,fill=Br_color_5[3][1])
        our_canvas.create_rectangle(162,73,180,91,fill=Br_color_5[3][2])
        our_canvas.create_rectangle(183,73,201,91,fill=Br_color_5[3][3])
        our_canvas.create_rectangle(204,73,222,91,fill=Br_color_5[3][4])

        our_canvas.create_rectangle(120,94,138,112,fill=Br_color_5[4][0])
        our_canvas.create_rectangle(141,94,159,112,fill=Br_color_5[4][1])
        our_canvas.create_rectangle(162,94,180,112,fill=Br_color_5[4][2])
        our_canvas.create_rectangle(183,94,201,112,fill=Br_color_5[4][3])
        our_canvas.create_rectangle(204,94,222,112,fill=Br_color_5[4][4])

        #L
        our_canvas.create_rectangle(12,118,30 ,136,fill=Lr_color_5[0][0])
        our_canvas.create_rectangle(33,118,51 ,136,fill=Lr_color_5[0][1])
        our_canvas.create_rectangle(54,118,72 ,136,fill=Lr_color_5[0][2])
        our_canvas.create_rectangle(75,118,93 ,136,fill=Lr_color_5[0][3])
        our_canvas.create_rectangle(96,118,114,136,fill=Lr_color_5[0][4])

        our_canvas.create_rectangle(12,139,30 ,157,fill=Lr_color_5[1][0])
        our_canvas.create_rectangle(33,139,51 ,157,fill=Lr_color_5[1][1])
        our_canvas.create_rectangle(54,139,72 ,157,fill=Lr_color_5[1][2])
        our_canvas.create_rectangle(75,139,93 ,157,fill=Lr_color_5[1][3])
        our_canvas.create_rectangle(96,139,114,157,fill=Lr_color_5[1][4])

        our_canvas.create_rectangle(12,160,30 ,178,fill=Lr_color_5[2][0])
        our_canvas.create_rectangle(33,160,51 ,178,fill=Lr_color_5[2][1])
        our_canvas.create_rectangle(54,160,72 ,178,fill=Lr_color_5[2][2])
        our_canvas.create_rectangle(75,160,93 ,178,fill=Lr_color_5[2][3])
        our_canvas.create_rectangle(96,160,114,178,fill=Lr_color_5[2][4])

        our_canvas.create_rectangle(12,181,30 ,199,fill=Lr_color_5[3][0])
        our_canvas.create_rectangle(33,181,51 ,199,fill=Lr_color_5[3][1])
        our_canvas.create_rectangle(54,181,72 ,199,fill=Lr_color_5[3][2])
        our_canvas.create_rectangle(75,181,93 ,199,fill=Lr_color_5[3][3])
        our_canvas.create_rectangle(96,181,114,199,fill=Lr_color_5[3][4])

        our_canvas.create_rectangle(12,202,30 ,220,fill=Lr_color_5[4][0])
        our_canvas.create_rectangle(33,202,51 ,220,fill=Lr_color_5[4][1])
        our_canvas.create_rectangle(54,202,72 ,220,fill=Lr_color_5[4][2])
        our_canvas.create_rectangle(75,202,93 ,220,fill=Lr_color_5[4][3])
        our_canvas.create_rectangle(96,202,114,220,fill=Lr_color_5[4][4])


        #F
        our_canvas.create_rectangle(120,118,138,136,fill=Vd_color_5[0][0])
        our_canvas.create_rectangle(141,118,159,136,fill=Vd_color_5[0][1])
        our_canvas.create_rectangle(162,118,180,136,fill=Vd_color_5[0][2])
        our_canvas.create_rectangle(183,118,201,136,fill=Vd_color_5[0][3])
        our_canvas.create_rectangle(204,118,222,136,fill=Vd_color_5[0][4])

        our_canvas.create_rectangle(120,139,138,157,fill=Vd_color_5[1][0])
        our_canvas.create_rectangle(141,139,159,157,fill=Vd_color_5[1][1])
        our_canvas.create_rectangle(162,139,180,157,fill=Vd_color_5[1][2])
        our_canvas.create_rectangle(183,139,201,157,fill=Vd_color_5[1][3])
        our_canvas.create_rectangle(204,139,222,157,fill=Vd_color_5[1][4])        

        our_canvas.create_rectangle(120,160,138,178,fill=Vd_color_5[2][0])
        our_canvas.create_rectangle(141,160,159,178,fill=Vd_color_5[2][1])
        our_canvas.create_rectangle(162,160,180,178,fill=Vd_color_5[2][2])
        our_canvas.create_rectangle(183,160,201,178,fill=Vd_color_5[2][3])
        our_canvas.create_rectangle(204,160,222,178,fill=Vd_color_5[2][4])

        our_canvas.create_rectangle(120,181,138,199,fill=Vd_color_5[3][0])
        our_canvas.create_rectangle(141,181,159,199,fill=Vd_color_5[3][1])
        our_canvas.create_rectangle(162,181,180,199,fill=Vd_color_5[3][2])
        our_canvas.create_rectangle(183,181,201,199,fill=Vd_color_5[3][3])
        our_canvas.create_rectangle(204,181,222,199,fill=Vd_color_5[3][4])

        our_canvas.create_rectangle(120,202,138,220,fill=Vd_color_5[4][0])
        our_canvas.create_rectangle(141,202,159,220,fill=Vd_color_5[4][1])
        our_canvas.create_rectangle(162,202,180,220,fill=Vd_color_5[4][2])
        our_canvas.create_rectangle(183,202,201,220,fill=Vd_color_5[4][3])
        our_canvas.create_rectangle(204,202,222,220,fill=Vd_color_5[4][4])

        #R
        our_canvas.create_rectangle(228,118,246,136,fill=Vm_color_5[0][0])
        our_canvas.create_rectangle(249,118,267,136,fill=Vm_color_5[0][1])
        our_canvas.create_rectangle(270,118,288,136,fill=Vm_color_5[0][2])
        our_canvas.create_rectangle(291,118,309,136,fill=Vm_color_5[0][3])
        our_canvas.create_rectangle(312,118,330,136,fill=Vm_color_5[0][4])

        our_canvas.create_rectangle(228,139,246,157,fill=Vm_color_5[1][0])
        our_canvas.create_rectangle(249,139,267,157,fill=Vm_color_5[1][1])
        our_canvas.create_rectangle(270,139,288,157,fill=Vm_color_5[1][2])
        our_canvas.create_rectangle(291,139,309,157,fill=Vm_color_5[1][3])
        our_canvas.create_rectangle(312,139,330,157,fill=Vm_color_5[1][4])

        our_canvas.create_rectangle(228,160,246,178,fill=Vm_color_5[2][0])
        our_canvas.create_rectangle(249,160,267,178,fill=Vm_color_5[2][1])
        our_canvas.create_rectangle(270,160,288,178,fill=Vm_color_5[2][2])
        our_canvas.create_rectangle(291,160,309,178,fill=Vm_color_5[2][3])
        our_canvas.create_rectangle(312,160,330,178,fill=Vm_color_5[2][4])

        our_canvas.create_rectangle(228,181,246,199,fill=Vm_color_5[3][0])
        our_canvas.create_rectangle(249,181,267,199,fill=Vm_color_5[3][1])
        our_canvas.create_rectangle(270,181,288,199,fill=Vm_color_5[3][2])
        our_canvas.create_rectangle(291,181,309,199,fill=Vm_color_5[3][3])
        our_canvas.create_rectangle(312,181,330,199,fill=Vm_color_5[3][4])

        our_canvas.create_rectangle(228,202,246,220,fill=Vm_color_5[4][0])
        our_canvas.create_rectangle(249,202,267,220,fill=Vm_color_5[4][1])
        our_canvas.create_rectangle(270,202,288,220,fill=Vm_color_5[4][2])
        our_canvas.create_rectangle(291,202,309,220,fill=Vm_color_5[4][3])
        our_canvas.create_rectangle(312,202,330,220,fill=Vm_color_5[4][4])


        #B
        our_canvas.create_rectangle(336,118,354,136,fill=Az_color_5[0][0])
        our_canvas.create_rectangle(357,118,373,136,fill=Az_color_5[0][1])
        our_canvas.create_rectangle(376,118,395,136,fill=Az_color_5[0][2])
        our_canvas.create_rectangle(399,118,417,136,fill=Az_color_5[0][3])
        our_canvas.create_rectangle(420,118,438,136,fill=Az_color_5[0][4])

        our_canvas.create_rectangle(336,139,354,157,fill=Az_color_5[1][0])
        our_canvas.create_rectangle(357,139,373,157,fill=Az_color_5[1][1])
        our_canvas.create_rectangle(376,139,395,157,fill=Az_color_5[1][2])
        our_canvas.create_rectangle(399,139,417,157,fill=Az_color_5[1][3])
        our_canvas.create_rectangle(420,139,438,157,fill=Az_color_5[1][4])

        our_canvas.create_rectangle(336,160,354,178,fill=Az_color_5[2][0])
        our_canvas.create_rectangle(357,160,373,178,fill=Az_color_5[2][1])
        our_canvas.create_rectangle(376,160,395,178,fill=Az_color_5[2][2])
        our_canvas.create_rectangle(399,160,417,178,fill=Az_color_5[2][3])
        our_canvas.create_rectangle(420,160,438,178,fill=Az_color_5[2][4])

        our_canvas.create_rectangle(336,181,354,199,fill=Az_color_5[3][0])
        our_canvas.create_rectangle(357,181,373,199,fill=Az_color_5[3][1])
        our_canvas.create_rectangle(376,181,395,199,fill=Az_color_5[3][2])
        our_canvas.create_rectangle(399,181,417,199,fill=Az_color_5[3][3])
        our_canvas.create_rectangle(420,181,438,199,fill=Az_color_5[3][4])

        our_canvas.create_rectangle(336,202,354,220,fill=Az_color_5[4][0])
        our_canvas.create_rectangle(357,202,373,220,fill=Az_color_5[4][1])
        our_canvas.create_rectangle(376,202,395,220,fill=Az_color_5[4][2])
        our_canvas.create_rectangle(399,202,417,220,fill=Az_color_5[4][3])
        our_canvas.create_rectangle(420,202,438,220,fill=Az_color_5[4][4])

        #D
        our_canvas.create_rectangle(120,226,138,244,fill=Am_color_5[0][0])
        our_canvas.create_rectangle(141,226,159,244,fill=Am_color_5[0][1])
        our_canvas.create_rectangle(162,226,180,244,fill=Am_color_5[0][2])
        our_canvas.create_rectangle(183,226,201,244,fill=Am_color_5[0][3])
        our_canvas.create_rectangle(204,226,222,244,fill=Am_color_5[0][4])

        our_canvas.create_rectangle(120,247,138,265,fill=Am_color_5[1][0])
        our_canvas.create_rectangle(141,247,159,265,fill=Am_color_5[1][1])
        our_canvas.create_rectangle(162,247,180,265,fill=Am_color_5[1][2])
        our_canvas.create_rectangle(183,247,201,265,fill=Am_color_5[1][3])
        our_canvas.create_rectangle(204,247,222,265,fill=Am_color_5[1][4])

        our_canvas.create_rectangle(120,268,138,286,fill=Am_color_5[2][0])
        our_canvas.create_rectangle(141,268,159,286,fill=Am_color_5[2][1])
        our_canvas.create_rectangle(162,268,180,286,fill=Am_color_5[2][2])
        our_canvas.create_rectangle(183,268,201,286,fill=Am_color_5[2][3])
        our_canvas.create_rectangle(204,268,222,286,fill=Am_color_5[2][4])

        our_canvas.create_rectangle(120,289,138,307,fill=Am_color_5[3][0])
        our_canvas.create_rectangle(141,289,159,307,fill=Am_color_5[3][1])
        our_canvas.create_rectangle(162,289,180,307,fill=Am_color_5[3][2])
        our_canvas.create_rectangle(183,289,201,307,fill=Am_color_5[3][3])
        our_canvas.create_rectangle(204,289,222,307,fill=Am_color_5[3][4])

        our_canvas.create_rectangle(120,310,138,328,fill=Am_color_5[4][0])
        our_canvas.create_rectangle(141,310,159,328,fill=Am_color_5[4][1])
        our_canvas.create_rectangle(162,310,180,328,fill=Am_color_5[4][2])
        our_canvas.create_rectangle(183,310,201,328,fill=Am_color_5[4][3])
        our_canvas.create_rectangle(204,310,222,328,fill=Am_color_5[4][4])
        
    elif cube == "6x6":
        Br_color_6 = np.where(Br_6 != 1, Br_color_6,"white")
        Lr_color_6 = np.where(Lr_6 != 1, Lr_color_6,"white")
        Vd_color_6 = np.where(Vd_6 != 1, Vd_color_6,"white")
        Vm_color_6 = np.where(Vm_6 != 1, Vm_color_6,"white")
        Az_color_6 = np.where(Az_6 != 1, Az_color_6,"white")    
        Am_color_6 = np.where(Am_6 != 1, Am_color_6,"white")  

        Br_color_6 = np.where(Br_6 != 2, Br_color_6,"orange")
        Lr_color_6 = np.where(Lr_6 != 2, Lr_color_6,"orange")
        Vd_color_6 = np.where(Vd_6 != 2, Vd_color_6,"orange")
        Vm_color_6 = np.where(Vm_6 != 2, Vm_color_6,"orange")
        Az_color_6 = np.where(Az_6 != 2, Az_color_6,"orange")    
        Am_color_6 = np.where(Am_6 != 2, Am_color_6,"orange")   

        Br_color_6 = np.where(Br_6 != 3, Br_color_6,"green")
        Lr_color_6 = np.where(Lr_6 != 3, Lr_color_6,"green")
        Vd_color_6 = np.where(Vd_6 != 3, Vd_color_6,"green")
        Vm_color_6 = np.where(Vm_6 != 3, Vm_color_6,"green")
        Az_color_6 = np.where(Az_6 != 3, Az_color_6,"green")
        Am_color_6 = np.where(Am_6 != 3, Am_color_6,"green")

        Br_color_6 = np.where(Br_6 != 4, Br_color_6,"red")
        Lr_color_6 = np.where(Lr_6 != 4, Lr_color_6,"red")
        Vd_color_6 = np.where(Vd_6 != 4, Vd_color_6,"red")
        Vm_color_6 = np.where(Vm_6 != 4, Vm_color_6,"red")
        Az_color_6 = np.where(Az_6 != 4, Az_color_6,"red")
        Am_color_6 = np.where(Am_6 != 4, Am_color_6,"red")

        Br_color_6 = np.where(Br_6 != 5, Br_color_6,"blue")
        Lr_color_6 = np.where(Lr_6 != 5, Lr_color_6,"blue")
        Vd_color_6 = np.where(Vd_6 != 5, Vd_color_6,"blue")
        Vm_color_6 = np.where(Vm_6 != 5, Vm_color_6,"blue")
        Az_color_6 = np.where(Az_6 != 5, Az_color_6,"blue")
        Am_color_6 = np.where(Am_6 != 5, Am_color_6,"blue")

        Br_color_6 = np.where(Br_6 != 6, Br_color_6,"yellow")
        Lr_color_6 = np.where(Lr_6 != 6, Lr_color_6,"yellow")
        Vd_color_6 = np.where(Vd_6 != 6, Vd_color_6,"yellow")
        Vm_color_6 = np.where(Vm_6 != 6, Vm_color_6,"yellow")
        Az_color_6 = np.where(Az_6 != 6, Az_color_6,"yellow")
        Am_color_6 = np.where(Am_6 != 6, Am_color_6,"yellow")  
        
        # print("---------------------------------------------------------")
        # print(Br_color_6)
        # print(Lr_color_6)
        # print(Vd_color_6)
        # print(Vm_color_6)
        # print(Az_color_6)
        # print(Am_color_6)

        #U
        our_canvas.create_rectangle(120,10,135,25,fill=Br_color_6[0][0])    
        our_canvas.create_rectangle(137,10,152,25,fill=Br_color_6[0][1])
        our_canvas.create_rectangle(154,10,169,25,fill=Br_color_6[0][2])
        our_canvas.create_rectangle(171,10,186,25,fill=Br_color_6[0][3])        
        our_canvas.create_rectangle(188,10,203,25,fill=Br_color_6[0][4])        
        our_canvas.create_rectangle(205,10,220,25,fill=Br_color_6[0][5])        

        our_canvas.create_rectangle(120,27,135,42,fill=Br_color_6[1][0])
        our_canvas.create_rectangle(137,27,152,42,fill=Br_color_6[1][1])
        our_canvas.create_rectangle(154,27,169,42,fill=Br_color_6[1][2])
        our_canvas.create_rectangle(171,27,186,42,fill=Br_color_6[1][3])
        our_canvas.create_rectangle(188,27,203,42,fill=Br_color_6[1][4])
        our_canvas.create_rectangle(205,27,220,42,fill=Br_color_6[1][5])

        our_canvas.create_rectangle(120,44,135,59,fill=Br_color_6[2][0])
        our_canvas.create_rectangle(137,44,152,59,fill=Br_color_6[2][1])
        our_canvas.create_rectangle(154,44,169,59,fill=Br_color_6[2][2])
        our_canvas.create_rectangle(171,44,186,59,fill=Br_color_6[2][3])
        our_canvas.create_rectangle(188,44,203,59,fill=Br_color_6[2][4])
        our_canvas.create_rectangle(205,44,220,59,fill=Br_color_6[2][5])

        our_canvas.create_rectangle(120,61,135,76,fill=Br_color_6[3][0])
        our_canvas.create_rectangle(137,61,152,76,fill=Br_color_6[3][1])
        our_canvas.create_rectangle(154,61,169,76,fill=Br_color_6[3][2])
        our_canvas.create_rectangle(171,61,186,76,fill=Br_color_6[3][3])
        our_canvas.create_rectangle(188,61,203,76,fill=Br_color_6[3][4])
        our_canvas.create_rectangle(205,61,220,76,fill=Br_color_6[3][5])

        our_canvas.create_rectangle(120,78,135,93,fill=Br_color_6[4][0])
        our_canvas.create_rectangle(137,78,152,93,fill=Br_color_6[4][1])
        our_canvas.create_rectangle(154,78,169,93,fill=Br_color_6[4][2])
        our_canvas.create_rectangle(171,78,186,93,fill=Br_color_6[4][3])
        our_canvas.create_rectangle(188,78,203,93,fill=Br_color_6[4][4])
        our_canvas.create_rectangle(205,78,220,93,fill=Br_color_6[4][5])

        our_canvas.create_rectangle(120,95,135,110,fill=Br_color_6[5][0])
        our_canvas.create_rectangle(137,95,152,110,fill=Br_color_6[5][1])
        our_canvas.create_rectangle(154,95,169,110,fill=Br_color_6[5][2])
        our_canvas.create_rectangle(171,95,186,110,fill=Br_color_6[5][3])
        our_canvas.create_rectangle(188,95,203,110,fill=Br_color_6[5][4])
        our_canvas.create_rectangle(205,95,220,110,fill=Br_color_6[5][5])

        #L
        our_canvas.create_rectangle(10,120,25 ,135,fill=Lr_color_6[0][0])
        our_canvas.create_rectangle(27,120,42 ,135,fill=Lr_color_6[0][1])
        our_canvas.create_rectangle(44,120,59 ,135,fill=Lr_color_6[0][2])
        our_canvas.create_rectangle(61,120,76 ,135,fill=Lr_color_6[0][3])
        our_canvas.create_rectangle(78,120,93 ,135,fill=Lr_color_6[0][4])
        our_canvas.create_rectangle(95,120,110,135,fill=Lr_color_6[0][5])

        our_canvas.create_rectangle(10,137,25 ,152,fill=Lr_color_6[1][0])
        our_canvas.create_rectangle(27,137,42 ,152,fill=Lr_color_6[1][1])
        our_canvas.create_rectangle(44,137,59 ,152,fill=Lr_color_6[1][2])
        our_canvas.create_rectangle(61,137,76 ,152,fill=Lr_color_6[1][3])
        our_canvas.create_rectangle(78,137,93 ,152,fill=Lr_color_6[1][4])
        our_canvas.create_rectangle(95,137,110,152,fill=Lr_color_6[1][5])

        our_canvas.create_rectangle(10,155,25 ,170,fill=Lr_color_6[2][0])
        our_canvas.create_rectangle(27,155,42 ,170,fill=Lr_color_6[2][1])
        our_canvas.create_rectangle(44,155,59 ,170,fill=Lr_color_6[2][2])
        our_canvas.create_rectangle(61,155,76 ,170,fill=Lr_color_6[2][3])
        our_canvas.create_rectangle(78,155,93 ,170,fill=Lr_color_6[2][4])
        our_canvas.create_rectangle(95,155,110,170,fill=Lr_color_6[2][5])

        our_canvas.create_rectangle(10,172,25 ,187,fill=Lr_color_6[3][0])
        our_canvas.create_rectangle(27,172,42 ,187,fill=Lr_color_6[3][1])
        our_canvas.create_rectangle(44,172,59 ,187,fill=Lr_color_6[3][2])
        our_canvas.create_rectangle(61,172,76 ,187,fill=Lr_color_6[3][3])
        our_canvas.create_rectangle(78,172,93 ,187,fill=Lr_color_6[3][4])
        our_canvas.create_rectangle(95,172,110,187,fill=Lr_color_6[3][5])

        our_canvas.create_rectangle(10,189,25 ,204,fill=Lr_color_6[4][0])
        our_canvas.create_rectangle(27,189,42 ,204,fill=Lr_color_6[4][1])
        our_canvas.create_rectangle(44,189,59 ,204,fill=Lr_color_6[4][2])
        our_canvas.create_rectangle(61,189,76 ,204,fill=Lr_color_6[4][3])
        our_canvas.create_rectangle(78,189,93 ,204,fill=Lr_color_6[4][4])
        our_canvas.create_rectangle(95,189,110,204,fill=Lr_color_6[4][5])

        our_canvas.create_rectangle(10,206,25 ,221,fill=Lr_color_6[5][0])
        our_canvas.create_rectangle(27,206,42 ,221,fill=Lr_color_6[5][1])
        our_canvas.create_rectangle(44,206,59 ,221,fill=Lr_color_6[5][2])
        our_canvas.create_rectangle(61,206,76 ,221,fill=Lr_color_6[5][3])
        our_canvas.create_rectangle(78,206,93 ,221,fill=Lr_color_6[5][4])
        our_canvas.create_rectangle(95,206,110,221,fill=Lr_color_6[5][5])


        #F
        our_canvas.create_rectangle(120,120,135,135,fill=Vd_color_6[0][0])
        our_canvas.create_rectangle(137,120,152,135,fill=Vd_color_6[0][1])
        our_canvas.create_rectangle(154,120,169,135,fill=Vd_color_6[0][2])
        our_canvas.create_rectangle(171,120,186,135,fill=Vd_color_6[0][3])
        our_canvas.create_rectangle(188,120,203,135,fill=Vd_color_6[0][4])
        our_canvas.create_rectangle(205,120,220,135,fill=Vd_color_6[0][5])

        our_canvas.create_rectangle(120,137,135,152,fill=Vd_color_6[1][0])
        our_canvas.create_rectangle(137,137,152,152,fill=Vd_color_6[1][1])
        our_canvas.create_rectangle(154,137,169,152,fill=Vd_color_6[1][2])
        our_canvas.create_rectangle(171,137,186,152,fill=Vd_color_6[1][3])
        our_canvas.create_rectangle(188,137,203,152,fill=Vd_color_6[1][4])        
        our_canvas.create_rectangle(205,137,220,152,fill=Vd_color_6[1][5])        

        our_canvas.create_rectangle(120,155,135,170,fill=Vd_color_6[2][0])
        our_canvas.create_rectangle(137,155,152,170,fill=Vd_color_6[2][1])
        our_canvas.create_rectangle(154,155,169,170,fill=Vd_color_6[2][2])
        our_canvas.create_rectangle(171,155,186,170,fill=Vd_color_6[2][3])
        our_canvas.create_rectangle(188,155,203,170,fill=Vd_color_6[2][4])
        our_canvas.create_rectangle(205,155,220,170,fill=Vd_color_6[2][5])

        our_canvas.create_rectangle(120,172,135,187,fill=Vd_color_6[3][0])
        our_canvas.create_rectangle(137,172,152,187,fill=Vd_color_6[3][1])
        our_canvas.create_rectangle(154,172,169,187,fill=Vd_color_6[3][2])
        our_canvas.create_rectangle(171,172,186,187,fill=Vd_color_6[3][3])
        our_canvas.create_rectangle(188,172,203,187,fill=Vd_color_6[3][4])
        our_canvas.create_rectangle(205,172,220,187,fill=Vd_color_6[3][5])

        our_canvas.create_rectangle(120,189,135,204,fill=Vd_color_6[4][0])
        our_canvas.create_rectangle(137,189,152,204,fill=Vd_color_6[4][1])
        our_canvas.create_rectangle(154,189,169,204,fill=Vd_color_6[4][2])
        our_canvas.create_rectangle(171,189,186,204,fill=Vd_color_6[4][3])
        our_canvas.create_rectangle(188,189,203,204,fill=Vd_color_6[4][4])
        our_canvas.create_rectangle(205,189,220,204,fill=Vd_color_6[4][5])

        our_canvas.create_rectangle(120,206,135,221,fill=Vd_color_6[5][0])
        our_canvas.create_rectangle(137,206,152,221,fill=Vd_color_6[5][1])
        our_canvas.create_rectangle(154,206,169,221,fill=Vd_color_6[5][2])
        our_canvas.create_rectangle(171,206,186,221,fill=Vd_color_6[5][3])
        our_canvas.create_rectangle(188,206,203,221,fill=Vd_color_6[5][4])
        our_canvas.create_rectangle(205,206,220,221,fill=Vd_color_6[5][5])

        #R
        our_canvas.create_rectangle(230,120,245,135,fill=Vm_color_6[0][0])
        our_canvas.create_rectangle(247,120,262,135,fill=Vm_color_6[0][1])
        our_canvas.create_rectangle(264,120,279,135,fill=Vm_color_6[0][2])
        our_canvas.create_rectangle(281,120,296,135,fill=Vm_color_6[0][3])
        our_canvas.create_rectangle(298,120,313,135,fill=Vm_color_6[0][4])
        our_canvas.create_rectangle(315,120,330,135,fill=Vm_color_6[0][5])

        our_canvas.create_rectangle(230,137,245,152,fill=Vm_color_6[1][0])
        our_canvas.create_rectangle(247,137,262,152,fill=Vm_color_6[1][1])
        our_canvas.create_rectangle(264,137,279,152,fill=Vm_color_6[1][2])
        our_canvas.create_rectangle(281,137,296,152,fill=Vm_color_6[1][3])
        our_canvas.create_rectangle(298,137,313,152,fill=Vm_color_6[1][4])
        our_canvas.create_rectangle(315,137,330,152,fill=Vm_color_6[1][5])

        our_canvas.create_rectangle(230,155,245,170,fill=Vm_color_6[2][0])
        our_canvas.create_rectangle(247,155,262,170,fill=Vm_color_6[2][1])
        our_canvas.create_rectangle(264,155,279,170,fill=Vm_color_6[2][2])
        our_canvas.create_rectangle(281,155,296,170,fill=Vm_color_6[2][3])
        our_canvas.create_rectangle(298,155,313,170,fill=Vm_color_6[2][4])
        our_canvas.create_rectangle(315,155,330,170,fill=Vm_color_6[2][5])

        our_canvas.create_rectangle(230,172,245,187,fill=Vm_color_6[3][0])
        our_canvas.create_rectangle(247,172,262,187,fill=Vm_color_6[3][1])
        our_canvas.create_rectangle(264,172,279,187,fill=Vm_color_6[3][2])
        our_canvas.create_rectangle(281,172,296,187,fill=Vm_color_6[3][3])
        our_canvas.create_rectangle(298,172,313,187,fill=Vm_color_6[3][4])
        our_canvas.create_rectangle(315,172,330,187,fill=Vm_color_6[3][5])

        our_canvas.create_rectangle(230,189,245,204,fill=Vm_color_6[4][0])
        our_canvas.create_rectangle(247,189,262,204,fill=Vm_color_6[4][1])
        our_canvas.create_rectangle(264,189,279,204,fill=Vm_color_6[4][2])
        our_canvas.create_rectangle(281,189,296,204,fill=Vm_color_6[4][3])
        our_canvas.create_rectangle(298,189,313,204,fill=Vm_color_6[4][4])
        our_canvas.create_rectangle(315,189,330,204,fill=Vm_color_6[4][5])

        our_canvas.create_rectangle(230,206,245,221,fill=Vm_color_6[5][0])
        our_canvas.create_rectangle(247,206,262,221,fill=Vm_color_6[5][1])
        our_canvas.create_rectangle(264,206,279,221,fill=Vm_color_6[5][2])
        our_canvas.create_rectangle(281,206,296,221,fill=Vm_color_6[5][3])
        our_canvas.create_rectangle(298,206,313,221,fill=Vm_color_6[5][4])
        our_canvas.create_rectangle(315,206,330,221,fill=Vm_color_6[5][5])


        #B
        our_canvas.create_rectangle(340,120,355,135,fill=Az_color_6[0][0])
        our_canvas.create_rectangle(357,120,372,135,fill=Az_color_6[0][1])
        our_canvas.create_rectangle(374,120,389,135,fill=Az_color_6[0][2])
        our_canvas.create_rectangle(391,120,406,135,fill=Az_color_6[0][3])
        our_canvas.create_rectangle(408,120,423,135,fill=Az_color_6[0][4])
        our_canvas.create_rectangle(425,120,440,135,fill=Az_color_6[0][5])

        our_canvas.create_rectangle(340,137,355,152,fill=Az_color_6[1][0])
        our_canvas.create_rectangle(357,137,372,152,fill=Az_color_6[1][1])
        our_canvas.create_rectangle(374,137,389,152,fill=Az_color_6[1][2])
        our_canvas.create_rectangle(391,137,406,152,fill=Az_color_6[1][3])
        our_canvas.create_rectangle(408,137,423,152,fill=Az_color_6[1][4])
        our_canvas.create_rectangle(425,137,440,152,fill=Az_color_6[1][5])

        our_canvas.create_rectangle(340,155,355,170,fill=Az_color_6[2][0])
        our_canvas.create_rectangle(357,155,372,170,fill=Az_color_6[2][1])
        our_canvas.create_rectangle(374,155,389,170,fill=Az_color_6[2][2])
        our_canvas.create_rectangle(391,155,406,170,fill=Az_color_6[2][3])
        our_canvas.create_rectangle(408,155,423,170,fill=Az_color_6[2][4])
        our_canvas.create_rectangle(425,155,440,170,fill=Az_color_6[2][5])

        our_canvas.create_rectangle(340,172,355,187,fill=Az_color_6[3][0])
        our_canvas.create_rectangle(357,172,372,187,fill=Az_color_6[3][1])
        our_canvas.create_rectangle(374,172,389,187,fill=Az_color_6[3][2])
        our_canvas.create_rectangle(391,172,406,187,fill=Az_color_6[3][3])
        our_canvas.create_rectangle(408,172,423,187,fill=Az_color_6[3][4])
        our_canvas.create_rectangle(425,172,440,187,fill=Az_color_6[3][5])

        our_canvas.create_rectangle(340,189,355,204,fill=Az_color_6[4][0])
        our_canvas.create_rectangle(357,189,372,204,fill=Az_color_6[4][1])
        our_canvas.create_rectangle(374,189,389,204,fill=Az_color_6[4][2])
        our_canvas.create_rectangle(391,189,406,204,fill=Az_color_6[4][3])
        our_canvas.create_rectangle(408,189,423,204,fill=Az_color_6[4][4])
        our_canvas.create_rectangle(425,189,440,204,fill=Az_color_6[4][5])

        our_canvas.create_rectangle(340,206,355,221,fill=Az_color_6[5][0])
        our_canvas.create_rectangle(357,206,372,221,fill=Az_color_6[5][1])
        our_canvas.create_rectangle(374,206,389,221,fill=Az_color_6[5][2])
        our_canvas.create_rectangle(391,206,406,221,fill=Az_color_6[5][3])
        our_canvas.create_rectangle(408,206,423,221,fill=Az_color_6[5][4])
        our_canvas.create_rectangle(425,206,440,221,fill=Az_color_6[5][5])

        #D
        our_canvas.create_rectangle(120,230,135,245,fill=Am_color_6[0][0])
        our_canvas.create_rectangle(137,230,152,245,fill=Am_color_6[0][1])
        our_canvas.create_rectangle(154,230,169,245,fill=Am_color_6[0][2])
        our_canvas.create_rectangle(171,230,186,245,fill=Am_color_6[0][3])
        our_canvas.create_rectangle(188,230,203,245,fill=Am_color_6[0][4])
        our_canvas.create_rectangle(205,230,220,245,fill=Am_color_6[0][5])

        our_canvas.create_rectangle(120,247,135,262,fill=Am_color_6[1][0])
        our_canvas.create_rectangle(137,247,152,262,fill=Am_color_6[1][1])
        our_canvas.create_rectangle(154,247,169,262,fill=Am_color_6[1][2])
        our_canvas.create_rectangle(171,247,186,262,fill=Am_color_6[1][3])
        our_canvas.create_rectangle(188,247,203,262,fill=Am_color_6[1][4])
        our_canvas.create_rectangle(205,247,220,262,fill=Am_color_6[1][5])

        our_canvas.create_rectangle(120,264,135,279,fill=Am_color_6[2][0])
        our_canvas.create_rectangle(137,264,152,279,fill=Am_color_6[2][1])
        our_canvas.create_rectangle(154,264,169,279,fill=Am_color_6[2][2])
        our_canvas.create_rectangle(171,264,186,279,fill=Am_color_6[2][3])
        our_canvas.create_rectangle(188,264,203,279,fill=Am_color_6[2][4])
        our_canvas.create_rectangle(205,264,220,279,fill=Am_color_6[2][5])

        our_canvas.create_rectangle(120,281,135,296,fill=Am_color_6[3][0])
        our_canvas.create_rectangle(137,281,152,296,fill=Am_color_6[3][1])
        our_canvas.create_rectangle(154,281,169,296,fill=Am_color_6[3][2])
        our_canvas.create_rectangle(171,281,186,296,fill=Am_color_6[3][3])
        our_canvas.create_rectangle(188,281,203,296,fill=Am_color_6[3][4])
        our_canvas.create_rectangle(205,281,220,296,fill=Am_color_6[3][5])

        our_canvas.create_rectangle(120,298,135,313,fill=Am_color_6[4][0])
        our_canvas.create_rectangle(137,298,152,313,fill=Am_color_6[4][1])
        our_canvas.create_rectangle(154,298,169,313,fill=Am_color_6[4][2])
        our_canvas.create_rectangle(171,298,186,313,fill=Am_color_6[4][3])
        our_canvas.create_rectangle(188,298,203,313,fill=Am_color_6[4][4])
        our_canvas.create_rectangle(205,298,220,313,fill=Am_color_6[4][5])

        our_canvas.create_rectangle(120,315,135,330,fill=Am_color_6[5][0])
        our_canvas.create_rectangle(137,315,152,330,fill=Am_color_6[5][1])
        our_canvas.create_rectangle(154,315,169,330,fill=Am_color_6[5][2])
        our_canvas.create_rectangle(171,315,186,330,fill=Am_color_6[5][3])
        our_canvas.create_rectangle(188,315,203,330,fill=Am_color_6[5][4])
        our_canvas.create_rectangle(205,315,220,330,fill=Am_color_6[5][5])
        
    elif cube == "7x7":
        Br_color_7 = np.where(Br_7 != 1, Br_color_7,"white")
        Lr_color_7 = np.where(Lr_7 != 1, Lr_color_7,"white")
        Vd_color_7 = np.where(Vd_7 != 1, Vd_color_7,"white")
        Vm_color_7 = np.where(Vm_7 != 1, Vm_color_7,"white")
        Az_color_7 = np.where(Az_7 != 1, Az_color_7,"white")    
        Am_color_7 = np.where(Am_7 != 1, Am_color_7,"white")  

        Br_color_7 = np.where(Br_7 != 2, Br_color_7,"orange")
        Lr_color_7 = np.where(Lr_7 != 2, Lr_color_7,"orange")
        Vd_color_7 = np.where(Vd_7 != 2, Vd_color_7,"orange")
        Vm_color_7 = np.where(Vm_7 != 2, Vm_color_7,"orange")
        Az_color_7 = np.where(Az_7 != 2, Az_color_7,"orange")    
        Am_color_7 = np.where(Am_7 != 2, Am_color_7,"orange")   

        Br_color_7 = np.where(Br_7 != 3, Br_color_7,"green")
        Lr_color_7 = np.where(Lr_7 != 3, Lr_color_7,"green")
        Vd_color_7 = np.where(Vd_7 != 3, Vd_color_7,"green")
        Vm_color_7 = np.where(Vm_7 != 3, Vm_color_7,"green")
        Az_color_7 = np.where(Az_7 != 3, Az_color_7,"green")
        Am_color_7 = np.where(Am_7 != 3, Am_color_7,"green")

        Br_color_7 = np.where(Br_7 != 4, Br_color_7,"red")
        Lr_color_7 = np.where(Lr_7 != 4, Lr_color_7,"red")
        Vd_color_7 = np.where(Vd_7 != 4, Vd_color_7,"red")
        Vm_color_7 = np.where(Vm_7 != 4, Vm_color_7,"red")
        Az_color_7 = np.where(Az_7 != 4, Az_color_7,"red")
        Am_color_7 = np.where(Am_7 != 4, Am_color_7,"red")

        Br_color_7 = np.where(Br_7 != 5, Br_color_7,"blue")
        Lr_color_7 = np.where(Lr_7 != 5, Lr_color_7,"blue")
        Vd_color_7 = np.where(Vd_7 != 5, Vd_color_7,"blue")
        Vm_color_7 = np.where(Vm_7 != 5, Vm_color_7,"blue")
        Az_color_7 = np.where(Az_7 != 5, Az_color_7,"blue")
        Am_color_7 = np.where(Am_7 != 5, Am_color_7,"blue")

        Br_color_7 = np.where(Br_7 != 6, Br_color_7,"yellow")
        Lr_color_7 = np.where(Lr_7 != 6, Lr_color_7,"yellow")
        Vd_color_7 = np.where(Vd_7 != 6, Vd_color_7,"yellow")
        Vm_color_7 = np.where(Vm_7 != 6, Vm_color_7,"yellow")
        Az_color_7 = np.where(Az_7 != 6, Az_color_7,"yellow")
        Am_color_7 = np.where(Am_7 != 6, Am_color_7,"yellow")  

        #U
        our_canvas.create_rectangle(120,10,133,23,fill=Br_color_7[0][0])    
        our_canvas.create_rectangle(135,10,148,23,fill=Br_color_7[0][1])
        our_canvas.create_rectangle(150,10,163,23,fill=Br_color_7[0][2])
        our_canvas.create_rectangle(165,10,178,23,fill=Br_color_7[0][3])        
        our_canvas.create_rectangle(180,10,193,23,fill=Br_color_7[0][4])        
        our_canvas.create_rectangle(195,10,208,23,fill=Br_color_7[0][5])        
        our_canvas.create_rectangle(210,10,223,23,fill=Br_color_7[0][6])        

        our_canvas.create_rectangle(120,25,133,38,fill=Br_color_7[1][0])
        our_canvas.create_rectangle(135,25,148,38,fill=Br_color_7[1][1])
        our_canvas.create_rectangle(150,25,163,38,fill=Br_color_7[1][2])
        our_canvas.create_rectangle(165,25,178,38,fill=Br_color_7[1][3])
        our_canvas.create_rectangle(180,25,193,38,fill=Br_color_7[1][4])
        our_canvas.create_rectangle(195,25,208,38,fill=Br_color_7[1][5])
        our_canvas.create_rectangle(210,25,223,38,fill=Br_color_7[1][6])

        our_canvas.create_rectangle(120,40,133,53,fill=Br_color_7[2][0])
        our_canvas.create_rectangle(135,40,148,53,fill=Br_color_7[2][1])
        our_canvas.create_rectangle(150,40,163,53,fill=Br_color_7[2][2])
        our_canvas.create_rectangle(165,40,178,53,fill=Br_color_7[2][3])
        our_canvas.create_rectangle(180,40,192,53,fill=Br_color_7[2][4])
        our_canvas.create_rectangle(195,40,208,53,fill=Br_color_7[2][5])
        our_canvas.create_rectangle(210,40,223,53,fill=Br_color_7[2][6])

        our_canvas.create_rectangle(120,55,133,68,fill=Br_color_7[3][0])
        our_canvas.create_rectangle(135,55,148,68,fill=Br_color_7[3][1])
        our_canvas.create_rectangle(150,55,163,68,fill=Br_color_7[3][2])
        our_canvas.create_rectangle(165,55,178,68,fill=Br_color_7[3][3])
        our_canvas.create_rectangle(180,55,192,68,fill=Br_color_7[3][4])
        our_canvas.create_rectangle(195,55,208,68,fill=Br_color_7[3][5])
        our_canvas.create_rectangle(210,55,223,68,fill=Br_color_7[3][6])

        our_canvas.create_rectangle(120,70,133,83,fill=Br_color_7[4][0])
        our_canvas.create_rectangle(135,70,148,83,fill=Br_color_7[4][1])
        our_canvas.create_rectangle(150,70,163,83,fill=Br_color_7[4][2])
        our_canvas.create_rectangle(165,70,178,83,fill=Br_color_7[4][3])
        our_canvas.create_rectangle(180,70,192,83,fill=Br_color_7[4][4])
        our_canvas.create_rectangle(195,70,208,83,fill=Br_color_7[4][5])
        our_canvas.create_rectangle(210,70,223,83,fill=Br_color_7[4][6])

        our_canvas.create_rectangle(120,85,133,98,fill=Br_color_7[5][0])
        our_canvas.create_rectangle(135,85,148,98,fill=Br_color_7[5][1])
        our_canvas.create_rectangle(150,85,163,98,fill=Br_color_7[5][2])
        our_canvas.create_rectangle(165,85,178,98,fill=Br_color_7[5][3])
        our_canvas.create_rectangle(180,85,192,98,fill=Br_color_7[5][4])
        our_canvas.create_rectangle(195,85,208,98,fill=Br_color_7[5][5])
        our_canvas.create_rectangle(210,85,223,98,fill=Br_color_7[5][6])

        our_canvas.create_rectangle(120,100,133,113,fill=Br_color_7[6][0])
        our_canvas.create_rectangle(135,100,148,113,fill=Br_color_7[6][1])
        our_canvas.create_rectangle(150,100,163,113,fill=Br_color_7[6][2])
        our_canvas.create_rectangle(165,100,178,113,fill=Br_color_7[6][3])
        our_canvas.create_rectangle(180,100,192,113,fill=Br_color_7[6][4])
        our_canvas.create_rectangle(195,100,208,113,fill=Br_color_7[6][5])
        our_canvas.create_rectangle(210,100,223,113,fill=Br_color_7[6][6])

        #L
        our_canvas.create_rectangle(10 ,120,23 ,133,fill=Lr_color_7[0][0])
        our_canvas.create_rectangle(25 ,120,38 ,133,fill=Lr_color_7[0][1])
        our_canvas.create_rectangle(40 ,120,53 ,133,fill=Lr_color_7[0][2])
        our_canvas.create_rectangle(55 ,120,68 ,133,fill=Lr_color_7[0][3])
        our_canvas.create_rectangle(70 ,120,83 ,133,fill=Lr_color_7[0][4])
        our_canvas.create_rectangle(85 ,120,98 ,133,fill=Lr_color_7[0][5])
        our_canvas.create_rectangle(100,120,113,133,fill=Lr_color_7[0][6])

        our_canvas.create_rectangle(10 ,135,23 ,148,fill=Lr_color_7[1][0])
        our_canvas.create_rectangle(25 ,135,38 ,148,fill=Lr_color_7[1][1])
        our_canvas.create_rectangle(40 ,135,53 ,148,fill=Lr_color_7[1][2])
        our_canvas.create_rectangle(55 ,135,68 ,148,fill=Lr_color_7[1][3])
        our_canvas.create_rectangle(70 ,135,83 ,148,fill=Lr_color_7[1][4])
        our_canvas.create_rectangle(85 ,135,98 ,148,fill=Lr_color_7[1][5])
        our_canvas.create_rectangle(100,135,113,148,fill=Lr_color_7[1][6])

        our_canvas.create_rectangle(10 ,150,23 ,163,fill=Lr_color_7[2][0])
        our_canvas.create_rectangle(25 ,150,38 ,163,fill=Lr_color_7[2][1])
        our_canvas.create_rectangle(40 ,150,53 ,163,fill=Lr_color_7[2][2])
        our_canvas.create_rectangle(55 ,150,68 ,163,fill=Lr_color_7[2][3])
        our_canvas.create_rectangle(70 ,150,83 ,163,fill=Lr_color_7[2][4])
        our_canvas.create_rectangle(85 ,150,98 ,163,fill=Lr_color_7[2][5])
        our_canvas.create_rectangle(100,150,113,163,fill=Lr_color_7[2][6])

        our_canvas.create_rectangle(10 ,165,23 ,178,fill=Lr_color_7[3][0])
        our_canvas.create_rectangle(25 ,165,38 ,178,fill=Lr_color_7[3][1])
        our_canvas.create_rectangle(40 ,165,53 ,178,fill=Lr_color_7[3][2])
        our_canvas.create_rectangle(55 ,165,68 ,178,fill=Lr_color_7[3][3])
        our_canvas.create_rectangle(70 ,165,83 ,178,fill=Lr_color_7[3][4])
        our_canvas.create_rectangle(85 ,165,98 ,178,fill=Lr_color_7[3][5])
        our_canvas.create_rectangle(100,165,113,178,fill=Lr_color_7[3][6])

        our_canvas.create_rectangle(10 ,180,23 ,193,fill=Lr_color_7[4][0])
        our_canvas.create_rectangle(25 ,180,38 ,193,fill=Lr_color_7[4][1])
        our_canvas.create_rectangle(40 ,180,53 ,193,fill=Lr_color_7[4][2])
        our_canvas.create_rectangle(55 ,180,68 ,193,fill=Lr_color_7[4][3])
        our_canvas.create_rectangle(70 ,180,83 ,193,fill=Lr_color_7[4][4])
        our_canvas.create_rectangle(85 ,180,98 ,193,fill=Lr_color_7[4][5])
        our_canvas.create_rectangle(100,180,113,193,fill=Lr_color_7[4][6])

        our_canvas.create_rectangle(10 ,195,23 ,208,fill=Lr_color_7[5][0])
        our_canvas.create_rectangle(25 ,195,38 ,208,fill=Lr_color_7[5][1])
        our_canvas.create_rectangle(40 ,195,53 ,208,fill=Lr_color_7[5][2])
        our_canvas.create_rectangle(55 ,195,68 ,208,fill=Lr_color_7[5][3])
        our_canvas.create_rectangle(70 ,195,83 ,208,fill=Lr_color_7[5][4])
        our_canvas.create_rectangle(85 ,195,98 ,208,fill=Lr_color_7[5][5])
        our_canvas.create_rectangle(100,195,113,208,fill=Lr_color_7[5][6])

        our_canvas.create_rectangle(10 ,210,23 ,223,fill=Lr_color_7[6][0])
        our_canvas.create_rectangle(25 ,210,38 ,223,fill=Lr_color_7[6][1])
        our_canvas.create_rectangle(40 ,210,53 ,223,fill=Lr_color_7[6][2])
        our_canvas.create_rectangle(55 ,210,68 ,223,fill=Lr_color_7[6][3])
        our_canvas.create_rectangle(70 ,210,83 ,223,fill=Lr_color_7[6][4])
        our_canvas.create_rectangle(85 ,210,98 ,223,fill=Lr_color_7[6][5])
        our_canvas.create_rectangle(100,210,113,223,fill=Lr_color_7[6][6])


        #F
        our_canvas.create_rectangle(120,120,133,133,fill=Vd_color_7[0][0])
        our_canvas.create_rectangle(135,120,148,133,fill=Vd_color_7[0][1])
        our_canvas.create_rectangle(150,120,163,133,fill=Vd_color_7[0][2])
        our_canvas.create_rectangle(165,120,178,133,fill=Vd_color_7[0][3])
        our_canvas.create_rectangle(180,120,193,133,fill=Vd_color_7[0][4])
        our_canvas.create_rectangle(195,120,208,133,fill=Vd_color_7[0][5])
        our_canvas.create_rectangle(210,120,223,133,fill=Vd_color_7[0][6])

        our_canvas.create_rectangle(120,135,133,148,fill=Vd_color_7[1][0])
        our_canvas.create_rectangle(135,135,148,148,fill=Vd_color_7[1][1])
        our_canvas.create_rectangle(150,135,163,148,fill=Vd_color_7[1][2])
        our_canvas.create_rectangle(165,135,178,148,fill=Vd_color_7[1][3])
        our_canvas.create_rectangle(180,135,193,148,fill=Vd_color_7[1][4])        
        our_canvas.create_rectangle(195,135,208,148,fill=Vd_color_7[1][5])        
        our_canvas.create_rectangle(210,135,223,148,fill=Vd_color_7[1][6])        

        our_canvas.create_rectangle(120,150,133,163,fill=Vd_color_7[2][0])
        our_canvas.create_rectangle(135,150,148,163,fill=Vd_color_7[2][1])
        our_canvas.create_rectangle(150,150,163,163,fill=Vd_color_7[2][2])
        our_canvas.create_rectangle(165,150,178,163,fill=Vd_color_7[2][3])
        our_canvas.create_rectangle(180,150,193,163,fill=Vd_color_7[2][4])
        our_canvas.create_rectangle(195,150,208,163,fill=Vd_color_7[2][5])
        our_canvas.create_rectangle(210,150,223,163,fill=Vd_color_7[2][6])

        our_canvas.create_rectangle(120,165,133,178,fill=Vd_color_7[3][0])
        our_canvas.create_rectangle(135,165,148,178,fill=Vd_color_7[3][1])
        our_canvas.create_rectangle(150,165,163,178,fill=Vd_color_7[3][2])
        our_canvas.create_rectangle(165,165,178,178,fill=Vd_color_7[3][3])
        our_canvas.create_rectangle(180,165,193,178,fill=Vd_color_7[3][4])
        our_canvas.create_rectangle(195,165,208,178,fill=Vd_color_7[3][5])
        our_canvas.create_rectangle(210,165,223,178,fill=Vd_color_7[3][6])

        our_canvas.create_rectangle(120,180,133,193,fill=Vd_color_7[4][0])
        our_canvas.create_rectangle(135,180,148,193,fill=Vd_color_7[4][1])
        our_canvas.create_rectangle(150,180,163,193,fill=Vd_color_7[4][2])
        our_canvas.create_rectangle(165,180,178,193,fill=Vd_color_7[4][3])
        our_canvas.create_rectangle(180,180,193,193,fill=Vd_color_7[4][4])
        our_canvas.create_rectangle(195,180,208,193,fill=Vd_color_7[4][5])
        our_canvas.create_rectangle(210,180,223,193,fill=Vd_color_7[4][6])

        our_canvas.create_rectangle(120,195,133,208,fill=Vd_color_7[5][0])
        our_canvas.create_rectangle(135,195,148,208,fill=Vd_color_7[5][1])
        our_canvas.create_rectangle(150,195,163,208,fill=Vd_color_7[5][2])
        our_canvas.create_rectangle(165,195,178,208,fill=Vd_color_7[5][3])
        our_canvas.create_rectangle(180,195,193,208,fill=Vd_color_7[5][4])
        our_canvas.create_rectangle(195,195,208,208,fill=Vd_color_7[5][5])
        our_canvas.create_rectangle(210,195,223,208,fill=Vd_color_7[5][6])

        our_canvas.create_rectangle(120,210,133,223,fill=Vd_color_7[6][0])
        our_canvas.create_rectangle(135,210,148,223,fill=Vd_color_7[6][1])
        our_canvas.create_rectangle(150,210,163,223,fill=Vd_color_7[6][2])
        our_canvas.create_rectangle(165,210,178,223,fill=Vd_color_7[6][3])
        our_canvas.create_rectangle(180,210,193,223,fill=Vd_color_7[6][4])
        our_canvas.create_rectangle(195,210,208,223,fill=Vd_color_7[6][5])
        our_canvas.create_rectangle(210,210,223,223,fill=Vd_color_7[6][6])

        #R
        our_canvas.create_rectangle(230,120,243,133,fill=Vm_color_7[0][0])
        our_canvas.create_rectangle(245,120,258,133,fill=Vm_color_7[0][1])
        our_canvas.create_rectangle(260,120,273,133,fill=Vm_color_7[0][2])
        our_canvas.create_rectangle(275,120,288,133,fill=Vm_color_7[0][3])
        our_canvas.create_rectangle(290,120,303,133,fill=Vm_color_7[0][4])
        our_canvas.create_rectangle(305,120,318,133,fill=Vm_color_7[0][5])
        our_canvas.create_rectangle(320,120,333,133,fill=Vm_color_7[0][6])

        our_canvas.create_rectangle(230,135,243,148,fill=Vm_color_7[1][0])
        our_canvas.create_rectangle(245,135,258,148,fill=Vm_color_7[1][1])
        our_canvas.create_rectangle(260,135,273,148,fill=Vm_color_7[1][2])
        our_canvas.create_rectangle(275,135,288,148,fill=Vm_color_7[1][3])
        our_canvas.create_rectangle(290,135,303,148,fill=Vm_color_7[1][4])
        our_canvas.create_rectangle(305,135,318,148,fill=Vm_color_7[1][5])
        our_canvas.create_rectangle(320,135,333,148,fill=Vm_color_7[1][6])

        our_canvas.create_rectangle(230,150,243,163,fill=Vm_color_7[2][0])
        our_canvas.create_rectangle(245,150,258,163,fill=Vm_color_7[2][1])
        our_canvas.create_rectangle(260,150,273,163,fill=Vm_color_7[2][2])
        our_canvas.create_rectangle(275,150,288,163,fill=Vm_color_7[2][3])
        our_canvas.create_rectangle(290,150,303,163,fill=Vm_color_7[2][4])
        our_canvas.create_rectangle(305,150,318,163,fill=Vm_color_7[2][5])
        our_canvas.create_rectangle(320,150,333,163,fill=Vm_color_7[2][6])

        our_canvas.create_rectangle(230,165,243,178,fill=Vm_color_7[3][0])
        our_canvas.create_rectangle(245,165,258,178,fill=Vm_color_7[3][1])
        our_canvas.create_rectangle(260,165,273,178,fill=Vm_color_7[3][2])
        our_canvas.create_rectangle(275,165,288,178,fill=Vm_color_7[3][3])
        our_canvas.create_rectangle(290,165,303,178,fill=Vm_color_7[3][4])
        our_canvas.create_rectangle(305,165,318,178,fill=Vm_color_7[3][5])
        our_canvas.create_rectangle(320,165,333,178,fill=Vm_color_7[3][6])

        our_canvas.create_rectangle(230,180,243,193,fill=Vm_color_7[4][0])
        our_canvas.create_rectangle(245,180,258,193,fill=Vm_color_7[4][1])
        our_canvas.create_rectangle(260,180,273,193,fill=Vm_color_7[4][2])
        our_canvas.create_rectangle(275,180,288,193,fill=Vm_color_7[4][3])
        our_canvas.create_rectangle(290,180,303,193,fill=Vm_color_7[4][4])
        our_canvas.create_rectangle(305,180,318,193,fill=Vm_color_7[4][5])
        our_canvas.create_rectangle(320,180,333,193,fill=Vm_color_7[4][6])

        our_canvas.create_rectangle(230,195,243,208,fill=Vm_color_7[5][0])
        our_canvas.create_rectangle(245,195,258,208,fill=Vm_color_7[5][1])
        our_canvas.create_rectangle(260,195,273,208,fill=Vm_color_7[5][2])
        our_canvas.create_rectangle(275,195,288,208,fill=Vm_color_7[5][3])
        our_canvas.create_rectangle(290,195,303,208,fill=Vm_color_7[5][4])
        our_canvas.create_rectangle(305,195,318,208,fill=Vm_color_7[5][5])
        our_canvas.create_rectangle(320,195,333,208,fill=Vm_color_7[5][6])

        our_canvas.create_rectangle(230,210,243,223,fill=Vm_color_7[6][0])
        our_canvas.create_rectangle(245,210,258,223,fill=Vm_color_7[6][1])
        our_canvas.create_rectangle(260,210,273,223,fill=Vm_color_7[6][2])
        our_canvas.create_rectangle(275,210,288,223,fill=Vm_color_7[6][3])
        our_canvas.create_rectangle(290,210,303,223,fill=Vm_color_7[6][4])
        our_canvas.create_rectangle(305,210,318,223,fill=Vm_color_7[6][5])
        our_canvas.create_rectangle(320,210,333,223,fill=Vm_color_7[6][6])


        #B
        our_canvas.create_rectangle(340,120,353,133,fill=Az_color_7[0][0])
        our_canvas.create_rectangle(355,120,368,133,fill=Az_color_7[0][1])
        our_canvas.create_rectangle(370,120,383,133,fill=Az_color_7[0][2])
        our_canvas.create_rectangle(385,120,398,133,fill=Az_color_7[0][3])
        our_canvas.create_rectangle(400,120,413,133,fill=Az_color_7[0][4])
        our_canvas.create_rectangle(415,120,428,133,fill=Az_color_7[0][5])
        our_canvas.create_rectangle(430,120,443,133,fill=Az_color_7[0][6])

        our_canvas.create_rectangle(340,135,353,148,fill=Az_color_7[1][0])
        our_canvas.create_rectangle(355,135,368,148,fill=Az_color_7[1][1])
        our_canvas.create_rectangle(370,135,383,148,fill=Az_color_7[1][2])
        our_canvas.create_rectangle(385,135,398,148,fill=Az_color_7[1][3])
        our_canvas.create_rectangle(400,135,413,148,fill=Az_color_7[1][4])
        our_canvas.create_rectangle(415,135,428,148,fill=Az_color_7[1][5])
        our_canvas.create_rectangle(430,135,443,148,fill=Az_color_7[1][6])

        our_canvas.create_rectangle(340,150,353,163,fill=Az_color_7[2][0])
        our_canvas.create_rectangle(355,150,368,163,fill=Az_color_7[2][1])
        our_canvas.create_rectangle(370,150,383,163,fill=Az_color_7[2][2])
        our_canvas.create_rectangle(385,150,398,163,fill=Az_color_7[2][3])
        our_canvas.create_rectangle(400,150,413,163,fill=Az_color_7[2][4])
        our_canvas.create_rectangle(415,150,428,163,fill=Az_color_7[2][5])
        our_canvas.create_rectangle(430,150,443,163,fill=Az_color_7[2][6])

        our_canvas.create_rectangle(340,165,353,178,fill=Az_color_7[3][0])
        our_canvas.create_rectangle(355,165,368,178,fill=Az_color_7[3][1])
        our_canvas.create_rectangle(370,165,383,178,fill=Az_color_7[3][2])
        our_canvas.create_rectangle(385,165,398,178,fill=Az_color_7[3][3])
        our_canvas.create_rectangle(400,165,413,178,fill=Az_color_7[3][4])
        our_canvas.create_rectangle(415,165,428,178,fill=Az_color_7[3][5])
        our_canvas.create_rectangle(430,165,443,178,fill=Az_color_7[3][6])

        our_canvas.create_rectangle(340,180,353,193,fill=Az_color_7[4][0])
        our_canvas.create_rectangle(355,180,368,193,fill=Az_color_7[4][1])
        our_canvas.create_rectangle(370,180,383,193,fill=Az_color_7[4][2])
        our_canvas.create_rectangle(385,180,398,193,fill=Az_color_7[4][3])
        our_canvas.create_rectangle(400,180,413,193,fill=Az_color_7[4][4])
        our_canvas.create_rectangle(415,180,428,193,fill=Az_color_7[4][5])
        our_canvas.create_rectangle(430,180,443,193,fill=Az_color_7[4][6])

        our_canvas.create_rectangle(340,195,353,208,fill=Az_color_7[5][0])
        our_canvas.create_rectangle(355,195,368,208,fill=Az_color_7[5][1])
        our_canvas.create_rectangle(370,195,383,208,fill=Az_color_7[5][2])
        our_canvas.create_rectangle(385,195,398,208,fill=Az_color_7[5][3])
        our_canvas.create_rectangle(400,195,413,208,fill=Az_color_7[5][4])
        our_canvas.create_rectangle(415,195,428,208,fill=Az_color_7[5][5])
        our_canvas.create_rectangle(430,195,443,208,fill=Az_color_7[5][6])

        our_canvas.create_rectangle(340,210,353,223,fill=Az_color_7[6][0])
        our_canvas.create_rectangle(355,210,368,223,fill=Az_color_7[6][1])
        our_canvas.create_rectangle(370,210,383,223,fill=Az_color_7[6][2])
        our_canvas.create_rectangle(385,210,398,223,fill=Az_color_7[6][3])
        our_canvas.create_rectangle(400,210,413,223,fill=Az_color_7[6][4])
        our_canvas.create_rectangle(415,210,428,223,fill=Az_color_7[6][5])
        our_canvas.create_rectangle(430,210,443,223,fill=Az_color_7[6][6])

        #D
        our_canvas.create_rectangle(120,230,133,243,fill=Am_color_7[0][0])
        our_canvas.create_rectangle(135,230,148,243,fill=Am_color_7[0][1])
        our_canvas.create_rectangle(150,230,163,243,fill=Am_color_7[0][2])
        our_canvas.create_rectangle(165,230,178,243,fill=Am_color_7[0][3])
        our_canvas.create_rectangle(180,230,193,243,fill=Am_color_7[0][4])
        our_canvas.create_rectangle(195,230,208,243,fill=Am_color_7[0][5])
        our_canvas.create_rectangle(210,230,223,243,fill=Am_color_7[0][6])

        our_canvas.create_rectangle(120,245,133,258,fill=Am_color_7[1][0])
        our_canvas.create_rectangle(135,245,148,258,fill=Am_color_7[1][1])
        our_canvas.create_rectangle(150,245,163,258,fill=Am_color_7[1][2])
        our_canvas.create_rectangle(165,245,178,258,fill=Am_color_7[1][3])
        our_canvas.create_rectangle(180,245,193,258,fill=Am_color_7[1][4])
        our_canvas.create_rectangle(195,245,208,258,fill=Am_color_7[1][5])
        our_canvas.create_rectangle(210,245,223,258,fill=Am_color_7[1][6])

        our_canvas.create_rectangle(120,260,133,273,fill=Am_color_7[2][0])
        our_canvas.create_rectangle(135,260,148,273,fill=Am_color_7[2][1])
        our_canvas.create_rectangle(150,260,163,273,fill=Am_color_7[2][2])
        our_canvas.create_rectangle(165,260,178,273,fill=Am_color_7[2][3])
        our_canvas.create_rectangle(180,260,193,273,fill=Am_color_7[2][4])
        our_canvas.create_rectangle(195,260,208,273,fill=Am_color_7[2][5])
        our_canvas.create_rectangle(210,260,223,273,fill=Am_color_7[2][6])

        our_canvas.create_rectangle(120,275,133,288,fill=Am_color_7[3][0])
        our_canvas.create_rectangle(135,275,148,288,fill=Am_color_7[3][1])
        our_canvas.create_rectangle(150,275,163,288,fill=Am_color_7[3][2])
        our_canvas.create_rectangle(165,275,178,288,fill=Am_color_7[3][3])
        our_canvas.create_rectangle(180,275,193,288,fill=Am_color_7[3][4])
        our_canvas.create_rectangle(195,275,208,288,fill=Am_color_7[3][5])
        our_canvas.create_rectangle(210,275,223,288,fill=Am_color_7[3][6])

        our_canvas.create_rectangle(120,290,133,303,fill=Am_color_7[4][0])
        our_canvas.create_rectangle(135,290,148,303,fill=Am_color_7[4][1])
        our_canvas.create_rectangle(150,290,163,303,fill=Am_color_7[4][2])
        our_canvas.create_rectangle(165,290,178,303,fill=Am_color_7[4][3])
        our_canvas.create_rectangle(180,290,193,303,fill=Am_color_7[4][4])
        our_canvas.create_rectangle(195,290,208,303,fill=Am_color_7[4][5])
        our_canvas.create_rectangle(210,290,223,303,fill=Am_color_7[4][6])

        our_canvas.create_rectangle(120,305,133,318,fill=Am_color_7[5][0])
        our_canvas.create_rectangle(135,305,148,318,fill=Am_color_7[5][1])
        our_canvas.create_rectangle(150,305,163,318,fill=Am_color_7[5][2])
        our_canvas.create_rectangle(165,305,178,318,fill=Am_color_7[5][3])
        our_canvas.create_rectangle(180,305,193,318,fill=Am_color_7[5][4])
        our_canvas.create_rectangle(195,305,208,318,fill=Am_color_7[5][5])
        our_canvas.create_rectangle(210,305,223,318,fill=Am_color_7[5][6])

        our_canvas.create_rectangle(120,320,133,333,fill=Am_color_7[6][0])
        our_canvas.create_rectangle(135,320,148,333,fill=Am_color_7[6][1])
        our_canvas.create_rectangle(150,320,163,333,fill=Am_color_7[6][2])
        our_canvas.create_rectangle(165,320,178,333,fill=Am_color_7[6][3])
        our_canvas.create_rectangle(180,320,193,333,fill=Am_color_7[6][4])
        our_canvas.create_rectangle(195,320,208,333,fill=Am_color_7[6][5])
        our_canvas.create_rectangle(210,320,223,333,fill=Am_color_7[6][6])
        
    elif cube == "pyraminx":            

        Vd_color_pyra = np.where(Vd_pyra != 1, Vd_color_pyra,"red")
        Vm_color_pyra = np.where(Vm_pyra != 1, Vm_color_pyra,"red")
        Az_color_pyra = np.where(Az_pyra != 1, Az_color_pyra,"red")
        Am_color_pyra = np.where(Am_pyra != 1, Am_color_pyra,"red")  
        
        Vd_color_pyra = np.where(Vd_pyra != 2, Vd_color_pyra,"green")
        Vm_color_pyra = np.where(Vm_pyra != 2, Vm_color_pyra,"green")
        Az_color_pyra = np.where(Az_pyra != 2, Az_color_pyra,"green")
        Am_color_pyra = np.where(Am_pyra != 2, Am_color_pyra,"green")

        Vd_color_pyra = np.where(Vd_pyra != 3, Vd_color_pyra,"blue")
        Vm_color_pyra = np.where(Vm_pyra != 3, Vm_color_pyra,"blue")
        Az_color_pyra = np.where(Az_pyra != 3, Az_color_pyra,"blue")
        Am_color_pyra = np.where(Am_pyra != 3, Am_color_pyra,"blue") 
               
        Vd_color_pyra = np.where(Vd_pyra != 4, Vd_color_pyra,"yellow")
        Vm_color_pyra = np.where(Vm_pyra != 4, Vm_color_pyra,"yellow")
        Az_color_pyra = np.where(Az_pyra != 4, Az_color_pyra,"yellow")
        Am_color_pyra = np.where(Am_pyra != 4, Am_color_pyra,"yellow")      

         

        #L
        our_canvas.create_polygon(10,10,50 ,10,30 ,45,fill=Vm_color_pyra[0][0])        
        our_canvas.create_polygon(52,10,92 ,10,72 ,45,fill=Vm_color_pyra[0][2])
        our_canvas.create_polygon(94,10,134,10,114,45,fill=Vm_color_pyra[0][4])
        
        our_canvas.create_polygon(31,46,71 ,46,51,11,fill=Vm_color_pyra[0][1])
        our_canvas.create_polygon(73,46,113,46,93,11,fill=Vm_color_pyra[0][3])


        our_canvas.create_polygon(30,48,71 ,48,51,83,fill=Vm_color_pyra[1][1])
        our_canvas.create_polygon(73,48,113,48,93,83,fill=Vm_color_pyra[1][3])

        our_canvas.create_polygon(52,84,92,84,72,48,fill=Vm_color_pyra[1][2])

        our_canvas.create_polygon(52,86,92,86,72,119,fill=Vm_color_pyra[2][2])
               
        
        #R
        our_canvas.create_polygon(154,10,194,10,174,45,fill=Az_color_pyra[0][0])        
        our_canvas.create_polygon(196,10,236,10,216,45,fill=Az_color_pyra[0][2])        
        our_canvas.create_polygon(238,10,278,10,258,45,fill=Az_color_pyra[0][4])        

        our_canvas.create_polygon(175,46,215,46,195,11,fill=Az_color_pyra[0][1])        
        our_canvas.create_polygon(217,46,257,46,237,11,fill=Az_color_pyra[0][3])    



        our_canvas.create_polygon(175,48,215,48,195,83,fill=Az_color_pyra[1][1])        
        our_canvas.create_polygon(217,48,257,48,237,83,fill=Az_color_pyra[1][3])  

        our_canvas.create_polygon(196,84,236,84,216,49,fill=Az_color_pyra[1][2])  

        our_canvas.create_polygon(196,86,236,86,216,119,fill=Az_color_pyra[2][2])  

        
        #F        

        our_canvas.create_polygon(124,45,164,45,144,10,fill=Vd_color_pyra[0][2]) 


        our_canvas.create_polygon(124,48,164,48,144,83,fill=Vd_color_pyra[1][2])  

        our_canvas.create_polygon(103,84,143,84,123,48,fill=Vd_color_pyra[1][1])  
        our_canvas.create_polygon(145,84,185,84,165,48,fill=Vd_color_pyra[1][3])  

        our_canvas.create_polygon(103,86,143,86,123,119,fill=Vd_color_pyra[2][1])  
        our_canvas.create_polygon(145,86,185,86,165,119,fill=Vd_color_pyra[2][3])  

        our_canvas.create_polygon(81 ,120,121,120,101,87,fill=Vd_color_pyra[2][0])  
        our_canvas.create_polygon(124,120,164,120,144,87,fill=Vd_color_pyra[2][2])  
        our_canvas.create_polygon(166,120,206,120,186,87,fill=Vd_color_pyra[2][4])  

       
        #D
        our_canvas.create_polygon(81,130,121,130,101,165,fill=Am_color_pyra[0][0])  
        our_canvas.create_polygon(124,130,164,130,144,165,fill=Am_color_pyra[0][2])  
        our_canvas.create_polygon(166,130,206,130,186,165,fill=Am_color_pyra[0][4]) 

        our_canvas.create_polygon(103,165,143,165,123,131,fill=Am_color_pyra[0][1])  
        our_canvas.create_polygon(145,165,185,165,165,131,fill=Am_color_pyra[0][3])  


        our_canvas.create_polygon(103,167,143,167,123,201,fill=Am_color_pyra[1][1])  
        our_canvas.create_polygon(145,167,185,167,165,201,fill=Am_color_pyra[1][3])  

        our_canvas.create_polygon(124,201,164,201,144,167,fill=Am_color_pyra[1][2])  

        our_canvas.create_polygon(124,203,164,203,144,238,fill=Am_color_pyra[2][2]) 



    elif cube == "megaminx":
        pass
    elif cube == "skewb":
        pass
    elif cube == "clock":
        pass


def next_scramble():
    ch_event = eventos.get()
    
    if ch_event == '2x2':
        scrambler_2x2()
    elif ch_event == '3x3':
        scrambler_3x3()
    elif ch_event == '4x4':
        scrambler_4x4()
    elif ch_event == '5x5':
        scrambler_5x5()
    elif ch_event == '6x6':
        scrambler_6x6()
    elif ch_event == '7x7':
        scrambler_7x7()
    elif ch_event == 'pyraminx':
        scrambler_pyraminx()
    elif ch_event == 'megaminx':
        scrambler_megaminx()
    elif ch_event == 'skewb':
        scrambler_skewb()
    elif ch_event == 'clock':
        scrambler_clock()

def scrambler_2x2():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0    

    sum_turns = []
    for i in range(12):

        while accepted == 0:
            n_move = random.randrange(1,10,1)
            # print(n_move)

            if (n_move == 1 or n_move == 2 or n_move == 3) and (pr_move == 1 or pr_move == 2 or pr_move == 3):
                accepted = 0
            elif (n_move == 4 or n_move == 5 or n_move == 6) and (pr_move == 4 or pr_move == 5 or pr_move == 6):
                accepted = 0
            elif (n_move == 7 or n_move == 8 or n_move == 9) and (pr_move == 7 or pr_move == 8 or pr_move == 9):
                accepted = 0            
            else:
                accepted = 1

        if n_move == 1:
            turn = "R"
            
        elif n_move == 2:
            turn = "R'"
            
        elif n_move == 3:
            turn = "R2"
            
        elif n_move == 4:
            turn = "U"
            
        elif n_move == 5:
            turn = "U'"
           
        elif n_move == 6:
            turn = "U2"
            
        elif n_move == 7:
            turn = "F"
            
        elif n_move == 8:
            turn = "F'"
            
        elif n_move == 9:
            turn = "F2"
            
        
        
        
        sum_turns.append(turn)
        pr_move = n_move
        turn_draw("2x2",turn)
        accepted = 0
    # print(actual_scramble)    
    
    actual_scramble.set(" ".join(sum_turns))    # print_scramble.update() 
    draw_scramble("2x2")

def scrambler_3x3():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0

    global flag_R
    global flag_L
    global flag_U
    global flag_D
    global flag_F
    global flag_B

    sum_turns = []
    for i in range(20):

        while accepted == 0:
            n_move = random.randrange(1, 19,1)
            # print(n_move)            


            if (n_move == 1 or n_move == 2 or n_move == 3) and (pr_move == 1 or pr_move == 2 or pr_move == 3 or flag_R == 1):
                accepted = 0
            elif (n_move == 4 or n_move == 5 or n_move == 6) and (pr_move == 4 or pr_move == 5 or pr_move == 6 or flag_L == 1):
                accepted = 0
            elif (n_move == 7 or n_move == 8 or n_move == 9) and (pr_move == 7 or pr_move == 8 or pr_move == 9 or flag_U == 1):
                accepted = 0
            elif (n_move == 10 or n_move == 11 or n_move == 12) and (pr_move == 10 or pr_move == 11 or pr_move == 12 or flag_D == 1):
                accepted = 0
            elif (n_move == 13 or n_move == 14 or n_move == 15) and (pr_move == 13 or pr_move == 14 or pr_move == 15 or flag_F == 1):
                accepted = 0
            elif (n_move == 16 or n_move == 17 or n_move == 18) and (pr_move == 16 or pr_move == 17 or pr_move == 18 or flag_B == 1):
                accepted = 0
            else:
                accepted = 1

        if n_move == 1:
            turn = "R"            
            
        elif n_move == 2:
            turn = "R'"            
            
        elif n_move == 3:
            turn = "R2"            
            
        elif n_move == 4:
            turn = "L"            
            
        elif n_move == 5:
            turn = "L'"            
            
        elif n_move == 6:
            turn = "L2"            
            
        elif n_move == 7:
            turn = "U"            
            
        elif n_move == 8:
            turn = "U'"            
            
        elif n_move == 9:
            turn = "U2"            
            
        elif n_move == 10:
            turn = "D"            
            
        elif n_move == 11:
            turn = "D'"            
            
        elif n_move == 12:
            turn = "D2"            
           
        elif n_move == 13:
            turn = "F"            
            
        elif n_move == 14:
            turn = "F'"            
            
        elif n_move == 15:
            turn = "F2"            
            
        elif n_move == 16:
            turn = "B"            
            
        elif n_move == 17:
            turn = "B'"            
            
        elif n_move == 18:
            turn = "B2"        

        turn_draw("3x3",turn)
        define_flags(n_move)

        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0

    # print(actual_scramble)    
    reset_flags()
    # reset_draw()
    
    
    actual_scramble.set(" ".join(sum_turns))
    draw_scramble("3x3")
    

def scrambler_4x4():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0
    global flag_R
    global flag_L
    global flag_U
    global flag_D
    global flag_F
    global flag_B

    global flag_Rw    
    global flag_Uw    
    global flag_Fw
    

    sum_turns = []      

    for i in range(44):

        while accepted == 0:
            n_move = random.randrange(1, 34,1)
            # print(n_move)            


            if (n_move == 1 or n_move == 2 or n_move == 3) and (pr_move == 1 or pr_move == 2 or pr_move == 3 or flag_R == 1):
                accepted = 0
            elif (n_move == 4 or n_move == 5 or n_move == 6) and (pr_move == 4 or pr_move == 5 or pr_move == 6 or flag_L == 1):
                accepted = 0
            elif (n_move == 7 or n_move == 8 or n_move == 9) and (pr_move == 7 or pr_move == 8 or pr_move == 9 or flag_U == 1):
                accepted = 0
            elif (n_move == 10 or n_move == 11 or n_move == 12) and (pr_move == 10 or pr_move == 11 or pr_move == 12 or flag_D == 1):
                accepted = 0
            elif (n_move == 13 or n_move == 14 or n_move == 15) and (pr_move == 13 or pr_move == 14 or pr_move == 15 or flag_F == 1):
                accepted = 0
            elif (n_move == 16 or n_move == 17 or n_move == 18) and (pr_move == 16 or pr_move == 17 or pr_move == 18 or flag_B == 1):
                accepted = 0
            elif (n_move == 19 or n_move == 20 or n_move == 21) and (pr_move == 19 or pr_move == 20 or pr_move == 21 or flag_Rw == 1):
                accepted = 0
            elif (n_move == 25 or n_move == 26 or n_move == 27) and (pr_move == 25 or pr_move == 26 or pr_move == 27 or flag_Uw == 1):
                accepted = 0
            elif (n_move == 31 or n_move == 32 or n_move == 33) and (pr_move == 31 or pr_move == 32 or pr_move == 33 or flag_Fw == 1):
                accepted = 0
            elif (n_move == 22 or n_move == 23 or n_move == 24 or n_move == 28 or n_move == 29 or n_move == 30):
                accepted = 0           
            else:
                accepted = 1


        if n_move == 1:
            turn = "R"
           
        elif n_move == 2:
            turn = "R'"
            
        elif n_move == 3:
            turn = "R2"
            
        elif n_move == 4:
            turn = "L"
           
        elif n_move == 5:
            turn = "L'"
            
        elif n_move == 6:
            turn = "L2"
            
        elif n_move == 7:
            turn = "U"
           
        elif n_move == 8:
            turn = "U'"
            
        elif n_move == 9:
            turn = "U2"
           
        elif n_move == 10:
            turn = "D"
            
        elif n_move == 11:
            turn = "D'"
           
        elif n_move == 12:
            turn = "D2"
            
        elif n_move == 13:
            turn = "F"
           
        elif n_move == 14:
            turn = "F'"
            
        elif n_move == 15:
            turn = "F2"
           
        elif n_move == 16:
            turn = "B"
            
        elif n_move == 17:
            turn = "B'"
            
        elif n_move == 18:
            turn = "B2"

           
        if n_move == 19:
            turn = "Rw"
            
        elif n_move == 20:
            turn = "Rw'"
            
        elif n_move == 21:
            turn = "Rw2"                   
            
        elif n_move == 25:
            turn = "Uw"
            
        elif n_move == 26:
            turn = "Uw'"
            
        elif n_move == 27:
            turn = "Uw2"        

        elif n_move == 31:
            turn = "Fw"
            
        elif n_move == 32:
            turn = "Fw'"
            
        elif n_move == 33:
            turn = "Fw2"       
        
        define_flags(n_move)
        turn_draw("4x4",turn)
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0

    reset_flags()
    
    # turn_draw("4x4","Fw")
    
    draw_scramble("4x4")
   
    # print(actual_scramble)    
    
    actual_scramble.set(" ".join(sum_turns))
    
    
def scrambler_5x5():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0
    global flag_R
    global flag_L
    global flag_U
    global flag_D
    global flag_F
    global flag_B

    global flag_Rw
    global flag_Lw
    global flag_Uw
    global flag_Dw
    global flag_Fw
    global flag_Bw

    sum_turns = []      

    for i in range(60):

        while accepted == 0:
            n_move = random.randrange(1, 37,1)
            # print(n_move)            


            if (n_move == 1 or n_move == 2 or n_move == 3) and (pr_move == 1 or pr_move == 2 or pr_move == 3 or flag_R == 1):
                accepted = 0
            elif (n_move == 4 or n_move == 5 or n_move == 6) and (pr_move == 4 or pr_move == 5 or pr_move == 6 or flag_L == 1):
                accepted = 0
            elif (n_move == 7 or n_move == 8 or n_move == 9) and (pr_move == 7 or pr_move == 8 or pr_move == 9 or flag_U == 1):
                accepted = 0
            elif (n_move == 10 or n_move == 11 or n_move == 12) and (pr_move == 10 or pr_move == 11 or pr_move == 12 or flag_D == 1):
                accepted = 0
            elif (n_move == 13 or n_move == 14 or n_move == 15) and (pr_move == 13 or pr_move == 14 or pr_move == 15 or flag_F == 1):
                accepted = 0
            elif (n_move == 16 or n_move == 17 or n_move == 18) and (pr_move == 16 or pr_move == 17 or pr_move == 18 or flag_B == 1):
                accepted = 0
            elif (n_move == 19 or n_move == 20 or n_move == 21) and (pr_move == 19 or pr_move == 20 or pr_move == 21 or flag_Rw == 1):
                accepted = 0
            elif (n_move == 22 or n_move == 23 or n_move == 24) and (pr_move == 22 or pr_move == 23 or pr_move == 24 or flag_Lw == 1):
                accepted = 0
            elif (n_move == 25 or n_move == 26 or n_move == 27) and (pr_move == 25 or pr_move == 26 or pr_move == 27 or flag_Uw == 1):
                accepted = 0
            elif (n_move == 28 or n_move == 29 or n_move == 30) and (pr_move == 28 or pr_move == 29 or pr_move == 30 or flag_Dw == 1):
                accepted = 0
            elif (n_move == 31 or n_move == 32 or n_move == 33) and (pr_move == 31 or pr_move == 32 or pr_move == 33 or flag_Fw == 1):
                accepted = 0
            elif (n_move == 34 or n_move == 35 or n_move == 36) and (pr_move == 34 or pr_move == 35 or pr_move == 36 or flag_Bw == 1):
                accepted = 0
            else:
                accepted = 1


        if n_move == 1:
            turn = "R"
           
        elif n_move == 2:
            turn = "R'"
            
        elif n_move == 3:
            turn = "R2"
            
        elif n_move == 4:
            turn = "L"
           
        elif n_move == 5:
            turn = "L'"
            
        elif n_move == 6:
            turn = "L2"
            
        elif n_move == 7:
            turn = "U"
           
        elif n_move == 8:
            turn = "U'"
            
        elif n_move == 9:
            turn = "U2"
           
        elif n_move == 10:
            turn = "D"
            
        elif n_move == 11:
            turn = "D'"
           
        elif n_move == 12:
            turn = "D2"
            
        elif n_move == 13:
            turn = "F"
           
        elif n_move == 14:
            turn = "F'"
            
        elif n_move == 15:
            turn = "F2"
           
        elif n_move == 16:
            turn = "B"
            
        elif n_move == 17:
            turn = "B'"
            
        elif n_move == 18:
            turn = "B2"

           
        if n_move == 19:
            turn = "Rw"
            
        elif n_move == 20:
            turn = "Rw'"
            
        elif n_move == 21:
            turn = "Rw2"            

        elif n_move == 22:
            turn = "Lw"
            
        elif n_move == 23:
            turn = "Lw'"
            
        elif n_move == 24:
            turn = "Lw2"
            
        elif n_move == 25:
            turn = "Uw"
            
        elif n_move == 26:
            turn = "Uw'"
            
        elif n_move == 27:
            turn = "Uw2"            

        elif n_move == 28:
            turn = "Dw"
            
        elif n_move == 29:
            turn = "Dw'"
           
        elif n_move == 30:
            turn = "Dw2"           

        elif n_move == 31:
            turn = "Fw"
            
        elif n_move == 32:
            turn = "Fw'"
            
        elif n_move == 33:
            turn = "Fw2"            

        elif n_move == 34:
            turn = "Bw"
            
        elif n_move == 35:
            turn = "Bw'"
            
        elif n_move == 36:
            turn = "Bw2"    
        
        define_flags(n_move)
        turn_draw("5x5",turn)
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0

    reset_flags()    
    # turn_draw("5x5","R")
    draw_scramble("5x5")
    # print(actual_scramble)    
    
    actual_scramble.set(" ".join(sum_turns))
    

def scrambler_6x6():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    accepted = 0

    global actual_scramble 
    
    global flag_R
    global flag_L
    global flag_U
    global flag_D
    global flag_F
    global flag_B

    global flag_Rw
    global flag_Lw
    global flag_Uw
    global flag_Dw
    global flag_Fw
    global flag_Bw

    global flag_3Rw
    global flag_3Lw
    global flag_3Uw
    global flag_3Dw
    global flag_3Fw
    global flag_3Bw

    global flag_7_event

    sum_turns = []

    if flag_7_event == 1:
        movs = 100
    else:
        movs = 80


    for i in range(movs):

        while accepted == 0:
            n_move = random.randrange(1, 55,1)
            # print(n_move)

            if (n_move == 1 or n_move == 2 or n_move == 3) and (pr_move == 1 or pr_move == 2 or pr_move == 3 or flag_R == 1):
                accepted = 0
            elif (n_move == 4 or n_move == 5 or n_move == 6) and (pr_move == 4 or pr_move == 5 or pr_move == 6 or flag_L == 1):
                accepted = 0
            elif (n_move == 7 or n_move == 8 or n_move == 9) and (pr_move == 7 or pr_move == 8 or pr_move == 9 or flag_U == 1):
                accepted = 0
            elif (n_move == 10 or n_move == 11 or n_move == 12) and (pr_move == 10 or pr_move == 11 or pr_move == 12 or flag_D == 1):
                accepted = 0
            elif (n_move == 13 or n_move == 14 or n_move == 15) and (pr_move == 13 or pr_move == 14 or pr_move == 15 or flag_F == 1):
                accepted = 0
            elif (n_move == 16 or n_move == 17 or n_move == 18) and (pr_move == 16 or pr_move == 17 or pr_move == 18 or flag_B == 1):
                accepted = 0

            elif (n_move == 19 or n_move == 20 or n_move == 21) and (pr_move == 19 or pr_move == 20 or pr_move == 21 or flag_Rw == 1):
                accepted = 0
            elif (n_move == 22 or n_move == 23 or n_move == 24) and (pr_move == 22 or pr_move == 23 or pr_move == 24 or flag_Lw == 1):
                accepted = 0
            elif (n_move == 25 or n_move == 26 or n_move == 27) and (pr_move == 25 or pr_move == 26 or pr_move == 27 or flag_Uw == 1):
                accepted = 0
            elif (n_move == 28 or n_move == 29 or n_move == 30) and (pr_move == 28 or pr_move == 29 or pr_move == 30 or flag_Dw == 1):
                accepted = 0
            elif (n_move == 31 or n_move == 32 or n_move == 33) and (pr_move == 31 or pr_move == 32 or pr_move == 33 or flag_Fw == 1):
                accepted = 0
            elif (n_move == 34 or n_move == 35 or n_move == 36) and (pr_move == 34 or pr_move == 35 or pr_move == 36 or flag_Bw == 1):
                accepted = 0

            elif (n_move == 37 or n_move == 38 or n_move == 39) and (pr_move == 37 or pr_move == 38 or pr_move == 39 or flag_3Rw == 1):
                accepted = 0
            elif (n_move == 40 or n_move == 41 or n_move == 42) and (pr_move == 40 or pr_move == 41 or pr_move == 42 or flag_3Lw == 1):
                accepted = 0
            elif (n_move == 43 or n_move == 44 or n_move == 45) and (pr_move == 43 or pr_move == 44 or pr_move == 45 or flag_3Uw == 1):
                accepted = 0
            elif (n_move == 46 or n_move == 47 or n_move == 48) and (pr_move == 46 or pr_move == 47 or pr_move == 48 or flag_3Dw == 1):
                accepted = 0
            elif (n_move == 49 or n_move == 50 or n_move == 51) and (pr_move == 49 or pr_move == 50 or pr_move == 51 or flag_3Fw == 1):
                accepted = 0
            elif (n_move == 52 or n_move == 53 or n_move == 54) and (pr_move == 52 or pr_move == 53 or pr_move == 54 or flag_3Bw == 1):
                accepted = 0
            else:
                accepted = 1

        if n_move == 1:
            turn = "R"
            
        elif n_move == 2:
            turn = "R'"
            
        elif n_move == 3:
            turn = "R2"
            
        elif n_move == 4:
            turn = "L"
            
        elif n_move == 5:
            turn = "L'"
           
        elif n_move == 6:
            turn = "L2"
            
        elif n_move == 7:
            turn = "U"
            
        elif n_move == 8:
            turn = "U'"
            
        elif n_move == 9:
            turn = "U2"
            
        elif n_move == 10:
            turn = "D"
            
        elif n_move == 11:
            turn = "D'"
           
        elif n_move == 12:
            turn = "D2"
           
        elif n_move == 13:
            turn = "F"
            
        elif n_move == 14:
            turn = "F'"
            
        elif n_move == 15:
            turn = "F2"
           
        elif n_move == 16:
            turn = "B"
           
        elif n_move == 17:
            turn = "B'"
           
        elif n_move == 18:
            turn = "B2"

        if n_move == 19:
            turn = "Rw"
           
        elif n_move == 20:
            turn = "Rw'"
            
        elif n_move == 21:
            turn = "Rw2"            

        elif n_move == 22:
            turn = "Lw"
            
        elif n_move == 23:
            turn = "Lw'"
           
        elif n_move == 24:
            turn = "Lw2"

        elif n_move == 25:
            turn = "Uw"
            
        elif n_move == 26:
            turn = "Uw'"
           
        elif n_move == 27:
            turn = "Uw2"            

        elif n_move == 28:
            turn = "Dw"
            
        elif n_move == 29:
            turn = "Dw'"
           
        elif n_move == 30:
            turn = "Dw2"           

        elif n_move == 31:
            turn = "Fw"
            
        elif n_move == 32:
            turn = "Fw'"
            
        elif n_move == 33:
            turn = "Fw2"           

        elif n_move == 34:
            turn = "Bw"
            
        elif n_move == 35:
            turn = "Bw'"
            
        elif n_move == 36:
            turn = "Bw2"  


        if n_move == 37:
            turn = "3Rw"
            
        elif n_move == 38:
            turn = "3Rw'"
            
        elif n_move == 39:
            turn = "3Rw2"            

        elif n_move == 40:
            turn = "3Lw"
            
        elif n_move == 41:
            turn = "3Lw'"
           
        elif n_move == 42:
            turn = "3Lw2"           

        elif n_move == 43:
            turn = "3Uw"
            
        elif n_move == 44:
            turn = "3Uw'"
           
        elif n_move == 45:
            turn = "3Uw2"
           
        elif n_move == 46:
            turn = "3Dw"
            
        elif n_move == 47:
            turn = "3Dw'"
            
        elif n_move == 48:
            turn = "3Dw2"
           
        elif n_move == 49:
            turn = "3Fw"
            
        elif n_move == 50:
            turn = "3Fw'"
           
        elif n_move == 51:
            turn = "3Fw2"
           
        elif n_move == 52:
            turn = "3Bw"
            
        elif n_move == 53:
            turn = "3Bw'"
            
        elif n_move == 54:
            turn = "3Bw2"    
        
        define_flags(n_move)
        print(turn)
        turn_draw("6x6",turn) if flag_7_event == 0 else turn_draw("7x7",turn)
        # draw_scramble("6x6") if flag_7_event == 0 else draw_scramble("7x7")
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    # print(actual_scramble)  
    reset_flags()      
    draw_scramble("6x6") if flag_7_event == 0 else draw_scramble("7x7")
    # turn_draw("6x6","R2")
    # draw_scramble("6x6")
    
    actual_scramble.set(" ".join(sum_turns))
    
   
def scrambler_7x7():    
    scrambler_6x6()

def scrambler_pyraminx():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0    

    sum_turns = []
    for i in range(12):

        while accepted == 0:
            n_move = random.randrange(1,9,1)
            # print(n_move)

            if (n_move == 1 or n_move == 2) and (pr_move == 1 or pr_move == 2):
                accepted = 0
            elif (n_move == 3 or n_move == 4) and (pr_move == 3 or pr_move == 4):
                accepted = 0
            elif (n_move == 5 or n_move == 6) and (pr_move == 5 or pr_move == 6):
                accepted = 0  
            elif (n_move == 7 or n_move == 8) and (pr_move == 7 or pr_move == 8):
                accepted = 0           
            else:
                accepted = 1

        if n_move == 1:
            turn = "R"
            
        elif n_move == 2:
            turn = "R'"       
            
        elif n_move == 3:
            turn = "U"
            
        elif n_move == 4:
            turn = "U'"
           
        elif n_move == 5:
            turn = "L"
            
        elif n_move == 6:
            turn = "L'"
            
        elif n_move == 7:
            turn = "B"
            
        elif n_move == 8:
            turn = "B'"           
        
        
        sum_turns.append(turn)
        pr_move = n_move
        turn_draw("pyraminx",turn)
        draw_scramble("pyraminx")
        print(turn) 
        accepted = 0

    n_caps = random.randrange(1,5,1)

    cap_r = 0
    cap_l = 0
    cap_u = 0
    cap_b = 0

    for i in range(n_caps):

        while accepted == 0:
            n_move = random.randrange(1,9,1)
            # print(n_move)

            if (n_move == 1 or n_move == 2) and (cap_r == 1):
                accepted = 0
            elif (n_move == 3 or n_move == 4) and (cap_u == 1):
                accepted = 0
            elif (n_move == 5 or n_move == 6) and (cap_l == 1):
                accepted = 0  
            elif (n_move == 7 or n_move == 8) and (cap_b == 1):
                accepted = 0           
            else:
                accepted = 1

        if n_move == 1:
            turn = "r"
            cap_r = 1
            
        elif n_move == 2:
            turn = "r'"       
            cap_r = 1
            
        elif n_move == 3:
            turn = "u"
            cap_u = 1
            
        elif n_move == 4:
            turn = "u'"
            cap_u = 1
           
        elif n_move == 5:
            turn = "l"
            cap_l = 1
            
        elif n_move == 6:
            turn = "l'"
            cap_l = 1
            
        elif n_move == 7:
            turn = "b"
            cap_b = 1
            
        elif n_move == 8:
            turn = "b'"           
            cap_b = 1
        
        
        sum_turns.append(turn)
        pr_move = n_move
        turn_draw("pyraminx",turn)
        draw_scramble("pyraminx")
        
        print(turn) 
        accepted = 0

   
    # print(actual_scramble)    
    
    actual_scramble.set(" ".join(sum_turns))
    
    
    

def scrambler_megaminx():
    sum_turns = []

    for i in range(7):
        for j in range(5):
            R = random.randrange(1,3)
            turn = "R++" if R == 1 else "R--"
            sum_turns.append(turn)

            D = random.randrange(1,3)
            turn = "D++" if D == 1 else "D--"
            sum_turns.append(turn)
        
        U = random.randrange(1,3)
        turn = "U" if U == 1 else "U'"
        sum_turns.append(turn)
    
    # print(sum_turns)
    
    actual_scramble.set(" ".join(sum_turns))
          
def scrambler_skewb():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0    

    sum_turns = []
    for i in range(12):

        while accepted == 0:
            n_move = random.randrange(1,9,1)
            # print(n_move)

            if (n_move == 1 or n_move == 2) and (pr_move == 1 or pr_move == 2):
                accepted = 0
            elif (n_move == 3 or n_move == 4) and (pr_move == 3 or pr_move == 4):
                accepted = 0
            elif (n_move == 5 or n_move == 6) and (pr_move == 5 or pr_move == 6):
                accepted = 0  
            elif (n_move == 7 or n_move == 8) and (pr_move == 7 or pr_move == 8):
                accepted = 0           
            else:
                accepted = 1

        if n_move == 1:
            turn = "R"
            
        elif n_move == 2:
            turn = "R'"       
            
        elif n_move == 3:
            turn = "U"
            
        elif n_move == 4:
            turn = "U'"
           
        elif n_move == 5:
            turn = "L"
            
        elif n_move == 6:
            turn = "L'"
            
        elif n_move == 7:
            turn = "B"
            
        elif n_move == 8:
            turn = "B'"
            
        
        
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    # print(actual_scramble)    
    
    actual_scramble.set(" ".join(sum_turns))
    

def scrambler_clock():    
    accepted = 0  
    sum_turns = []

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("UR"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("DR"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("DL"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("UL"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("U"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("R"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("D"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("L"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("ALL"+number+signal)

    sum_turns.append("y2")

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("U"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("R"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("D"+number+signal)

    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("L"+number+signal)
    
    number = random.randrange(0+7+1)
    number = str(number)
    signal = random.randrange(0+2+1)
    signal = "+" if signal == 1 else  "-"        
    sum_turns.append("ALL"+number+signal)

    n_caps = random.randrange(1,5,1)

    cap_ur = 0
    cap_dr = 0
    cap_dl = 0
    cap_ul = 0

    for i in range(n_caps):

        while accepted == 0:
            n_move = random.randrange(1,5,1)
            # print(n_move)

            if  (n_move == 1) and (cap_ur == 1):
                accepted = 0
            elif (n_move == 2) and (cap_dr == 1):
                accepted = 0
            elif (n_move == 3) and (cap_dl == 1):
                accepted = 0  
            elif (n_move == 4) and (cap_ul == 1):
                accepted = 0           
            else:
                accepted = 1

        if n_move == 1:
            sum_turns.append("UR")
            cap_ur = 1
            
        elif n_move == 2:
            sum_turns.append("DR")     
            cap_dr = 1
            
        elif n_move == 3:
            sum_turns.append("DL")
            cap_dl = 1
            
        elif n_move == 4:
            sum_turns.append("UL")
            cap_ul = 1

        accepted = 0   


    print(sum_turns)
    # print(actual_scramble)    
    
    actual_scramble.set(" ".join(sum_turns))
    



def enter_time():

    global precisionTimer

    if input_timer.get() == "" :
      messagebox.showinfo( "Warning", "Digite um valor!")
      return   
    
    chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\|<>;/?´`[{]}=!@#$%¨&*() *-+')
    if any((c in chars) for c in input_timer.get()):        
        messagebox.showinfo( "Warning", "Digite apenas números!")
        return
    
    chars = set(',')
    if any((c in chars) for c in input_timer.get()):        
        messagebox.showinfo( "Warning", "Utilize ponto ao inves de virgula")
        return
    
    
    
    chars = set('.')
    if any((c in chars) for c in input_timer.get()):    #encontrou o ponto
        chars = set(':')
        if any((c in chars) for c in input_timer.get()):        #encontrou o ponto e dois ponto  1:23.54
            t = input_timer.get().split(':')        
            t = float(t[0]) * 60 + float(t[1])    
        else:                                           #encontrou o ponto e nao o dois pontos   12.43
            t = input_timer.get()        
    else:        
        if int(input_timer.get()) >= 10000 and precisionTimer == 2:                
            t = int(input_timer.get()) 
            x = [int(a) for a in str(t)]
            m = x[0]
            s = x[1]*10 + x[2]
            c = (x[3]*10 + x[4])/100
            t = m*60 + s + c 
            print(t)                                
        elif int(input_timer.get()) < 10000 and precisionTimer == 2:
            t = float(input_timer.get())/100  
        
        elif int(input_timer.get()) >= 100000 and precisionTimer == 3:              
            t = int(input_timer.get()) 
            x = [int(a) for a in str(t)]
            m = x[0]
            s = x[1]*10 + x[2]
            c = (x[3]*100 + x[4]*10 + x[5])/1000
            t = m*60 + s + c 
            print(t)                                
        elif int(input_timer.get()) < 100000 and precisionTimer == 3:
            t = float(input_timer.get())/1000  
        
        
    
        
        
    
    data = datetime.datetime.now()
    datas.append(data)

    tempo = float(t)
    tempo = trunc(tempo,precisionTimer)
    tempos.append(tempo)

    ptempo = time_convert(tempo)        

    global actual_timer
    
    actual_timer.set(ptempo)    

    global scrambles

    scrambles.append(actual_scramble.get())  

    estatistica(len(tempos))
    input_timer.delete(0,tk.END)

    reset_draw()
    next_scramble() 
    


def on_press_esc(event):
    global timer_state
    global countdown 
    global run_inspecton
    global actual_timer

    run_inspecton = False    
    timer_state = 0    
    countdown = 15
    
    actual_timer.set("0:00")   
    print("parou....")


def inspection():
    
    global countdown
    global run_inspecton
    if run_inspecton:
        print("inspeção")   
        # Just beore starting        
        # show = str(count)

        # mark.config(text = count)
        global actual_timer
        actual_timer.set(countdown)
        
        print(countdown)
        #Increment the count after
        #every 1 second
        root.after(1000, inspection)
        countdown -= 1 

_short_press = None
_do_space_longpress = None
enable_start_timer = False

timer_state = 0

# set timer for long press
def on_press_space(event):
    global _short_press
    global _do_space_longpress   
    global timer_state 
    global holdSpace
    if timer_state == 0 and inputVar.get() == 2:
        timer_state = 1
    
    if timer_state == 2:
        pass

    if timer_state == 4:
        stop_timer()

    stop_timer()
    
    if _short_press is None: # only set timer if a key press is not ongoing
        
        _short_press = True
        _do_space_longpress = root.after(holdSpace, do_space_longpress)


# if it was a short press, cancel event. If it was a long press, event already happened
def on_release_space(event):
    global timer_state
    if timer_state == 1:
        timer_state = 2
        global run_inspecton
        run_inspecton = True
        inspection()

    if timer_state == 3:
        start_timer()
    
    if timer_state == 5:
        if inspecionVar.get() == 1:
            timer_state = 0
        else:
            timer_state = 2
        # timer_state = 2

    start_timer()
    global _short_press
    if _short_press:
        cancel_do_space_longpress()

# do long press action
def do_space_longpress():
    global timer_state
    if timer_state == 2:
        # cancel_do_space_longpress() # cancel any outstanding timers, if they exist
        print('pronto..')
        global enable_start_timer
        enable_start_timer = True
        timer_state = 3


# cancels long press events
def cancel_do_space_longpress():
    global _short_press
    global _do_space_longpress
    global enable_start_timer
    enable_start_timer = False
    _short_press = None
    if _do_space_longpress:
        root.after_cancel(_do_space_longpress)

                
def start_timer():  
    global enable_start_timer    
    
    global t0
    global timer_state
    
    if timer_state == 3:
        t0 = time.time()
        
        print("rodando........")

        global actual_timer
        actual_timer.set("rodando........")

        timer_state = 4
        global run_inspecton
        run_inspecton = False
    
def stop_timer(): 
    
    global timer_state

    if timer_state == 4:
        t1 = time.time()
        data = datetime.datetime.now()
        # print(data)

        global t0        
        global enable_start_timer 

        dt = t1-t0         
        tempo = dt
        
        datas.append(data)
        
        enable_start_timer = False
        
        timer_state = 5                
        
        global countdown 
        countdown = 15

        global precisionTimer

        tempo = trunc(tempo,precisionTimer)
        tempos.append(tempo)

        ptempo = time_convert(tempo)        

        global actual_timer

        
        actual_timer.set(ptempo)    

        global scrambles

        scrambles.append(actual_scramble.get())

        # print(tempos)
        # print(scrambles)


        estatistica(len(tempos))

        reset_draw()
        next_scramble() 

       
        
def change_event(event):  

    resetar()     
    
    global flag_7_event 
    # messagebox.showinfo( "Hello Python", eventos.get())
    ch_event = eventos.get()
    if ch_event == '2x2':
        scrambler_2x2()    
        flag_7_event = 0
    elif ch_event == '3x3':
        scrambler_3x3()        
        flag_7_event = 0
    elif ch_event == '4x4':        
        flag_7_event = 0
        scrambler_4x4()        
    elif ch_event == '5x5':        
        flag_7_event = 0
        scrambler_5x5()       
    elif ch_event == '6x6':        
        flag_7_event = 0
        scrambler_6x6()
    elif ch_event == '7x7':         
        flag_7_event = 1
        scrambler_7x7()        
    elif ch_event == 'pyraminx':
        scrambler_pyraminx()        
        flag_7_event = 0
    elif ch_event == 'megaminx':
        # print_scramble = tk.Label(row2,textvariable = actual_scramble,wraplength = 500)
        # print_scramble.config(wraplength = 500)
        scrambler_megaminx()        
        flag_7_event = 0
    elif ch_event == 'skewb':
        scrambler_skewb()        
        flag_7_event = 0
    elif ch_event == 'clock':
        scrambler_clock()        
        flag_7_event = 0

def plot():   
    

	# the figure that will contain the plot 
    window = tk.Toplevel(root)

    # global tempos 
    fig = Figure(figsize = (5, 5),dpi = 100) 

	# list of squares 
    x = tempos  
    y = mo_3
    z = ao_5
    a = ao_12   


	# adding the subplot 
    plot1 = fig.add_subplot(111) 

	# plotting the graph 
    plot1.plot(x) 
    
    plot1.plot(y) 
    
    plot1.plot(z) 
    
    plot1.plot(a) 


    if len(mo_3) >= 3:
        plot1.plot(y) 
    if len(ao_5) >= 5:
        plot1.plot(z) 
    if len(ao_12) >= 12:
        plot1.plot(a) 

	# creating the Tkinter canvas 
	# containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig,	master = window) 
    canvas.draw() 

	# placing the canvas on the Tkinter root 
    canvas.get_tk_widget().pack()  

    


	# creating the Matplotlib toolbar 
    # toolbar = NavigationToolbar2Tk(canvas,root) 
    # toolbar.update() 

	# placing the toolbar on the Tkinter root 
    # canvas.get_tk_widget().pack() 

    canvas.flush_events()


def importar():

    resetar()

    name_file = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("CSV Files","*.csv"),("Text File", "*.txt"),("All Files","*.*")),title = "Choose a file.")

    with open(name_file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:                         
            print(f'\t{row["No."]} ; {row["Time"]} ; {row["Scramble"]} ; {row["Date"]}.')            
                
            tempos.append(float(row["Time"]))            
            scrambles.append(row["Scramble"])
            datas.append(row["Date"])


            line_count += 1
            estatistica(line_count)
            

        print(f'Processed {line_count} lines.')
        

def exportar():

    name_file = filedialog.asksaveasfilename(defaultextension=".csv")
    name_file = str(name_file)

    with open(name_file, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(["No.", "Time", "Scramble","Date"])

        for i in range(len(tempos)):
            employee_writer.writerow([i+1, tempos[i], scrambles[i], datas[i]])

    messagebox.showinfo( "Warning", "Export completo.")
     

def resetar():
    global tempos
    global scrambles
    global datas

    global global_best_solve
    global global_worst_solve

    global best_mo3
    global best_ao5
    global best_ao12

    global media_3
    global media_5
    global media_12

    tempos.clear()
    mo_3.clear()
    ao_5.clear()
    ao_12.clear()
    scrambles.clear()
    datas.clear()

    reset_draw()

    global_best_solve = 9999
    global_worst_solve = 0

    best_mo3  = 9999
    best_ao5  = 9999
    best_ao12 = 9999

    media_3  = 9999
    media_5  = 9999
    media_12 = 9999

    for i in tb_times.get_children():
        tb_times.delete(i) 
    
    for i in tb_stat.get_children():
        tb_stat.delete(i) 

    
    

def deletar():
    global tempos
    global scrambles
    global datas

    global global_best_solve
    global global_worst_solve   

    global media_3 
    global media_5
    global media_12

    global best_mo3
    global best_ao5
    global best_ao12

    

    selected = tb_times.focus()     
    selected = int(selected)    
    tb_times.delete(selected) 

    del tempos[selected-1]
    del scrambles[selected-1]
    del datas[selected-1]

    mo_3.clear()
    ao_5.clear()
    ao_12.clear()

    global_best_solve = 9999
    global_worst_solve = 0

    media_3  = 9999
    media_5  = 9999
    media_12 = 9999

    best_mo3  = 9999
    best_ao5  = 9999
    best_ao12 = 9999

    for i in tb_stat.get_children():
        tb_stat.delete(i) 

    for i in tb_times.get_children():
        tb_times.delete(i) 

        
    s1 = 0
    

    for solve in range(len(tempos)):
        s1 += 1
        
        # print(s1)
        estatistica(s1)

        print(tempos)


def on_press_enter(event):
    if inputVar.get() == 1:
        print(inputVar.get())
        enter_time()


def inputVar_change():
    
    plot_button.pack_forget() 
    reset_button.pack_forget()
    delete_button.pack_forget()

    if inputVar.get() == 1:
        print_timer.pack_forget()
        input_timer.pack()
        
    elif inputVar.get() == 2:
        input_timer.pack_forget()
        print_timer.pack()
    

    plot_button.pack() 
    reset_button.pack()
    delete_button.pack()
    

def precisionVar_change():
    global precisionTimer
    if precisionVar.get() == 1:
        precisionTimer = 2
        
        
    elif precisionVar.get() == 2:
        precisionTimer = 3    


def holdVar_change():
    global holdSpace
    if holdVar.get() == 1:
        holdSpace = 0        
        
    elif holdVar.get() == 2:
        holdSpace = 300

    elif holdVar.get() == 3:
        holdSpace = 550
    
    elif holdVar.get() == 4:
        holdSpace = 1000
    
def inspecionVar_change():
    global timer_state 
    
    if inspecionVar.get() == 0:
        timer_state = 2
        
    elif inspecionVar.get() == 1:
        timer_state = 0

def scrambleVar_change():
    global timer_state 
    
    if scrambleVar.get() == 0:
        our_canvas.pack_forget() 
        
    elif scrambleVar.get() == 1:
        our_canvas.pack() 
    
    
def donothing():
   filewin = tk.Toplevel(root)
   button = tk.Button(filewin, text="Do nothing button")
   button.pack()

def donothing_event(event):
   filewin = tk.Toplevel(root)
   button = tk.Button(filewin, text="Do nothing button")
   button.pack()
   selected = tb_times.focus()   
   print(selected)

   print_valor = tk.Label(filewin, text = tempos[int(selected)-1]) 
   print_valor.pack()


ttk.Label(row1, text = "Modalidade :").grid(column = 0,row = 0) 

# n = tk.StringVar() 
# eventos = ttk.Combobox(row1, width = 10,textvariable = n,state = "readonly") 
eventos = ttk.Combobox(row1, width = 10,state = "readonly") 
# Adding combobox drop down list 
eventos['values'] = ('2x2','3x3', '4x4','5x5','6x6','7x7','pyraminx','megaminx','skewb','clock') 

eventos.grid(column = 1, row = 0) 
eventos.bind('<<ComboboxSelected>>',change_event)
# Shows number as a default value 
eventos.current(1) 




# img = tk.PhotoImage(file = r"C:\Users\gabri\OneDrive\Documentos\VScode\lena.png")
# label_img = tk.Label(root, image = img)
# label_img.pack(expand = "yes",anchor = tk.SE)
# label_img.pack(fill = "both", expand = "yes",side=tk.TOP , anchor = tk.S)

print_scramble = tk.Label(row2,textvariable = actual_scramble,wraplength = 500)
print_scramble.grid(column = 0, row = 0)

actual_timer.set("0:00")

print_timer = tk.Label(root,textvariable = actual_timer)
print_timer.pack()

input_timer  = tk.Entry(root)
# input_timer.pack()





tb_times = ttk.Treeview(row3)

tb_times['columns'] = ('n','tempo','mo3', 'ao5','ao12')

tb_times.column("#0", width=0,  stretch=tk.NO)
tb_times.column("n",anchor=tk.CENTER,width=80)
tb_times.column("tempo",anchor=tk.CENTER, width=80)
tb_times.column("mo3",anchor=tk.CENTER,width=80)
tb_times.column("ao5",anchor=tk.CENTER,width=80)
tb_times.column("ao12",anchor=tk.CENTER,width=80)

tb_times.heading("#0",text="",anchor=tk.CENTER)
tb_times.heading("n",text="n",anchor=tk.CENTER)
tb_times.heading("tempo",text="tempo",anchor=tk.CENTER)
tb_times.heading("mo3",text="mo3",anchor=tk.CENTER)
tb_times.heading("ao5",text="ao5",anchor=tk.CENTER)
tb_times.heading("ao12",text="ao12",anchor=tk.CENTER)


tb_times.grid(column = 0, row = 1)

tb_times.bind('<ButtonRelease-1>', donothing_event )








tb_stat = ttk.Treeview(row3)

tb_stat['columns'] = ('tempos','atual', 'melhor')

tb_stat.column("#0", width=0,  stretch=tk.NO)
tb_stat.column("tempos",anchor=tk.CENTER,width=80)
tb_stat.column("atual",anchor=tk.CENTER, width=80)
tb_stat.column("melhor",anchor=tk.CENTER,width=80)

tb_stat.heading("#0",text="",anchor=tk.CENTER)
tb_stat.heading("tempos",text="",anchor=tk.CENTER)
tb_stat.heading("atual",text="atual",anchor=tk.CENTER)
tb_stat.heading("melhor",text="melhor",anchor=tk.CENTER)

tb_stat.grid(column = 0, row = 0)
# tb_stat.insert(parent='',index='end',iid=0,text='',
# values=('time',str(tempos[-1]),str(global_best_solve)))
# tb_stat.insert(parent='',index='end',iid=1,text='',
# values=('mo3',str(media_3),str(best_mo3)))
# tb_stat.insert(parent='',index='end',iid=2,text='',
# values=('ao5',str(media_5),str(best_ao5)))
# tb_stat.insert(parent='',index='end',iid=3,text='',
# values=('ao12',str(media_12),str(best_ao12)))




# tb_stat.pack()






scrambler_3x3()


root.bind("<KeyPress-space>",on_press_space)
root.bind("<KeyRelease-space>",on_release_space)
root.bind("<KeyPress-Escape>",on_press_esc)
root.bind("<KeyPress-Return>",on_press_enter)


plot_button = tk.Button(master = root,command = plot,	height = 2, width = 10, text = "Plot") 
plot_button.pack() 

# import_button  = tk.Button(master = root,command = importar,	height = 2, width = 10, text = "Import") 
# import_button.pack()

# export_button  = tk.Button(master = root,command = exportar,	height = 2, width = 10, text = "Export") 
# export_button.pack()

reset_button  = tk.Button(master = root,command = resetar,	height = 2, width = 10, text = "Reset") 
reset_button.pack()

delete_button  = tk.Button(master = root,command = deletar,	height = 2, width = 10, text = "Delete") 
delete_button.pack()





menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
optionmenu = tk.Menu(menubar, tearoff=0)
precisionmenu = tk.Menu(menubar, tearoff=0)
inputmenu = tk.Menu(menubar, tearoff=0)
holdmenu = tk.Menu(menubar, tearoff=0)
helpmenu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Opções", menu=optionmenu)
menubar.add_cascade(label="Help", menu=helpmenu)


filemenu.add_command(label="Importar...", command=importar)
filemenu.add_command(label="Exportar...", command=exportar)
filemenu.add_separator()
filemenu.add_command(label="Sair", command=exportar)

inspecionVar = tk.BooleanVar()
scrambleVar = tk.BooleanVar()
inputVar = tk.IntVar()
precisionVar = tk.IntVar()
holdVar = tk.IntVar()

inspecionVar.set(1)
inputVar.set(2)
precisionVar.set(1)
holdVar.set(3)
scrambleVar.set(1)






optionmenu.add_checkbutton(label="Tempo de Inspeção", onvalue=1, offvalue=0, variable=inspecionVar, command= inspecionVar_change)
optionmenu.add_checkbutton(label="Desenho scramble", onvalue=1, offvalue=0, variable=scrambleVar, command= scrambleVar_change)
optionmenu.add_cascade(label="Disparador cronômetro", menu=inputmenu)
optionmenu.add_cascade(label="Precisão timer", menu=precisionmenu)
optionmenu.add_cascade(label="Tempo segurar Espaço", menu=holdmenu)


inputmenu.add_radiobutton(label="Manual input", value=1, variable=inputVar, command=inputVar_change)
inputmenu.add_radiobutton(label="Tecla Espaço", value=2, variable=inputVar, command=inputVar_change)
inputmenu.add_radiobutton(label="Stackmat", value=3, variable=inputVar, command=inputVar_change)


precisionmenu.add_radiobutton(label="0.01", value=1, variable=precisionVar, command= precisionVar_change)
precisionmenu.add_radiobutton(label="0.001", value=2, variable=precisionVar, command= precisionVar_change)

holdmenu.add_radiobutton(label="0", value=1, variable=holdVar, command= holdVar_change)
holdmenu.add_radiobutton(label="0.3", value=2, variable=holdVar, command= holdVar_change)
holdmenu.add_radiobutton(label="0.55", value=3, variable=holdVar, command= holdVar_change)
holdmenu.add_radiobutton(label="1", value=4, variable=holdVar, command= holdVar_change)


helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)



root.config(menu=menubar)
root.mainloop() 
