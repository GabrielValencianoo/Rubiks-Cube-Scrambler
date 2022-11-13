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
from msvcrt import getch
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import datetime
import csv

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)



root = tk.Tk() 
root.geometry('1000x600+1200+200') 

# Label 
row1 = ttk.LabelFrame(root)
row2 = ttk.LabelFrame(root)
row3 = ttk.LabelFrame(root)

row1.pack()
row2.pack()
# row2.pack(side=tk.TOP,anchor = tk.W)
row3.pack(side=tk.LEFT,anchor = tk.N)

timing = 0
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
scrambles = []
datas = []

best_mo3  = 9999
best_ao5  = 9999
best_ao12 = 9999

media_3  = 9999
media_5  = 9999
media_12 = 9999

global_best_solve = 9999
global_worst_solve = 0

countdown = 15
run_inspecton = False

def trunc(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def time_convert(time):
    
    minutes, seconds = divmod(time, 60)  
    seconds = trunc(seconds,2)    
    minutes = int(minutes)
    return minutes , seconds

def best_worst(lista,type):
    
    if type == 1:
        global global_best_solve
        global global_worst_solve
        if lista[-1] < global_best_solve:
            global_best_solve = lista[-1]
        if lista[-1] > global_worst_solve:
            global_worst_solve = lista[-1]

        return global_best_solve, global_worst_solve
        
    if type == 2:
        local_best_solve = 9999
        local_worst_solve = 0
        for solve in lista:
            if solve < local_best_solve:
                local_best_solve = solve
            if solve > local_worst_solve:
                local_worst_solve = solve
    
        return local_best_solve, local_worst_solve
 
def average():
    return sum(tempos)/len(tempos)

def mo3():
    list_3 = tempos[-3:]
    average = sum(list_3)/len(list_3) 
    return average    

def ao5():
    list_5 = tempos[-5:]
    b,w = best_worst(list_5,2)
    print(b,w)
    average = (sum(list_5)-b-w)/3
    return average    

def ao12():
    list_12 = tempos[-12:]
    b,w = best_worst(list_12,2)
    average = (sum(list_12)-b-w)/10
    return average    

def estatistica():
    global global_best_solve
    global global_worst_solve
    global best_mo3
    global best_ao5
    global best_ao12
    global media_3
    global media_5
    global media_12
    media = average()

    media_3  = mo3() if len(tempos) >= 3 else media_3
    media_5  = ao5() if len(tempos) >= 5 else media_5
    media_12 = ao12() if len(tempos) >= 12 else media_12

    global_best_solve,global_worst_solve = best_worst(tempos,1)
    
    best_mo3 = media_3 if media_3 < best_mo3 else best_mo3

    best_ao5 = media_5 if media_5 < best_ao5 else best_ao5

    best_ao12 = media_12 if media_12 < best_ao12 else best_ao12


    global_best_solve = trunc(global_best_solve,2)
    global_worst_solve = trunc(global_worst_solve,2)


    if global_best_solve > 60:
        m, s = time_convert(global_best_solve) 
        pglobal_best_solve = str(m) + ":" + str(s)
    else:
        global_best_solve = trunc(global_best_solve,2)
        pglobal_best_solve = global_best_solve

    if global_worst_solve > 60:
        m, s = time_convert(global_worst_solve) 
        pglobal_worst_solve = str(m) + ":" + str(s)
    else:
        global_worst_solve = trunc(global_worst_solve,2)
        pglobal_worst_solve = global_worst_solve

    if media > 60:
        m, s = time_convert(media) 
        pmedia = str(m) + ":" + str(s)
    else:
        media = trunc(media,2)
        pmedia = media

    if media_3 > 60:
        m, s = time_convert(media_3) 
        pmedia_3 = str(m) + ":" + str(s)
    else:
        media_3 = trunc(media_3,2)
        pmedia_3 = media_3
    
    if media_5 > 60:
        m, s = time_convert(media_5) 
        pmedia_5 = str(m) + ":" + str(s)
    else:
        media_5 = trunc(media_5,2)
        pmedia_5 = media_5

    if media_12 > 60:
        m, s = time_convert(media_12) 
        pmedia_12 = str(m) + ":" + str(s)
    else:
        media_12 = trunc(media_12,2)
        pmedia_12 = media_12

    if best_mo3 > 60:
        m, s = time_convert(best_mo3) 
        pbest_mo3 = str(m) + ":" + str(s)
    else:
        best_mo3 = trunc(best_mo3,2)
        pbest_mo3 = best_mo3

    if best_ao5 > 60:
        m, s = time_convert(best_ao5) 
        pbest_ao5 = str(m) + ":" + str(s)
    else:
        best_ao5 = trunc(best_ao5,2)
        pbest_ao5 = best_ao5

    if best_ao12 > 60:
        m, s = time_convert(best_ao12) 
        pbest_ao12 = str(m) + ":" + str(s)
    else:
        best_ao12 = trunc(best_ao12,2)
        pbest_ao12 = best_ao12

    
    hist2.delete(0,9)    

    pmedia_3  = pmedia_3 if len(tempos) >= 3 else 0
    pmedia_5  = pmedia_5 if len(tempos) >= 5 else 0
    pmedia_12 = pmedia_12 if len(tempos) >= 12 else 0

    pbest_mo3  = pbest_mo3 if len(tempos) >= 3 else 0
    pbest_ao5  = pbest_ao5 if len(tempos) >= 5 else 0
    pbest_ao12 = pbest_ao12 if len(tempos) >= 12 else 0


    hist2.insert(tk.END,"n° solves: " + str(len(tempos)))
    hist2.insert(tk.END,"melhor: " + str(pglobal_best_solve))
    hist2.insert(tk.END,"pior:" + str(pglobal_worst_solve))
    hist2.insert(tk.END,"media: " + str(pmedia))
    hist2.insert(tk.END,"mo3: " + str(pmedia_3))
    hist2.insert(tk.END,"ao5: " + str(pmedia_5))
    hist2.insert(tk.END,"ao12: " + str(pmedia_12))
    hist2.insert(tk.END,"PB ao3: " + str(pbest_mo3))
    hist2.insert(tk.END,"PB ao5: " + str(pbest_ao5))
    hist2.insert(tk.END,"PB ao12: " + str(pbest_ao12))


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
        accepted = 0
    # print(actual_scramble)    
    scrambles.append( " ".join(sum_turns))
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 

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
        

        define_flags(n_move)
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0

    # print(actual_scramble)    
    reset_flags()
    
    scrambles.append( " ".join(sum_turns))
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 

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
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0

    reset_flags()
    # print(actual_scramble)    
    scrambles.append( " ".join(sum_turns))
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 
    
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
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0

    reset_flags()
    # print(actual_scramble)    
    scrambles.append( " ".join(sum_turns))
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 

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
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    # print(actual_scramble)  
    reset_flags()  
    scrambles.append( " ".join(sum_turns))
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 
   
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
        accepted = 0


    print(sum_turns)
    # print(actual_scramble)    
    scrambles.append( " ".join(sum_turns))
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 

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
    scrambles.append( " ".join(sum_turns))
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
    scrambles.append( " ".join(sum_turns))
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 

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
    scrambles.append( " ".join(sum_turns))
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 
           

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
    if timer_state == 0:
        timer_state = 1
    
    if timer_state == 2:
        pass

    if timer_state == 4:
        stop_timer()

    stop_timer()
    
    if _short_press is None: # only set timer if a key press is not ongoing
        
        _short_press = True
        _do_space_longpress = root.after(550, do_space_longpress)


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
        timer_state = 0
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
    global timing
    global t0
    global timer_state
    
    if timer_state == 3:
        t0 = time.time()
        timing = 1    
        print("rodando........")

        global actual_timer
        actual_timer.set("rodando........")

        timer_state = 4
        global run_inspecton
        run_inspecton = False
    

def stop_timer(): 
    global timing
    global timer_state

    if timer_state == 4:
        t1 = time.time()
        data = datetime.datetime.now()
        print(data)

        global t0        
        global enable_start_timer 

        dt = t1-t0         
        tempo = dt
        tempos.append(tempo)
        datas.append(data)
        
        enable_start_timer = False
        timing = 0
        timer_state = 5
        # messagebox.showinfo( "Hello Python", "Time Lapsed = {0:.2f}".format(x))
        
        print(tempos)
        global countdown 
        countdown = 15

        tempo = trunc(tempo,2)
        if tempo > 60:
            m, s = time_convert(tempo) 
            ptempo = str(m)+":"+str(s)
        else:   
            ptempo = tempo

        global actual_timer

        hist.insert(tk.END,ptempo)
        actual_timer.set(ptempo)       


        estatistica()
        next_scramble() 

        t2 = time.time()
        print(t2-t1)
        

def change_event(event):   
    
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
    global tempos 
    fig = Figure(figsize = (5, 5),dpi = 100) 

	# list of squares 
    y = tempos
    

	# adding the subplot 
    plot1 = fig.add_subplot(111) 

	# plotting the graph 
    plot1.plot(y) 

	# creating the Tkinter canvas 
	# containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig,	master = root) 
    canvas.draw() 

	# placing the canvas on the Tkinter root 
    canvas.get_tk_widget().pack()     

	# creating the Matplotlib toolbar 
    # toolbar = NavigationToolbar2Tk(canvas,root) 
    # toolbar.update() 

	# placing the toolbar on the Tkinter root 
    # canvas.get_tk_widget().pack() 

ttk.Label(row1, text = "Modalidade :").grid(column = 0,row = 0) 

n = tk.StringVar() 
eventos = ttk.Combobox(row1, width = 10,textvariable = n,state = "readonly") 

# Adding combobox drop down list 
eventos['values'] = ('2x2','3x3', '4x4','5x5','6x6','7x7','pyraminx','megaminx','skewb','clock') 

eventos.grid(column = 1, row = 0) 
eventos.bind('<<ComboboxSelected>>',change_event)
# Shows number as a default value 
eventos.current(1) 
# eventos.current(7) 
# eventos.bind('<FocusOut>', lambda e: eventos.selection_clear(0, tk.END))


# print(actual_scramble)

img = tk.PhotoImage(file = r"C:\Users\gabri\OneDrive\Documentos\VScode\lena.png")
label_img = tk.Label(root, image = img)
# label_img.pack(expand = "yes",anchor = tk.SE)
# label_img.pack(fill = "both", expand = "yes",side=tk.TOP , anchor = tk.S)





print_scramble = tk.Label(row2,textvariable = actual_scramble,wraplength = 500)
print_scramble.grid(column = 0, row = 0)

actual_timer.set("0:00")

print_timer = tk.Label(root,textvariable = actual_timer)
print_timer.pack()


# hist = tk.Listbox(row3,yscrollcommand = scrollbar.set,takefocus = 0,state = tk.DISABLED)



# hist.bind('<FocusOut>', lambda e: hist.selection_clear(0, tk.END))

scrollbar = tk.Scrollbar(row3)

# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.grid(column = 1, row = 0)



hist = tk.Listbox(row3,yscrollcommand = scrollbar.set)
hist.grid(column = 0, row = 0)

hist2 = tk.Listbox(row3)
hist2.grid(column = 2, row = 0)



scrollbar.config(command=hist.yview)



scrambler_3x3()
# scrambler_megaminx()


# root.focus_set()
# root.focus_force()
root.bind("<KeyPress-space>",on_press_space)
root.bind("<KeyRelease-space>",on_release_space)


plot_button = tk.Button(master = root,command = plot,	height = 2, width = 10, text = "Plot") 



plot_button.pack() 


root.mainloop() 