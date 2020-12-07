# DP1 Project

import tkinter as Tk


def fun_quit():
    global CONTINUE
    print('Quit...Goodbye')
    CONTINUE = False


def fun_test():
    LabelB4.config(bg='yellow')
    LabelF5Sharp.config(bg='yellow')


CONTINUE = True

# Define Tk root
root = Tk.Tk()
root.geometry('1400x600')

# Define Tk variables
Button_Quit = Tk.Button(root, text='Quit', command=fun_quit)

LabelC4 = Tk.Label(root, text='\n\n\n\n\n\n\nC4', borderwidth=3, relief='raised', width=4, height=14)
LabelD4 = Tk.Label(root, text='\n\n\n\n\n\n\nD4', borderwidth=3, relief='raised', width=4, height=14)
LabelE4 = Tk.Label(root, text='\n\n\n\n\n\n\nE4', borderwidth=3, relief='raised', width=4, height=14)
LabelF4 = Tk.Label(root, text='\n\n\n\n\n\n\nF4', borderwidth=3, relief='raised', width=4, height=14)
LabelG4 = Tk.Label(root, text='\n\n\n\n\n\n\nG4', borderwidth=3, relief='raised', width=4, height=14)
LabelA4 = Tk.Label(root, text='\n\n\n\n\n\n\nA4', borderwidth=3, relief='raised', width=4, height=14)
LabelB4 = Tk.Label(root, text='\n\n\n\n\n\n\nB4', borderwidth=3, relief='raised', width=4, height=14)
LabelC5 = Tk.Label(root, text='\n\n\n\n\n\n\nC5', borderwidth=3, relief='raised', width=4, height=14)
LabelD5 = Tk.Label(root, text='\n\n\n\n\n\n\nD5', borderwidth=3, relief='raised', width=4, height=14)
LabelE5 = Tk.Label(root, text='\n\n\n\n\n\n\nE5', borderwidth=3, relief='raised', width=4, height=14)
LabelF5 = Tk.Label(root, text='\n\n\n\n\n\n\nF5', borderwidth=3, relief='raised', width=4, height=14)
LabelG5 = Tk.Label(root, text='\n\n\n\n\n\n\nG5', borderwidth=3, relief='raised', width=4, height=14)
LabelA5 = Tk.Label(root, text='\n\n\n\n\n\n\nA5', borderwidth=3, relief='raised', width=4, height=14)
LabelB5 = Tk.Label(root, text='\n\n\n\n\n\n\nB5', borderwidth=3, relief='raised', width=4, height=14)

LabelC4Sharp = Tk.Label(root, text='C#4', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelD4Sharp = Tk.Label(root, text='D#4', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelF4Sharp = Tk.Label(root, text='F#4', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelG4Sharp = Tk.Label(root, text='G#4', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelA4Sharp = Tk.Label(root, text='A#4', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelC5Sharp = Tk.Label(root, text='C#5', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelD5Sharp = Tk.Label(root, text='D#5', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelF5Sharp = Tk.Label(root, text='F#5', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelG5Sharp = Tk.Label(root, text='G#5', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')
LabelA5Sharp = Tk.Label(root, text='A#5', borderwidth=3, relief='raised', width=4, height=8, bg='gray60')

# Place Tk variables
Button_Quit.place(x=0, y=0)

LabelC4.place(x=80, y=80)
LabelD4.place(x=120, y=80)
LabelE4.place(x=160, y=80)
LabelF4.place(x=200, y=80)
LabelG4.place(x=240, y=80)
LabelA4.place(x=280, y=80)
LabelB4.place(x=320, y=80)
LabelC5.place(x=360, y=80)
LabelD5.place(x=400, y=80)
LabelE5.place(x=440, y=80)
LabelF5.place(x=480, y=80)
LabelG5.place(x=520, y=80)
LabelA5.place(x=560, y=80)
LabelB5.place(x=600, y=80)

LabelC4Sharp.place(x=100, y=80)
LabelD4Sharp.place(x=140, y=80)
LabelF4Sharp.place(x=220, y=80)
LabelG4Sharp.place(x=260, y=80)
LabelA4Sharp.place(x=300, y=80)
LabelC5Sharp.place(x=380, y=80)
LabelD5Sharp.place(x=420, y=80)
LabelF5Sharp.place(x=500, y=80)
LabelG5Sharp.place(x=540, y=80)
LabelA5Sharp.place(x=580, y=80)

# TEST CODE FOR CHANGE LABEL COLOR
Button_Test = Tk.Button(root, text='B4 & F#5 Pressed', command=fun_test).place(x=0, y=40)

while CONTINUE:
    root.update()
