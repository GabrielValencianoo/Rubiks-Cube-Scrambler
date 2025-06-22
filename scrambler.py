#scrambler
#meta 1 - gerar embaralhamento - (igual ao c++)
#meta 1/2 - gerar embaralhamento de todos os puzzles
#meta 2 - adicionar timer
#meta 3 - guardar tempos e fazer continhas (botão de reset)
#meta 4 - gerar graficos
#meta 5 - gerar desenho do scramble
#meta 6 - ler stackmat
#meta 10 - ler dados wca e dizer em qual posição estaria 
#meta 11 - Ler JSON e descobrir se existe dado atualizado - OK
#meta 12 - download automático dados WCA
#meta 13 - unzip e ler os dados novamente

import random
import time
import statistics
# from msvcrt import getch
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from tkinter import filedialog
# from tkinter.filedialog import askopenfilename
# from tkinter.filedialog import asksaveasfile
# from tkinter.filedialog import askdirectory
import customtkinter as ctk
from tkinter import colorchooser
# import lovelyplots as lp

import datetime
import csv
import numpy as np
import pandas as pd
import os

from matplotlib.figure import Figure 
from matplotlib.ticker import FuncFormatter, MaxNLocator
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

import threading
import requests
import json

from icecream import ic
import mplcursors

from zipfile import ZipFile


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mpl_toolkits.mplot3d.art3d as art3d

root = ctk.CTk() 
root.title('timezinho') 
root.geometry('1600x700+1200+200') 

# root.iconphoto(False, tk.PhotoImage(file='/path/to/ico/icon.png'))


try:               
    with open('Scrambler_Settings.json', 'r') as openfile:
        jsonSettings = json.load(openfile)
    
    theme = jsonSettings['colorTheme']    

    if theme == '1':        
        ctk.set_default_color_theme("blue")
        
    elif theme == '2':        
        ctk.set_default_color_theme("green")               
    
except:
    pass    

# Label 
row1 = ctk.CTkFrame(root)
row2 = ctk.CTkFrame(root)
row3 = ctk.CTkFrame(root)
row4 = ctk.CTkFrame(root)


row1.pack()
row2.pack()
# row2.pack(side=tk.TOP,anchor = tk.W)
row3.pack(side=tk.LEFT,anchor = tk.N)
row4.pack(side=tk.RIGHT,anchor = tk.E)
# row3.pack()


t0 = 0
t1 = 0

actual_scramble = []
actual_timer = tk.StringVar()
sum_turns_str = ""

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


tempos = []
mo_3  = []
ao_5  = []
ao_12 = []
scrambles = []
countdowns = []
status = []
inputs = []
datas = []
des_padrao = []
mediana = []
faceColors = {'1':'#FFFFFF','2':'#FFA500','3':'#00FF00','4':'#FF0000','5':'#0000FF','6':'#FFFF00'}
precisions = {'2x2':'2','3x3':'2','4x4':'2','5x5':'2','6x6':'2','7x7':'2','pyraminx':'2','megaminx':'2','skewb':'2','clock':'2','3x3 OH':'2'}
first_scan = False
flag_change_event = False   
precisionTimer = 2
holdSpace = 550
enableRanking = 0
rankingPath = ""
gender = 0
saveTime = 0

best_mo3  = 9999999999
best_ao5  = 9999999999
best_ao12 = 9999999999

worst_mo3  = 0
worst_ao5  = 0
worst_ao12 = 0

media_3  = 9999999999
media_5  = 9999999999
media_12 = 9999999999

global_best_solve = 9999999999
global_worst_solve = 0

index_best_mo3  = 0
index_best_ao5  = 0
index_best_ao12 = 0

countdown = 15
run_inspecton = False

ranking_WR_Average = pd.DataFrame()
ranking_CR_Average = pd.DataFrame()
ranking_NR_Average = pd.DataFrame()

ranking_WR_Single = pd.DataFrame()
ranking_CR_Single = pd.DataFrame()
ranking_NR_Single = pd.DataFrame()

our_canvas=tk.Canvas(row4,width=450,height=350,bg="white")
# our_canvas.pack(side = tk.RIGHT,anchor = tk.S)

fig = plt.figure()
canvas = FigureCanvasTkAgg(fig,	master = root) 

#faces

def treat_status(vf,average):
    list_3  = status[vf-3:vf]
    list_5  = status[vf-5:vf]
    list_12 = status[vf-12:vf]    

    if average == "3":
        if "DNF" in list_3:
            return "DNF"
    if average == "5":
        if list_5.count("DNF") >= 2:
            return "DNF"
    if average == "12":
        if list_12.count("DNF") >= 2:
            return "DNF"
    else:
        return average
        


def trunc(n, decimals=0):
    
    multiplier = 10 ** decimals
    return int(int(n * multiplier) / multiplier)

def time_convert(time):
    global precisionTimer    

    if precisionTimer == 1:        
        time /= 10
    
    elif precisionTimer == 2:        
        time /= 100

    elif precisionTimer == 3:        
        time /= 1000

    
    if time < 60:
        presult = str(time)
        
    else:
        
        m = time // 60        
        m = int(m)    

        s = time % 60          

        if precisionTimer == 1:                  
            sStr = format(s,'.1f')              

        if precisionTimer == 2:
            sStr = format(s,'.2f')      
               
        elif precisionTimer == 3:
            sStr = format(s,'.3f')

        if s < 10:                   
            presult = str(m) + ":0" + sStr    
            
        else:                                
            presult = str(m) + ":" + sStr
            
        
    return presult

def best_worst(lista):   

    local_best_solve  = min(lista)        
    local_worst_solve = max(lista)        

    return local_best_solve, local_worst_solve
 
def average():
    return sum(tempos)/len(tempos) 

def mo3(vf):
    
    list_3 = tempos[vf-3:vf]
    # print(list_3)
    average = sum(list_3)/len(list_3) 
    return average    

def ao5(vf):
    list_5 = tempos[vf-5:vf]    
    b,w = best_worst(list_5)    
    average = (sum(list_5)-b-w)/3
    return average    

def ao12(vf):
    list_12 = tempos[vf-12:vf]
    b,w = best_worst(list_12)
    average = (sum(list_12)-b-w)/10
    return average    

def rangeNext(vf):
    list_5 = tempos[vf-4:vf]
    list_5.append(0)
    b,w = best_worst(list_5)  
    best = (sum(list_5)-b-w)/3

    list_5 = tempos[vf-4:vf]
    list_5.append(9999999999)
    b,w = best_worst(list_5)  
    worst = (sum(list_5)-b-w)/3
    return best,worst

def bestNext(vf,avg):
    list_4 = tempos[vf-4:vf]
    b,w = best_worst(list_4) 
    result = (3*avg) - (sum(list_4))+b+w
    return result


def estatistica(index):
    global global_best_solve
    global global_worst_solve
    global best_mo3
    global best_ao5
    global best_ao12
    global worst_mo3
    global worst_ao5
    global worst_ao12
    global media_3
    global media_5
    global media_12
    global precisionTimer
    global index_best_mo3
    global index_best_ao5 
    global index_best_ao12
    global enableRanking
    global rankingPath   
    global mediana
    global des_padrao
    global statusFlag

    
    # global tempos

    media = average()
    media_3  = mo3(index)  if index >= 3  else media_3
    media_5  = ao5(index)  if index >= 5  else media_5
    media_12 = ao12(index) if index >= 12 else media_12
    next_avg  = rangeNext(index)  if index >= 5  else (9999999999,9999999999)
    best_next , _ = next_avg

    mediana = statistics.median(tempos)    
    ic(media)
    ic(mediana)
    des_padrao = statistics.stdev(tempos) if index >= 3  else des_padrao
    ic(des_padrao)  

    ic(next_avg) 

    

    
        
    global_best_solve  = tempos[index-1] if tempos[index-1] < global_best_solve else global_best_solve
    global_worst_solve  = tempos[index-1] if tempos[index-1] > global_worst_solve else global_worst_solve


    best_mo3  = media_3 if media_3 < best_mo3 else best_mo3
    worst_mo3 = media_3 if media_3 > worst_mo3 and media_3 != 9999999999 else worst_mo3

    best_ao5 = media_5 if media_5 < best_ao5 else best_ao5
    worst_ao5 = media_5 if media_5 > worst_ao5 and media_5 != 9999999999 else worst_ao5

    best_ao12 = media_12 if media_12 < best_ao12 else best_ao12
    worst_ao12 = media_12 if media_12 > worst_ao12 and media_12 != 9999999999 else worst_ao12

    index_best_mo3  = index if media_3 < best_mo3 else index_best_mo3

    index_best_ao5  = index if media_5 < best_ao5 else index_best_ao5

    index_best_ao12  = index if media_12 < best_ao12 else index_best_ao12


    if best_next < best_ao5:
        new_best = bestNext(index,best_ao5-1)        
        ic(tempos[index-5:index])
        ic(new_best)
        print(f"O proximo tempo precisa ser menor que {new_best} para melhor o PB")
        

    precisionTimer = int(precisionTimer)

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
    worst_mo3 = trunc(worst_mo3,precisionTimer)
    worst_ao5 = trunc(worst_ao5,precisionTimer)
    worst_ao12 = trunc(worst_ao12,precisionTimer)

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

    pworst_mo3 = time_convert(worst_mo3) 
    pworst_ao5 = time_convert(worst_ao5) 
    pworst_ao12 = time_convert(worst_ao12)    
   

    pmedia_3Status   = treat_status(index,"3")
    pmedia_5Status   = treat_status(index,"5")
    pmedia_12Status  = treat_status(index,"12")  

    pbest_mo3Status  = treat_status(index,"3") 
    pbest_ao5Status  = treat_status(index,"5") 
    pbest_ao12Status = treat_status(index,"12") 
    
    if pmedia_3Status == "DNF":
        pmedia_3 = "DNF"        
    if pbest_mo3Status == "DNF":
        pbest_mo3 = "DNF"
    if index < 3:
        pmedia_3 = 0
        pbest_mo3 = 0
    
    if pmedia_5Status == "DNF":
        pmedia_5 = "DNF"        
    if pbest_ao5Status == "DNF":
        pbest_ao5 = "DNF"
    if index < 5:
        pmedia_5 = 0
        pbest_ao5 = 0
    
    if pmedia_12Status == "DNF":
        pmedia_12 = "DNF"        
    if pbest_ao12Status == "DNF":
        pbest_ao12 = "DNF"
    if index < 12:
        pmedia_12 = 0
        pbest_ao12 = 0

    
    if status[index-1] == "DNF":
        ptempo = "DNF"
    elif status[index-1] == "+2":
        ptempo += "+"
       

    # tb_stat.delete(1)    
    for i in tb_stat.get_children():
        tb_stat.delete(i)
        
    for i in tb_ranking.get_children():
        tb_ranking.delete(i)
    root.update()

    tb_stat.insert(parent='',index='end',iid=0,text='',
    values=('time',str(ptempo),str(pglobal_best_solve),str(pglobal_worst_solve)))

    if index >=3:
        tb_stat.insert(parent='',index='end',iid=1,text='',
        values=('mo3',str(pmedia_3),str(pbest_mo3),str(pworst_mo3)))
    
    if index >=5:
        tb_stat.insert(parent='',index='end',iid=2,text='',
        values=('ao5',str(pmedia_5),str(pbest_ao5),str(pworst_ao5)))
    
    if index >=12:
        tb_stat.insert(parent='',index='end',iid=3,text='',
        values=('ao12',str(pmedia_12),str(pbest_ao12),str(pworst_ao12)))
    
    tb_stat.insert(parent='',index='end',iid=4,text='',
        values=('ao',str(media),str(mediana),str(des_padrao)))

    tb_times.insert(parent='',index='end',iid=index,text='',
    values=(str(index),str(ptempo),str(pmedia_3),str(pmedia_5),str(pmedia_12)))
    
    tb_times.yview_moveto(1)

    if media_3 != 9999999999:
        mo_3.append(media_3)
    else:
        mo_3.append(None)
    
    if media_5 != 9999999999:
        ao_5.append(media_5)
    else:
        ao_5.append(None)
    
    if media_12 != 9999999999:
        ao_12.append(media_12)
    else:
        ao_12.append(None)
    
    if saveTime == 1 and first_scan == False and flag_change_event == False:
        # print("printoo")
        update_file_tempos(index)    

    ch_event = eventsComboBox.get()    
  
    if enableRanking == 1:
        if ch_event == '6x6' or ch_event == '7x7':
            media = media_3
            best = best_mo3
            pmedia = pmedia_3
            pbest = pbest_mo3
        else:
            media = media_5
            best = best_ao5
            pmedia = pmedia_5
            pbest = pbest_ao5      
               
        current_ranking = ranking_position(tempos[index-1],media)
        best_ranking = ranking_position(global_best_solve,best)

        tb_ranking.insert(parent='',index='end',iid=0,text='',
        values=(str(best_ranking[2]),str(best_ranking[1]),str(best_ranking[0]),str(pglobal_best_solve),str(pbest),
            str(best_ranking[3]),str(best_ranking[4]),str(best_ranking[5])))

        tb_ranking.insert(parent='',index='end',iid=1,text='',
        values=(str(current_ranking[2]),str(current_ranking[1]),str(current_ranking[0]),str(ptempo),str(pmedia),
            str(current_ranking[3]),str(current_ranking[4]),str(current_ranking[5])))
            

def define_flags(cube,n_move):

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
    
    if cube == "2x2":
        flag_L = 1
        flag_D = 1
        flag_B = 1
    
    if cube == "4x4":
        flag_Lw = 1
        flag_Dw = 1
        flag_Bw = 1


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

def createMatrix(cube,type):
    global faceColors

    if cube == "2x2":
        n = 2
    elif cube == "3x3":
        n = 3
    elif cube == "4x4":
        n = 4
    elif cube == "5x5":
        n = 5
    elif cube == "6x6":
        n = 6
    elif cube == "7x7":
        n = 7
    elif cube == "pyraminx":
        n = 5
    elif cube == "skewb":
        n = 4
    elif cube == "clock":   
        n = 3    
    elif cube == "3x3 OH":
        n = 3
    else:
        n = 4
    
    
    
    Br_color = np.full((n,n), faceColors["1"])

    Lr_color = np.full((n,n), faceColors["2"])

    Vd_color = np.full((n,n), faceColors["3"])

    Vm_color = np.full((n,n), faceColors["4"])

    Az_color = np.full((n,n), faceColors["5"])

    Am_color = np.full((n,n), faceColors["6"])

    Buffer = np.full((4,n), "#000000") 

    return Br_color, Lr_color, Vd_color, Vm_color, Az_color, Am_color, Buffer    
    

    
def turn_draw(cube,turn,Br_color,Lr_color,Vd_color,Vm_color ,Az_color, Am_color,Buffer):  

    if cube == "2x2":        
        LL = 1
        cubeN = 'n'
    elif cube == "3x3":        
        LL = 2
        cubeN = 'n'
    elif cube == "4x4":        
        LL = 3
        cubeN = 'n'
    elif cube == "5x5":        
        LL = 4
        cubeN = 'n'
    elif cube == "6x6":        
        LL = 5
        cubeN = 'n'
    elif cube == "7x7":        
        LL = 6
        cubeN = 'n'
    elif cube == "pyraminx":
        cubeN = 'nn' 
    elif cube == "megaminx":
        cubeN = 'nn' 
    elif cube == "skewb":
        cubeN = 'nn' 
    elif cube == "clock":
        cubeN = 'nn' 
    elif cube == "3x3 OH":        
        LL = 2
        cubeN = 'n'
    
    

    if "'" in turn:
        loop = 3        
    elif "2" in turn:
        loop = 2    
    else:
        loop = 1
        
    if cubeN == "n":
        if "R" in turn:            
            for i in range(loop):            
                Buffer[0] = Vd_color[:,LL]
                Buffer[1] = np.flip(Br_color[:,LL],0)
                Buffer[2] = np.flip(Az_color[:,0],0)
                Buffer[3] = Am_color[:,LL]           

                Br_color[:,LL] = Buffer[0]
                Az_color[:,0] = Buffer[1]
                Am_color[:,LL] = Buffer[2]
                Vd_color[:,LL] = Buffer[3]            
            
                Vm_color = np.rot90(Vm_color,1,(1,0))        
           
        elif "L" in turn:
            for i in range(loop):
                Buffer[0] = Vd_color[:,0]
                Buffer[1] = np.flip(Am_color[:,0],0)
                Buffer[2] = np.flip(Az_color[:,LL],0)
                Buffer[3] = Br_color[:,0]

                Am_color[:,0] = Buffer[0]
                Az_color[:,LL] = Buffer[1]
                Br_color[:,0] = Buffer[2]
                Vd_color[:,0] = Buffer[3]

                Lr_color = np.rot90(Lr_color,1,(1,0))
        
        elif "U" in turn:
            for i in range(loop):
                Buffer[0] = Vd_color[0]
                Buffer[1] = Lr_color[0]
                Buffer[2] = Az_color[0]
                Buffer[3] = Vm_color[0]

                Lr_color[0] = Buffer[0]
                Az_color[0] = Buffer[1]
                Vm_color[0] = Buffer[2]
                Vd_color[0] = Buffer[3]

                Br_color = np.rot90(Br_color,1,(1,0))
        
        elif "D" in turn:
            for i in range(loop):
                Buffer[0] = Vd_color[LL]
                Buffer[1] = Vm_color[LL]
                Buffer[2] = Az_color[LL]
                Buffer[3] = Lr_color[LL]

                Vm_color[LL] = Buffer[0]
                Az_color[LL] = Buffer[1]
                Lr_color[LL] = Buffer[2]
                Vd_color[LL] = Buffer[3]

                Am_color = np.rot90(Am_color,1,(1,0))
        
        elif "F" in turn:
            for i in range(loop):
                Buffer[0] = Br_color[LL]
                Buffer[1] = np.flip(Vm_color[:,0],0)
                Buffer[2] = Am_color[0]
                Buffer[3] = np.flip(Lr_color[:,LL],0)

                Vm_color[:,0] = Buffer[0]
                Am_color[0]   = Buffer[1]
                Lr_color[:,LL] = Buffer[2]
                Br_color[LL]   = Buffer[3]

                Vd_color = np.rot90(Vd_color,1,(1,0))
        
        elif "B" in turn:
            for i in range(loop):
                Buffer[0] = np.flip(Br_color[0],0)
                Buffer[1] = Lr_color[:,0]
                Buffer[2] = np.flip(Am_color[LL],0)
                Buffer[3] = Vm_color[:,LL]

                Lr_color[:,0] = Buffer[0]
                Am_color[LL]   = Buffer[1]
                Vm_color[:,LL] = Buffer[2]
                Br_color[0]   = Buffer[3]

                Az_color = np.rot90(Az_color,1,(1,0))        
        
        LL -= 1           
        if "Rw" in turn:   
                        
            for i in range(loop):
                Buffer[0] = Vd_color[:,LL]
                Buffer[1] = np.flip(Br_color[:,LL],0)
                Buffer[2] = np.flip(Az_color[:,1],0)
                Buffer[3] = Am_color[:,LL]           

                Br_color[:,LL] = Buffer[0]
                Az_color[:,1] = Buffer[1]
                Am_color[:,LL] = Buffer[2]
                Vd_color[:,LL] = Buffer[3]     
                
        elif "Lw" in turn:       
            
            for i in range(loop):

                Buffer[0] = Vd_color[:,1]
                Buffer[1] = np.flip(Am_color[:,1],0)
                Buffer[2] = np.flip(Az_color[:,LL],0)
                Buffer[3] = Br_color[:,1]

                Am_color[:,1] = Buffer[0]
                Az_color[:,LL] = Buffer[1]
                Br_color[:,1] = Buffer[2]
                Vd_color[:,1] = Buffer[3]
                
       
        elif "Uw" in turn:              

            for i in range(loop):
                Buffer[0] = Vd_color[1]
                Buffer[1] = Lr_color[1]
                Buffer[2] = Az_color[1]
                Buffer[3] = Vm_color[1]

                Lr_color[1] = Buffer[0]
                Az_color[1] = Buffer[1]
                Vm_color[1] = Buffer[2]
                Vd_color[1] = Buffer[3]              
        
        elif "Dw" in turn:            
            
            for i in range(loop):
                Buffer[0] = Vd_color[LL]
                Buffer[1] = Vm_color[LL]
                Buffer[2] = Az_color[LL]
                Buffer[3] = Lr_color[LL]

                Vm_color[LL] = Buffer[0]
                Az_color[LL] = Buffer[1]
                Lr_color[LL] = Buffer[2]
                Vd_color[LL] = Buffer[3]
                       
        elif "Fw" in turn:      
           
            for i in range(loop):
                Buffer[0] = Br_color[LL]
                Buffer[1] = np.flip(Vm_color[:,1],0)
                Buffer[2] = Am_color[1]
                Buffer[3] = np.flip(Lr_color[:,LL],0)

                Vm_color[:,1] = Buffer[0]
                Am_color[1]   = Buffer[1]
                Lr_color[:,LL] = Buffer[2]
                Br_color[LL]   = Buffer[3]
                
        elif "Bw" in turn:          
            
            for i in range(loop):

                Buffer[0] = np.flip(Br_color[1],0)
                Buffer[1] = Lr_color[:,1]
                Buffer[2] = np.flip(Am_color[LL],0)
                Buffer[3] = Vm_color[:,LL]

                Lr_color[:,1] = Buffer[0]
                Am_color[LL]   = Buffer[1]
                Vm_color[:,LL] = Buffer[2]
                Br_color[1]   = Buffer[3]

        LL -= 1                        
        if "3Rw" in turn:           
            
            for i in range(loop):
                Buffer[0] = Vd_color[:,LL]
                Buffer[1] = np.flip(Br_color[:,LL],0)
                Buffer[2] = np.flip(Az_color[:,2],0)
                Buffer[3] = Am_color[:,LL]           

                Br_color[:,LL] = Buffer[0]
                Az_color[:,2] = Buffer[1]
                Am_color[:,LL] = Buffer[2]
                Vd_color[:,LL] = Buffer[3]        
            
        elif "3Lw" in turn:            
            
            for i in range(loop):
                Buffer[0] = Vd_color[:,2]
                Buffer[1] = np.flip(Am_color[:,2],0)
                Buffer[2] = np.flip(Az_color[:,LL],0)
                Buffer[3] = Br_color[:,2]

                Am_color[:,2] = Buffer[0]
                Az_color[:,LL] = Buffer[1]
                Br_color[:,2] = Buffer[2]
                Vd_color[:,2] = Buffer[3]            
       
        elif "3Uw" in turn:   

            for i in range(loop):          
                Buffer[0] = Vd_color[2]
                Buffer[1] = Lr_color[2]
                Buffer[2] = Az_color[2]
                Buffer[3] = Vm_color[2]

                Lr_color[2] = Buffer[0]
                Az_color[2] = Buffer[1]
                Vm_color[2] = Buffer[2]
                Vd_color[2] = Buffer[3]            
       
        elif "3Dw" in turn:            
            
            for i in range(loop):     

                Buffer[0] = Vd_color[LL]
                Buffer[1] = Vm_color[LL]
                Buffer[2] = Az_color[LL]
                Buffer[3] = Lr_color[LL]

                Vm_color[LL] = Buffer[0]
                Az_color[LL] = Buffer[1]
                Lr_color[LL] = Buffer[2]
                Vd_color[LL] = Buffer[3]            
       
        elif "3Fw" in turn:            
            
            for i in range(loop):    

                Buffer[0] = Br_color[LL]
                Buffer[1] = np.flip(Vm_color[:,2],0)
                Buffer[2] = Am_color[2]
                Buffer[3] = np.flip(Lr_color[:,LL],0)

                Vm_color[:,2] = Buffer[0]
                Am_color[2]   = Buffer[1]
                Lr_color[:,LL] = Buffer[2]
                Br_color[LL]   = Buffer[3]   
        
        elif "3Bw" in turn:            
            
            for i in range(loop):  

                Buffer[0] = np.flip(Br_color[2],0)
                Buffer[1] = Lr_color[:,2]
                Buffer[2] = np.flip(Am_color[LL],0)
                Buffer[3] = Vm_color[:,LL]

                Lr_color[:,2] = Buffer[0]
                Am_color[LL]   = Buffer[1]
                Vm_color[:,LL] = Buffer[2]
                Br_color[2]   = Buffer[3]         

        
    elif cube == "pyraminx":
        if turn == "R":
            Buffer[0][0] = Vd_color[1,3]
            Buffer[0][1] = Vd_color[2,2]
            Buffer[0][2] = Vd_color[2,3]
            Buffer[0][3] = Vd_color[2,4]

            Buffer[1][0] = Az_color[1,1]
            Buffer[1][1] = Az_color[1,2]
            Buffer[1][2] = Az_color[1,3]
            Buffer[1][3] = Az_color[2,2]

            Buffer[2][0] = Am_color[0,2]
            Buffer[2][1] = Am_color[0,3]
            Buffer[2][2] = Am_color[0,4]
            Buffer[2][3] = Am_color[1,3]             

            Az_color[1,3] = Buffer[0][0] 
            Az_color[1,1] = Buffer[0][1] 
            Az_color[1,2] = Buffer[0][2] 
            Az_color[2,2] = Buffer[0][3] 

            Am_color[1,3] = Buffer[1][0] 
            Am_color[0,3] = Buffer[1][1] 
            Am_color[0,2] = Buffer[1][2] 
            Am_color[0,4] = Buffer[1][3] 

            Vd_color[1,3] = Buffer[2][0] 
            Vd_color[2,3] = Buffer[2][1] 
            Vd_color[2,4] = Buffer[2][2] 
            Vd_color[2,2] = Buffer[2][3]
        
        elif turn == "R'":
            for i in range(2):
                Buffer[0][0] = Vd_color[1,3]
                Buffer[0][1] = Vd_color[2,2]
                Buffer[0][2] = Vd_color[2,3]
                Buffer[0][3] = Vd_color[2,4]

                Buffer[1][0] = Az_color[1,1]
                Buffer[1][1] = Az_color[1,2]
                Buffer[1][2] = Az_color[1,3]
                Buffer[1][3] = Az_color[2,2]

                Buffer[2][0] = Am_color[0,2]
                Buffer[2][1] = Am_color[0,3]
                Buffer[2][2] = Am_color[0,4]
                Buffer[2][3] = Am_color[1,3]             

                Az_color[1,3] = Buffer[0][0] 
                Az_color[1,1] = Buffer[0][1] 
                Az_color[1,2] = Buffer[0][2] 
                Az_color[2,2] = Buffer[0][3] 

                Am_color[1,3] = Buffer[1][0] 
                Am_color[0,3] = Buffer[1][1] 
                Am_color[0,2] = Buffer[1][2] 
                Am_color[0,4] = Buffer[1][3] 

                Vd_color[1,3] = Buffer[2][0] 
                Vd_color[2,3] = Buffer[2][1] 
                Vd_color[2,4] = Buffer[2][2] 
                Vd_color[2,2] = Buffer[2][3]                               
                    
        elif turn == "L":
            Buffer[0][0] = Vd_color[1,1]
            Buffer[0][1] = Vd_color[2,0]
            Buffer[0][2] = Vd_color[2,1]
            Buffer[0][3] = Vd_color[2,2]            

            Buffer[1][0] = Am_color[0,0]
            Buffer[1][1] = Am_color[0,1]
            Buffer[1][2] = Am_color[0,2]
            Buffer[1][3] = Am_color[1,1]

            Buffer[2][0] = Vm_color[1,1]
            Buffer[2][1] = Vm_color[1,2]
            Buffer[2][2] = Vm_color[1,3]
            Buffer[2][3] = Vm_color[2,2] 


            Am_color[0,2] = Buffer[0][0] 
            Am_color[0,0] = Buffer[0][1] 
            Am_color[0,1] = Buffer[0][2] 
            Am_color[1,1] = Buffer[0][3] 

            Vm_color[2,2] = Buffer[1][0] 
            Vm_color[1,2] = Buffer[1][1] 
            Vm_color[1,1] = Buffer[1][2] 
            Vm_color[1,3] = Buffer[1][3]             

            Vd_color[1,1] = Buffer[2][0] 
            Vd_color[2,1] = Buffer[2][1] 
            Vd_color[2,2] = Buffer[2][2] 
            Vd_color[2,0] = Buffer[2][3]
        
        elif turn == "L'":
            for i in range(2):
                Buffer[0][0] = Vd_color[1,1]
                Buffer[0][1] = Vd_color[2,0]
                Buffer[0][2] = Vd_color[2,1]
                Buffer[0][3] = Vd_color[2,2]            

                Buffer[1][0] = Am_color[0,0]
                Buffer[1][1] = Am_color[0,1]
                Buffer[1][2] = Am_color[0,2]
                Buffer[1][3] = Am_color[1,1]

                Buffer[2][0] = Vm_color[1,1]
                Buffer[2][1] = Vm_color[1,2]
                Buffer[2][2] = Vm_color[1,3]
                Buffer[2][3] = Vm_color[2,2] 


                Am_color[0,2] = Buffer[0][0] 
                Am_color[0,0] = Buffer[0][1] 
                Am_color[0,1] = Buffer[0][2] 
                Am_color[1,1] = Buffer[0][3] 

                Vm_color[2,2] = Buffer[1][0] 
                Vm_color[1,2] = Buffer[1][1] 
                Vm_color[1,1] = Buffer[1][2] 
                Vm_color[1,3] = Buffer[1][3]             

                Vd_color[1,1] = Buffer[2][0] 
                Vd_color[2,1] = Buffer[2][1] 
                Vd_color[2,2] = Buffer[2][2] 
                Vd_color[2,0] = Buffer[2][3]          
                       
        elif turn == "U":
            Buffer[0][0] = Vd_color[0,2]
            Buffer[0][1] = Vd_color[1,1]
            Buffer[0][2] = Vd_color[1,2]
            Buffer[0][3] = Vd_color[1,3]                       

            Buffer[1][0] = Vm_color[0,2]
            Buffer[1][1] = Vm_color[0,3]
            Buffer[1][2] = Vm_color[0,4]
            Buffer[1][3] = Vm_color[1,3]           

            Buffer[2][0] = Az_color[0,0]
            Buffer[2][1] = Az_color[0,1]
            Buffer[2][2] = Az_color[0,2]
            Buffer[2][3] = Az_color[1,1]

            Vm_color[0,4] = Buffer[0][0] 
            Vm_color[0,2] = Buffer[0][1] 
            Vm_color[0,3] = Buffer[0][2] 
            Vm_color[1,3] = Buffer[0][3]

            Az_color[1,1] = Buffer[1][0] 
            Az_color[0,1] = Buffer[1][1] 
            Az_color[0,0] = Buffer[1][2] 
            Az_color[0,2] = Buffer[1][3]                          

            Vd_color[0,2] = Buffer[2][0] 
            Vd_color[1,2] = Buffer[2][1] 
            Vd_color[1,3] = Buffer[2][2] 
            Vd_color[1,1] = Buffer[2][3]

        
        elif turn == "U'":
            for i in range(2):
                Buffer[0][0] = Vd_color[0,2]
                Buffer[0][1] = Vd_color[1,1]
                Buffer[0][2] = Vd_color[1,2]
                Buffer[0][3] = Vd_color[1,3]                       

                Buffer[1][0] = Vm_color[0,2]
                Buffer[1][1] = Vm_color[0,3]
                Buffer[1][2] = Vm_color[0,4]
                Buffer[1][3] = Vm_color[1,3]           

                Buffer[2][0] = Az_color[0,0]
                Buffer[2][1] = Az_color[0,1]
                Buffer[2][2] = Az_color[0,2]
                Buffer[2][3] = Az_color[1,1]

                Vm_color[0,4] = Buffer[0][0] 
                Vm_color[0,2] = Buffer[0][1] 
                Vm_color[0,3] = Buffer[0][2] 
                Vm_color[1,3] = Buffer[0][3]

                Az_color[1,1] = Buffer[1][0] 
                Az_color[0,1] = Buffer[1][1] 
                Az_color[0,0] = Buffer[1][2] 
                Az_color[0,2] = Buffer[1][3]                          

                Vd_color[0,2] = Buffer[2][0] 
                Vd_color[1,2] = Buffer[2][1] 
                Vd_color[1,3] = Buffer[2][2] 
                Vd_color[1,1] = Buffer[2][3]
                                         
        elif turn == "B":

            Buffer[0][0] = Az_color[0,2]
            Buffer[0][1] = Az_color[0,3]
            Buffer[0][2] = Az_color[0,4]
            Buffer[0][3] = Az_color[1,3]

            Buffer[1][0] = Vm_color[0,0]
            Buffer[1][1] = Vm_color[0,1]
            Buffer[1][2] = Vm_color[0,2]
            Buffer[1][3] = Vm_color[1,1]

            Buffer[2][0] = Am_color[1,1]
            Buffer[2][1] = Am_color[1,2]
            Buffer[2][2] = Am_color[1,3]
            Buffer[2][3] = Am_color[2,2] 

            Vm_color[1,1] = Buffer[0][0] 
            Vm_color[0,1] = Buffer[0][1] 
            Vm_color[0,0] = Buffer[0][2] 
            Vm_color[0,2] = Buffer[0][3]

            Am_color[2,2] = Buffer[1][0] 
            Am_color[1,2] = Buffer[1][1] 
            Am_color[1,1] = Buffer[1][2] 
            Am_color[1,3] = Buffer[1][3]

            Az_color[1,3] = Buffer[2][0] 
            Az_color[0,3] = Buffer[2][1] 
            Az_color[0,2] = Buffer[2][2] 
            Az_color[0,4] = Buffer[2][3] 

        elif turn == "B'":
            for i in range(2):
                Buffer[0][0] = Az_color[0,2]
                Buffer[0][1] = Az_color[0,3]
                Buffer[0][2] = Az_color[0,4]
                Buffer[0][3] = Az_color[1,3]

                Buffer[1][0] = Vm_color[0,0]
                Buffer[1][1] = Vm_color[0,1]
                Buffer[1][2] = Vm_color[0,2]
                Buffer[1][3] = Vm_color[1,1]

                Buffer[2][0] = Am_color[1,1]
                Buffer[2][1] = Am_color[1,2]
                Buffer[2][2] = Am_color[1,3]
                Buffer[2][3] = Am_color[2,2] 

                Vm_color[1,1] = Buffer[0][0] 
                Vm_color[0,1] = Buffer[0][1] 
                Vm_color[0,0] = Buffer[0][2] 
                Vm_color[0,2] = Buffer[0][3]

                Am_color[2,2] = Buffer[1][0] 
                Am_color[1,2] = Buffer[1][1] 
                Am_color[1,1] = Buffer[1][2] 
                Am_color[1,3] = Buffer[1][3]

                Az_color[1,3] = Buffer[2][0] 
                Az_color[0,3] = Buffer[2][1] 
                Az_color[0,2] = Buffer[2][2] 
                Az_color[0,4] = Buffer[2][3]          
                                         
        elif turn == "r":
            
            Buffer[0][3] = Vd_color[2,4]            
            Buffer[1][3] = Az_color[2,2]           
            Buffer[2][2] = Am_color[0,4]                
          
            Az_color[2,2] = Buffer[0][3]            
            Am_color[0,4] = Buffer[1][3]          
            Vd_color[2,4] = Buffer[2][2] 
        
        elif turn == "r'":
            for i in range(2):            
                Buffer[0][3] = Vd_color[2,4]            
                Buffer[1][3] = Az_color[2,2]           
                Buffer[2][2] = Am_color[0,4]                
            
                Az_color[2,2] = Buffer[0][3]            
                Am_color[0,4] = Buffer[1][3]          
                Vd_color[2,4] = Buffer[2][2] 
            
        elif turn == "l":
           
            Buffer[0][1] = Vd_color[2,0]   
            Buffer[1][0] = Am_color[0,0]  
            Buffer[2][3] = Vm_color[2,2]


            Am_color[0,0] = Buffer[0][1]         
            Vm_color[2,2] = Buffer[1][0]               
            Vd_color[2,0] = Buffer[2][3]
        
        elif turn == "l'":
            for i in range(2):           
                Buffer[0][1] = Vd_color[2,0]   
                Buffer[1][0] = Am_color[0,0]  
                Buffer[2][3] = Vm_color[2,2]                
                        
                Am_color[0,0] = Buffer[0][1]         
                Vm_color[2,2] = Buffer[1][0]               
                Vd_color[2,0] = Buffer[2][3]           
        
        elif turn == "u":
            Buffer[0][0] = Vd_color[0,2]                         
            Buffer[1][2] = Vm_color[0,4]               
            Buffer[2][0] = Az_color[0,0]
           

            Vm_color[0,4] = Buffer[0][0]   
            Az_color[0,0] = Buffer[1][2]                                 
            Vd_color[0,2] = Buffer[2][0]

        elif turn == "u'":
            for i in range(2):
                Buffer[0][0] = Vd_color[0,2]                         
                Buffer[1][2] = Vm_color[0,4]               
                Buffer[2][0] = Az_color[0,0]            

                Vm_color[0,4] = Buffer[0][0]   
                Az_color[0,0] = Buffer[1][2]                                 
                Vd_color[0,2] = Buffer[2][0]            
        
        elif turn == "b":  
                        
            Buffer[0][2] = Az_color[0,4]          
            Buffer[1][0] = Vm_color[0,0]     
            Buffer[2][3] = Am_color[2,2]

            Vm_color[0,0] = Buffer[0][2]        
            Am_color[2,2] = Buffer[1][0]      
            Az_color[0,4] = Buffer[2][3]      
            
        
        elif turn == "b'":
            for i in range(2):
                Buffer[0][2] = Az_color[0,4]          
                Buffer[1][0] = Vm_color[0,0]     
                Buffer[2][3] = Am_color[2,2]

                Vm_color[0,0] = Buffer[0][2]        
                Am_color[2,2] = Buffer[1][0]      
                Az_color[0,4] = Buffer[2][3]                     


    elif cube == "megaminx":
        pass
    elif cube == "skewb":        
        if turn == "R":

            Buffer[0][0] = Vm_color[0,2]
            Buffer[0][1] = Vm_color[1,1]
            Buffer[0][2] = Vm_color[2,0]
            Buffer[0][3] = Vm_color[2,2]

            Buffer[1][0] = Az_color[0,0]
            Buffer[1][1] = Az_color[1,1]
            Buffer[1][2] = Az_color[2,0]
            Buffer[1][3] = Az_color[2,2]


            Buffer[2][0] = Am_color[0,2]
            Buffer[2][1] = Am_color[1,1]
            Buffer[2][2] = Am_color[2,0]
            Buffer[2][3] = Am_color[2,2]           

            Buffer[3][0] = Vd_color[2,2]
            Buffer[3][1] = Br_color[0,2]            
            Buffer[3][2] = Lr_color[2,0]

            #  =============================================================

            Az_color[2,2] = Buffer[0][0] 
            Az_color[1,1] = Buffer[0][1] 
            Az_color[0,0] = Buffer[0][2] 
            Az_color[2,0] = Buffer[0][3] 

            Am_color[2,0] = Buffer[1][0] 
            Am_color[1,1] = Buffer[1][1] 
            Am_color[2,2] = Buffer[1][2] 
            Am_color[0,2] = Buffer[1][3] 

            Vm_color[0,2] = Buffer[2][0] 
            Vm_color[1,1] = Buffer[2][1] 
            Vm_color[2,0] = Buffer[2][2] 
            Vm_color[2,2] = Buffer[2][3]

            Br_color[0,2] = Buffer[3][0]
            Lr_color[2,0] = Buffer[3][1]
            Vd_color[2,2] = Buffer[3][2]
        
        elif turn == "R'":
            for i in range(2):
                Buffer[0][0] = Vm_color[0,2]
                Buffer[0][1] = Vm_color[1,1]
                Buffer[0][2] = Vm_color[2,0]
                Buffer[0][3] = Vm_color[2,2]

                Buffer[1][0] = Az_color[0,0]
                Buffer[1][1] = Az_color[1,1]
                Buffer[1][2] = Az_color[2,0]
                Buffer[1][3] = Az_color[2,2]


                Buffer[2][0] = Am_color[0,2]
                Buffer[2][1] = Am_color[1,1]
                Buffer[2][2] = Am_color[2,0]
                Buffer[2][3] = Am_color[2,2]           

                Buffer[3][0] = Vd_color[2,2]
                Buffer[3][1] = Br_color[0,2]            
                Buffer[3][2] = Lr_color[2,0]

                #  =============================================================

                Az_color[2,2] = Buffer[0][0] 
                Az_color[1,1] = Buffer[0][1] 
                Az_color[0,0] = Buffer[0][2] 
                Az_color[2,0] = Buffer[0][3] 

                Am_color[2,0] = Buffer[1][0] 
                Am_color[1,1] = Buffer[1][1] 
                Am_color[2,2] = Buffer[1][2] 
                Am_color[0,2] = Buffer[1][3] 

                Vm_color[0,2] = Buffer[2][0] 
                Vm_color[1,1] = Buffer[2][1] 
                Vm_color[2,0] = Buffer[2][2] 
                Vm_color[2,2] = Buffer[2][3]

                Br_color[0,2] = Buffer[3][0]
                Lr_color[2,0] = Buffer[3][1]
                Vd_color[2,2] = Buffer[3][2]
        
        elif turn == "L":
            Buffer[0][0] = Vd_color[0,0]
            Buffer[0][1] = Vd_color[1,1]
            Buffer[0][2] = Vd_color[2,0]
            Buffer[0][3] = Vd_color[2,2]

            Buffer[1][0] = Am_color[0,0]
            Buffer[1][1] = Am_color[0,2]
            Buffer[1][2] = Am_color[1,1]
            Buffer[1][3] = Am_color[2,0]


            Buffer[2][0] = Lr_color[0,2]
            Buffer[2][1] = Lr_color[1,1]
            Buffer[2][2] = Lr_color[2,0]
            Buffer[2][3] = Lr_color[2,2]           

            Buffer[3][0] = Vm_color[2,0]
            Buffer[3][1] = Br_color[2,0]            
            Buffer[3][2] = Az_color[2,2]

            #  =============================================================

            Am_color[0,2] = Buffer[0][0] 
            Am_color[1,1] = Buffer[0][1] 
            Am_color[0,0] = Buffer[0][2] 
            Am_color[2,0] = Buffer[0][3] 

            Lr_color[2,2] = Buffer[1][0] 
            Lr_color[2,0] = Buffer[1][1] 
            Lr_color[1,1] = Buffer[1][2] 
            Lr_color[0,2] = Buffer[1][3] 

            Vd_color[2,2] = Buffer[2][0] 
            Vd_color[1,1] = Buffer[2][1] 
            Vd_color[0,0] = Buffer[2][2] 
            Vd_color[2,0] = Buffer[2][3]

            Az_color[2,2] = Buffer[3][0]
            Vm_color[2,0] = Buffer[3][1]
            Br_color[2,0] = Buffer[3][2]
        
        elif turn == "L'":
            for i in range(2):
                Buffer[0][0] = Vd_color[0,0]
                Buffer[0][1] = Vd_color[1,1]
                Buffer[0][2] = Vd_color[2,0]
                Buffer[0][3] = Vd_color[2,2]

                Buffer[1][0] = Am_color[0,0]
                Buffer[1][1] = Am_color[0,2]
                Buffer[1][2] = Am_color[1,1]
                Buffer[1][3] = Am_color[2,0]


                Buffer[2][0] = Lr_color[0,2]
                Buffer[2][1] = Lr_color[1,1]
                Buffer[2][2] = Lr_color[2,0]
                Buffer[2][3] = Lr_color[2,2]           

                Buffer[3][0] = Vm_color[2,0]
                Buffer[3][1] = Br_color[2,0]            
                Buffer[3][2] = Az_color[2,2]

                #  =============================================================

                Am_color[0,2] = Buffer[0][0] 
                Am_color[1,1] = Buffer[0][1] 
                Am_color[0,0] = Buffer[0][2] 
                Am_color[2,0] = Buffer[0][3] 

                Lr_color[2,2] = Buffer[1][0] 
                Lr_color[2,0] = Buffer[1][1] 
                Lr_color[1,1] = Buffer[1][2] 
                Lr_color[0,2] = Buffer[1][3] 

                Vd_color[2,2] = Buffer[2][0] 
                Vd_color[1,1] = Buffer[2][1] 
                Vd_color[0,0] = Buffer[2][2] 
                Vd_color[2,0] = Buffer[2][3]

                Az_color[2,2] = Buffer[3][0]
                Vm_color[2,0] = Buffer[3][1]
                Br_color[2,0] = Buffer[3][2]
        
        elif turn == "U":
            Buffer[0][0] = Br_color[0,0]
            Buffer[0][1] = Br_color[0,2]
            Buffer[0][2] = Br_color[1,1]
            Buffer[0][3] = Br_color[2,0]

            Buffer[1][0] = Lr_color[0,0]
            Buffer[1][1] = Lr_color[0,2]
            Buffer[1][2] = Lr_color[1,1]
            Buffer[1][3] = Lr_color[2,0]


            Buffer[2][0] = Az_color[0,0]
            Buffer[2][1] = Az_color[0,2]
            Buffer[2][2] = Az_color[1,1]
            Buffer[2][3] = Az_color[2,2]           

            Buffer[3][0] = Vm_color[0,2]
            Buffer[3][1] = Vd_color[0,0]            
            Buffer[3][2] = Am_color[2,0]

            #  =============================================================

            Lr_color[0,0] = Buffer[0][0] 
            Lr_color[0,2] = Buffer[0][1] 
            Lr_color[1,1] = Buffer[0][2] 
            Lr_color[2,0] = Buffer[0][3] 

            Az_color[0,2] = Buffer[1][0] 
            Az_color[2,2] = Buffer[1][1] 
            Az_color[1,1] = Buffer[1][2] 
            Az_color[0,0] = Buffer[1][3] 

            Br_color[2,0] = Buffer[2][0] 
            Br_color[0,0] = Buffer[2][1] 
            Br_color[1,1] = Buffer[2][2] 
            Br_color[0,2] = Buffer[2][3]

            Vd_color[0,0] = Buffer[3][0]
            Am_color[2,0] = Buffer[3][1]
            Vm_color[0,2] = Buffer[3][2]
        
        elif turn == "U'":
            for i in range(2):
                Buffer[0][0] = Br_color[0,0]
                Buffer[0][1] = Br_color[0,2]
                Buffer[0][2] = Br_color[1,1]
                Buffer[0][3] = Br_color[2,0]

                Buffer[1][0] = Lr_color[0,0]
                Buffer[1][1] = Lr_color[0,2]
                Buffer[1][2] = Lr_color[1,1]
                Buffer[1][3] = Lr_color[2,0]


                Buffer[2][0] = Az_color[0,0]
                Buffer[2][1] = Az_color[0,2]
                Buffer[2][2] = Az_color[1,1]
                Buffer[2][3] = Az_color[2,2]           

                Buffer[3][0] = Vm_color[0,2]
                Buffer[3][1] = Vd_color[0,0]            
                Buffer[3][2] = Am_color[2,0]

                #  =============================================================

                Lr_color[0,0] = Buffer[0][0] 
                Lr_color[0,2] = Buffer[0][1] 
                Lr_color[1,1] = Buffer[0][2] 
                Lr_color[2,0] = Buffer[0][3] 

                Az_color[0,2] = Buffer[1][0] 
                Az_color[2,2] = Buffer[1][1] 
                Az_color[1,1] = Buffer[1][2] 
                Az_color[0,0] = Buffer[1][3] 

                Br_color[2,0] = Buffer[2][0] 
                Br_color[0,0] = Buffer[2][1] 
                Br_color[1,1] = Buffer[2][2] 
                Br_color[0,2] = Buffer[2][3]

                Vd_color[0,0] = Buffer[3][0]
                Am_color[2,0] = Buffer[3][1]
                Vm_color[0,2] = Buffer[3][2]
        
        elif turn == "B":
            Buffer[0][0] = Az_color[0,2]
            Buffer[0][1] = Az_color[1,1]
            Buffer[0][2] = Az_color[2,0]
            Buffer[0][3] = Az_color[2,2]

            Buffer[1][0] = Lr_color[0,0]
            Buffer[1][1] = Lr_color[1,1]
            Buffer[1][2] = Lr_color[2,0]
            Buffer[1][3] = Lr_color[2,2]


            Buffer[2][0] = Am_color[0,0]
            Buffer[2][1] = Am_color[1,1]
            Buffer[2][2] = Am_color[2,0]
            Buffer[2][3] = Am_color[2,2]           

            Buffer[3][0] = Vm_color[2,2]
            Buffer[3][1] = Br_color[0,0]            
            Buffer[3][2] = Vd_color[2,0]

            #  =============================================================

            Lr_color[2,2] = Buffer[0][0] 
            Lr_color[1,1] = Buffer[0][1] 
            Lr_color[0,0] = Buffer[0][2] 
            Lr_color[2,0] = Buffer[0][3] 

            Am_color[0,0] = Buffer[1][0] 
            Am_color[1,1] = Buffer[1][1] 
            Am_color[2,0] = Buffer[1][2] 
            Am_color[2,2] = Buffer[1][3] 

            Az_color[2,0] = Buffer[2][0] 
            Az_color[1,1] = Buffer[2][1] 
            Az_color[2,2] = Buffer[2][2] 
            Az_color[0,2] = Buffer[2][3]

            Br_color[0,0] = Buffer[3][0]
            Vd_color[2,0] = Buffer[3][1]
            Vm_color[2,2] = Buffer[3][2]
        
        elif turn == "B'":
            for i in range(2):
                Buffer[0][0] = Az_color[0,2]
                Buffer[0][1] = Az_color[1,1]
                Buffer[0][2] = Az_color[2,0]
                Buffer[0][3] = Az_color[2,2]

                Buffer[1][0] = Lr_color[0,0]
                Buffer[1][1] = Lr_color[1,1]
                Buffer[1][2] = Lr_color[2,0]
                Buffer[1][3] = Lr_color[2,2]


                Buffer[2][0] = Am_color[0,0]
                Buffer[2][1] = Am_color[1,1]
                Buffer[2][2] = Am_color[2,0]
                Buffer[2][3] = Am_color[2,2]           

                Buffer[3][0] = Vm_color[2,2]
                Buffer[3][1] = Br_color[0,0]            
                Buffer[3][2] = Vd_color[2,0]

                #  =============================================================

                Lr_color[2,2] = Buffer[0][0] 
                Lr_color[1,1] = Buffer[0][1] 
                Lr_color[0,0] = Buffer[0][2] 
                Lr_color[2,0] = Buffer[0][3] 

                Am_color[0,0] = Buffer[1][0] 
                Am_color[1,1] = Buffer[1][1] 
                Am_color[2,0] = Buffer[1][2] 
                Am_color[2,2] = Buffer[1][3] 

                Az_color[2,0] = Buffer[2][0] 
                Az_color[1,1] = Buffer[2][1] 
                Az_color[2,2] = Buffer[2][2] 
                Az_color[0,2] = Buffer[2][3]

                Br_color[0,0] = Buffer[3][0]
                Vd_color[2,0] = Buffer[3][1]
                Vm_color[2,2] = Buffer[3][2]
        

        

        
    elif cube == "clock":
        if "UR" in turn:
            pass
        elif "DR" in turn:
            pass
        elif "DL" in turn:
            pass
        elif "UL" in turn:
            pass
        elif "ALL" in turn:
            pass
        elif "U" in turn:
            pass
        elif "R" in turn:
            pass
        elif "D" in turn:
            pass
        elif "L" in turn:
            pass
        

    return Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color


def draw_scramble(cube,Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color):           

    our_canvas.delete("all")    
   
    if cube == "2x2":
        
        #U
        our_canvas.create_rectangle(120,10,165,55, fill=Br_color[0][0])    
        our_canvas.create_rectangle(170,10,215,55, fill=Br_color[0][1])

        our_canvas.create_rectangle(120,60,165,105, fill=Br_color[1][0])
        our_canvas.create_rectangle(170,60,215,105, fill=Br_color[1][1])

        #L
        our_canvas.create_rectangle(10,120,55 ,165,fill=Lr_color[0][0])
        our_canvas.create_rectangle(60,120,105,165,fill=Lr_color[0][1])        

        our_canvas.create_rectangle(10,170,55 ,215,fill=Lr_color[1][0])
        our_canvas.create_rectangle(60,170,105,215,fill=Lr_color[1][1])     

        #F
        our_canvas.create_rectangle(120,120,165,165,fill=Vd_color[0][0])
        our_canvas.create_rectangle(170,120,215,165,fill=Vd_color[0][1])        

        our_canvas.create_rectangle(120,170,165,215,fill=Vd_color[1][0])
        our_canvas.create_rectangle(170,170,215,215,fill=Vd_color[1][1])     


        #R
        our_canvas.create_rectangle(230,120,275,165,fill=Vm_color[0][0])
        our_canvas.create_rectangle(280,120,325,165,fill=Vm_color[0][1])        

        our_canvas.create_rectangle(230,170,275,215,fill=Vm_color[1][0])
        our_canvas.create_rectangle(280,170,325,215,fill=Vm_color[1][1])               

        #B
        our_canvas.create_rectangle(340,120,385,165,fill=Az_color[0][0])
        our_canvas.create_rectangle(390,120,435,165,fill=Az_color[0][1])        

        our_canvas.create_rectangle(340,170,385,215,fill=Az_color[1][0])
        our_canvas.create_rectangle(390,170,435,215,fill=Az_color[1][1])               

        #D
        our_canvas.create_rectangle(120,230,165,275,fill=Am_color[0][0])
        our_canvas.create_rectangle(170,230,215,275,fill=Am_color[0][1])        

        our_canvas.create_rectangle(120,280,165,325,fill=Am_color[1][0])
        our_canvas.create_rectangle(170,280,215,325,fill=Am_color[1][1])           
        

    elif cube == "3x3" or cube == "3x3 OH":
        
        #U
        our_canvas.create_rectangle(120,10,150,40, fill=Br_color[0][0])    
        our_canvas.create_rectangle(155,10,185,40, fill=Br_color[0][1])
        our_canvas.create_rectangle(190,10,220,40, fill=Br_color[0][2])
        

        our_canvas.create_rectangle(120,45,150,75, fill=Br_color[1][0])
        our_canvas.create_rectangle(155,45,185,75, fill=Br_color[1][1])
        our_canvas.create_rectangle(190,45,220,75, fill=Br_color[1][2])

        our_canvas.create_rectangle(120,80,150,110,fill=Br_color[2][0])
        our_canvas.create_rectangle(155,80,185,110,fill=Br_color[2][1])
        our_canvas.create_rectangle(190,80,220,110,fill=Br_color[2][2])


        #L
        our_canvas.create_rectangle(10,120,40 ,150,fill=Lr_color[0][0])
        our_canvas.create_rectangle(45,120,75 ,150,fill=Lr_color[0][1])
        our_canvas.create_rectangle(80,120,110,150,fill=Lr_color[0][2])

        our_canvas.create_rectangle(10,155,40 ,185,fill=Lr_color[1][0])
        our_canvas.create_rectangle(45,155,75 ,185,fill=Lr_color[1][1])
        our_canvas.create_rectangle(80,155,110,185,fill=Lr_color[1][2])

        our_canvas.create_rectangle(10,190,40 ,220,fill=Lr_color[2][0])
        our_canvas.create_rectangle(45,190,75 ,220,fill=Lr_color[2][1])
        our_canvas.create_rectangle(80,190,110,220,fill=Lr_color[2][2])


        #F
        our_canvas.create_rectangle(120,120,150,150,fill=Vd_color[0][0])
        our_canvas.create_rectangle(155,120,185,150,fill=Vd_color[0][1])
        our_canvas.create_rectangle(190,120,220,150,fill=Vd_color[0][2])

        our_canvas.create_rectangle(120,155,150,185,fill=Vd_color[1][0])
        our_canvas.create_rectangle(155,155,185,185,fill=Vd_color[1][1])
        our_canvas.create_rectangle(190,155,220,185,fill=Vd_color[1][2])

        our_canvas.create_rectangle(120,190,150,220,fill=Vd_color[2][0])
        our_canvas.create_rectangle(155,190,185,220,fill=Vd_color[2][1])
        our_canvas.create_rectangle(190,190,220,220,fill=Vd_color[2][2])


        #R
        our_canvas.create_rectangle(230,120,260,150,fill=Vm_color[0][0])
        our_canvas.create_rectangle(265,120,295,150,fill=Vm_color[0][1])
        our_canvas.create_rectangle(300,120,330,150,fill=Vm_color[0][2])

        our_canvas.create_rectangle(230,155,260,185,fill=Vm_color[1][0])
        our_canvas.create_rectangle(265,155,295,185,fill=Vm_color[1][1])
        our_canvas.create_rectangle(300,155,330,185,fill=Vm_color[1][2])

        our_canvas.create_rectangle(230,190,260,220,fill=Vm_color[2][0])
        our_canvas.create_rectangle(265,190,295,220,fill=Vm_color[2][1])
        our_canvas.create_rectangle(300,190,330,220,fill=Vm_color[2][2])


        #B
        our_canvas.create_rectangle(340,120,370,150,fill=Az_color[0][0])
        our_canvas.create_rectangle(375,120,405,150,fill=Az_color[0][1])
        our_canvas.create_rectangle(410,120,440,150,fill=Az_color[0][2])

        our_canvas.create_rectangle(340,155,370,185,fill=Az_color[1][0])
        our_canvas.create_rectangle(375,155,405,185,fill=Az_color[1][1])
        our_canvas.create_rectangle(410,155,440,185,fill=Az_color[1][2])

        our_canvas.create_rectangle(340,190,370,220,fill=Az_color[2][0])
        our_canvas.create_rectangle(375,190,405,220,fill=Az_color[2][1])
        our_canvas.create_rectangle(410,190,440,220,fill=Az_color[2][2])

        #D
        our_canvas.create_rectangle(120,230,150,260,fill=Am_color[0][0])
        our_canvas.create_rectangle(155,230,185,260,fill=Am_color[0][1])
        our_canvas.create_rectangle(190,230,220,260,fill=Am_color[0][2])

        our_canvas.create_rectangle(120,265,150,295,fill=Am_color[1][0])
        our_canvas.create_rectangle(155,265,185,295,fill=Am_color[1][1])
        our_canvas.create_rectangle(190,265,220,295,fill=Am_color[1][2])

        our_canvas.create_rectangle(120,300,150,330,fill=Am_color[2][0])
        our_canvas.create_rectangle(155,300,185,330,fill=Am_color[2][1])
        our_canvas.create_rectangle(190,300,220,330,fill=Am_color[2][2])

    elif cube == "4x4": 

        #U
        our_canvas.create_rectangle(115,10,135,30, fill=Br_color[0][0])    
        our_canvas.create_rectangle(140,10,160,30, fill=Br_color[0][1])
        our_canvas.create_rectangle(165,10,185,30, fill=Br_color[0][2])
        our_canvas.create_rectangle(190,10,210,30, fill=Br_color[0][3])        

        our_canvas.create_rectangle(115,35,135,55, fill=Br_color[1][0])
        our_canvas.create_rectangle(140,35,160,55, fill=Br_color[1][1])
        our_canvas.create_rectangle(165,35,185,55, fill=Br_color[1][2])
        our_canvas.create_rectangle(190,35,210,55, fill=Br_color[1][3])

        our_canvas.create_rectangle(115,60,135,80,fill=Br_color[2][0])
        our_canvas.create_rectangle(140,60,160,80,fill=Br_color[2][1])
        our_canvas.create_rectangle(165,60,185,80,fill=Br_color[2][2])
        our_canvas.create_rectangle(190,60,210,80,fill=Br_color[2][3])

        our_canvas.create_rectangle(115,85,135,105,fill=Br_color[3][0])
        our_canvas.create_rectangle(140,85,160,105,fill=Br_color[3][1])
        our_canvas.create_rectangle(165,85,185,105,fill=Br_color[3][2])
        our_canvas.create_rectangle(190,85,210,105,fill=Br_color[3][3])

        #L
        our_canvas.create_rectangle(10,115,30 ,135,fill=Lr_color[0][0])
        our_canvas.create_rectangle(35,115,55 ,135,fill=Lr_color[0][1])
        our_canvas.create_rectangle(60,115,80 ,135,fill=Lr_color[0][2])
        our_canvas.create_rectangle(85,115,105,135,fill=Lr_color[0][3])

        our_canvas.create_rectangle(10,140,30 ,160,fill=Lr_color[1][0])
        our_canvas.create_rectangle(35,140,55 ,160,fill=Lr_color[1][1])
        our_canvas.create_rectangle(60,140,80 ,160,fill=Lr_color[1][2])
        our_canvas.create_rectangle(85,140,105,160,fill=Lr_color[1][3])

        our_canvas.create_rectangle(10,165,30 ,185,fill=Lr_color[2][0])
        our_canvas.create_rectangle(35,165,55 ,185,fill=Lr_color[2][1])
        our_canvas.create_rectangle(60,165,80 ,185,fill=Lr_color[2][2])
        our_canvas.create_rectangle(85,165,105,185,fill=Lr_color[2][3])

        our_canvas.create_rectangle(10,190,30 ,210,fill=Lr_color[3][0])
        our_canvas.create_rectangle(35,190,55 ,210,fill=Lr_color[3][1])
        our_canvas.create_rectangle(60,190,80 ,210,fill=Lr_color[3][2])
        our_canvas.create_rectangle(85,190,105,210,fill=Lr_color[3][3])


        #F
        our_canvas.create_rectangle(115,115,135,135,fill=Vd_color[0][0])
        our_canvas.create_rectangle(140,115,160,135,fill=Vd_color[0][1])
        our_canvas.create_rectangle(165,115,185,135,fill=Vd_color[0][2])
        our_canvas.create_rectangle(190,115,210,135,fill=Vd_color[0][3])

        our_canvas.create_rectangle(115,140,135,160,fill=Vd_color[1][0])
        our_canvas.create_rectangle(140,140,160,160,fill=Vd_color[1][1])
        our_canvas.create_rectangle(165,140,185,160,fill=Vd_color[1][2])
        our_canvas.create_rectangle(190,140,210,160,fill=Vd_color[1][3])

        our_canvas.create_rectangle(115,165,135,185,fill=Vd_color[2][0])
        our_canvas.create_rectangle(140,165,160,185,fill=Vd_color[2][1])
        our_canvas.create_rectangle(165,165,185,185,fill=Vd_color[2][2])
        our_canvas.create_rectangle(190,165,210,185,fill=Vd_color[2][3])

        our_canvas.create_rectangle(115,190,135,210,fill=Vd_color[3][0])
        our_canvas.create_rectangle(140,190,160,210,fill=Vd_color[3][1])
        our_canvas.create_rectangle(165,190,185,210,fill=Vd_color[3][2])
        our_canvas.create_rectangle(190,190,210,210,fill=Vd_color[3][3])



        #R
        our_canvas.create_rectangle(220,115,240,135,fill=Vm_color[0][0])
        our_canvas.create_rectangle(245,115,265,135,fill=Vm_color[0][1])
        our_canvas.create_rectangle(270,115,290,135,fill=Vm_color[0][2])
        our_canvas.create_rectangle(295,115,315,135,fill=Vm_color[0][3])

        our_canvas.create_rectangle(220,140,240,160,fill=Vm_color[1][0])
        our_canvas.create_rectangle(245,140,265,160,fill=Vm_color[1][1])
        our_canvas.create_rectangle(270,140,290,160,fill=Vm_color[1][2])
        our_canvas.create_rectangle(295,140,315,160,fill=Vm_color[1][3])

        our_canvas.create_rectangle(220,165,240,185,fill=Vm_color[2][0])
        our_canvas.create_rectangle(245,165,265,185,fill=Vm_color[2][1])
        our_canvas.create_rectangle(270,165,290,185,fill=Vm_color[2][2])
        our_canvas.create_rectangle(295,165,315,185,fill=Vm_color[2][3])

        our_canvas.create_rectangle(220,190,240,210,fill=Vm_color[3][0])
        our_canvas.create_rectangle(245,190,265,210,fill=Vm_color[3][1])
        our_canvas.create_rectangle(270,190,290,210,fill=Vm_color[3][2])
        our_canvas.create_rectangle(295,190,315,210,fill=Vm_color[3][3])


        #B
        our_canvas.create_rectangle(325,115,345,135,fill=Az_color[0][0])
        our_canvas.create_rectangle(350,115,370,135,fill=Az_color[0][1])
        our_canvas.create_rectangle(375,115,395,135,fill=Az_color[0][2])
        our_canvas.create_rectangle(400,115,420,135,fill=Az_color[0][3])

        our_canvas.create_rectangle(325,140,345,160,fill=Az_color[1][0])
        our_canvas.create_rectangle(350,140,370,160,fill=Az_color[1][1])
        our_canvas.create_rectangle(375,140,395,160,fill=Az_color[1][2])
        our_canvas.create_rectangle(400,140,420,160,fill=Az_color[1][3])

        our_canvas.create_rectangle(325,165,345,185,fill=Az_color[2][0])
        our_canvas.create_rectangle(350,165,370,185,fill=Az_color[2][1])
        our_canvas.create_rectangle(375,165,395,185,fill=Az_color[2][2])
        our_canvas.create_rectangle(400,165,420,185,fill=Az_color[2][3])

        our_canvas.create_rectangle(325,190,345,210,fill=Az_color[3][0])
        our_canvas.create_rectangle(350,190,370,210,fill=Az_color[3][1])
        our_canvas.create_rectangle(375,190,395,210,fill=Az_color[3][2])
        our_canvas.create_rectangle(400,190,420,210,fill=Az_color[3][3])

        #D
        our_canvas.create_rectangle(115,220,135,240,fill=Am_color[0][0])
        our_canvas.create_rectangle(140,220,160,240,fill=Am_color[0][1])
        our_canvas.create_rectangle(165,220,185,240,fill=Am_color[0][2])
        our_canvas.create_rectangle(190,220,210,240,fill=Am_color[0][3])

        our_canvas.create_rectangle(115,245,135,265,fill=Am_color[1][0])
        our_canvas.create_rectangle(140,245,160,265,fill=Am_color[1][1])
        our_canvas.create_rectangle(165,245,185,265,fill=Am_color[1][2])
        our_canvas.create_rectangle(190,245,210,265,fill=Am_color[1][3])

        our_canvas.create_rectangle(115,270,135,290,fill=Am_color[2][0])
        our_canvas.create_rectangle(140,270,160,290,fill=Am_color[2][1])
        our_canvas.create_rectangle(165,270,185,290,fill=Am_color[2][2])
        our_canvas.create_rectangle(190,270,210,290,fill=Am_color[2][3])

        our_canvas.create_rectangle(115,295,135,315,fill=Am_color[3][0])
        our_canvas.create_rectangle(140,295,160,315,fill=Am_color[3][1])
        our_canvas.create_rectangle(165,295,185,315,fill=Am_color[3][2])
        our_canvas.create_rectangle(190,295,210,315,fill=Am_color[3][3])
        
    elif cube == "5x5":

        #U
        our_canvas.create_rectangle(120,10,138,28,fill=Br_color[0][0])    
        our_canvas.create_rectangle(141,10,159,28,fill=Br_color[0][1])
        our_canvas.create_rectangle(162,10,180,28,fill=Br_color[0][2])
        our_canvas.create_rectangle(183,10,201,28,fill=Br_color[0][3])        
        our_canvas.create_rectangle(204,10,222,28,fill=Br_color[0][4])        

        our_canvas.create_rectangle(120,31,138,49,fill=Br_color[1][0])
        our_canvas.create_rectangle(141,31,159,49,fill=Br_color[1][1])
        our_canvas.create_rectangle(162,31,180,49,fill=Br_color[1][2])
        our_canvas.create_rectangle(183,31,201,49,fill=Br_color[1][3])
        our_canvas.create_rectangle(204,31,222,49,fill=Br_color[1][4])

        our_canvas.create_rectangle(120,52,138,70,fill=Br_color[2][0])
        our_canvas.create_rectangle(141,52,159,70,fill=Br_color[2][1])
        our_canvas.create_rectangle(162,52,180,70,fill=Br_color[2][2])
        our_canvas.create_rectangle(183,52,201,70,fill=Br_color[2][3])
        our_canvas.create_rectangle(204,52,222,70,fill=Br_color[2][4])

        our_canvas.create_rectangle(120,73,138,91,fill=Br_color[3][0])
        our_canvas.create_rectangle(141,73,159,91,fill=Br_color[3][1])
        our_canvas.create_rectangle(162,73,180,91,fill=Br_color[3][2])
        our_canvas.create_rectangle(183,73,201,91,fill=Br_color[3][3])
        our_canvas.create_rectangle(204,73,222,91,fill=Br_color[3][4])

        our_canvas.create_rectangle(120,94,138,112,fill=Br_color[4][0])
        our_canvas.create_rectangle(141,94,159,112,fill=Br_color[4][1])
        our_canvas.create_rectangle(162,94,180,112,fill=Br_color[4][2])
        our_canvas.create_rectangle(183,94,201,112,fill=Br_color[4][3])
        our_canvas.create_rectangle(204,94,222,112,fill=Br_color[4][4])

        #L
        our_canvas.create_rectangle(12,118,30 ,136,fill=Lr_color[0][0])
        our_canvas.create_rectangle(33,118,51 ,136,fill=Lr_color[0][1])
        our_canvas.create_rectangle(54,118,72 ,136,fill=Lr_color[0][2])
        our_canvas.create_rectangle(75,118,93 ,136,fill=Lr_color[0][3])
        our_canvas.create_rectangle(96,118,114,136,fill=Lr_color[0][4])

        our_canvas.create_rectangle(12,139,30 ,157,fill=Lr_color[1][0])
        our_canvas.create_rectangle(33,139,51 ,157,fill=Lr_color[1][1])
        our_canvas.create_rectangle(54,139,72 ,157,fill=Lr_color[1][2])
        our_canvas.create_rectangle(75,139,93 ,157,fill=Lr_color[1][3])
        our_canvas.create_rectangle(96,139,114,157,fill=Lr_color[1][4])

        our_canvas.create_rectangle(12,160,30 ,178,fill=Lr_color[2][0])
        our_canvas.create_rectangle(33,160,51 ,178,fill=Lr_color[2][1])
        our_canvas.create_rectangle(54,160,72 ,178,fill=Lr_color[2][2])
        our_canvas.create_rectangle(75,160,93 ,178,fill=Lr_color[2][3])
        our_canvas.create_rectangle(96,160,114,178,fill=Lr_color[2][4])

        our_canvas.create_rectangle(12,181,30 ,199,fill=Lr_color[3][0])
        our_canvas.create_rectangle(33,181,51 ,199,fill=Lr_color[3][1])
        our_canvas.create_rectangle(54,181,72 ,199,fill=Lr_color[3][2])
        our_canvas.create_rectangle(75,181,93 ,199,fill=Lr_color[3][3])
        our_canvas.create_rectangle(96,181,114,199,fill=Lr_color[3][4])

        our_canvas.create_rectangle(12,202,30 ,220,fill=Lr_color[4][0])
        our_canvas.create_rectangle(33,202,51 ,220,fill=Lr_color[4][1])
        our_canvas.create_rectangle(54,202,72 ,220,fill=Lr_color[4][2])
        our_canvas.create_rectangle(75,202,93 ,220,fill=Lr_color[4][3])
        our_canvas.create_rectangle(96,202,114,220,fill=Lr_color[4][4])


        #F
        our_canvas.create_rectangle(120,118,138,136,fill=Vd_color[0][0])
        our_canvas.create_rectangle(141,118,159,136,fill=Vd_color[0][1])
        our_canvas.create_rectangle(162,118,180,136,fill=Vd_color[0][2])
        our_canvas.create_rectangle(183,118,201,136,fill=Vd_color[0][3])
        our_canvas.create_rectangle(204,118,222,136,fill=Vd_color[0][4])

        our_canvas.create_rectangle(120,139,138,157,fill=Vd_color[1][0])
        our_canvas.create_rectangle(141,139,159,157,fill=Vd_color[1][1])
        our_canvas.create_rectangle(162,139,180,157,fill=Vd_color[1][2])
        our_canvas.create_rectangle(183,139,201,157,fill=Vd_color[1][3])
        our_canvas.create_rectangle(204,139,222,157,fill=Vd_color[1][4])        

        our_canvas.create_rectangle(120,160,138,178,fill=Vd_color[2][0])
        our_canvas.create_rectangle(141,160,159,178,fill=Vd_color[2][1])
        our_canvas.create_rectangle(162,160,180,178,fill=Vd_color[2][2])
        our_canvas.create_rectangle(183,160,201,178,fill=Vd_color[2][3])
        our_canvas.create_rectangle(204,160,222,178,fill=Vd_color[2][4])

        our_canvas.create_rectangle(120,181,138,199,fill=Vd_color[3][0])
        our_canvas.create_rectangle(141,181,159,199,fill=Vd_color[3][1])
        our_canvas.create_rectangle(162,181,180,199,fill=Vd_color[3][2])
        our_canvas.create_rectangle(183,181,201,199,fill=Vd_color[3][3])
        our_canvas.create_rectangle(204,181,222,199,fill=Vd_color[3][4])

        our_canvas.create_rectangle(120,202,138,220,fill=Vd_color[4][0])
        our_canvas.create_rectangle(141,202,159,220,fill=Vd_color[4][1])
        our_canvas.create_rectangle(162,202,180,220,fill=Vd_color[4][2])
        our_canvas.create_rectangle(183,202,201,220,fill=Vd_color[4][3])
        our_canvas.create_rectangle(204,202,222,220,fill=Vd_color[4][4])

        #R
        our_canvas.create_rectangle(228,118,246,136,fill=Vm_color[0][0])
        our_canvas.create_rectangle(249,118,267,136,fill=Vm_color[0][1])
        our_canvas.create_rectangle(270,118,288,136,fill=Vm_color[0][2])
        our_canvas.create_rectangle(291,118,309,136,fill=Vm_color[0][3])
        our_canvas.create_rectangle(312,118,330,136,fill=Vm_color[0][4])

        our_canvas.create_rectangle(228,139,246,157,fill=Vm_color[1][0])
        our_canvas.create_rectangle(249,139,267,157,fill=Vm_color[1][1])
        our_canvas.create_rectangle(270,139,288,157,fill=Vm_color[1][2])
        our_canvas.create_rectangle(291,139,309,157,fill=Vm_color[1][3])
        our_canvas.create_rectangle(312,139,330,157,fill=Vm_color[1][4])

        our_canvas.create_rectangle(228,160,246,178,fill=Vm_color[2][0])
        our_canvas.create_rectangle(249,160,267,178,fill=Vm_color[2][1])
        our_canvas.create_rectangle(270,160,288,178,fill=Vm_color[2][2])
        our_canvas.create_rectangle(291,160,309,178,fill=Vm_color[2][3])
        our_canvas.create_rectangle(312,160,330,178,fill=Vm_color[2][4])

        our_canvas.create_rectangle(228,181,246,199,fill=Vm_color[3][0])
        our_canvas.create_rectangle(249,181,267,199,fill=Vm_color[3][1])
        our_canvas.create_rectangle(270,181,288,199,fill=Vm_color[3][2])
        our_canvas.create_rectangle(291,181,309,199,fill=Vm_color[3][3])
        our_canvas.create_rectangle(312,181,330,199,fill=Vm_color[3][4])

        our_canvas.create_rectangle(228,202,246,220,fill=Vm_color[4][0])
        our_canvas.create_rectangle(249,202,267,220,fill=Vm_color[4][1])
        our_canvas.create_rectangle(270,202,288,220,fill=Vm_color[4][2])
        our_canvas.create_rectangle(291,202,309,220,fill=Vm_color[4][3])
        our_canvas.create_rectangle(312,202,330,220,fill=Vm_color[4][4])


        #B
        our_canvas.create_rectangle(336,118,354,136,fill=Az_color[0][0])
        our_canvas.create_rectangle(357,118,373,136,fill=Az_color[0][1])
        our_canvas.create_rectangle(376,118,395,136,fill=Az_color[0][2])
        our_canvas.create_rectangle(399,118,417,136,fill=Az_color[0][3])
        our_canvas.create_rectangle(420,118,438,136,fill=Az_color[0][4])

        our_canvas.create_rectangle(336,139,354,157,fill=Az_color[1][0])
        our_canvas.create_rectangle(357,139,373,157,fill=Az_color[1][1])
        our_canvas.create_rectangle(376,139,395,157,fill=Az_color[1][2])
        our_canvas.create_rectangle(399,139,417,157,fill=Az_color[1][3])
        our_canvas.create_rectangle(420,139,438,157,fill=Az_color[1][4])

        our_canvas.create_rectangle(336,160,354,178,fill=Az_color[2][0])
        our_canvas.create_rectangle(357,160,373,178,fill=Az_color[2][1])
        our_canvas.create_rectangle(376,160,395,178,fill=Az_color[2][2])
        our_canvas.create_rectangle(399,160,417,178,fill=Az_color[2][3])
        our_canvas.create_rectangle(420,160,438,178,fill=Az_color[2][4])

        our_canvas.create_rectangle(336,181,354,199,fill=Az_color[3][0])
        our_canvas.create_rectangle(357,181,373,199,fill=Az_color[3][1])
        our_canvas.create_rectangle(376,181,395,199,fill=Az_color[3][2])
        our_canvas.create_rectangle(399,181,417,199,fill=Az_color[3][3])
        our_canvas.create_rectangle(420,181,438,199,fill=Az_color[3][4])

        our_canvas.create_rectangle(336,202,354,220,fill=Az_color[4][0])
        our_canvas.create_rectangle(357,202,373,220,fill=Az_color[4][1])
        our_canvas.create_rectangle(376,202,395,220,fill=Az_color[4][2])
        our_canvas.create_rectangle(399,202,417,220,fill=Az_color[4][3])
        our_canvas.create_rectangle(420,202,438,220,fill=Az_color[4][4])

        #D
        our_canvas.create_rectangle(120,226,138,244,fill=Am_color[0][0])
        our_canvas.create_rectangle(141,226,159,244,fill=Am_color[0][1])
        our_canvas.create_rectangle(162,226,180,244,fill=Am_color[0][2])
        our_canvas.create_rectangle(183,226,201,244,fill=Am_color[0][3])
        our_canvas.create_rectangle(204,226,222,244,fill=Am_color[0][4])

        our_canvas.create_rectangle(120,247,138,265,fill=Am_color[1][0])
        our_canvas.create_rectangle(141,247,159,265,fill=Am_color[1][1])
        our_canvas.create_rectangle(162,247,180,265,fill=Am_color[1][2])
        our_canvas.create_rectangle(183,247,201,265,fill=Am_color[1][3])
        our_canvas.create_rectangle(204,247,222,265,fill=Am_color[1][4])

        our_canvas.create_rectangle(120,268,138,286,fill=Am_color[2][0])
        our_canvas.create_rectangle(141,268,159,286,fill=Am_color[2][1])
        our_canvas.create_rectangle(162,268,180,286,fill=Am_color[2][2])
        our_canvas.create_rectangle(183,268,201,286,fill=Am_color[2][3])
        our_canvas.create_rectangle(204,268,222,286,fill=Am_color[2][4])

        our_canvas.create_rectangle(120,289,138,307,fill=Am_color[3][0])
        our_canvas.create_rectangle(141,289,159,307,fill=Am_color[3][1])
        our_canvas.create_rectangle(162,289,180,307,fill=Am_color[3][2])
        our_canvas.create_rectangle(183,289,201,307,fill=Am_color[3][3])
        our_canvas.create_rectangle(204,289,222,307,fill=Am_color[3][4])

        our_canvas.create_rectangle(120,310,138,328,fill=Am_color[4][0])
        our_canvas.create_rectangle(141,310,159,328,fill=Am_color[4][1])
        our_canvas.create_rectangle(162,310,180,328,fill=Am_color[4][2])
        our_canvas.create_rectangle(183,310,201,328,fill=Am_color[4][3])
        our_canvas.create_rectangle(204,310,222,328,fill=Am_color[4][4])
        
    elif cube == "6x6":        

        #U
        our_canvas.create_rectangle(120,10,135,25,fill=Br_color[0][0])    
        our_canvas.create_rectangle(137,10,152,25,fill=Br_color[0][1])
        our_canvas.create_rectangle(154,10,169,25,fill=Br_color[0][2])
        our_canvas.create_rectangle(171,10,186,25,fill=Br_color[0][3])        
        our_canvas.create_rectangle(188,10,203,25,fill=Br_color[0][4])        
        our_canvas.create_rectangle(205,10,220,25,fill=Br_color[0][5])        

        our_canvas.create_rectangle(120,27,135,42,fill=Br_color[1][0])
        our_canvas.create_rectangle(137,27,152,42,fill=Br_color[1][1])
        our_canvas.create_rectangle(154,27,169,42,fill=Br_color[1][2])
        our_canvas.create_rectangle(171,27,186,42,fill=Br_color[1][3])
        our_canvas.create_rectangle(188,27,203,42,fill=Br_color[1][4])
        our_canvas.create_rectangle(205,27,220,42,fill=Br_color[1][5])

        our_canvas.create_rectangle(120,44,135,59,fill=Br_color[2][0])
        our_canvas.create_rectangle(137,44,152,59,fill=Br_color[2][1])
        our_canvas.create_rectangle(154,44,169,59,fill=Br_color[2][2])
        our_canvas.create_rectangle(171,44,186,59,fill=Br_color[2][3])
        our_canvas.create_rectangle(188,44,203,59,fill=Br_color[2][4])
        our_canvas.create_rectangle(205,44,220,59,fill=Br_color[2][5])

        our_canvas.create_rectangle(120,61,135,76,fill=Br_color[3][0])
        our_canvas.create_rectangle(137,61,152,76,fill=Br_color[3][1])
        our_canvas.create_rectangle(154,61,169,76,fill=Br_color[3][2])
        our_canvas.create_rectangle(171,61,186,76,fill=Br_color[3][3])
        our_canvas.create_rectangle(188,61,203,76,fill=Br_color[3][4])
        our_canvas.create_rectangle(205,61,220,76,fill=Br_color[3][5])

        our_canvas.create_rectangle(120,78,135,93,fill=Br_color[4][0])
        our_canvas.create_rectangle(137,78,152,93,fill=Br_color[4][1])
        our_canvas.create_rectangle(154,78,169,93,fill=Br_color[4][2])
        our_canvas.create_rectangle(171,78,186,93,fill=Br_color[4][3])
        our_canvas.create_rectangle(188,78,203,93,fill=Br_color[4][4])
        our_canvas.create_rectangle(205,78,220,93,fill=Br_color[4][5])

        our_canvas.create_rectangle(120,95,135,110,fill=Br_color[5][0])
        our_canvas.create_rectangle(137,95,152,110,fill=Br_color[5][1])
        our_canvas.create_rectangle(154,95,169,110,fill=Br_color[5][2])
        our_canvas.create_rectangle(171,95,186,110,fill=Br_color[5][3])
        our_canvas.create_rectangle(188,95,203,110,fill=Br_color[5][4])
        our_canvas.create_rectangle(205,95,220,110,fill=Br_color[5][5])

        #L
        our_canvas.create_rectangle(10,120,25 ,135,fill=Lr_color[0][0])
        our_canvas.create_rectangle(27,120,42 ,135,fill=Lr_color[0][1])
        our_canvas.create_rectangle(44,120,59 ,135,fill=Lr_color[0][2])
        our_canvas.create_rectangle(61,120,76 ,135,fill=Lr_color[0][3])
        our_canvas.create_rectangle(78,120,93 ,135,fill=Lr_color[0][4])
        our_canvas.create_rectangle(95,120,110,135,fill=Lr_color[0][5])

        our_canvas.create_rectangle(10,137,25 ,152,fill=Lr_color[1][0])
        our_canvas.create_rectangle(27,137,42 ,152,fill=Lr_color[1][1])
        our_canvas.create_rectangle(44,137,59 ,152,fill=Lr_color[1][2])
        our_canvas.create_rectangle(61,137,76 ,152,fill=Lr_color[1][3])
        our_canvas.create_rectangle(78,137,93 ,152,fill=Lr_color[1][4])
        our_canvas.create_rectangle(95,137,110,152,fill=Lr_color[1][5])

        our_canvas.create_rectangle(10,155,25 ,170,fill=Lr_color[2][0])
        our_canvas.create_rectangle(27,155,42 ,170,fill=Lr_color[2][1])
        our_canvas.create_rectangle(44,155,59 ,170,fill=Lr_color[2][2])
        our_canvas.create_rectangle(61,155,76 ,170,fill=Lr_color[2][3])
        our_canvas.create_rectangle(78,155,93 ,170,fill=Lr_color[2][4])
        our_canvas.create_rectangle(95,155,110,170,fill=Lr_color[2][5])

        our_canvas.create_rectangle(10,172,25 ,187,fill=Lr_color[3][0])
        our_canvas.create_rectangle(27,172,42 ,187,fill=Lr_color[3][1])
        our_canvas.create_rectangle(44,172,59 ,187,fill=Lr_color[3][2])
        our_canvas.create_rectangle(61,172,76 ,187,fill=Lr_color[3][3])
        our_canvas.create_rectangle(78,172,93 ,187,fill=Lr_color[3][4])
        our_canvas.create_rectangle(95,172,110,187,fill=Lr_color[3][5])

        our_canvas.create_rectangle(10,189,25 ,204,fill=Lr_color[4][0])
        our_canvas.create_rectangle(27,189,42 ,204,fill=Lr_color[4][1])
        our_canvas.create_rectangle(44,189,59 ,204,fill=Lr_color[4][2])
        our_canvas.create_rectangle(61,189,76 ,204,fill=Lr_color[4][3])
        our_canvas.create_rectangle(78,189,93 ,204,fill=Lr_color[4][4])
        our_canvas.create_rectangle(95,189,110,204,fill=Lr_color[4][5])

        our_canvas.create_rectangle(10,206,25 ,221,fill=Lr_color[5][0])
        our_canvas.create_rectangle(27,206,42 ,221,fill=Lr_color[5][1])
        our_canvas.create_rectangle(44,206,59 ,221,fill=Lr_color[5][2])
        our_canvas.create_rectangle(61,206,76 ,221,fill=Lr_color[5][3])
        our_canvas.create_rectangle(78,206,93 ,221,fill=Lr_color[5][4])
        our_canvas.create_rectangle(95,206,110,221,fill=Lr_color[5][5])


        #F
        our_canvas.create_rectangle(120,120,135,135,fill=Vd_color[0][0])
        our_canvas.create_rectangle(137,120,152,135,fill=Vd_color[0][1])
        our_canvas.create_rectangle(154,120,169,135,fill=Vd_color[0][2])
        our_canvas.create_rectangle(171,120,186,135,fill=Vd_color[0][3])
        our_canvas.create_rectangle(188,120,203,135,fill=Vd_color[0][4])
        our_canvas.create_rectangle(205,120,220,135,fill=Vd_color[0][5])

        our_canvas.create_rectangle(120,137,135,152,fill=Vd_color[1][0])
        our_canvas.create_rectangle(137,137,152,152,fill=Vd_color[1][1])
        our_canvas.create_rectangle(154,137,169,152,fill=Vd_color[1][2])
        our_canvas.create_rectangle(171,137,186,152,fill=Vd_color[1][3])
        our_canvas.create_rectangle(188,137,203,152,fill=Vd_color[1][4])        
        our_canvas.create_rectangle(205,137,220,152,fill=Vd_color[1][5])        

        our_canvas.create_rectangle(120,155,135,170,fill=Vd_color[2][0])
        our_canvas.create_rectangle(137,155,152,170,fill=Vd_color[2][1])
        our_canvas.create_rectangle(154,155,169,170,fill=Vd_color[2][2])
        our_canvas.create_rectangle(171,155,186,170,fill=Vd_color[2][3])
        our_canvas.create_rectangle(188,155,203,170,fill=Vd_color[2][4])
        our_canvas.create_rectangle(205,155,220,170,fill=Vd_color[2][5])

        our_canvas.create_rectangle(120,172,135,187,fill=Vd_color[3][0])
        our_canvas.create_rectangle(137,172,152,187,fill=Vd_color[3][1])
        our_canvas.create_rectangle(154,172,169,187,fill=Vd_color[3][2])
        our_canvas.create_rectangle(171,172,186,187,fill=Vd_color[3][3])
        our_canvas.create_rectangle(188,172,203,187,fill=Vd_color[3][4])
        our_canvas.create_rectangle(205,172,220,187,fill=Vd_color[3][5])

        our_canvas.create_rectangle(120,189,135,204,fill=Vd_color[4][0])
        our_canvas.create_rectangle(137,189,152,204,fill=Vd_color[4][1])
        our_canvas.create_rectangle(154,189,169,204,fill=Vd_color[4][2])
        our_canvas.create_rectangle(171,189,186,204,fill=Vd_color[4][3])
        our_canvas.create_rectangle(188,189,203,204,fill=Vd_color[4][4])
        our_canvas.create_rectangle(205,189,220,204,fill=Vd_color[4][5])

        our_canvas.create_rectangle(120,206,135,221,fill=Vd_color[5][0])
        our_canvas.create_rectangle(137,206,152,221,fill=Vd_color[5][1])
        our_canvas.create_rectangle(154,206,169,221,fill=Vd_color[5][2])
        our_canvas.create_rectangle(171,206,186,221,fill=Vd_color[5][3])
        our_canvas.create_rectangle(188,206,203,221,fill=Vd_color[5][4])
        our_canvas.create_rectangle(205,206,220,221,fill=Vd_color[5][5])

        #R
        our_canvas.create_rectangle(230,120,245,135,fill=Vm_color[0][0])
        our_canvas.create_rectangle(247,120,262,135,fill=Vm_color[0][1])
        our_canvas.create_rectangle(264,120,279,135,fill=Vm_color[0][2])
        our_canvas.create_rectangle(281,120,296,135,fill=Vm_color[0][3])
        our_canvas.create_rectangle(298,120,313,135,fill=Vm_color[0][4])
        our_canvas.create_rectangle(315,120,330,135,fill=Vm_color[0][5])

        our_canvas.create_rectangle(230,137,245,152,fill=Vm_color[1][0])
        our_canvas.create_rectangle(247,137,262,152,fill=Vm_color[1][1])
        our_canvas.create_rectangle(264,137,279,152,fill=Vm_color[1][2])
        our_canvas.create_rectangle(281,137,296,152,fill=Vm_color[1][3])
        our_canvas.create_rectangle(298,137,313,152,fill=Vm_color[1][4])
        our_canvas.create_rectangle(315,137,330,152,fill=Vm_color[1][5])

        our_canvas.create_rectangle(230,155,245,170,fill=Vm_color[2][0])
        our_canvas.create_rectangle(247,155,262,170,fill=Vm_color[2][1])
        our_canvas.create_rectangle(264,155,279,170,fill=Vm_color[2][2])
        our_canvas.create_rectangle(281,155,296,170,fill=Vm_color[2][3])
        our_canvas.create_rectangle(298,155,313,170,fill=Vm_color[2][4])
        our_canvas.create_rectangle(315,155,330,170,fill=Vm_color[2][5])

        our_canvas.create_rectangle(230,172,245,187,fill=Vm_color[3][0])
        our_canvas.create_rectangle(247,172,262,187,fill=Vm_color[3][1])
        our_canvas.create_rectangle(264,172,279,187,fill=Vm_color[3][2])
        our_canvas.create_rectangle(281,172,296,187,fill=Vm_color[3][3])
        our_canvas.create_rectangle(298,172,313,187,fill=Vm_color[3][4])
        our_canvas.create_rectangle(315,172,330,187,fill=Vm_color[3][5])

        our_canvas.create_rectangle(230,189,245,204,fill=Vm_color[4][0])
        our_canvas.create_rectangle(247,189,262,204,fill=Vm_color[4][1])
        our_canvas.create_rectangle(264,189,279,204,fill=Vm_color[4][2])
        our_canvas.create_rectangle(281,189,296,204,fill=Vm_color[4][3])
        our_canvas.create_rectangle(298,189,313,204,fill=Vm_color[4][4])
        our_canvas.create_rectangle(315,189,330,204,fill=Vm_color[4][5])

        our_canvas.create_rectangle(230,206,245,221,fill=Vm_color[5][0])
        our_canvas.create_rectangle(247,206,262,221,fill=Vm_color[5][1])
        our_canvas.create_rectangle(264,206,279,221,fill=Vm_color[5][2])
        our_canvas.create_rectangle(281,206,296,221,fill=Vm_color[5][3])
        our_canvas.create_rectangle(298,206,313,221,fill=Vm_color[5][4])
        our_canvas.create_rectangle(315,206,330,221,fill=Vm_color[5][5])


        #B
        our_canvas.create_rectangle(340,120,355,135,fill=Az_color[0][0])
        our_canvas.create_rectangle(357,120,372,135,fill=Az_color[0][1])
        our_canvas.create_rectangle(374,120,389,135,fill=Az_color[0][2])
        our_canvas.create_rectangle(391,120,406,135,fill=Az_color[0][3])
        our_canvas.create_rectangle(408,120,423,135,fill=Az_color[0][4])
        our_canvas.create_rectangle(425,120,440,135,fill=Az_color[0][5])

        our_canvas.create_rectangle(340,137,355,152,fill=Az_color[1][0])
        our_canvas.create_rectangle(357,137,372,152,fill=Az_color[1][1])
        our_canvas.create_rectangle(374,137,389,152,fill=Az_color[1][2])
        our_canvas.create_rectangle(391,137,406,152,fill=Az_color[1][3])
        our_canvas.create_rectangle(408,137,423,152,fill=Az_color[1][4])
        our_canvas.create_rectangle(425,137,440,152,fill=Az_color[1][5])

        our_canvas.create_rectangle(340,155,355,170,fill=Az_color[2][0])
        our_canvas.create_rectangle(357,155,372,170,fill=Az_color[2][1])
        our_canvas.create_rectangle(374,155,389,170,fill=Az_color[2][2])
        our_canvas.create_rectangle(391,155,406,170,fill=Az_color[2][3])
        our_canvas.create_rectangle(408,155,423,170,fill=Az_color[2][4])
        our_canvas.create_rectangle(425,155,440,170,fill=Az_color[2][5])

        our_canvas.create_rectangle(340,172,355,187,fill=Az_color[3][0])
        our_canvas.create_rectangle(357,172,372,187,fill=Az_color[3][1])
        our_canvas.create_rectangle(374,172,389,187,fill=Az_color[3][2])
        our_canvas.create_rectangle(391,172,406,187,fill=Az_color[3][3])
        our_canvas.create_rectangle(408,172,423,187,fill=Az_color[3][4])
        our_canvas.create_rectangle(425,172,440,187,fill=Az_color[3][5])

        our_canvas.create_rectangle(340,189,355,204,fill=Az_color[4][0])
        our_canvas.create_rectangle(357,189,372,204,fill=Az_color[4][1])
        our_canvas.create_rectangle(374,189,389,204,fill=Az_color[4][2])
        our_canvas.create_rectangle(391,189,406,204,fill=Az_color[4][3])
        our_canvas.create_rectangle(408,189,423,204,fill=Az_color[4][4])
        our_canvas.create_rectangle(425,189,440,204,fill=Az_color[4][5])

        our_canvas.create_rectangle(340,206,355,221,fill=Az_color[5][0])
        our_canvas.create_rectangle(357,206,372,221,fill=Az_color[5][1])
        our_canvas.create_rectangle(374,206,389,221,fill=Az_color[5][2])
        our_canvas.create_rectangle(391,206,406,221,fill=Az_color[5][3])
        our_canvas.create_rectangle(408,206,423,221,fill=Az_color[5][4])
        our_canvas.create_rectangle(425,206,440,221,fill=Az_color[5][5])

        #D
        our_canvas.create_rectangle(120,230,135,245,fill=Am_color[0][0])
        our_canvas.create_rectangle(137,230,152,245,fill=Am_color[0][1])
        our_canvas.create_rectangle(154,230,169,245,fill=Am_color[0][2])
        our_canvas.create_rectangle(171,230,186,245,fill=Am_color[0][3])
        our_canvas.create_rectangle(188,230,203,245,fill=Am_color[0][4])
        our_canvas.create_rectangle(205,230,220,245,fill=Am_color[0][5])

        our_canvas.create_rectangle(120,247,135,262,fill=Am_color[1][0])
        our_canvas.create_rectangle(137,247,152,262,fill=Am_color[1][1])
        our_canvas.create_rectangle(154,247,169,262,fill=Am_color[1][2])
        our_canvas.create_rectangle(171,247,186,262,fill=Am_color[1][3])
        our_canvas.create_rectangle(188,247,203,262,fill=Am_color[1][4])
        our_canvas.create_rectangle(205,247,220,262,fill=Am_color[1][5])

        our_canvas.create_rectangle(120,264,135,279,fill=Am_color[2][0])
        our_canvas.create_rectangle(137,264,152,279,fill=Am_color[2][1])
        our_canvas.create_rectangle(154,264,169,279,fill=Am_color[2][2])
        our_canvas.create_rectangle(171,264,186,279,fill=Am_color[2][3])
        our_canvas.create_rectangle(188,264,203,279,fill=Am_color[2][4])
        our_canvas.create_rectangle(205,264,220,279,fill=Am_color[2][5])

        our_canvas.create_rectangle(120,281,135,296,fill=Am_color[3][0])
        our_canvas.create_rectangle(137,281,152,296,fill=Am_color[3][1])
        our_canvas.create_rectangle(154,281,169,296,fill=Am_color[3][2])
        our_canvas.create_rectangle(171,281,186,296,fill=Am_color[3][3])
        our_canvas.create_rectangle(188,281,203,296,fill=Am_color[3][4])
        our_canvas.create_rectangle(205,281,220,296,fill=Am_color[3][5])

        our_canvas.create_rectangle(120,298,135,313,fill=Am_color[4][0])
        our_canvas.create_rectangle(137,298,152,313,fill=Am_color[4][1])
        our_canvas.create_rectangle(154,298,169,313,fill=Am_color[4][2])
        our_canvas.create_rectangle(171,298,186,313,fill=Am_color[4][3])
        our_canvas.create_rectangle(188,298,203,313,fill=Am_color[4][4])
        our_canvas.create_rectangle(205,298,220,313,fill=Am_color[4][5])

        our_canvas.create_rectangle(120,315,135,330,fill=Am_color[5][0])
        our_canvas.create_rectangle(137,315,152,330,fill=Am_color[5][1])
        our_canvas.create_rectangle(154,315,169,330,fill=Am_color[5][2])
        our_canvas.create_rectangle(171,315,186,330,fill=Am_color[5][3])
        our_canvas.create_rectangle(188,315,203,330,fill=Am_color[5][4])
        our_canvas.create_rectangle(205,315,220,330,fill=Am_color[5][5])
        
    elif cube == "7x7":        

        #U
        our_canvas.create_rectangle(120,10,133,23,fill=Br_color[0][0])    
        our_canvas.create_rectangle(135,10,148,23,fill=Br_color[0][1])
        our_canvas.create_rectangle(150,10,163,23,fill=Br_color[0][2])
        our_canvas.create_rectangle(165,10,178,23,fill=Br_color[0][3])        
        our_canvas.create_rectangle(180,10,193,23,fill=Br_color[0][4])        
        our_canvas.create_rectangle(195,10,208,23,fill=Br_color[0][5])        
        our_canvas.create_rectangle(210,10,223,23,fill=Br_color[0][6])        

        our_canvas.create_rectangle(120,25,133,38,fill=Br_color[1][0])
        our_canvas.create_rectangle(135,25,148,38,fill=Br_color[1][1])
        our_canvas.create_rectangle(150,25,163,38,fill=Br_color[1][2])
        our_canvas.create_rectangle(165,25,178,38,fill=Br_color[1][3])
        our_canvas.create_rectangle(180,25,193,38,fill=Br_color[1][4])
        our_canvas.create_rectangle(195,25,208,38,fill=Br_color[1][5])
        our_canvas.create_rectangle(210,25,223,38,fill=Br_color[1][6])

        our_canvas.create_rectangle(120,40,133,53,fill=Br_color[2][0])
        our_canvas.create_rectangle(135,40,148,53,fill=Br_color[2][1])
        our_canvas.create_rectangle(150,40,163,53,fill=Br_color[2][2])
        our_canvas.create_rectangle(165,40,178,53,fill=Br_color[2][3])
        our_canvas.create_rectangle(180,40,192,53,fill=Br_color[2][4])
        our_canvas.create_rectangle(195,40,208,53,fill=Br_color[2][5])
        our_canvas.create_rectangle(210,40,223,53,fill=Br_color[2][6])

        our_canvas.create_rectangle(120,55,133,68,fill=Br_color[3][0])
        our_canvas.create_rectangle(135,55,148,68,fill=Br_color[3][1])
        our_canvas.create_rectangle(150,55,163,68,fill=Br_color[3][2])
        our_canvas.create_rectangle(165,55,178,68,fill=Br_color[3][3])
        our_canvas.create_rectangle(180,55,192,68,fill=Br_color[3][4])
        our_canvas.create_rectangle(195,55,208,68,fill=Br_color[3][5])
        our_canvas.create_rectangle(210,55,223,68,fill=Br_color[3][6])

        our_canvas.create_rectangle(120,70,133,83,fill=Br_color[4][0])
        our_canvas.create_rectangle(135,70,148,83,fill=Br_color[4][1])
        our_canvas.create_rectangle(150,70,163,83,fill=Br_color[4][2])
        our_canvas.create_rectangle(165,70,178,83,fill=Br_color[4][3])
        our_canvas.create_rectangle(180,70,192,83,fill=Br_color[4][4])
        our_canvas.create_rectangle(195,70,208,83,fill=Br_color[4][5])
        our_canvas.create_rectangle(210,70,223,83,fill=Br_color[4][6])

        our_canvas.create_rectangle(120,85,133,98,fill=Br_color[5][0])
        our_canvas.create_rectangle(135,85,148,98,fill=Br_color[5][1])
        our_canvas.create_rectangle(150,85,163,98,fill=Br_color[5][2])
        our_canvas.create_rectangle(165,85,178,98,fill=Br_color[5][3])
        our_canvas.create_rectangle(180,85,192,98,fill=Br_color[5][4])
        our_canvas.create_rectangle(195,85,208,98,fill=Br_color[5][5])
        our_canvas.create_rectangle(210,85,223,98,fill=Br_color[5][6])

        our_canvas.create_rectangle(120,100,133,113,fill=Br_color[6][0])
        our_canvas.create_rectangle(135,100,148,113,fill=Br_color[6][1])
        our_canvas.create_rectangle(150,100,163,113,fill=Br_color[6][2])
        our_canvas.create_rectangle(165,100,178,113,fill=Br_color[6][3])
        our_canvas.create_rectangle(180,100,192,113,fill=Br_color[6][4])
        our_canvas.create_rectangle(195,100,208,113,fill=Br_color[6][5])
        our_canvas.create_rectangle(210,100,223,113,fill=Br_color[6][6])

        #L
        our_canvas.create_rectangle(10 ,120,23 ,133,fill=Lr_color[0][0])
        our_canvas.create_rectangle(25 ,120,38 ,133,fill=Lr_color[0][1])
        our_canvas.create_rectangle(40 ,120,53 ,133,fill=Lr_color[0][2])
        our_canvas.create_rectangle(55 ,120,68 ,133,fill=Lr_color[0][3])
        our_canvas.create_rectangle(70 ,120,83 ,133,fill=Lr_color[0][4])
        our_canvas.create_rectangle(85 ,120,98 ,133,fill=Lr_color[0][5])
        our_canvas.create_rectangle(100,120,113,133,fill=Lr_color[0][6])

        our_canvas.create_rectangle(10 ,135,23 ,148,fill=Lr_color[1][0])
        our_canvas.create_rectangle(25 ,135,38 ,148,fill=Lr_color[1][1])
        our_canvas.create_rectangle(40 ,135,53 ,148,fill=Lr_color[1][2])
        our_canvas.create_rectangle(55 ,135,68 ,148,fill=Lr_color[1][3])
        our_canvas.create_rectangle(70 ,135,83 ,148,fill=Lr_color[1][4])
        our_canvas.create_rectangle(85 ,135,98 ,148,fill=Lr_color[1][5])
        our_canvas.create_rectangle(100,135,113,148,fill=Lr_color[1][6])

        our_canvas.create_rectangle(10 ,150,23 ,163,fill=Lr_color[2][0])
        our_canvas.create_rectangle(25 ,150,38 ,163,fill=Lr_color[2][1])
        our_canvas.create_rectangle(40 ,150,53 ,163,fill=Lr_color[2][2])
        our_canvas.create_rectangle(55 ,150,68 ,163,fill=Lr_color[2][3])
        our_canvas.create_rectangle(70 ,150,83 ,163,fill=Lr_color[2][4])
        our_canvas.create_rectangle(85 ,150,98 ,163,fill=Lr_color[2][5])
        our_canvas.create_rectangle(100,150,113,163,fill=Lr_color[2][6])

        our_canvas.create_rectangle(10 ,165,23 ,178,fill=Lr_color[3][0])
        our_canvas.create_rectangle(25 ,165,38 ,178,fill=Lr_color[3][1])
        our_canvas.create_rectangle(40 ,165,53 ,178,fill=Lr_color[3][2])
        our_canvas.create_rectangle(55 ,165,68 ,178,fill=Lr_color[3][3])
        our_canvas.create_rectangle(70 ,165,83 ,178,fill=Lr_color[3][4])
        our_canvas.create_rectangle(85 ,165,98 ,178,fill=Lr_color[3][5])
        our_canvas.create_rectangle(100,165,113,178,fill=Lr_color[3][6])

        our_canvas.create_rectangle(10 ,180,23 ,193,fill=Lr_color[4][0])
        our_canvas.create_rectangle(25 ,180,38 ,193,fill=Lr_color[4][1])
        our_canvas.create_rectangle(40 ,180,53 ,193,fill=Lr_color[4][2])
        our_canvas.create_rectangle(55 ,180,68 ,193,fill=Lr_color[4][3])
        our_canvas.create_rectangle(70 ,180,83 ,193,fill=Lr_color[4][4])
        our_canvas.create_rectangle(85 ,180,98 ,193,fill=Lr_color[4][5])
        our_canvas.create_rectangle(100,180,113,193,fill=Lr_color[4][6])

        our_canvas.create_rectangle(10 ,195,23 ,208,fill=Lr_color[5][0])
        our_canvas.create_rectangle(25 ,195,38 ,208,fill=Lr_color[5][1])
        our_canvas.create_rectangle(40 ,195,53 ,208,fill=Lr_color[5][2])
        our_canvas.create_rectangle(55 ,195,68 ,208,fill=Lr_color[5][3])
        our_canvas.create_rectangle(70 ,195,83 ,208,fill=Lr_color[5][4])
        our_canvas.create_rectangle(85 ,195,98 ,208,fill=Lr_color[5][5])
        our_canvas.create_rectangle(100,195,113,208,fill=Lr_color[5][6])

        our_canvas.create_rectangle(10 ,210,23 ,223,fill=Lr_color[6][0])
        our_canvas.create_rectangle(25 ,210,38 ,223,fill=Lr_color[6][1])
        our_canvas.create_rectangle(40 ,210,53 ,223,fill=Lr_color[6][2])
        our_canvas.create_rectangle(55 ,210,68 ,223,fill=Lr_color[6][3])
        our_canvas.create_rectangle(70 ,210,83 ,223,fill=Lr_color[6][4])
        our_canvas.create_rectangle(85 ,210,98 ,223,fill=Lr_color[6][5])
        our_canvas.create_rectangle(100,210,113,223,fill=Lr_color[6][6])


        #F
        our_canvas.create_rectangle(120,120,133,133,fill=Vd_color[0][0])
        our_canvas.create_rectangle(135,120,148,133,fill=Vd_color[0][1])
        our_canvas.create_rectangle(150,120,163,133,fill=Vd_color[0][2])
        our_canvas.create_rectangle(165,120,178,133,fill=Vd_color[0][3])
        our_canvas.create_rectangle(180,120,193,133,fill=Vd_color[0][4])
        our_canvas.create_rectangle(195,120,208,133,fill=Vd_color[0][5])
        our_canvas.create_rectangle(210,120,223,133,fill=Vd_color[0][6])

        our_canvas.create_rectangle(120,135,133,148,fill=Vd_color[1][0])
        our_canvas.create_rectangle(135,135,148,148,fill=Vd_color[1][1])
        our_canvas.create_rectangle(150,135,163,148,fill=Vd_color[1][2])
        our_canvas.create_rectangle(165,135,178,148,fill=Vd_color[1][3])
        our_canvas.create_rectangle(180,135,193,148,fill=Vd_color[1][4])        
        our_canvas.create_rectangle(195,135,208,148,fill=Vd_color[1][5])        
        our_canvas.create_rectangle(210,135,223,148,fill=Vd_color[1][6])        

        our_canvas.create_rectangle(120,150,133,163,fill=Vd_color[2][0])
        our_canvas.create_rectangle(135,150,148,163,fill=Vd_color[2][1])
        our_canvas.create_rectangle(150,150,163,163,fill=Vd_color[2][2])
        our_canvas.create_rectangle(165,150,178,163,fill=Vd_color[2][3])
        our_canvas.create_rectangle(180,150,193,163,fill=Vd_color[2][4])
        our_canvas.create_rectangle(195,150,208,163,fill=Vd_color[2][5])
        our_canvas.create_rectangle(210,150,223,163,fill=Vd_color[2][6])

        our_canvas.create_rectangle(120,165,133,178,fill=Vd_color[3][0])
        our_canvas.create_rectangle(135,165,148,178,fill=Vd_color[3][1])
        our_canvas.create_rectangle(150,165,163,178,fill=Vd_color[3][2])
        our_canvas.create_rectangle(165,165,178,178,fill=Vd_color[3][3])
        our_canvas.create_rectangle(180,165,193,178,fill=Vd_color[3][4])
        our_canvas.create_rectangle(195,165,208,178,fill=Vd_color[3][5])
        our_canvas.create_rectangle(210,165,223,178,fill=Vd_color[3][6])

        our_canvas.create_rectangle(120,180,133,193,fill=Vd_color[4][0])
        our_canvas.create_rectangle(135,180,148,193,fill=Vd_color[4][1])
        our_canvas.create_rectangle(150,180,163,193,fill=Vd_color[4][2])
        our_canvas.create_rectangle(165,180,178,193,fill=Vd_color[4][3])
        our_canvas.create_rectangle(180,180,193,193,fill=Vd_color[4][4])
        our_canvas.create_rectangle(195,180,208,193,fill=Vd_color[4][5])
        our_canvas.create_rectangle(210,180,223,193,fill=Vd_color[4][6])

        our_canvas.create_rectangle(120,195,133,208,fill=Vd_color[5][0])
        our_canvas.create_rectangle(135,195,148,208,fill=Vd_color[5][1])
        our_canvas.create_rectangle(150,195,163,208,fill=Vd_color[5][2])
        our_canvas.create_rectangle(165,195,178,208,fill=Vd_color[5][3])
        our_canvas.create_rectangle(180,195,193,208,fill=Vd_color[5][4])
        our_canvas.create_rectangle(195,195,208,208,fill=Vd_color[5][5])
        our_canvas.create_rectangle(210,195,223,208,fill=Vd_color[5][6])

        our_canvas.create_rectangle(120,210,133,223,fill=Vd_color[6][0])
        our_canvas.create_rectangle(135,210,148,223,fill=Vd_color[6][1])
        our_canvas.create_rectangle(150,210,163,223,fill=Vd_color[6][2])
        our_canvas.create_rectangle(165,210,178,223,fill=Vd_color[6][3])
        our_canvas.create_rectangle(180,210,193,223,fill=Vd_color[6][4])
        our_canvas.create_rectangle(195,210,208,223,fill=Vd_color[6][5])
        our_canvas.create_rectangle(210,210,223,223,fill=Vd_color[6][6])

        #R
        our_canvas.create_rectangle(230,120,243,133,fill=Vm_color[0][0])
        our_canvas.create_rectangle(245,120,258,133,fill=Vm_color[0][1])
        our_canvas.create_rectangle(260,120,273,133,fill=Vm_color[0][2])
        our_canvas.create_rectangle(275,120,288,133,fill=Vm_color[0][3])
        our_canvas.create_rectangle(290,120,303,133,fill=Vm_color[0][4])
        our_canvas.create_rectangle(305,120,318,133,fill=Vm_color[0][5])
        our_canvas.create_rectangle(320,120,333,133,fill=Vm_color[0][6])

        our_canvas.create_rectangle(230,135,243,148,fill=Vm_color[1][0])
        our_canvas.create_rectangle(245,135,258,148,fill=Vm_color[1][1])
        our_canvas.create_rectangle(260,135,273,148,fill=Vm_color[1][2])
        our_canvas.create_rectangle(275,135,288,148,fill=Vm_color[1][3])
        our_canvas.create_rectangle(290,135,303,148,fill=Vm_color[1][4])
        our_canvas.create_rectangle(305,135,318,148,fill=Vm_color[1][5])
        our_canvas.create_rectangle(320,135,333,148,fill=Vm_color[1][6])

        our_canvas.create_rectangle(230,150,243,163,fill=Vm_color[2][0])
        our_canvas.create_rectangle(245,150,258,163,fill=Vm_color[2][1])
        our_canvas.create_rectangle(260,150,273,163,fill=Vm_color[2][2])
        our_canvas.create_rectangle(275,150,288,163,fill=Vm_color[2][3])
        our_canvas.create_rectangle(290,150,303,163,fill=Vm_color[2][4])
        our_canvas.create_rectangle(305,150,318,163,fill=Vm_color[2][5])
        our_canvas.create_rectangle(320,150,333,163,fill=Vm_color[2][6])

        our_canvas.create_rectangle(230,165,243,178,fill=Vm_color[3][0])
        our_canvas.create_rectangle(245,165,258,178,fill=Vm_color[3][1])
        our_canvas.create_rectangle(260,165,273,178,fill=Vm_color[3][2])
        our_canvas.create_rectangle(275,165,288,178,fill=Vm_color[3][3])
        our_canvas.create_rectangle(290,165,303,178,fill=Vm_color[3][4])
        our_canvas.create_rectangle(305,165,318,178,fill=Vm_color[3][5])
        our_canvas.create_rectangle(320,165,333,178,fill=Vm_color[3][6])

        our_canvas.create_rectangle(230,180,243,193,fill=Vm_color[4][0])
        our_canvas.create_rectangle(245,180,258,193,fill=Vm_color[4][1])
        our_canvas.create_rectangle(260,180,273,193,fill=Vm_color[4][2])
        our_canvas.create_rectangle(275,180,288,193,fill=Vm_color[4][3])
        our_canvas.create_rectangle(290,180,303,193,fill=Vm_color[4][4])
        our_canvas.create_rectangle(305,180,318,193,fill=Vm_color[4][5])
        our_canvas.create_rectangle(320,180,333,193,fill=Vm_color[4][6])

        our_canvas.create_rectangle(230,195,243,208,fill=Vm_color[5][0])
        our_canvas.create_rectangle(245,195,258,208,fill=Vm_color[5][1])
        our_canvas.create_rectangle(260,195,273,208,fill=Vm_color[5][2])
        our_canvas.create_rectangle(275,195,288,208,fill=Vm_color[5][3])
        our_canvas.create_rectangle(290,195,303,208,fill=Vm_color[5][4])
        our_canvas.create_rectangle(305,195,318,208,fill=Vm_color[5][5])
        our_canvas.create_rectangle(320,195,333,208,fill=Vm_color[5][6])

        our_canvas.create_rectangle(230,210,243,223,fill=Vm_color[6][0])
        our_canvas.create_rectangle(245,210,258,223,fill=Vm_color[6][1])
        our_canvas.create_rectangle(260,210,273,223,fill=Vm_color[6][2])
        our_canvas.create_rectangle(275,210,288,223,fill=Vm_color[6][3])
        our_canvas.create_rectangle(290,210,303,223,fill=Vm_color[6][4])
        our_canvas.create_rectangle(305,210,318,223,fill=Vm_color[6][5])
        our_canvas.create_rectangle(320,210,333,223,fill=Vm_color[6][6])


        #B
        our_canvas.create_rectangle(340,120,353,133,fill=Az_color[0][0])
        our_canvas.create_rectangle(355,120,368,133,fill=Az_color[0][1])
        our_canvas.create_rectangle(370,120,383,133,fill=Az_color[0][2])
        our_canvas.create_rectangle(385,120,398,133,fill=Az_color[0][3])
        our_canvas.create_rectangle(400,120,413,133,fill=Az_color[0][4])
        our_canvas.create_rectangle(415,120,428,133,fill=Az_color[0][5])
        our_canvas.create_rectangle(430,120,443,133,fill=Az_color[0][6])

        our_canvas.create_rectangle(340,135,353,148,fill=Az_color[1][0])
        our_canvas.create_rectangle(355,135,368,148,fill=Az_color[1][1])
        our_canvas.create_rectangle(370,135,383,148,fill=Az_color[1][2])
        our_canvas.create_rectangle(385,135,398,148,fill=Az_color[1][3])
        our_canvas.create_rectangle(400,135,413,148,fill=Az_color[1][4])
        our_canvas.create_rectangle(415,135,428,148,fill=Az_color[1][5])
        our_canvas.create_rectangle(430,135,443,148,fill=Az_color[1][6])

        our_canvas.create_rectangle(340,150,353,163,fill=Az_color[2][0])
        our_canvas.create_rectangle(355,150,368,163,fill=Az_color[2][1])
        our_canvas.create_rectangle(370,150,383,163,fill=Az_color[2][2])
        our_canvas.create_rectangle(385,150,398,163,fill=Az_color[2][3])
        our_canvas.create_rectangle(400,150,413,163,fill=Az_color[2][4])
        our_canvas.create_rectangle(415,150,428,163,fill=Az_color[2][5])
        our_canvas.create_rectangle(430,150,443,163,fill=Az_color[2][6])

        our_canvas.create_rectangle(340,165,353,178,fill=Az_color[3][0])
        our_canvas.create_rectangle(355,165,368,178,fill=Az_color[3][1])
        our_canvas.create_rectangle(370,165,383,178,fill=Az_color[3][2])
        our_canvas.create_rectangle(385,165,398,178,fill=Az_color[3][3])
        our_canvas.create_rectangle(400,165,413,178,fill=Az_color[3][4])
        our_canvas.create_rectangle(415,165,428,178,fill=Az_color[3][5])
        our_canvas.create_rectangle(430,165,443,178,fill=Az_color[3][6])

        our_canvas.create_rectangle(340,180,353,193,fill=Az_color[4][0])
        our_canvas.create_rectangle(355,180,368,193,fill=Az_color[4][1])
        our_canvas.create_rectangle(370,180,383,193,fill=Az_color[4][2])
        our_canvas.create_rectangle(385,180,398,193,fill=Az_color[4][3])
        our_canvas.create_rectangle(400,180,413,193,fill=Az_color[4][4])
        our_canvas.create_rectangle(415,180,428,193,fill=Az_color[4][5])
        our_canvas.create_rectangle(430,180,443,193,fill=Az_color[4][6])

        our_canvas.create_rectangle(340,195,353,208,fill=Az_color[5][0])
        our_canvas.create_rectangle(355,195,368,208,fill=Az_color[5][1])
        our_canvas.create_rectangle(370,195,383,208,fill=Az_color[5][2])
        our_canvas.create_rectangle(385,195,398,208,fill=Az_color[5][3])
        our_canvas.create_rectangle(400,195,413,208,fill=Az_color[5][4])
        our_canvas.create_rectangle(415,195,428,208,fill=Az_color[5][5])
        our_canvas.create_rectangle(430,195,443,208,fill=Az_color[5][6])

        our_canvas.create_rectangle(340,210,353,223,fill=Az_color[6][0])
        our_canvas.create_rectangle(355,210,368,223,fill=Az_color[6][1])
        our_canvas.create_rectangle(370,210,383,223,fill=Az_color[6][2])
        our_canvas.create_rectangle(385,210,398,223,fill=Az_color[6][3])
        our_canvas.create_rectangle(400,210,413,223,fill=Az_color[6][4])
        our_canvas.create_rectangle(415,210,428,223,fill=Az_color[6][5])
        our_canvas.create_rectangle(430,210,443,223,fill=Az_color[6][6])

        #D
        our_canvas.create_rectangle(120,230,133,243,fill=Am_color[0][0])
        our_canvas.create_rectangle(135,230,148,243,fill=Am_color[0][1])
        our_canvas.create_rectangle(150,230,163,243,fill=Am_color[0][2])
        our_canvas.create_rectangle(165,230,178,243,fill=Am_color[0][3])
        our_canvas.create_rectangle(180,230,193,243,fill=Am_color[0][4])
        our_canvas.create_rectangle(195,230,208,243,fill=Am_color[0][5])
        our_canvas.create_rectangle(210,230,223,243,fill=Am_color[0][6])

        our_canvas.create_rectangle(120,245,133,258,fill=Am_color[1][0])
        our_canvas.create_rectangle(135,245,148,258,fill=Am_color[1][1])
        our_canvas.create_rectangle(150,245,163,258,fill=Am_color[1][2])
        our_canvas.create_rectangle(165,245,178,258,fill=Am_color[1][3])
        our_canvas.create_rectangle(180,245,193,258,fill=Am_color[1][4])
        our_canvas.create_rectangle(195,245,208,258,fill=Am_color[1][5])
        our_canvas.create_rectangle(210,245,223,258,fill=Am_color[1][6])

        our_canvas.create_rectangle(120,260,133,273,fill=Am_color[2][0])
        our_canvas.create_rectangle(135,260,148,273,fill=Am_color[2][1])
        our_canvas.create_rectangle(150,260,163,273,fill=Am_color[2][2])
        our_canvas.create_rectangle(165,260,178,273,fill=Am_color[2][3])
        our_canvas.create_rectangle(180,260,193,273,fill=Am_color[2][4])
        our_canvas.create_rectangle(195,260,208,273,fill=Am_color[2][5])
        our_canvas.create_rectangle(210,260,223,273,fill=Am_color[2][6])

        our_canvas.create_rectangle(120,275,133,288,fill=Am_color[3][0])
        our_canvas.create_rectangle(135,275,148,288,fill=Am_color[3][1])
        our_canvas.create_rectangle(150,275,163,288,fill=Am_color[3][2])
        our_canvas.create_rectangle(165,275,178,288,fill=Am_color[3][3])
        our_canvas.create_rectangle(180,275,193,288,fill=Am_color[3][4])
        our_canvas.create_rectangle(195,275,208,288,fill=Am_color[3][5])
        our_canvas.create_rectangle(210,275,223,288,fill=Am_color[3][6])

        our_canvas.create_rectangle(120,290,133,303,fill=Am_color[4][0])
        our_canvas.create_rectangle(135,290,148,303,fill=Am_color[4][1])
        our_canvas.create_rectangle(150,290,163,303,fill=Am_color[4][2])
        our_canvas.create_rectangle(165,290,178,303,fill=Am_color[4][3])
        our_canvas.create_rectangle(180,290,193,303,fill=Am_color[4][4])
        our_canvas.create_rectangle(195,290,208,303,fill=Am_color[4][5])
        our_canvas.create_rectangle(210,290,223,303,fill=Am_color[4][6])

        our_canvas.create_rectangle(120,305,133,318,fill=Am_color[5][0])
        our_canvas.create_rectangle(135,305,148,318,fill=Am_color[5][1])
        our_canvas.create_rectangle(150,305,163,318,fill=Am_color[5][2])
        our_canvas.create_rectangle(165,305,178,318,fill=Am_color[5][3])
        our_canvas.create_rectangle(180,305,193,318,fill=Am_color[5][4])
        our_canvas.create_rectangle(195,305,208,318,fill=Am_color[5][5])
        our_canvas.create_rectangle(210,305,223,318,fill=Am_color[5][6])

        our_canvas.create_rectangle(120,320,133,333,fill=Am_color[6][0])
        our_canvas.create_rectangle(135,320,148,333,fill=Am_color[6][1])
        our_canvas.create_rectangle(150,320,163,333,fill=Am_color[6][2])
        our_canvas.create_rectangle(165,320,178,333,fill=Am_color[6][3])
        our_canvas.create_rectangle(180,320,193,333,fill=Am_color[6][4])
        our_canvas.create_rectangle(195,320,208,333,fill=Am_color[6][5])
        our_canvas.create_rectangle(210,320,223,333,fill=Am_color[6][6])
        
    elif cube == "pyraminx":               
       
        #L
        our_canvas.create_polygon(10,10,50 ,10,30 ,45,fill=Vm_color[0][0])        
        our_canvas.create_polygon(52,10,92 ,10,72 ,45,fill=Vm_color[0][2])
        our_canvas.create_polygon(94,10,134,10,114,45,fill=Vm_color[0][4])
        
        our_canvas.create_polygon(31,46,71 ,46,51,11,fill=Vm_color[0][1])
        our_canvas.create_polygon(73,46,113,46,93,11,fill=Vm_color[0][3])


        our_canvas.create_polygon(30,48,71 ,48,51,83,fill=Vm_color[1][1])
        our_canvas.create_polygon(73,48,113,48,93,83,fill=Vm_color[1][3])

        our_canvas.create_polygon(52,84,92,84,72,48,fill=Vm_color[1][2])

        our_canvas.create_polygon(52,86,92,86,72,119,fill=Vm_color[2][2])
               
        
        #R
        our_canvas.create_polygon(154,10,194,10,174,45,fill=Az_color[0][0])        
        our_canvas.create_polygon(196,10,236,10,216,45,fill=Az_color[0][2])        
        our_canvas.create_polygon(238,10,278,10,258,45,fill=Az_color[0][4])        

        our_canvas.create_polygon(175,46,215,46,195,11,fill=Az_color[0][1])        
        our_canvas.create_polygon(217,46,257,46,237,11,fill=Az_color[0][3])    



        our_canvas.create_polygon(175,48,215,48,195,83,fill=Az_color[1][1])        
        our_canvas.create_polygon(217,48,257,48,237,83,fill=Az_color[1][3])  

        our_canvas.create_polygon(196,84,236,84,216,49,fill=Az_color[1][2])  

        our_canvas.create_polygon(196,86,236,86,216,119,fill=Az_color[2][2])  

        
        #F        

        our_canvas.create_polygon(124,45,164,45,144,10,fill=Vd_color[0][2]) 


        our_canvas.create_polygon(124,48,164,48,144,83,fill=Vd_color[1][2])  

        our_canvas.create_polygon(103,84,143,84,123,48,fill=Vd_color[1][1])  
        our_canvas.create_polygon(145,84,185,84,165,48,fill=Vd_color[1][3])  

        our_canvas.create_polygon(103,86,143,86,123,119,fill=Vd_color[2][1])  
        our_canvas.create_polygon(145,86,185,86,165,119,fill=Vd_color[2][3])  

        our_canvas.create_polygon(81 ,120,121,120,101,87,fill=Vd_color[2][0])  
        our_canvas.create_polygon(124,120,164,120,144,87,fill=Vd_color[2][2])  
        our_canvas.create_polygon(166,120,206,120,186,87,fill=Vd_color[2][4])  

       
        #D
        our_canvas.create_polygon(81,130,121,130,101,165,fill=Am_color[0][0])  
        our_canvas.create_polygon(124,130,164,130,144,165,fill=Am_color[0][2])  
        our_canvas.create_polygon(166,130,206,130,186,165,fill=Am_color[0][4]) 

        our_canvas.create_polygon(103,165,143,165,123,131,fill=Am_color[0][1])  
        our_canvas.create_polygon(145,165,185,165,165,131,fill=Am_color[0][3])  


        our_canvas.create_polygon(103,167,143,167,123,201,fill=Am_color[1][1])  
        our_canvas.create_polygon(145,167,185,167,165,201,fill=Am_color[1][3])  

        our_canvas.create_polygon(124,201,164,201,144,167,fill=Am_color[1][2])  

        our_canvas.create_polygon(124,203,164,203,144,238,fill=Am_color[2][2]) 

    elif cube == "megaminx":
        pass
    elif cube == "skewb":
        pass
    elif cube == "clock":
        pass
    plot3D(cube,Br_color,Lr_color,Vd_color,Vm_color,Az_color,Am_color)


def next_scramble():
    ch_event = eventsComboBox.get()
    
    if ch_event == '2x2':
        scrambler_NxN("2x2")                 
    elif ch_event == '3x3':
        scrambler_NxN("3x3")
    elif ch_event == '4x4':                        
        scrambler_NxN("4x4")  
    elif ch_event == '5x5':          
        scrambler_NxN("5x5")
    elif ch_event == '6x6':                        
        scrambler_NxN("6x6")
    elif ch_event == '7x7':         
        scrambler_NxN("7x7")
    elif ch_event == 'pyraminx':
        scrambler_pyraminx()
    elif ch_event == 'megaminx':
        scrambler_megaminx()
    elif ch_event == 'skewb':
        scrambler_skewb()
    elif ch_event == 'clock':
        scrambler_clock()
    elif ch_event == '3x3 OH':
        scrambler_NxN("3x3")

def dividir_texto(texto, max_caracteres=100):
    """ Divide o texto em linhas para evitar que fique muito longo """
    palavras = texto.split(" ")
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        if len(linha_atual) + len(palavra) + 1 > max_caracteres:
            linhas.append(linha_atual.strip())
            linha_atual = palavra
        else:
            linha_atual += " " + palavra

    if linha_atual:  # Adiciona a última linha
        linhas.append(linha_atual.strip())

    return linhas

def update_label_scramble(novo_texto):
    """ Atualiza a interface com um novo texto """
    global actual_scramble  # Permite modificar a lista de labels
    for widget in row2.winfo_children():
        widget.destroy()  # Remove os labels e frames antigos

    actual_scramble = []  # Reseta a lista de labels
    linhas = dividir_texto(novo_texto)

    for linha in linhas:
        linha_frame = ctk.CTkFrame(row2)  # Cada linha fica em um novo frame
        linha_frame.pack(anchor="w")  # Mantém alinhado à esquerda

        for i, palavra in enumerate(linha.split(" ")):
            print_scramble = ctk.CTkLabel(linha_frame,text = palavra + " ", font=("Arial", 18),wraplength = 500)            
            print_scramble.pack(side=tk.LEFT)            
            print_scramble.bind("<Button-1>", lambda e, idx=len(actual_scramble): on_word_click(e, idx))
            actual_scramble.append(print_scramble)
    

def on_word_click(event, index):
    """ Destaca todas as palavras até o índice clicado e apaga as seguintes """
    cube = eventsComboBox.get()
    Br_color, Lr_color, Vd_color, Vm_color, Az_color, Am_color, Buffer = createMatrix(cube,"color")     
    
    for i, label in enumerate(actual_scramble):        
        turn = label.cget("text")  
        turn = turn.strip()            
        if i <= index:
            label.configure(text_color="white")  # Palavras já clicadas ficam normais
            
            Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color = turn_draw(cube,turn,Br_color,Lr_color,Vd_color,Vm_color ,Az_color, Am_color,Buffer)
        else:
            label.configure(text_color="gray")  # Palavras futuras ficam apagadas
    
    draw_scramble(cube,Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color)    
    # ic(Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color)

def scrambler_NxN(cube):
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    accepted = 0

    global actual_scramble 
    global sum_turns_str
    sum_turns_str = ""
    
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

    sum_turns = []

    if cube == "2x2":
        movs = 12
        range_turn = 19
    elif cube == "3x3" or cube == "3x3 OH":
        movs = 20
        range_turn = 19
    elif cube == "4x4":
       movs = 44
       range_turn = 37
    elif cube == "5x5":
        movs = 60
        range_turn = 37
    elif cube == "6x6":
        movs = 80
        range_turn = 55
    elif cube == "7x7":
        movs = 100
        range_turn = 55    
    
    Br_color, Lr_color, Vd_color, Vm_color, Az_color, Am_color, Buffer = createMatrix(cube,"color") 

    define_flags(cube,n_move)


    for i in range(movs):

        while accepted == 0:
            n_move = random.randrange(1, range_turn,1)
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
        
        define_flags(cube,n_move)
        
        Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color = turn_draw(cube,turn,Br_color,Lr_color,Vd_color,Vm_color ,Az_color, Am_color,Buffer)
        
        # sum_turns.append(" ")
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    
    reset_flags()      
    draw_scramble(cube,Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color)    
    
    sum_turns_str = (" ".join(sum_turns))
    
    update_label_scramble(sum_turns_str)



def scrambler_pyraminx():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0   

    global sum_turns_str
    sum_turns_str = "" 

    Br_color, Lr_color, Vd_color, Vm_color, Az_color, Am_color, Buffer = createMatrix("pyraminx","color") 

    sum_turns = []
    for i in range(12):

        while accepted == 0:
            n_move = random.randrange(1,9,1)
            

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
        Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color = turn_draw("pyraminx",turn,Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color,Buffer)
        # draw_scramble("pyraminx",Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color) 
        # print(turn) 
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
        Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color = turn_draw("pyraminx",turn,Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color,Buffer)
        
    
        # print(turn) 
        accepted = 0    
    draw_scramble("pyraminx",Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color)   
    sum_turns_str = (" ".join(sum_turns))
    
    update_label_scramble(sum_turns_str) 

   
    # print(actual_scramble)    
    
    # actual_scramble.set(" ".join(sum_turns))
    

def scrambler_megaminx():
    global sum_turns_str
    sum_turns_str = ""
    sum_turns = []
    Br_color, Lr_color, Vd_color, Vm_color, Az_color, Am_color, Buffer = createMatrix("megaminx","color")  

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
    draw_scramble("megaminx",Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color) 
    sum_turns_str = (" ".join(sum_turns))
    update_label_scramble(sum_turns_str) 
    
    # actual_scramble.set(" ".join(sum_turns))
          
def scrambler_skewb():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0    
    Br_color, Lr_color, Vd_color, Vm_color, Az_color, Am_color, Buffer = createMatrix("skewb","color") 

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
            
        Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color = turn_draw("skewb",turn,Br_color,Lr_color,Vd_color,Vm_color ,Az_color, Am_color,Buffer)
        
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    # print(actual_scramble)    
    draw_scramble("skewb",Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color) 
    sum_turns_str = (" ".join(sum_turns))
    
    update_label_scramble(sum_turns_str)
    # actual_scramble.set(" ".join(sum_turns))
    

def scrambler_clock():    
    
    sum_turns = []
    Br_color, Lr_color, Vd_color, Vm_color, Az_color, Am_color, Buffer = createMatrix("clock","color")  

    moves1 = ["UR","DR","DL","UL","U","R","D","L","ALL"]
    moves2 = ["U","R","D","L","ALL"]   

    for move in moves1:
        number = random.randrange(0,7)
        number = str(number)
        signal = random.randrange(0,2)
        signal = "+" if signal == 1 else  "-"        
        sum_turns.append(move+number+signal)   
        turn =  move+number+signal
        Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color = turn_draw("clock",turn,Br_color,Lr_color,Vd_color,Vm_color ,Az_color, Am_color,Buffer)

    sum_turns.append("y2")
    
    for move in moves2:
        number = random.randrange(0,7)
        number = str(number)
        signal = random.randrange(0,2)
        signal = "+" if signal == 1 else  "-"        
        sum_turns.append(move+number+signal)    


    draw_scramble("clock",Br_color ,Lr_color,Vd_color,Vm_color ,Az_color, Am_color) 
    sum_turns_str = (" ".join(sum_turns))
    
    update_label_scramble(sum_turns_str)
    
    # actual_scramble.set(" ".join(sum_turns))
    
def create_ranking():   

    global ranking_WR_Average
    global ranking_CR_Average
    global ranking_NR_Average
    global ranking_WR_Single
    global ranking_CR_Single
    global ranking_NR_Single
    global rankingPath
    global enableRanking
    global gender

    if enableRanking == 1:     

        try:
            paises = pd.read_csv('WCA_export_Countries.tsv', sep='\t', header=0)
            pessoas = pd.read_csv('WCA_export_Persons.tsv', sep='\t', header=0)
            ranking_single = pd.read_csv('WCA_export_RanksSingle.tsv', sep='\t', header=0,dtype={'eventId': 'string'})       
            ranking_average = pd.read_csv('WCA_export_RanksAverage.tsv' , sep='\t', header=0,dtype={'eventId': 'string'})   
        
            # ranking_average = ranking_average.astype({'eventId': 'string','personId': 'string'})
            # ranking_single = ranking_single.astype({'eventId': 'string'})
            pessoas = pessoas.astype({'gender': 'string'})
            print("dentro da pasta")
            print(ranking_single.dtypes)
        except:
            try:
                paises = pd.read_csv(os.path.join(rankingPath,'WCA_export_Countries.tsv'), sep='\t', header=0)
                pessoas = pd.read_csv(os.path.join(rankingPath,'WCA_export_Persons.tsv'), sep='\t', header=0)
                ranking_single = pd.read_csv(os.path.join(rankingPath,'WCA_export_RanksSingle.tsv'), sep='\t', header=0)       
                ranking_average = pd.read_csv( os.path.join(rankingPath,'WCA_export_RanksAverage.tsv') , sep='\t', header=0)
        
                ranking_average = ranking_average.astype({'eventId': 'string'})
                ranking_single = ranking_single.astype({'eventId': 'string'})
                pessoas = pessoas.astype({'gender': 'string'})
                print("No path")

            except:
                messagebox.showinfo( "Ranking Files", "Caminho não encontrado")
                return
    

    else:
        return

   
    pais = paises.query('name == "Brazil"') 
    continente = pais[['continentId']]

    pais = pais['name'].tolist()
    continente = continente['continentId'].tolist()

    
    CR = paises.query('continentId == @continente')
    CR = CR['id'].tolist()

    # print(pessoas.dtypes)

    if gender == 3:
        country_Person = pessoas.query('countryId == @pais and gender == "f"')
        continent_Person = pessoas.query('countryId == @CR and gender == "f"')
        world_Person = pessoas.query('gender == "f"')
        
    elif gender == 2:
        country_Person = pessoas.query('countryId == @pais and gender == "m"')
        continent_Person = pessoas.query('countryId == @CR and gender == "m"')
        world_Person = pessoas.query('gender == "m"')
    else:
        country_Person = pessoas.query('countryId == @pais')
        continent_Person = pessoas.query('countryId == @CR')
        # world_Person = pessoas.query('gender == "f" or gender == "m"')
        world_Person = pessoas
    

    # country_Person = pessoas.query('countryId == @pais')
    # continent_Person = pessoas.query('countryId == @CR')
    
    country_Person = country_Person['id'].tolist()    
    continent_Person = continent_Person['id'].tolist()
    world_Person = world_Person['id'].tolist()    

    # print(world_Person)


    ch_event = eventsComboBox.get()

    if ch_event == '2x2':
        modalidade = "222"  
        
    elif ch_event == '3x3':
        modalidade = "333"       
        
    elif ch_event == '4x4':                
       modalidade = "444"      

    elif ch_event == '5x5':  
        modalidade = "555"     

    elif ch_event == '6x6':                
        modalidade = "666"

    elif ch_event == '7x7':                 
        modalidade = "777"

    elif ch_event == 'pyraminx':
        modalidade = "pyram"
        
    elif ch_event == 'megaminx':        
        modalidade = "minx"
        
    elif ch_event == 'skewb':
        modalidade = "skewb"
        
    elif ch_event == 'clock':
        modalidade = "clock"
    
    elif ch_event == '3x3 OH':
        modalidade = "333oh"



    #criar tabelas dos rankings ( apenas quando alterar modalidade ou pais)

    ranking_WR_Average = ranking_average[(ranking_average.eventId == modalidade)&(ranking_average.personId.isin(world_Person))]
    ranking_WR_Average = ranking_WR_Average.drop(columns=['continentRank','countryRank'])
    # print(ranking_WR_Average)
    ranking_WR_Average['worldRank'] = range(1, 1+len(ranking_WR_Average))
    


    ranking_CR_Average = ranking_average[(ranking_average.eventId == modalidade)&(ranking_average.personId.isin(continent_Person))]
    ranking_CR_Average = ranking_CR_Average.drop(columns=['worldRank','countryRank'])
    # print(ranking_CR_Average)
    ranking_CR_Average['continentRank'] = range(1, 1+len(ranking_CR_Average))
    


    ranking_NR_Average = ranking_average[(ranking_average.eventId == modalidade)&(ranking_average.personId.isin(country_Person))]
    ranking_NR_Average = ranking_NR_Average.drop(columns=['worldRank','continentRank'])
    # print(ranking_NR_Average)
    ranking_NR_Average['countryRank'] = range(1, 1+len(ranking_NR_Average))
    

    # -----------------------------------------------------------------

    ranking_WR_Single = ranking_single[(ranking_single.eventId == modalidade)&(ranking_single.personId.isin(world_Person))]
    ranking_WR_Single = ranking_WR_Single.drop(columns=['continentRank','countryRank'])
    # print(ranking_WR_Single)
    ranking_WR_Single['worldRank'] = range(1, 1+len(ranking_WR_Single))
    
    print(ranking_WR_Single)


    ranking_CR_Single = ranking_single[(ranking_single.eventId == modalidade)&(ranking_single.personId.isin(continent_Person))]
    ranking_CR_Single = ranking_CR_Single.drop(columns=['worldRank','countryRank'])
    # print(ranking_CR_Single)
    ranking_CR_Single['continentRank'] = range(1, 1+len(ranking_CR_Single))
    
    print(ranking_CR_Single)


    ranking_NR_Single = ranking_single[(ranking_single.eventId == modalidade)&(ranking_single.personId.isin(country_Person))]
    ranking_NR_Single = ranking_NR_Single.drop(columns=['worldRank','continentRank'])
    # ranking_NR_Single['New_continentRank'] = ranking_NR_Single.index + 1
    ranking_NR_Single['countryRank'] = range(1, 1+len(ranking_NR_Single))
    # print(ranking_NR_Single)
    
    
    print(ranking_NR_Single)
   
def ranking_position(tempo_single,tempo_ao5):

    global ranking_WR_Average
    global ranking_CR_Average
    global ranking_NR_Average
    global ranking_WR_Single
    global ranking_CR_Single
    global ranking_NR_Single      

    #analizar a cada solve a posição ( e tbm guardar o melhor valor)
    
    try:    
        position_WR_Average = position_WR_Average[(position_WR_Average.best >= tempo_ao5)].iloc[0].to_list()[3]
    except:
        position_WR_Average = len(ranking_WR_Average[(ranking_WR_Average.best <= tempo_ao5)])+1
        
    
    try:
        position_CR_Average = position_CR_Average[(position_CR_Average.best >= tempo_ao5)].iloc[0].to_list()[3]
    except:
        position_CR_Average = len(ranking_CR_Average[(ranking_CR_Average.best <= tempo_ao5)])+1
    
    try:
        position_NR_Average = position_NR_Average[(position_NR_Average.best >= tempo_ao5)].iloc[0].to_list()[3]
    except:
        position_NR_Average = len(ranking_NR_Average[(ranking_NR_Average.best <= tempo_ao5)])+1
    

    # ----------------------------------------------------
    try:
        position_WR_Single = position_WR_Single[(position_WR_Single.best >= tempo_single)].iloc[0].to_list()[3]
    except:
        position_WR_Single = len(ranking_WR_Single[(ranking_WR_Single.best <= tempo_single)])+1
    
    try:
        position_CR_Single = position_CR_Single[(position_CR_Single.best >= tempo_single)].iloc[0].to_list()[3]
    except:
        position_CR_Single = len(ranking_CR_Single[(ranking_CR_Single.best <= tempo_single)])+1
    
    try:
        position_NR_Single = ranking_NR_Single[(ranking_NR_Single.best >= tempo_single)].iloc[0].to_list()[3]
    except:
        position_NR_Single = len(ranking_NR_Single[(ranking_NR_Single.best <= tempo_single)])+1
    

    if tempo_ao5 == 9999999999:
        position_WR_Average = position_CR_Average = position_NR_Average = 0  
    

    return [position_WR_Single,position_CR_Single,position_NR_Single,
            position_WR_Average,position_CR_Average,position_NR_Average]
   



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
        if precisionTimer == 1:
            multiplier = 10
        elif precisionTimer == 2:
            multiplier = 100
        elif precisionTimer == 3:
            multiplier = 1000

        if any((c in chars) for c in input_timer.get()):        #encontrou o ponto e dois ponto  1:23.54 
            t = input_timer.get().split(':')        
            t = float(t[0]) * 60 + float(t[1])    
            t *=multiplier
        elif not(any((c in chars) for c in input_timer.get())):      #encontrou o ponto e nao o dois pontos   12.43
            t = int(float(input_timer.get())*multiplier)
        


    else:        #escrita sem ponto   1354

        if int(input_timer.get()) >= 1000 and precisionTimer == 1:        #escrita sem ponto (11268) maior que 60 segundo e com decimos        
            t = int(input_timer.get())             
            x = [int(a) for a in str(t)]            
            m = x[0]
            s = x[1]*10 + x[2]
            c = (x[3])/10
            t = m*60 + s + c 
            t *=10            
       
        
        if int(input_timer.get()) >= 10000 and precisionTimer == 2:        #escrita sem ponto (11268) maior que 60 segundo e com centesimos        
            t = int(input_timer.get())             
            x = [int(a) for a in str(t)]            
            m = x[0]
            s = x[1]*10 + x[2]
            c = (x[3]*10 + x[4])/100
            t = m*60 + s + c 
            t *=100
           
                
        elif int(input_timer.get()) >= 100000 and precisionTimer == 3:           #escrita sem ponto (135460) maior que 60 segundo e com milesimos   
            t = int(input_timer.get()) 
            x = [int(a) for a in str(t)]
            m = x[0]
            s = x[1]*10 + x[2]
            c = (x[3]*100 + x[4]*10 + x[5])/1000
            t = m*60 + s + c 
            t *=1000
            
        else:    #escrita sem ponto (13546) menor que 60 segundo   
            t = int(input_timer.get())
        
               
    
    data = datetime.datetime.now()
    datas.append(data)

    tempo = int(t)

    print(tempo)
    
    tempos.append(tempo)    

    tempo = trunc(tempo,precisionTimer)

    ptempo = time_convert(tempo)        

    global actual_timer
    
    actual_timer.set(ptempo)    

    global scrambles

    scrambles.append(actual_scramble.get())  

    global statusFlag
    statusFlag = "OK"
    status.append(statusFlag)

    global countdown 
    ic(countdown)        
    countdowns.append(0)

    global inputs
    dic = {1:"Manual",2:"Timer",3:"Stackmat"}
    ax = dic[inputVar.get()]
    inputs.append(ax)
    

    estatistica(len(tempos))
    input_timer.delete(0,tk.END)

    
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
    print_timer.configure(text_color= ("black","white"))


def inspection():
    
    global countdown
    global run_inspecton
    global statusFlag
    if run_inspecton:
        print("inspeção")   
        # Just beore starting        
        # show = str(count)

        # mark.config(text = count)
        global actual_timer
        actual_timer.set(int(countdown))        
       
        if countdown <= -2:
            statusFlag = "DNF"
            actual_timer.set("DNF")
        elif countdown <= 0:
            statusFlag = "+2"
            actual_timer.set("+2")
        else:
            statusFlag = "OK"


        #Increment the count after
        #every 1 second
        root.after(100, inspection)
        countdown -= 0.1 

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
        print_timer.configure(text_color= "yellow")

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
        print_timer.configure(text_color= "green")
        #DEIXAR VERDEEEEE


# cancels long press events
def cancel_do_space_longpress():
    global _short_press
    global _do_space_longpress
    global enable_start_timer
    enable_start_timer = False
    _short_press = None
    if _do_space_longpress:
        root.after_cancel(_do_space_longpress)
        print_timer.configure(text_color= ("black","white"))

def atualizar_label():
    global t0
    global actual_timer
    if timer_state == 4:
        tempo_decorrido = time.time() - t0
        minutos, segundos = divmod(tempo_decorrido, 60)
        segundos, centesimos = divmod(segundos, 1)
        actual_timer.set(f"{int(minutos):02d}:{int(segundos):02d}:{int(centesimos*100):02d}")
        root.after(10, atualizar_label)
                
def start_timer():     
    
    global t0
    global timer_state
    
    if timer_state == 3:
        t0 = time.time()
        
        print("rodando........")
        print_timer.configure(text_color= "white")
        
        timer_state = 4
        global run_inspecton
        run_inspecton = False
        atualizar_label()
    
def stop_timer(): 
    
    global timer_state

    if timer_state == 4:
        t1 = time.time()
        data = datetime.datetime.now()
        # print(data)

        global t0        
        global enable_start_timer 

        global precisionTimer  
        precisionTimer = int(precisionTimer)        

        if precisionTimer == 1:
            multiplier = 10
            penalty = 20
        elif precisionTimer == 2:
            multiplier = 100
            penalty = 200
        elif precisionTimer == 3:
            multiplier = 1000
            penalty = 2000    

        dt = (t1-t0)*multiplier
        tempo = dt
        print(tempo)

        
        datas.append(data)
        
        enable_start_timer = False
        
        timer_state = 5                
        
        global countdown 
        ic(countdown)        
        countdowns.append(round(15-countdown,1))
        countdown = 15

        global statusFlag
        ic(statusFlag)
        ic(tempo)
        if statusFlag == "+2":            
            tempo+=penalty
        ic(tempo)
        status.append(statusFlag)

        tempo = trunc(tempo,precisionTimer)
        tempos.append(tempo)

        ptempo = time_convert(tempo)        

        global actual_timer

        
        actual_timer.set(ptempo)    

        global scrambles
        global sum_turns_str

        scrambles.append(sum_turns_str)

        global inputs
        dic = {1:"Manual",2:"Timer",3:"Stackmat"}
        ax = dic[inputVar.get()]
        inputs.append(ax)

        estatistica(len(tempos))

        next_scramble() 

       
        
def change_event(event):  
    global flag_change_event
    flag_change_event = True
    print("entroo")

    resetar()     
    create_ranking()   
    # guardar_tempos() 
    importar_tempos_file()    
        
    ch_event = eventsComboBox.get()
    print(ch_event)    
    if ch_event == '2x2':
        scrambler_NxN("2x2")                 
    elif ch_event == '3x3':
        scrambler_NxN("3x3")
    elif ch_event == '4x4':                        
        scrambler_NxN("4x4")  
    elif ch_event == '5x5':          
        scrambler_NxN("5x5")
    elif ch_event == '6x6':                        
        scrambler_NxN("6x6")
    elif ch_event == '7x7':         
        scrambler_NxN("7x7")
    elif ch_event == 'pyraminx':
        scrambler_pyraminx()            
    elif ch_event == 'megaminx':                
        scrambler_megaminx()               
    elif ch_event == 'skewb':
        scrambler_skewb()                  
    elif ch_event == 'clock':
        scrambler_clock()  
    elif ch_event == '3x3 OH':
        scrambler_NxN("3x3")

    flag_change_event = False   
    write_txt_setting()   
    # precisionVar_change(ch_event)    


# Função para formatar o eixo Y
def format_time(time,pos):
    global precisionTimer    

    if precisionTimer == 1:        
        time /= 10
    
    elif precisionTimer == 2:        
        time /= 100

    elif precisionTimer == 3:        
        time /= 1000

    
    if time < 60:
        presult = str(time)
        
    else:
        
        m = time // 60        
        m = int(m)    

        s = time % 60          

        if precisionTimer == 1:                  
            sStr = format(s,'.1f')              

        if precisionTimer == 2:
            sStr = format(s,'.2f')      
            
        elif precisionTimer == 3:
            sStr = format(s,'.3f')

        if s < 10:                   
            presult = str(m) + ":0" + sStr    
            
        else:                                
            presult = str(m) + ":" + sStr
            
        
    return presult

def plot():       

	# the figure that will contain the plot 
    window = tk.Toplevel(root)
    window.geometry('1200x700+1200+200') 

    # global tempos 
    fig  = Figure(figsize = (8, 8),dpi = 100)   
    fig2 = Figure(figsize = (8, 8),dpi = 100)   
    fig3 = Figure(figsize = (8, 8),dpi = 100)   

	# adding the subplot 
    plot1 = fig.add_subplot(111) 
    plot2 = fig2.add_subplot(111) 
    plot3 = fig3.add_subplot(111) 

	# plotting the graph 
    plot3.hist(countdowns)     
    plot2.hist(tempos)     
    plot1.plot(tempos)     
    plot1.plot(mo_3)     
    plot1.plot(ao_5)     
    plot1.plot(ao_12)
    plot1.legend(['Tempos', 'mo3','ao5','ao12']) 

    #Formatar para mostrar valores corretos no eixos de tempo
    plot1.yaxis.set_major_formatter(FuncFormatter(format_time))
    plot2.xaxis.set_major_formatter(FuncFormatter(format_time))

    # Forçando valores inteiros no eixo X
    plot1.xaxis.set_major_locator(MaxNLocator(integer=True))  # Forçando valores inteiros no eixo X

    mplcursors.cursor(plot1)
	# creating the Tkinter canvas 
	# containing the Matplotlib figure 
    canvas  = FigureCanvasTkAgg(fig,	master = window) 
    canvas2 = FigureCanvasTkAgg(fig2,	master = window) 
    canvas3 = FigureCanvasTkAgg(fig3,	master = window) 
    canvas.draw() 
    canvas2.draw() 
    canvas3.draw() 

	# placing the canvas on the Tkinter root 
    canvas.get_tk_widget().pack(side = tk.LEFT)  
    canvas2.get_tk_widget().pack(side = tk.LEFT)  
    canvas3.get_tk_widget().pack(side = tk.RIGHT)  

    


	# creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas,window) 
    toolbar.update() 

	# placing the toolbar on the Tkinter root 
    # canvas.get_tk_widget().pack() 

    canvas.flush_events()
    canvas2.flush_events()
    canvas3.flush_events()



def plot3D(cube,Br_color,Lr_color,Vd_color,Vm_color,Az_color,Am_color):      
    
    ax = fig.add_subplot(projection='3d')      
    ax.set_aspect("auto")
    # ax.set_autoscale_on(True)  
    # ax.dist = 20
    ax.axis('off') 
    # ax.set_box_aspect(None, zoom=10)

    # colors = {
    # 'x': [Lr_color, Vm_color],
    # 'y': [Vd_color, Az_color],
    # 'z': [Am_color, Br_color]
    # }

    # for z in [0, 2]:
    #     for axis, color in colors.items():
    #         for i in range(2):
    #             for j in range(2):
    #                 side = Rectangle((i, j), 1, 1, facecolor=color[z//2][1-i][1-j])
    #                 ax.add_patch(side)
    #                 art3d.pathpatch_2d_to_3d(side, z=z, zdir=axis)

    if cube == "2x2":        
        LL = 1
        length = 2        
        cubeN = 'n'
        
    elif cube == "3x3":        
        LL = 2
        length = 3
        cubeN = 'n'
        
    elif cube == "4x4":        
        LL = 3
        length = 4
        cubeN = 'n'
        
    elif cube == "5x5":        
        LL = 4
        length = 5
        cubeN = 'n'
        
    elif cube == "6x6":        
        LL = 5
        length = 6
        cubeN = 'n'
        
    elif cube == "7x7":        
        LL = 6
        length = 7
        cubeN = 'n'
    elif cube == "pyraminx":  
        cubeN = 'nn'
        length = 5
    elif cube == "skewb":  
        cubeN = 'nn'
        length = 3    
    
    elif cube == "3x3 OH":        
        LL = 2
        length = 3
        cubeN = 'n'
    else:
        cubeN = 'nn'
        length = 3
        

    if cubeN == "n":
        # Eixo XXXXXXXXXXXXXXXXXXXXXXXXXXXX         

        for i in range(length):
            for j in range(length):
                side = Rectangle((i, j), 1, 1, edgecolor='k', facecolor=Lr_color[LL-j][LL-i])
                ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=0, zdir='x')

        # Eixo YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY        

        for i in range(length):
            for j in range(length):
                side = Rectangle((i, j), 1, 1, edgecolor='k', facecolor=Vd_color[LL-j][i])
                ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=0, zdir='y')

        # Eixo ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
        
        for i in range(length):
            for j in range(length):
                side = Rectangle((i, j), 1, 1, edgecolor='k', facecolor=Am_color[j][i])
                ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=0, zdir='z')

        # Eixo XXXXXXXXXXXXXXXXXXXXXXXXXXXX
        
        for i in range(length):
            for j in range(length):
                side = Rectangle((i, j), 1, 1, edgecolor='k', facecolor=Vm_color[LL-j][i])
                ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=length, zdir='x')

        # Eixo YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY        

        for i in range(length):
            for j in range(length):
                side = Rectangle((i, j), 1, 1, edgecolor='k', facecolor=Az_color[LL-j][LL-i])
                ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=length, zdir='y')

        # Eixo ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ           

        for i in range(length):
            for j in range(length):
                side = Rectangle((i, j), 1, 1, edgecolor='k', facecolor=Br_color[LL-j][i])
                ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=length, zdir='z') 
   
    elif cube == "pyraminx":
        
        trianglesyellow =  [
        ((0,0,0),(2,0,0),(1,1.71,0)),
        ((2,0,0),(4,0,0),(3,1.71,0)),
        ((4,0,0),(6,0,0),(5,1.71,0)),

        ((2,0,0),(1,1.71,0),(3,1.71,0)),
        ((4,0,0),(3,1.71,0),(5,1.71,0)),

        ((2,3.44,0),(1,1.71,0),(3,1.71,0)),
        ((4,3.44,0),(3,1.71,0),(5,1.71,0)),

        ((3,1.71,0),(2,3.44,0),(4,3.44,0)),

        ((3,5.13,0),(2,3.44,0),(4,3.44,0)),

        ]


        trianglesgreen =  [

        ((0,0,0),(2,0,0),(1,0.5,1.71)),
        ((2,0,0),(4,0,0),(3,0.5,1.71)),
        ((4,0,0),(6,0,0),(5,0.5,1.71)),

        ((2,0,0),(1,0.5,1.71),(3,0.5,1.71)),
        ((4,0,0),(3,0.5,1.71),(5,0.5,1.71)),

        ((2,1,3.44),(1,0.5,1.71),(3,0.5,1.71)),
        ((4,1,3.44),(3,0.5,1.71),(5,0.5,1.71)),

        ((2,1,3.44),(4,1,3.44),(3,0.5,1.71)),

        ((2,1,3.44),(4,1,3.44),(3,1.5,5.13)),

        ]

        trianglesred =  [

        ((0,0,0),(1,1.71,0),(1,0.5,1.71)),
        ((1,1.71,0),(2,3.44,0),(2,1.71,1.71)),
        ((2,3.44,0),(3,5.13,0),(3,3.44,1.71)),

        ((1,1.71,0),(2,1.71,1.71),(1,0.5,1.71)),
        ((2,3.44,0),(3,3.44,1.71),(2,1.71,1.71)),

        ((2,1,3.44),(2,1.71,1.71),(1,0.5,1.71)),
        ((2,1.71,1.71),(3,3.44,1.71),(3,2,3.44)),


        ((2,1.71,1.71),(2,1,3.44),(3,2,3.44)),

        ((3,1.5,5.13),(2,1,3.44),(3,2,3.44)),


        ]

        trianglesblue =  [

        ((6,0,0),(5,1.71,0),(5,0.5,1.71)),
        ((5,1.71,0),(4,3.44,0),(4,1.71,1.71)),
        ((4,3.44,0),(3,5.13,0),(3,3.44,1.71)),


        ((5,1.71,0),(5,0.5,1.71),(4,1.71,1.71)),
        ((4,3.44,0),(4,1.71,1.71),(3,3.44,1.71)),

        ((4,1,3.44),(5,0.5,1.71),(4,1.71,1.71)),
        ((3,2,3.44),(4,1.71,1.71),(3,3.44,1.71)),


        ((4,1.71,1.71),(4,1,3.44),(3,2,3.44)),

        ((3,1.5,5.13),(4,1,3.44),(3,2,3.44)),

        ]


        posyellow =  [
            (Am_color[0,0]),
            (Am_color[0,2]),
            (Am_color[0,4]),

            (Am_color[0,1]),
            (Am_color[0,3]),

            (Am_color[1,1]),
            (Am_color[1,3]),

            (Am_color[1,2]),

            (Am_color[2,2]),

            ]


        posgreen =  [

            (Vd_color[2,0]),
            (Vd_color[2,2]),
            (Vd_color[2,4]),

            (Vd_color[2,1]),
            (Vd_color[2,3]),

            (Vd_color[1,1]),
            (Vd_color[1,3]),

            (Vd_color[1,2]),

            (Vd_color[0,2]),

            ]

        posred =  [

            (Vm_color[2,2]),
            (Vm_color[1,1]),
            (Vm_color[0,0]),

            (Vm_color[1,2]),
            (Vm_color[0,1]),

            (Vm_color[1,3]),
            (Vm_color[0,2]),

            (Vm_color[0,3]),

            (Vm_color[0,4]),


            ]

        posblue =  [

            (Az_color[2,2]),
            (Az_color[1,3]),
            (Az_color[0,4]),

            (Az_color[1,2]),
            (Az_color[0,3]),

            (Az_color[1,1]),
            (Az_color[0,2]),

            (Az_color[0,1]),

            (Az_color[0,0]),

            ]
        



        # for i in range(posgreen):
        ax.add_collection(Poly3DCollection(trianglesgreen, edgecolor='k',facecolor=posgreen)) 


        ax.add_collection(Poly3DCollection(trianglesyellow, edgecolor='k',facecolor=posyellow))               

        ax.add_collection(Poly3DCollection(trianglesred, edgecolor='k',facecolor=posred))    

        ax.add_collection(Poly3DCollection(trianglesblue, edgecolor='k',facecolor=posblue))    


    elif cube == "skewb":
        trianglesyellow =  [

        ((0,0,0),(1,0,0),(0,1,0)),
        ((1,0,0),(2,0,0),(2,1,0)),
        ((0,1,0),(0,2,0),(1,2,0)),
        ((2,1,0),(2,2,0),(1,2,0)),

        ((1,0,0),(0,1,0),(1,2,0),(2,1,0)),

        ]

        triangleswhite =  [

        ((0,0,2),(1,0,2),(0,1,2)),
        ((1,0,2),(2,0,2),(2,1,2)),
        ((0,1,2),(0,2,2),(1,2,2)),
        ((2,1,2),(2,2,2),(1,2,2)),

        ((1,0,2),(0,1,2),(1,2,2),(2,1,2)),

        ]


        trianglesgreen =  [

        ((0,0,0),(1,0,0),(0,0,1)),
        ((1,0,0),(2,0,0),(2,0,1)),
        ((0,0,1),(0,0,2),(1,0,2)),
        ((2,0,1),(2,0,2),(1,0,2)),

        ((1,0,0),(0,0,1),(1,0,2),(2,0,1)),

        ]

        trianglesred =  [

        ((2,0,0),(2,1,0),(2,0,1)),
        ((2,1,0),(2,2,0),(2,2,1)),
        ((2,0,1),(2,0,2),(2,1,2)),
        ((2,2,1),(2,2,2),(2,1,2)),

        ((2,1,0),(2,0,1),(2,1,2),(2,2,1)),

        ]

        trianglesblue =  [

        ((0,2,0),(1,2,0),(0,2,1)),
        ((1,2,0),(2,2,0),(2,2,1)),
        ((0,2,1),(0,2,2),(1,2,2)),
        ((2,2,1),(2,2,2),(1,2,2)),

        ((1,2,0),(0,2,1),(1,2,2),(2,2,1)),

        ]

        trianglesorange =  [

        ((0,0,0),(0,1,0),(0,0,1)),
        ((0,1,0),(0,2,0),(0,2,1)),
        ((0,0,1),(0,0,2),(0,1,2)),
        ((0,2,1),(0,2,2),(0,1,2)),

        ((0,1,0),(0,0,1),(0,1,2),(0,2,1)),

        ]

        poswhite =  [
            (Br_color[2,0]),
            (Br_color[2,2]),

            (Br_color[0,0]),
            (Br_color[0,2]),

            (Br_color[1,1]),
            
            ]




        posyellow =  [
            (Am_color[0,0]),
            (Am_color[0,2]),

            (Am_color[2,0]),
            (Am_color[2,2]),

            (Am_color[1,1]),

            ]


        posgreen =  [

            (Vd_color[2,0]),
            (Vd_color[2,2]),

            (Vd_color[0,0]),
            (Vd_color[0,2]),

            (Vd_color[1,1]),            

            ]

        posred =  [

            (Vm_color[2,0]),
            (Vm_color[2,2]),

            (Vm_color[0,0]),
            (Vm_color[0,2]),

            (Vm_color[1,1]),        

            ]

        posblue =  [

            (Az_color[2,2]),
            (Az_color[2,0]),

            (Az_color[0,2]),
            (Az_color[0,0]),

            (Az_color[1,1]),            

            ]
        
        posorange =  [

            (Lr_color[2,2]),
            (Lr_color[2,0]),

            (Lr_color[0,2]),
            (Lr_color[0,0]),

            (Lr_color[1,1]),
            

            ]

        ax.add_collection(Poly3DCollection(trianglesyellow, edgecolor='k',facecolor=posyellow))    

        ax.add_collection(Poly3DCollection(trianglesgreen, edgecolor='k',facecolor=posgreen))        

        ax.add_collection(Poly3DCollection(trianglesred, edgecolor='k',facecolor=posred))    

        ax.add_collection(Poly3DCollection(trianglesblue, edgecolor='k',facecolor=posblue))    

        ax.add_collection(Poly3DCollection(trianglesorange, edgecolor='k',facecolor=posorange))    

        ax.add_collection(Poly3DCollection(triangleswhite, edgecolor='k',facecolor=poswhite)) 


    # Hide axes ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlim([0,length])
    ax.set_ylim([0,length])
    ax.set_zlim([0,length])
    
    # ax.set_visible(False)
    # ax.set_facecolor('pink')    
	
    canvas.draw() 

	# placing the canvas on the Tkinter root 
    # canvas.get_tk_widget().pack()      


	# creating the Matplotlib toolbar 
    # toolbar = NavigationToolbar2Tk(canvas,root) 
    # toolbar.update() 

	# placing the toolbar on the Tkinter root 
    # canvas.get_tk_widget().pack() 

    canvas.flush_events()




def download_file(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 KB
    downloaded = 0
    start_time = time.time()

    with open(save_path, 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
            downloaded += len(data)
            elapsed = time.time() - start_time
            speed = downloaded / elapsed if elapsed > 0 else 0
            percent = int(downloaded * 100 / total_size) if total_size else 0

            # Atualiza a GUI
            progress_var.set(percent)
            percent_label.config(text=f"{percent}%")
            speed_label.config(text=f"{speed/1024:.2f} KB/s")
            downloaded_label.config(text=f"{downloaded/1024:.2f} KB / {total_size/1024:.2f} KB")
            DownloadWin.update_idletasks()

    status_label.config(text="Download concluído!")
    unzip_database()

def start_download():   
    global rankingPath
    url =  "https://www.worldcubeassociation.org/export/results/WCA_export.tsv.zip"
    nome_do_arquivo = rankingPath + '/' + 'WCA_export.zip'

    status_label.config(text="Baixando...")
    threading.Thread(
        target=download_file,
        args=(url, nome_do_arquivo),
        daemon=True
    ).start()





def update_ranking():

    global rankingPath

    url_API = "https://www.worldcubeassociation.org/api/v0/export/public"

    # 2. download the data behind the URL
    response = requests.get(url_API)


    # 3. Open the response into a new file called instagram.ico
    open("export_api.json", "wb").write(response.content)

    with open('export_api.json', 'r') as f:
        data_api = json.load(f)

    print(data_api["export_date"])
    print(data_api["tsv_url"])
    print("OK")



    url = data_api["tsv_url"]
    url = str(url)
    print(url)

    metadata_path = rankingPath + "/" + 'metadata.json' if rankingPath != "" else 'metadata.json'

    try:
        with open(metadata_path, 'r') as f:
            dado_local = json.load(f)
            print(data_api["export_date"])
            print(dado_local["export_date"])

        if dado_local["export_date"] == data_api["export_date"]:
            messagebox.showinfo( "Ranking Files", "Arquivos atualizados")
            return  
        else:   
            res = messagebox.askquestion( "Ranking Files", "Arquivo não atualizado. \n Deseja atualizar ?")     
            if res == 'yes':                                
                start_download()                

            else:
                pass    
        
    
    except:
        res = messagebox.askquestion( "Ranking Files", "Arquivos não encontrados. \n Deseja baixa-los ?")     
        if res == 'yes':                                
            start_download()            

        else:
            pass            
        # ----------------------------------------------------------------------------------------


def unzip_database():
    global rankingPath
    nome_do_arquivo = rankingPath + '/' + 'WCA_export.zip'

    # name_file = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
    #                        filetypes =(("ZIP Files","*.zip"),("All Files","*.*")),title = "Choose a file.")

    # print(name_file)    
    # rankingPath = name_file.replace(name_file.split('/')[-1],'')
    # print(rankingPath)
    

    # loading the temp.zip and creating a zip object
    with ZipFile(nome_do_arquivo, 'r') as zObject:
    
        # Extracting all the members of the zip 
        # into a specific location.
        # zObject.extractall(path="C:\\Users\\sai mohan pulamolu\\Desktop\\geeks_dir\\temp")
        zObject.extractall(rankingPath)       
    

    os.remove(rankingPath+"WCA_export_championships.tsv") 
    os.remove(rankingPath+"WCA_export_Competitions.tsv") 
    os.remove(rankingPath+"WCA_export_Continents.tsv") 
    os.remove(rankingPath+"WCA_export_eligible_country_iso2s_for_championship.tsv") 
    os.remove(rankingPath+"WCA_export_Events.tsv")     
    os.remove(rankingPath+"WCA_export_Formats.tsv") 
    os.remove(rankingPath+"WCA_export_Results.tsv") 
    # os.remove(rankingPath+"WCA_export_Rounds.tsv") 
    os.remove(rankingPath+"WCA_export_RoundTypes.tsv") 
    os.remove(rankingPath+"WCA_export_Scrambles.tsv") 
    os.remove(rankingPath+"README.md") 

    create_ranking()

    messagebox.showinfo( "Warning", "Import concluido.")

def importar_ranking():    
    global rankingPath

    rankingPath = filedialog.askdirectory()
    print(str(rankingPath))

    write_txt_setting() 

    create_ranking()

def importar_tempos_file():    

    global first_scan
    global flag_change_event
    if first_scan == False and flag_change_event == False:
        name_file = filedialog.askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                            filetypes =(("CSV Files","*.csv"),("Text File", "*.txt"),("All Files","*.*")),title = "Choose a file.")
    elif first_scan == True or flag_change_event == True:
        name_file = str(eventsComboBox.get()) + '.csv' 

    try:
        with open(name_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            line_count = 0
            resetar()
            for index,row in enumerate(csv_reader,1):                      
                tempos.append(float(row["Time"]))   
                countdowns.append(float(row["Inspection"]))          
                scrambles.append(row["Scramble"])
                datas.append(row["Date"])
                status.append(row["Status"])
                inputs.append(row["Input"])
                
                estatistica(index)                    

            print(f'Processed {line_count} lines.')
    except Exception as error: 
        print("An error occurred:", error) # An error occurred: name 'x' is not defined:      
        print("nao foi possivel importar")

def importar_tempos_folder():    
    
    events = ['2x2','3x3', '4x4','5x5','6x6','7x7','pyraminx','megaminx','skewb','clock','3x3 OH']
    
    folderPath = filedialog.askdirectory(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                        filetypes =(("CSV Files","*.csv"),("Text File", "*.txt"),("All Files","*.*")),title = "Choose a file.")
    # folderPath = filedialog.askdirectory()

    for event in events:
        event = folderPath + event + '.csv' 
        try:
            with open(event, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=';')
                line_count = 0
                resetar()
                for index,row in enumerate(csv_reader,1):                      
                    tempos.append(float(row["Time"])) 
                    countdowns.append(float(row["Inspection"]))            
                    scrambles.append(row["Scramble"])
                    datas.append(row["Date"])
                    status.append(row["Status"])
                    inputs.append(row["Input"])
                    
                    estatistica(index)                    

                print(f'Processed {line_count} lines.')
        except Exception as error: 
            print("An error occurred:", error) # An error occurred: name 'x' is not defined:      
            print("nao foi possivel importar")
        

def exportar_tempos():
    
    name_file = filedialog.asksaveasfilename(defaultextension=".csv")
    name_file = str(name_file)

    with open(name_file, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(["No.", "Time", "Inspection","Scramble","Date","Status","Input","Mo3","Ao5","Ao12"])

        for i in range(len(tempos)):
            employee_writer.writerow([i+1, tempos[i], scrambles[i], datas[i],status[i],inputs[i],mo_3[i],ao_5[i],ao_12[i]])

    messagebox.showinfo( "Warning", "Export completo.")


def clear_file_tempos():    
    name_file = eventsComboBox.get()  
    name_file = name_file + '.csv'

    with open(name_file, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(["No.", "Time", "Inspection","Scramble","Date","Status","Input","Mo3","Ao5","Ao12"])

def update_file_tempos(index):    
    name_file = eventsComboBox.get()  
    name_file = name_file + '.csv'

    try:
        with open(name_file, mode='a') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            employee_writer.writerow([index, tempos[index-1],countdowns[index-1], scrambles[index-1], datas[index-1],status[index-1],inputs[index-1],mo_3[index-1],ao_5[index-1],ao_12[index-1]])
            # print("insert feito")

    except Exception as error: 
            print("An error occurred:", error) # An error occurred: name 'x' is not defined:      
            print("nao foi possivel importar")
def guardar_tempos():    
    events = ['2x2','3x3', '4x4','5x5','6x6','7x7','pyraminx','megaminx','skewb','clock','3x3 OH']
    
    for event in events:        
        name_file = event + '.csv' 
        with open(name_file, mode='w') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(["No.", "Time", "Inspection","Scramble","Date","Status","Input","Mo3","Ao5","Ao12"])
            
            if event == eventsComboBox.get():
                for i in range(len(tempos)):
                    employee_writer.writerow([i+1, tempos[i], countdowns[i],scrambles[i], datas[i],status[i],inputs[i],mo_3[i],ao_5[i],ao_12[i]])
    
    messagebox.showinfo( "Warning", "Export completo.")

    
def changeColorScramble(side):
    choose = colorchooser.askcolor(faceColors[side])[1] 
    if choose != None:
        faceColors[side] = choose
    
    if first_scan == False:      
        write_txt_setting()

    
def ResetColorScramble():
    global faceColors
    global first_scan
    faceColors = {'1':'#FFFFFF','2':'#FFA500','3':'#00FF00','4':'#FF0000','5':'#0000FF','6':'#FFFF00'}
        
    if first_scan == False:      
        write_txt_setting()

def clearTables():
    for i in tb_stat.get_children():
        tb_stat.delete(i) 

    for i in tb_times.get_children():
        tb_times.delete(i) 
    
    for i in tb_ranking.get_children():
        tb_ranking.delete(i) 

def resetar():
    global tempos
    global scrambles
    global datas
    global inputs

    global global_best_solve
    global global_worst_solve

    global best_mo3
    global best_ao5
    global best_ao12

    global worst_mo3
    global worst_ao5
    global worst_ao12

    global media_3
    global media_5
    global media_12

    global first_scan
    global flag_change_event

    tempos.clear()
    mo_3.clear()
    ao_5.clear()
    ao_12.clear()
    scrambles.clear()
    datas.clear()
    status.clear()
    inputs.clear()

    

    global_best_solve = 9999999999
    global_worst_solve = 0

    best_mo3  = 9999999999
    best_ao5  = 9999999999
    best_ao12 = 9999999999

    worst_mo3  = 0
    worst_ao5  = 0
    worst_ao12 = 0
    

    media_3  = 9999999999
    media_5  = 9999999999
    media_12 = 9999999999
    

    clearTables()
    
    if flag_change_event == False and first_scan == False:    
        name_file = eventsComboBox.get() 
        name_file = name_file + '.csv'  
        with open(name_file, mode='w') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(["No.", "Time", "Scramble","Date","Status"])

def atualizar():
    global tempos      

    clearTables()

    clear_file_tempos()
    
    for index,_ in enumerate(tempos,1):    
        estatistica(index)   
        
def atualizarTempoPrecision(multiplier,divider):
    global tempos   

    clearTables()   
    clear_file_tempos()

    global global_best_solve
    global global_worst_solve

    global best_mo3
    global best_ao5
    global best_ao12

    global worst_mo3
    global worst_ao5
    global worst_ao12

    global media_3
    global media_5
    global media_12    
    
    mo_3.clear()
    ao_5.clear()
    ao_12.clear()   

    global_best_solve = 9999999999
    global_worst_solve = 0

    best_mo3  = 9999999999
    best_ao5  = 9999999999
    best_ao12 = 9999999999

    worst_mo3  = 0
    worst_ao5  = 0
    worst_ao12 = 0    

    media_3  = 9999999999
    media_5  = 9999999999
    media_12 = 9999999999  

    if multiplier != 1:
        print('no multiplier')
        for index, tempo in enumerate(tempos):
            ic(tempo)
            tempo *= multiplier
            tempos[index] = tempo

    elif  divider != 1:
        for index, tempo in enumerate(tempos):
            ic(tempo)
            tempo = int(tempo/divider)
            tempos[index] = tempo
    
    ic(tempos)
    
    for index,_ in enumerate(tempos,1):    
        estatistica(index)  

    

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
    del status[selected-1]

    mo_3.clear()
    ao_5.clear()
    ao_12.clear()

    global_best_solve = 9999999999    
    global_worst_solve = 0

    media_3  = 9999999999
    media_5  = 9999999999
    media_12 = 9999999999
    best_mo3  = 9999999999
    best_ao5  = 9999999999
    best_ao12 = 9999999999
    

    clearTables() 

    clear_file_tempos()

    for index,_ in enumerate(tempos,1):    
        estatistica(index)   


def on_press_enter(event):
    if inputVar.get() == 1:
        # print(inputVar.get())
        enter_time()


def inputVar_change():
    global first_scan
    plot_button.grid_forget() 
    reset_button.grid_forget()
    delete_button.grid_forget()

    if inputVar.get() == 1:
        print_timer.grid_forget()
        input_timer.grid(row = 0, column = 0, sticky = tk.W, pady = 2)
        
        
    elif inputVar.get() == 2:
        input_timer.grid_forget()
        print_timer.grid(row = 0, column = 1, pady = 2)
        # print_timer.grid(row = 0, column = 1, sticky = tk.W, pady = 2)
    

    plot_button.grid  (row = 1, column = 0, sticky = tk.W, pady = 2) 
    reset_button.grid (row = 2, column = 0, sticky = tk.W, pady = 2)
    delete_button.grid(row = 3, column = 0, sticky = tk.W, pady = 2)

    if first_scan == False:      
        write_txt_setting()

    
def precisionVar_change(cube):
    global precisionTimer
    global first_scan    

    if first_scan == True: 
        if precisionVar.get() == 1:
            precisionTimer = 1

        if precisionVar.get() == 2:
            precisionTimer = 2        
            
        elif precisionVar.get() == 3:
            precisionTimer = 3  
        return
    elif first_scan == False: 
        if precisionVar.get() == 1:
            precisionTimer = 1

        if precisionVar.get() == 2:
            precisionTimer = 2        
            
        elif precisionVar.get() == 3:
            precisionTimer = 3  

    precision = int(precisions[cube])
    statusValue = precision
    action = precisionVar.get()
    ic(statusValue)
    ic(action)

    if statusValue == 1 and action == 2: #Décimo para centésimo
        multiplier = 10   
        divider = 1    
        precisionTimer = 2   
    elif statusValue == 1 and action == 3: #Décimo para milésimo
        multiplier = 100
        divider = 1
        precisionTimer = 3
    elif statusValue == 2 and action == 1: #Centésimo para Décimo
        divider = 10  
        multiplier = 1      
        precisionTimer = 1
    elif statusValue == 2 and action == 3: #Centésimo para milésimo
        multiplier = 10
        divider = 1
        precisionTimer = 3
    elif statusValue == 3 and action == 1:     #milésimo para décimo
        divider = 100
        multiplier = 1
        precisionTimer = 1
    elif statusValue == 3 and action == 2:    #milésimo para Centésimo
        divider = 10  
        multiplier = 1 
        precisionTimer = 2   
    else: 
        divider = 1  
        multiplier = 1 
        precisionTimer = precisions[cube]

    
    precisions[cube] = precisionTimer
    ic(multiplier)
    ic(divider)

   
    atualizarTempoPrecision(multiplier,divider)
    

    if first_scan == False:      
        write_txt_setting()

def holdVar_change():
    global first_scan
    global holdSpace

    if holdVar.get() == 1:
        holdSpace = 0        
        
    elif holdVar.get() == 2:
        holdSpace = 300

    elif holdVar.get() == 3:
        holdSpace = 550
    
    elif holdVar.get() == 4:
        holdSpace = 1000
    
    if first_scan == False:      
        write_txt_setting()
    
def inspecionVar_change():
    global first_scan
    global timer_state 
    
    if inspecionVar.get() == 0:
        timer_state = 2
        
    elif inspecionVar.get() == 1:
        timer_state = 0
    
    if first_scan == False:      
        write_txt_setting()

def scrambleVar_change(): 
    global first_scan   
    
    if scrambleVar.get() == 0:
        our_canvas.grid_forget() 
        
    elif scrambleVar.get() == 1:                
        our_canvas.grid(row = 5, column = 1, sticky = tk.E, pady = 2)
    
    if first_scan == False:      
        write_txt_setting()
    
def scramble3DVar_change(): 
    global first_scan   
    
    if scramble3DVar.get() == 0:
        canvas.get_tk_widget().pack_forget()
        
    elif scramble3DVar.get() == 1:                   
        canvas.get_tk_widget().pack()                 
    
    if first_scan == False:      
        write_txt_setting()

def savetimeVar_change():
    global saveTime 
    global first_scan
    
    if savetimeVar.get() == 0:
        saveTime = 0
        
    elif savetimeVar.get() == 1:       
        saveTime = 1
        # if first_scan == True:
        #     importar_tempos()
        if first_scan == False:
            guardar_tempos()    

    if first_scan == False:      
        write_txt_setting()
  
def rankingVar_change():
    global first_scan
    global timer_state 
    global enableRanking
    
    if rankingVar.get() == 0:
        enableRanking = 0      
        tb_ranking.grid_forget()  
        
    elif rankingVar.get() == 1:
        enableRanking = 1
        tb_ranking.grid(row = 1, column = 1, columnspan = 2, rowspan = 2, sticky = tk.W, pady = 2)
        # create_ranking()        
    
    write_txt_setting()    
   
def genderVar_change():
    global gender
    global first_scan
    
    if genderVar.get() == 1:
        gender = 1  
        
    elif genderVar.get() == 2:
        gender = 2
    
    elif genderVar.get() == 3:
        gender = 3
        
        
    create_ranking()
    
    if first_scan == False:      
        write_txt_setting()
    
        for i in tb_stat.get_children():
            tb_stat.delete(i) 

        for i in tb_times.get_children():
            tb_times.delete(i) 

        for i in tb_ranking.get_children():
            tb_ranking.delete(i) 

        for index,_ in enumerate(tempos,1):    
            estatistica(index)   

def ModeVar_change():    
    
    if ModeVar.get() == 1:
        ctk.set_appearance_mode("system")
        
    elif ModeVar.get() == 2:
        ctk.set_appearance_mode("light")
    
    elif ModeVar.get() == 3:
        ctk.set_appearance_mode("dark")
    
    if first_scan == False:      
        write_txt_setting()

def themeVar_change():    
    
    if themeVar.get() == 1:        
        ctk.set_default_color_theme("blue")
        
    elif themeVar.get() == 2:        
        ctk.set_default_color_theme("green")
    
    
    if first_scan == False:      
        write_txt_setting()

def statusVar_Change(tempoValue,statusValue,action,selected):
    
    if precisionTimer == 1:
        multiplier = 10
    elif precisionTimer == 2:
        multiplier = 100
    elif precisionTimer == 3:
        multiplier = 1000

    if statusValue == "OK" and action == "+2":
        tempos[int(selected)-1] +=2*multiplier
        status[int(selected)-1] = "+2"
    elif statusValue == "OK" and action == "DNF":
        status[int(selected)-1] = "DNF"
    elif statusValue == "+2" and action == "OK":
        tempos[int(selected)-1] -=2*multiplier
        status[int(selected)-1] = "OK"
    elif statusValue == "+2" and action == "DNF":
        tempos[int(selected)-1] -=2*multiplier
        status[int(selected)-1] = "DNF"
    elif statusValue == "DNF" and action == "OK":        
        status[int(selected)-1] = "OK"
    elif statusValue == "DNF" and action == "+2":
        tempos[int(selected)-1] +=2*multiplier
        status[int(selected)-1] = "+2"    
    
    atualizar()

    


    

def donothing():
   filewin = tk.Toplevel(root)
   button = tk.Button(filewin, text="Do nothing button")
   button.pack()

def donothing_event(event):  
   
   try:
       filewin.quit()
       filewin.destroy()
   
   except:       
       filewin = tk.Toplevel(root)
       filewin.geometry('600x300+1200+200') 
       button = tk.Button(filewin, text="Do nothing button")
       button.pack()
       selected = tb_times.focus()   
       print(selected)      

       print_valor = tk.Label(filewin, text = tempos[int(selected)-1]) 
       print_status = tk.Label(filewin, text = status[int(selected)-1]) 
       print_valor.pack()       
       print_status.pack()       
       btn_mo03 = tk.Button(filewin, text = "mo03") 
       btn_ao05 = tk.Button(filewin, text = "ao05") 
       btn_ao12 = tk.Button(filewin, text = "ao12") 
       btn_OK = tk.Button(filewin, text = "OK",command= lambda: statusVar_Change(tempos[int(selected)-1],status[int(selected)-1],"OK",selected)) 
       btn_2 = tk.Button(filewin, text = "+2",command= lambda: statusVar_Change(tempos[int(selected)-1],status[int(selected)-1],"+2",selected)) 
       btn_DNF = tk.Button(filewin, text = "DNF",command= lambda: statusVar_Change(tempos[int(selected)-1],status[int(selected)-1],"DNF",selected)) 
       btn_mo03.pack(side = tk.LEFT, anchor = tk.W)
       btn_ao05.pack(side = tk.LEFT, anchor = tk.W)
       btn_ao12.pack(side = tk.LEFT, anchor = tk.W)
       btn_OK.pack(side = tk.LEFT, anchor = tk.W)
       btn_2.pack(side = tk.LEFT, anchor = tk.W)
       btn_DNF.pack(side = tk.LEFT, anchor = tk.W)
    #    print_valor = tk.Label(filewin, text = tempos[int(selected)-1]) 
    #    print_valor.pack()       


ctk.CTkLabel(row1, text = "Modalidade :").grid(column = 0,row = 0) 

eventosValues = ['2x2','3x3', '4x4','5x5','6x6','7x7','pyraminx','megaminx','skewb','clock','3x3 OH']
eventsComboBox = ctk.CTkComboBox(row1,state = "readonly", values = eventosValues, command=change_event) 
# Adding combobox drop down list 


eventsComboBox.grid(column = 1, row = 0) 
# eventos.bind('<<ComboboxSelected>>',change_event)
# Shows number as a default value 
# eventsComboBox.set('3x3') 


# img = tk.PhotoImage(file = r"C:\Users\gabri\OneDrive\Documentos\VScode\lena.png")
# label_img = tk.Label(root, image = img)
# label_img.pack(expand = "yes",anchor = tk.SE)
# label_img.pack(fill = "both", expand = "yes",side=tk.TOP , anchor = tk.S)

# print_scramble = ctk.CTkLabel(row2,text = actual_scramble,wraplength = 500,font = ("Arial", 18))
# print_scramble.grid(column = 0, row = 0)


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

tb_stat['columns'] = ('tempos','atual', 'melhor',"pior")

tb_stat.column("#0", width=0,  stretch=tk.NO)
tb_stat.column("tempos",anchor=tk.CENTER,width=80)
tb_stat.column("atual",anchor=tk.CENTER, width=80)
tb_stat.column("melhor",anchor=tk.CENTER,width=80)
tb_stat.column("pior",anchor=tk.CENTER,width=80)

tb_stat.heading("#0",text="",anchor=tk.CENTER)
tb_stat.heading("tempos",text="",anchor=tk.CENTER)
tb_stat.heading("atual",text="atual",anchor=tk.CENTER)
tb_stat.heading("melhor",text="melhor",anchor=tk.CENTER)
tb_stat.heading("pior",text="pior",anchor=tk.CENTER)

tb_stat.grid(column = 0, row = 0)



root.bind("<KeyPress-space>",on_press_space)
root.bind("<KeyRelease-space>",on_release_space)
root.bind("<KeyPress-Escape>",on_press_esc)
root.bind("<KeyPress-Return>",on_press_enter)


actual_timer.set("0:00")

print_timer = ctk.CTkLabel(row4,textvariable = actual_timer, font = ("Arial", 24))
# print_timer.pack(anchor=tk.CENTER)
# print_timer.pack(side = tk.LEFT,anchor=tk.N)

input_timer  = ctk.CTkEntry(row4)

plot_button = ctk.CTkButton(master = row4,command = plot,	height = 2, width = 10, text = "Plot") 
# plot_button.pack(anchor = tk.CENTER) 
# plot_button.pack(side = tk.LEFT,anchor = tk.W) 

reset_button  = ctk.CTkButton(master = row4,command = resetar,	height = 2, width = 10, text = "Reset") 
# reset_button.pack(side = tk.LEFT,anchor = tk.W)

delete_button  = ctk.CTkButton(master = row4,command = deletar,	height = 2, width = 10, text = "Delete") 
# delete_button.pack(side = tk.LEFT,anchor = tk.W)

tb_ranking = ttk.Treeview(row4, height=2)

tb_ranking['columns'] = ('NRS','CRS','WRS', 'Tempo único','Média','WRA','CRA','NRA')

tb_ranking.column("#0", width=0,  stretch=tk.NO)
tb_ranking.column("NRS",anchor=tk.CENTER,width=80)
tb_ranking.column("CRS",anchor=tk.CENTER, width=80)
tb_ranking.column("WRS",anchor=tk.CENTER,width=80)
tb_ranking.column("Tempo único",anchor=tk.CENTER,width=80)
tb_ranking.column("Média",anchor=tk.CENTER,width=80)
tb_ranking.column("WRA",anchor=tk.CENTER,width=80)
tb_ranking.column("CRA",anchor=tk.CENTER,width=80)
tb_ranking.column("NRA",anchor=tk.CENTER,width=80)

tb_ranking.heading("#0",text="",anchor=tk.CENTER)
tb_ranking.heading("NRS",text="NR",anchor=tk.CENTER)
tb_ranking.heading("CRS",text="CR",anchor=tk.CENTER)
tb_ranking.heading("WRS",text="WR",anchor=tk.CENTER)
tb_ranking.heading("Tempo único",text="Tempo",anchor=tk.CENTER)
tb_ranking.heading("Média",text="Média",anchor=tk.CENTER)
tb_ranking.heading("WRA",text="WR",anchor=tk.CENTER)
tb_ranking.heading("CRA",text="CR",anchor=tk.CENTER)
tb_ranking.heading("NRA",text="NR",anchor=tk.CENTER)

# tb_ranking.pack(side = tk.RIGHT,anchor=tk.NE)
# tb_ranking.pack(anchor=tk.NE)

# our_canvas.pack(side = tk.RIGHT,anchor = tk.S)
# delete_button.pack(side = tk.LEFT)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
importFileMenu = tk.Menu(menubar, tearoff=0)
optionmenu = tk.Menu(menubar, tearoff=0)
precisionmenu = tk.Menu(menubar, tearoff=0)
colormenu = tk.Menu(menubar, tearoff=0)
inputmenu = tk.Menu(menubar, tearoff=0)
holdmenu = tk.Menu(menubar, tearoff=0)
rankingmenu = tk.Menu(menubar, tearoff=0)
gendermenu = tk.Menu(menubar, tearoff=0)
UImenu = tk.Menu(menubar, tearoff=0)
modemenu = tk.Menu(menubar, tearoff=0)
thememenu = tk.Menu(menubar, tearoff=0)
helpmenu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Opções", menu=optionmenu)
menubar.add_cascade(label="Ranking", menu=rankingmenu)
menubar.add_cascade(label="UI", menu=UImenu)
menubar.add_cascade(label="Help", menu=helpmenu)


filemenu.add_cascade(label="Importar tempos", menu=importFileMenu)
filemenu.add_command(label="Exportar tempos", command=exportar_tempos)


importFileMenu.add_command(label="Arquivo", command=importar_tempos_file)
importFileMenu.add_command(label="Pasta", command=importar_tempos_folder)

filemenu.add_separator()
filemenu.add_command(label="Sair", command=exportar_tempos)

inspecionVar = tk.BooleanVar()
scrambleVar = tk.BooleanVar()
scramble3DVar = tk.BooleanVar()
savetimeVar = tk.BooleanVar()
rankingVar = tk.BooleanVar()
inputVar = tk.IntVar()
precisionVar = tk.IntVar()
holdVar = tk.IntVar()
genderVar = tk.IntVar()
ModeVar = tk.IntVar()
themeVar = tk.IntVar()

optionmenu.add_checkbutton(label="Guardar tempos", onvalue=1, offvalue=0, variable=savetimeVar, command= savetimeVar_change)
optionmenu.add_checkbutton(label="Tempo de Inspeção", onvalue=1, offvalue=0, variable=inspecionVar, command= inspecionVar_change)
optionmenu.add_checkbutton(label="Desenho scramble", onvalue=1, offvalue=0, variable=scrambleVar, command= scrambleVar_change)
optionmenu.add_checkbutton(label="Desenho 3D scramble", onvalue=1, offvalue=0, variable=scramble3DVar, command= scramble3DVar_change)
optionmenu.add_cascade(label="Change color scramble", menu=colormenu)
optionmenu.add_cascade(label="Disparador cronômetro", menu=inputmenu)
optionmenu.add_cascade(label="Precisão timer", menu=precisionmenu)
optionmenu.add_cascade(label="Tempo segurar Espaço", menu=holdmenu)


colormenu.add_command(label="Face 1", command= lambda: changeColorScramble('1'))
colormenu.add_command(label="Face 2", command= lambda: changeColorScramble('2'))
colormenu.add_command(label="Face 3", command= lambda: changeColorScramble('3'))
colormenu.add_command(label="Face 4", command= lambda: changeColorScramble('4'))
colormenu.add_command(label="Face 5", command= lambda: changeColorScramble('5'))
colormenu.add_command(label="Face 6", command= lambda: changeColorScramble('6'))
colormenu.add_command(label="Reset Colors", command= ResetColorScramble)

inputmenu.add_radiobutton(label="Manual", value=1, variable=inputVar, command=inputVar_change)
inputmenu.add_radiobutton(label="Timer", value=2, variable=inputVar, command=inputVar_change)
inputmenu.add_radiobutton(label="Stackmat", value=3, variable=inputVar, command=inputVar_change)

precisionmenu.add_radiobutton(label="0.1", value=1, variable=precisionVar, command= lambda: precisionVar_change(str(eventsComboBox.get())))
precisionmenu.add_radiobutton(label="0.01", value=2, variable=precisionVar, command= lambda: precisionVar_change(str(eventsComboBox.get())))
precisionmenu.add_radiobutton(label="0.001", value=3, variable=precisionVar, command= lambda: precisionVar_change(str(eventsComboBox.get())))
holdmenu.add_radiobutton(label="0", value=1, variable=holdVar, command= holdVar_change)
holdmenu.add_radiobutton(label="0.3", value=2, variable=holdVar, command= holdVar_change)
holdmenu.add_radiobutton(label="0.55", value=3, variable=holdVar, command= holdVar_change)
holdmenu.add_radiobutton(label="1", value=4, variable=holdVar, command= holdVar_change)


rankingmenu.add_command(label="Importar ranking", command=importar_ranking)
rankingmenu.add_command(label="Unzip ranking", command=unzip_database)
rankingmenu.add_checkbutton(label="Habilitar Ranking ", onvalue=1, offvalue=0, variable=rankingVar, command= rankingVar_change)
rankingmenu.add_cascade(label="Gênero", menu=gendermenu)
rankingmenu.add_command(label="Verificar update", command=update_ranking)

gendermenu.add_radiobutton(label="*", value=1, variable=genderVar, command= genderVar_change)
gendermenu.add_radiobutton(label="m", value=2, variable=genderVar, command= genderVar_change)
gendermenu.add_radiobutton(label="f", value=3, variable=genderVar, command= genderVar_change)

UImenu.add_cascade(label="Mode", menu=modemenu)
UImenu.add_cascade(label="Color Theme", menu=thememenu)

modemenu.add_radiobutton(label="System", value=1, variable=ModeVar, command= ModeVar_change)
modemenu.add_radiobutton(label="Light", value=2, variable=ModeVar, command= ModeVar_change)
modemenu.add_radiobutton(label="Dark", value=3, variable=ModeVar, command= ModeVar_change)

thememenu.add_radiobutton(label="Blue", value=1, variable=themeVar, command= themeVar_change)
thememenu.add_radiobutton(label="Green", value=2, variable=themeVar, command= themeVar_change)

helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)



# GUI Download WCA Ranking
DownloadWin = tk.Toplevel()
DownloadWin.title("Downloader")

progress_var = tk.IntVar()

ttk.Label(DownloadWin, text="Progresso do Download:").pack(pady=5)
progress_bar = ttk.Progressbar(DownloadWin, length=400, variable=progress_var, maximum=100)
progress_bar.pack(pady=5)

percent_label = ttk.Label(DownloadWin, text="0%")
percent_label.pack()

speed_label = ttk.Label(DownloadWin, text="Velocidade: 0 KB/s")
speed_label.pack()

downloaded_label = ttk.Label(DownloadWin, text="0 KB / 0 KB")
downloaded_label.pack()

status_label = ttk.Label(DownloadWin, text="Pronto")
status_label.pack(pady=10)

ttk.Button(DownloadWin, text="Iniciar Download", command=start_download).pack(pady=10)

jsonSettings = {}

def read_txt_setting():

    global rankingPath
    global first_scan
    global faceColors
    global precisions

    first_scan = True
    try:
        if first_scan == True:

            
            with open('Scrambler_Settings.json', 'r') as openfile:
                jsonSettings = json.load(openfile)               

            precisions = json.loads(jsonSettings["precisions"].replace("'", '"'))                    
            inspecionVar.set(jsonSettings['Tempo de inspecao'])
            scrambleVar.set(jsonSettings['Desenho Scrambler'])        
            inputVar.set(jsonSettings['Disparador cronometro'])        
            holdVar.set(jsonSettings['Tempo hold'])           
            eventsComboBox.set(jsonSettings['Modalidade'])           
            rankingVar.set(jsonSettings['Habilitar Ranking'])
            genderVar.set(jsonSettings['Genero'])                           
            savetimeVar.set(jsonSettings['Salvar tempo'])        
            rankingPath = jsonSettings['Ranking Path']
            scramble3DVar.set(jsonSettings['Desenho Scrambler 3D']) 
            ModeVar.set(jsonSettings['Mode']) 
            themeVar.set(jsonSettings['colorTheme'])               
            precisionVar.set(precisions[str(eventsComboBox.get())])  
            faceColors = json.loads(jsonSettings["colors"].replace("'", '"'))        
            

            inputVar_change()
            precisionVar_change(precisionVar_change(eventsComboBox.get()))
            holdVar_change()
            inspecionVar_change()
            scrambleVar_change()
            change_event(jsonSettings['Modalidade'])
            genderVar_change()  
            savetimeVar_change()         
            rankingVar_change()   
            scramble3DVar_change()  
            ModeVar_change() 
            themeVar_change()         
            
            with open('Scrambler_Settings.json', 'w') as openfile:
                jsonSettings = json.dump(jsonSettings,openfile,indent=4)  

    except Exception as error:
        print("An error occurred:", error) # An error occurred: name 'x' is not defined:
        if first_scan == True:  
            
            
            inspecionVar.set(1)
            inputVar.set(2) 
            precisionVar.set(2)
            holdVar.set(3)
            scrambleVar.set(1)
            eventsComboBox.set('3x3') 
            rankingVar.set(0)
            genderVar.set(0)
            inspecionVar.set(1)
            savetimeVar.set(0)  
            scramble3DVar.set(1)  
            ModeVar.set(3)    

            inputVar_change()
            precisionVar_change(precisionVar_change(eventsComboBox.get()))
            holdVar_change()
            inspecionVar_change()
            scrambleVar_change()
            change_event(rankingPath)
            rankingVar_change()
            savetimeVar_change()         
            create_ranking()
            scramble3DVar_change()
            ModeVar_change()
            themeVar_change()
            
            
            write_txt_setting()
    first_scan = False
    

def write_txt_setting():
    global rankingPath    
    global faceColors
    global precisions

    global gender    
    jsonSettings = {}
      
    jsonSettings['Tempo de inspecao']= str(inspecionVar.get())
    jsonSettings['Desenho Scrambler'] = str(scrambleVar.get())
    jsonSettings['Disparador cronometro'] = str(inputVar.get())
    jsonSettings['Precisao'] = str(precisionVar.get())
    jsonSettings['Tempo hold'] = str(holdVar.get())
    jsonSettings['Modalidade'] =  str(eventsComboBox.get())    
    jsonSettings['Habilitar Ranking'] = str(rankingVar.get())
    jsonSettings['Genero'] = str(gender)
    jsonSettings['Salvar tempo'] = str(savetimeVar.get())
    jsonSettings['Ranking Path'] = str(rankingPath)
    jsonSettings['Desenho Scrambler 3D'] = str(scramble3DVar.get())  
    jsonSettings['Mode'] = str(ModeVar.get())  
    jsonSettings['colorTheme'] = str(themeVar.get())  
    jsonSettings['colors'] = str(faceColors)  
    jsonSettings['precisions'] = str(precisions)  

    with open('Scrambler_Settings.json', 'w') as openfile:
        jsonSettings = json.dump(jsonSettings,openfile,indent=4)    

read_txt_setting()
root.config(menu=menubar)
root.mainloop() 
