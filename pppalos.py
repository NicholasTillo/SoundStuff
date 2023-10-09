import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk
from pynput import keyboard
import pygame
import os


def getRandom(plist):
    import random
    x = random.randint(0,len(plist)-1)
    return plist[x]


def create_list(folder):
    return_entries = os.listdir(folder)
    for i in range(0,len(return_entries)):
        return_entries[i] = folder + return_entries[i]
    return return_entries


def on_press(key):
    print('{0} pressed'.format(key))

    if type(key) == keyboard.Key:
        return
    
    current = root.nametowidget(".qoo.boo.foo")
    
    current.config(text=key) 

    for i in range(0,100):
        if not x.Channel(i).get_busy():
            x.Channel(i).play(x.Sound(getRandom(entires_dict[key.char])))
            break



def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def start_listen():
    listener.start()


def end_listen():
    listener.stop()
    

def load_dir(key):
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    tempdir = tempdir.split("SoundStuff/")
    file1 = open("saves\savefile.txt", "r")  # append mode
    data = file1.readlines()
    counter = 0

    for i in data:
        if i[0] == key:
            data[counter] = key+": "+tempdir[1] + "/"
        counter += 1
    file1.close()

    file2 = open("saves\savefile.txt", "w")
    file2.writelines(data)
    file2.close()
    load_into_dict()


def clear_dir():
    open("saves\savefile.txt", "w").close() 
    
def load_into_dict():
    file1 = open("saves\savefile.txt", "r") 
    data = file1.readlines()
    for i in data:
        entires_dict[i[0]] = create_list(str(i[3:]))
        

def starting_screen():
    tabControl = ttk.Notebook(root,name = "qoo")
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl,name = "boo")
    tab3 = ttk.Frame(tabControl)
    tabControl.add(tab1)
    tabControl.add(tab2)
    tabControl.add(tab3)


    tabControl.pack(expand="1",fill="both")
    Title = ttk.Label(tab1,text="Title")
    Title.pack()



    return_button = ttk.Button(tab3,text = "Back To Menu", command= starting_screen)
    return_button.pack()
    return_button = ttk.Button(tab3,text = "Button M File", command= lambda : load_dir("m"))
    return_button.pack()
    return_button = ttk.Button(tab3,text = "Button X File", command= lambda : load_dir("x"))
    return_button.pack()
    return_button = ttk.Button(tab3,text = "Button P File", command= lambda : load_dir("p"))
    return_button.pack()
    return_button = ttk.Button(tab3,text = "Button S File", command= lambda : load_dir("s"))
    return_button.pack()
    return_button = ttk.Button(tab3,text = "Clear ", command=clear_dir)
    return_button.pack()



    current = ttk.Label(tab2,text="Hello, Tkinter",name="foo")
    current.place(x=75,y=10)
    start_button = ttk.Button(tab2,text = "Start", command= start_listen)
    start_button.place(x=75,y=100)
    end_button = ttk.Button(tab2,text = "Stop", command= end_listen)
    end_button.place(x=75,y=150)
    ret_button = ttk.Button(tab2,text = "Back To Menu", command= starting_screen)
    ret_button.place(x=75,y=200)


root = ThemedTk(theme ="equilux")
root.geometry("200x400")


"""style = ttk.Style()
style.theme_use('xpnative')
style.theme_use()
print(style.theme_names())
"""

entires_dict = {'p': create_list("SEffects/Plop/"), 's': create_list("SEffects/Sword/"), 'x': create_list("SEffects/Arrow/"),'m':create_list("SEffects/Moo/")}

load_into_dict()

x = pygame.mixer
x.init() 
x.set_num_channels(100) 
x.music.set_volume(1)


listener = keyboard.Listener(on_press=on_press ,on_release=on_release)
starting_screen()
root.mainloop()
