import pyautogui, sys
from pynput import keyboard
import Tkinter as tk


def on_press(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc:
        return False # stop listener
    if k == from_1:# keys interested
        pyautogui.press('backspace')
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_1)
    if k == from_2:# keys interested
        pyautogui.press('backspace')
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_2)
    if k == from_3:# keys interested
        pyautogui.press('backspace')
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_3)

        
def saving(event):
    from_1 = from_ent1.get()
    to_1 = to_ent1.get()
    
    from_2 = from_ent2.get()
    to_2 = to_ent2.get()

    from_3 = from_ent3.get()
    to_3 = to_ent3.get()
    try:
       global from_1
       global  to_1
       global from_2
       global  to_2
       global from_3
       global  to_3
    except:
        pass
    btn_text.set("saved")
    mbutton.pack()

def quit(event):    
    mGui.quit()

def master_quit(event):
    mGui.destroy()
    sys.exit()
######################################
### called all the necessary class ###
######################################
mGui = tk.Tk()
input = tk.StringVar()
result = tk.StringVar()

#################################
### set the inital background ###
#################################
mGui.geometry('600x300')
mGui.title('Auto Filin')

##############################################
### asking which text is going to analysis ###
##############################################
frame = tk.Frame(mGui)
frame.pack()

tk.Label(frame, text='From').grid(row=0, column=0)
from_ent1 = tk.Entry(frame)
from_ent1.grid(row=1, column=0)
tk.Label(frame, text='To').grid(row=0, column=1)
to_ent1 = tk.Entry(frame)
to_ent1.grid(row=1, column=1)

tk.Label(frame, text='From').grid(row=2, column=0)
from_ent2 = tk.Entry(frame)
from_ent2.grid(row=3, column=0)
tk.Label(frame, text='To').grid(row=2, column=1)
to_ent2 = tk.Entry(frame)
to_ent2.grid(row=3, column=1)

tk.Label(frame, text='From').grid(row=4, column=0)
from_ent3 = tk.Entry(frame)
from_ent3.grid(row=5, column=0)
tk.Label(frame, text='To').grid(row=4, column=1)
to_ent3 = tk.Entry(frame)
to_ent3.grid(row=5, column=1)

result.set('Welcome!!!, Press Esc to leave')
textlabel =  tk.Label(mGui,textvariable = result,font=('',14))
textlabel.pack()

################################################
### getting the result from click and return ###
################################################
btn_text = tk.StringVar()
mGui.bind('<Return>', saving)
mbutton = tk.Button(mGui,height=2, width=20, textvariable=btn_text,font=('',15))
mbutton.bind('<Button-1>', saving)
btn_text.set("save")
mbutton.pack()

mGui.bind('<Escape>', master_quit)
mbutton2 = tk.Button(mGui,height=2, width=20, text='GO',font=('',10))
mbutton2.bind('<Button-1>', quit)
mbutton2.pack()

###########################
### run the message box ###
###########################
mGui.mainloop()

print (from_1,'------>',to_1)
print (from_2,'------>',to_2)
print (from_3,'------>',to_3)


################################
### run the keyboard control ###
################################

lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
lis.join() # no this if main thread is polling self.keys

mGui.destroy()

