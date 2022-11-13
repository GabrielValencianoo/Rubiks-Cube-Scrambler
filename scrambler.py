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




root = tk.Tk() 
root.geometry('500x500+1200+200') 
# Label 
row1 = ttk.LabelFrame(root)
row2 = ttk.LabelFrame(root)
row3 = ttk.LabelFrame(root)

row1.pack()
row2.pack(side=tk.TOP,anchor = tk.W)
row3.pack(side=tk.LEFT,anchor = tk.N)

scrollbar = tk.Scrollbar(row3)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.grid(column = 1, row = 0)
timing = 0
t1 = 0


actual_scramble = tk.StringVar()


def define_flags(n_move):
    
    if (n_move == 1 or n_move == 2 or n_move == 3):
                accepted = 0
    elif (n_move == 4 or n_move == 5 or n_move == 6):
                accepted = 0
    elif (n_move == 7 or n_move == 8 or n_move == 9):
                accepted = 0
    elif (n_move == 10 or n_move == 11 or n_move == 12):
                accepted = 0
    elif (n_move == 13 or n_move == 14 or n_move == 15):
                accepted = 0
    elif (n_move == 16 or n_move == 17 or n_move == 18):
                accepted = 0

    elif (n_move == 19 or n_move == 20 or n_move == 21):
                accepted = 0
    elif (n_move == 22 or n_move == 23 or n_move == 24):
                accepted = 0
    elif (n_move == 25 or n_move == 26 or n_move == 27):
                accepted = 0
    elif (n_move == 28 or n_move == 29 or n_move == 30):
                accepted = 0
    elif (n_move == 31 or n_move == 32 or n_move == 33):
                accepted = 0
    elif (n_move == 34 or n_move == 35 or n_move == 36):
                accepted = 0

    elif (n_move == 37 or n_move == 38 or n_move == 39):
                accepted = 0
    elif (n_move == 40 or n_move == 41 or n_move == 42):
                accepted = 0
    elif (n_move == 43 or n_move == 44 or n_move == 45):
                accepted = 0
    elif (n_move == 46 or n_move == 47 or n_move == 48):
                accepted = 0
    elif (n_move == 49 or n_move == 50 or n_move == 51):
                accepted = 0
    elif (n_move == 52 or n_move == 53 or n_move == 54):
                accepted = 0




def next_scramble():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0
    flag_R = 0
    flag_L = 0
    flag_U = 0
    flag_D = 0
    flag_F = 0
    flag_B = 0
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
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 2:
            turn = "R'"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 3:
            turn = "R2"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 4:
            turn = "L"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 5:
            turn = "L'"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 6:
            turn = "L2"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 7:
            turn = "U"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 8:
            turn = "U'"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 9:
            turn = "U2"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 10:
            turn = "D"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 11:
            turn = "D'"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 12:
            turn = "D2"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 13:
            turn = "F"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 14:
            turn = "F'"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 15:
            turn = "F2"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 16:
            turn = "B"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 17:
            turn = "B'"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 18:
            turn = "B2"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    # print(actual_scramble)    
    x = " ".join(sum_turns)
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update()    

def scrambler_2x2():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0
    flag_R = 0
    flag_L = 0
    flag_U = 0
    flag_D = 0
    flag_F = 0
    flag_B = 0
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
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 2:
            turn = "R'"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 3:
            turn = "R2"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 4:
            turn = "L"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 5:
            turn = "L'"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 6:
            turn = "L2"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 7:
            turn = "U"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 8:
            turn = "U'"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 9:
            turn = "U2"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 10:
            turn = "D"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 11:
            turn = "D'"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 12:
            turn = "D2"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 13:
            turn = "F"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 14:
            turn = "F'"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 15:
            turn = "F2"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 16:
            turn = "B"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 17:
            turn = "B'"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 18:
            turn = "B2"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    # print(actual_scramble)    
    x = " ".join(sum_turns)
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 

def scrambler_3x3():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0
    flag_R = 0
    flag_L = 0
    flag_U = 0
    flag_D = 0
    flag_F = 0
    flag_B = 0
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
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 2:
            turn = "R'"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 3:
            turn = "R2"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 4:
            turn = "L"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 5:
            turn = "L'"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 6:
            turn = "L2"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 7:
            turn = "U"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 8:
            turn = "U'"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 9:
            turn = "U2"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 10:
            turn = "D"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 11:
            turn = "D'"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 12:
            turn = "D2"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 13:
            turn = "F"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 14:
            turn = "F'"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 15:
            turn = "F2"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 16:
            turn = "B"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 17:
            turn = "B'"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 18:
            turn = "B2"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    # print(actual_scramble)    
    x = " ".join(sum_turns)
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 

def scrambler_4x4():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0
    flag_R = 0
    flag_L = 0
    flag_U = 0
    flag_D = 0
    flag_F = 0
    flag_B = 0
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
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 2:
            turn = "R'"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 3:
            turn = "R2"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 4:
            turn = "L"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 5:
            turn = "L'"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 6:
            turn = "L2"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 7:
            turn = "U"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 8:
            turn = "U'"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 9:
            turn = "U2"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 10:
            turn = "D"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 11:
            turn = "D'"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 12:
            turn = "D2"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 13:
            turn = "F"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 14:
            turn = "F'"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 15:
            turn = "F2"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 16:
            turn = "B"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 17:
            turn = "B'"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 18:
            turn = "B2"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    # print(actual_scramble)    
    x = " ".join(sum_turns)
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 

def scrambler_5x5():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0
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
    sum_turns = []
    for i in range(40):

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
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 2:
            turn = "R'"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 3:
            turn = "R2"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 4:
            turn = "L"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 5:
            turn = "L'"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 6:
            turn = "L2"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 7:
            turn = "U"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 8:
            turn = "U'"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 9:
            turn = "U2"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 10:
            turn = "D"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 11:
            turn = "D'"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 12:
            turn = "D2"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 13:
            turn = "F"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 14:
            turn = "F'"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 15:
            turn = "F2"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 16:
            turn = "B"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 17:
            turn = "B'"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 18:
            turn = "B2"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0


        if n_move == 19:
            turn = "Rw"
            flag_Rw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 20:
            turn = "Rw'"
            flag_Rw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 21:
            turn = "Rw2"
            flag_Rw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0

        elif n_move == 22:
            turn = "Lw"
            flag_Lw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 23:
            turn = "Lw'"
            flag_Lw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 24:
            turn = "Lw2"
            flag_Lw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0


        elif n_move == 25:
            turn = "Uw"
            flag_Uw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 26:
            turn = "Uw'"
            flag_Uw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 27:
            turn = "Uw2"
            flag_Uw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0

        elif n_move == 28:
            turn = "Dw"
            flag_Dw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 29:
            turn = "Dw'"
            flag_Dw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 30:
            turn = "Dw2"
            flag_Dw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0

        elif n_move == 31:
            turn = "Fw"
            flag_Fw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0
        elif n_move == 32:
            turn = "Fw'"
            flag_Fw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0
        elif n_move == 33:
            turn = "Fw2"
            flag_Fw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0

        elif n_move == 34:
            turn = "Bw"
            flag_Bw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0
        elif n_move == 35:
            turn = "Bw'"
            flag_Bw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0
        elif n_move == 36:
            turn = "Bw2"
            flag_Bw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0





    
        
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    # print(actual_scramble)    
    x = " ".join(sum_turns)
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 

def scrambler_6x6():
    turn = "" #actual turn (string)
    n_move = 0 #actual turn
    pr_move = 0 #previous turn
    global actual_scramble 
    accepted = 0
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



    sum_turns = []
    for i in range(40):

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
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 2:
            turn = "R'"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 3:
            turn = "R2"
            flag_R = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 4:
            turn = "L"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 5:
            turn = "L'"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 6:
            turn = "L2"
            flag_L = 1
            
            flag_U = 0
            flag_D = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 7:
            turn = "U"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 8:
            turn = "U'"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 9:
            turn = "U2"
            flag_U = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 10:
            turn = "D"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 11:
            turn = "D'"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 12:
            turn = "D2"
            flag_D = 1
            
            flag_R = 0
            flag_L = 0
            flag_F = 0
            flag_B = 0
        elif n_move == 13:
            turn = "F"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 14:
            turn = "F'"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 15:
            turn = "F2"
            flag_F = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 16:
            turn = "B"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 17:
            turn = "B'"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0
        elif n_move == 18:
            turn = "B2"
            flag_B = 1
            
            flag_R = 0
            flag_L = 0
            flag_D = 0
            flag_U = 0


        if n_move == 19:
            turn = "Rw"
            flag_Rw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 20:
            turn = "Rw'"
            flag_Rw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 21:
            turn = "Rw2"
            flag_Rw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0

        elif n_move == 22:
            turn = "Lw"
            flag_Lw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 23:
            turn = "Lw'"
            flag_Lw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 24:
            turn = "Lw2"
            flag_Lw = 1
            
            flag_Uw = 0
            flag_Dw = 0
            flag_Fw = 0
            flag_Bw = 0


        elif n_move == 25:
            turn = "Uw"
            flag_Uw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 26:
            turn = "Uw'"
            flag_Uw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 27:
            turn = "Uw2"
            flag_Uw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0

        elif n_move == 28:
            turn = "Dw"
            flag_Dw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 29:
            turn = "Dw'"
            flag_Dw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0
        elif n_move == 30:
            turn = "Dw2"
            flag_Dw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Fw = 0
            flag_Bw = 0

        elif n_move == 31:
            turn = "Fw"
            flag_Fw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0
        elif n_move == 32:
            turn = "Fw'"
            flag_Fw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0
        elif n_move == 33:
            turn = "Fw2"
            flag_Fw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0

        elif n_move == 34:
            turn = "Bw"
            flag_Bw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0
        elif n_move == 35:
            turn = "Bw'"
            flag_Bw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0
        elif n_move == 36:
            turn = "Bw2"
            flag_Bw = 1
            
            flag_Rw = 0
            flag_Lw = 0
            flag_Dw = 0
            flag_Uw = 0

        if n_move == 37:
            turn = "3Rw"
            flag_3Rw = 1
            
            flag_3Uw = 0
            flag_3Dw = 0
            flag_3Fw = 0
            flag_3Bw = 0
        elif n_move == 38:
            turn = "3Rw'"
            flag_3Rw = 1
            
            flag_3Uw = 0
            flag_3Dw = 0
            flag_3Fw = 0
            flag_3Bw = 0
        elif n_move == 39:
            turn = "3Rw2"
            flag_3Rw = 1
            
            flag_3Uw = 0
            flag_3Dw = 0
            flag_3Fw = 0
            flag_3Bw = 0

        elif n_move == 40:
            turn = "3Lw"
            flag_3Lw = 1
            
            flag_3Uw = 0
            flag_3Dw = 0
            flag_3Fw = 0
            flag_3Bw = 0
        elif n_move == 41:
            turn = "3Lw'"
            flag_3Lw = 1
            
            flag_3Uw = 0
            flag_3Dw = 0
            flag_3Fw = 0
            flag_3Bw = 0
        elif n_move == 42:
            turn = "3Lw2"
            flag_3Lw = 1
            
            flag_3Uw = 0
            flag_3Dw = 0
            flag_3Fw = 0
            flag_3Bw = 0

        elif n_move == 43:
            turn = "3Uw"
            flag_3Uw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Fw = 0
            flag_3Bw = 0
        elif n_move == 44:
            turn = "3Uw'"
            flag_3Uw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Fw = 0
            flag_3Bw = 0
        elif n_move == 45:
            turn = "3Uw2"
            flag_3Uw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Fw = 0
            flag_3Bw = 0

        elif n_move == 46:
            turn = "3Dw"
            flag_3Dw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Fw = 0
            flag_3Bw = 0
        elif n_move == 47:
            turn = "3Dw'"
            flag_3Dw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Fw = 0
            flag_3Bw = 0
        elif n_move == 48:
            turn = "3Dw2"
            flag_3Dw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Fw = 0
            flag_3Bw = 0

        elif n_move == 49:
            turn = "3Fw"
            flag_3Fw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Dw = 0
            flag_3Uw = 0
        elif n_move == 50:
            turn = "3Fw'"
            flag_3Fw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Dw = 0
            flag_3Uw = 0
        elif n_move == 51:
            turn = "3Fw2"
            flag_3Fw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Dw = 0
            flag_3Uw = 0

        elif n_move == 52:
            turn = "3Bw"
            flag_3Bw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Dw = 0
            flag_3Uw = 0
        elif n_move == 53:
            turn = "3Bw'"
            flag_3Bw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Dw = 0
            flag_3Uw = 0
        elif n_move == 54:
            turn = "3Bw2"
            flag_3Bw = 1
            
            flag_3Rw = 0
            flag_3Lw = 0
            flag_3Dw = 0
            flag_3Uw = 0



    
        
        sum_turns.append(turn)
        pr_move = n_move
        accepted = 0
    # print(actual_scramble)    
    x = " ".join(sum_turns)
    actual_scramble.set(" ".join(sum_turns))
    # print_scramble.update() 

    

def scrambler_7x7():
    pass

def scrambler_pyraminx():
    pass

def scrambler_megaminx():
    pass

def scrambler_skewb():
    pass

def scrambler_clock():
    pass





def time_convert(sec):
    mins = sec // 60
    sec = sec % 60    
    sec = round(sec,2)
    
    if mins == 0:
        print("Time Lapsed = {0}".format(sec))

    else:
        print("Time Lapsed = {0}:{1}".format(int(mins),sec))
    
    return sec


def timer_event(event):    
    t0 = time.time()
    global t1
    global timing
    
    if timing == 0:
        timing = 1
        t1=t0
        print("rodando........")
    else:
        dt = t0-t1
        timing = 0
        x = time_convert(dt)
        # messagebox.showinfo( "Hello Python", "Time Lapsed = {0:.2f}".format(x))
        hist.insert(tk.END,x)

        scrambler_5x5()




def change_event(event):    
    messagebox.showinfo( "Hello Python", eventos.get())
    ch_event = eventos.get()
    if ch_event == '2x2':
        pass
    elif ch_event == '3x3':
        pass
    elif ch_event == '4x4':
        pass
    elif ch_event == '5x5':
        pass
    elif ch_event == '6x6':
        pass
    elif ch_event == '7x7':
        pass
    elif ch_event == 'pyraminx':
        pass
    elif ch_event == 'megaminx':
        pass
    elif ch_event == 'skewb':
        pass
    elif ch_event == 'clock':
        pass




ttk.Label(row1, text = "Modalidade :").grid(column = 0,row = 0) 

n = tk.StringVar() 
eventos = ttk.Combobox(row1, width = 10,textvariable = n,state = "readonly") 

# Adding combobox drop down list 
eventos['values'] = ('2x2','3x3', '4x4','5x5','6x6','7x7','pyraminx','megaminx','skewb','clock') 

eventos.grid(column = 1, row = 0) 
eventos.bind('<<ComboboxSelected>>',change_event)
# Shows february as a default value 
eventos.current(1) 
# eventos.bind('<FocusOut>', lambda e: eventos.selection_clear(0, tk.END))


# print(actual_scramble)

img = tk.PhotoImage(file = r"C:\Users\gabri\OneDrive\Documentos\VScode\lena.png")
label_img = tk.Label(root, image = img)
label_img.pack(side = "bottom", fill = "both", expand = "yes")






print_scramble = tk.Label(row2,textvariable = actual_scramble )
print_scramble.grid(column = 0, row = 0)


# hist = tk.Listbox(row3,yscrollcommand = scrollbar.set,takefocus = 0,state = tk.DISABLED)
hist = tk.Listbox(row3,yscrollcommand = scrollbar.set)
hist.grid(column = 0, row = 0)


# hist.bind('<FocusOut>', lambda e: hist.selection_clear(0, tk.END))

scrollbar.config(command=hist.yview)

scrambler_5x5()


# root.focus_set()
# root.focus_force()
root.bind("<space>",timer_event)


root.mainloop() 







# t1 = n_move == 1
        # t2 = n_move == 2
        # t3 = n_move == 3
        # t4 = n_move == 4
        # t5 = n_move == 5
        # t6 = n_move == 6
        # t7 = n_move == 7
        # t8 = n_move == 8
        # t9 = n_move == 9
        # t10 = n_move == 10
        # t11 = n_move == 11
        # t12 = n_move == 12
        # t13 = n_move == 13
        # t14 = n_move == 14
        # t15 = n_move == 15
        # t16 = n_move == 16
        # t17 = n_move == 17
        # t18 = n_move == 18