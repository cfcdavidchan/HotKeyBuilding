import pyautogui, sys, time
from pynput import keyboard
import Tkinter as tk
import ttk


def on_press(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc:
        return False # stop listener
    if k == from_11:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_11)
    if k == from_12:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_12)
    if k == from_13:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_13)
    if k == from_14:# keys interested
            pyautogui.press('backspace')
            time.sleep(0.01)
            print('Key pressed: ' + k)
            pyautogui.typewrite(to_14)
    if k == from_15:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_15)

    ###################################################
    if k == from_21:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_21)
    if k == from_22:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_22)
    if k == from_23:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_23)
    if k == from_24:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_24)
    if k == from_25:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_25)

    ###################################################
    if k == from_31:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_31)
    if k == from_32:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_32)
    if k == from_33:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_33)
    if k == from_34:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_34)
    if k == from_35:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_35)

    ###################################################
    if k == from_41:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_41)
    if k == from_42:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_42)
    if k == from_43:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_43)
    if k == from_44:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_44)
    if k == from_45:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_45)

    ###################################################
    if k == from_51:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_51)
    if k == from_52:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_52)
    if k == from_53:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_53)
    if k == from_54:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_54)
    if k == from_55:# keys interested
        pyautogui.press('backspace')
        time.sleep(0.01)
        print('Key pressed: ' + k)
        pyautogui.typewrite(to_55)

def saving(event):

    try:
        global from_11,to_11,from_12,to_12,from_13,to_13,from_14,to_14,from_15,to_15
        global from_21,to_21,from_22,to_22,from_23,to_23,from_24,to_24,from_25,to_25
        global from_31,to_31,from_32,to_32,from_33,to_33,from_34,to_34,from_35,to_35
        global from_41,to_41,from_42,to_42,from_43,to_43,from_44,to_44,from_45,to_45
        global from_51,to_51,from_52,to_52,from_53,to_53,from_54,to_54,from_55,to_55
    except:
        pass

    from_11 = from_ent11.get()
    to_11 = to_ent11.get()
    from_12 = from_ent12.get()
    to_12 = to_ent12.get()
    from_13 = from_ent13.get()
    to_13 = to_ent13.get()
    from_14 = from_ent14.get()
    to_14 = to_ent14.get()
    from_15 = from_ent15.get()
    to_15 = to_ent15.get()

    from_21 = from_ent21.get()
    to_21 = to_ent21.get()
    from_22 = from_ent22.get()
    to_22 = to_ent22.get()
    from_23 = from_ent23.get()
    to_23 = to_ent23.get()
    from_24 = from_ent24.get()
    to_24 = to_ent24.get()
    from_25 = from_ent25.get()
    to_25 = to_ent25.get()

    from_31 = from_ent31.get()
    to_31 = to_ent31.get()
    from_32 = from_ent32.get()
    to_32 = to_ent32.get()
    from_33 = from_ent33.get()
    to_33 = to_ent33.get()
    from_34 = from_ent34.get()
    to_34 = to_ent34.get()
    from_35 = from_ent35.get()
    to_35 = to_ent35.get()

    from_41 = from_ent41.get()
    to_41 = to_ent41.get()
    from_42 = from_ent42.get()
    to_42 = to_ent42.get()
    from_43 = from_ent43.get()
    to_43 = to_ent43.get()
    from_44 = from_ent44.get()
    to_44 = to_ent44.get()
    from_45 = from_ent45.get()
    to_45 = to_ent45.get()

    from_51 = from_ent51.get()
    to_51 = to_ent51.get()
    from_52 = from_ent52.get()
    to_52 = to_ent52.get()
    from_53 = from_ent53.get()
    to_53 = to_ent53.get()
    from_54 = from_ent54.get()
    to_54 = to_ent54.get()
    from_55 = from_ent55.get()
    to_55 = to_ent55.get()

    btn_text.set("saved")
    mGui.update()

def go(event):
    btn_text2.set("running")
    mGui.update()

    ###########################
    ### run the message box ###
    ###########################
    try:
        print (from_11, '------>', to_11)
        print (from_12, '------>', to_12)
        print (from_13, '------>', to_13)
        print (from_14, '------>', to_14)
        print (from_15, '------>', to_15)

        print (from_21, '------>', to_21)
        print (from_22, '------>', to_22)
        print (from_23, '------>', to_23)
        print (from_24, '------>', to_25)
        print (from_24, '------>', to_25)

        print (from_31, '------>', to_31)
        print (from_32, '------>', to_32)
        print (from_33, '------>', to_33)
        print (from_34, '------>', to_34)
        print (from_35, '------>', to_35)

        print (from_41, '------>', to_41)
        print (from_42, '------>', to_42)
        print (from_43, '------>', to_43)
        print (from_44, '------>', to_44)
        print (from_45, '------>', to_45)

        print (from_51, '------>', to_51)
        print (from_52, '------>', to_52)
        print (from_53, '------>', to_53)
        print (from_54, '------>', to_54)
        print (from_55, '------>', to_55)

    except:
        pass
    ################################
    ### run the keyboard control ###
    ################################
    lis = keyboard.Listener(on_press=on_press)
    lis.start()  # start to listen on a separate thread
    lis.join()  # no this if main thread is polling self.keys

    ################################
    ### run the keyboard control ###
    ################################
    begining

def begining(event):
    btn_text.set("save")
    btn_text2.set("go")
    mGui.update()


def master_quit(event):
    mGui.destroy()
    sys.exit()


#############################################
### called all the necessary tkinterclass ###
#############################################
mGui = tk.Tk()
input = tk.StringVar()
result = tk.StringVar()

#################################
### set the inital background ###
#################################
mGui.geometry('1000x400')
mGui.title('Auto Filin')

##############################################
### asking which text is going to analysis ###
##############################################
frame = tk.Frame(mGui)
frame.pack()

### 1 st set ###
tk.Label(frame, text='From').grid(row=0, column=0)
from_ent11 = tk.Entry(frame,width=5)
from_ent11.grid(row=1, column=0)
tk.Label(frame, text='To').grid(row=0, column=1)
to_ent11 = tk.Entry(frame,width=15)
to_ent11.grid(row=1, column=1)
tk.Label(frame, text='From').grid(row=2, column=0)
from_ent12 = tk.Entry(frame,width=5)
from_ent12.grid(row=3, column=0)
tk.Label(frame, text='To').grid(row=2, column=1)
to_ent12 = tk.Entry(frame,width=15)
to_ent12.grid(row=3, column=1)
tk.Label(frame, text='From').grid(row=4, column=0)
from_ent13 = tk.Entry(frame,width=5)
from_ent13.grid(row=5, column=0)
tk.Label(frame, text='To').grid(row=4, column=1)
to_ent13 = tk.Entry(frame,width=15)
to_ent13.grid(row=5, column=1)
tk.Label(frame, text='From').grid(row=6, column=0)
from_ent14 = tk.Entry(frame,width=5)
from_ent14.grid(row=7, column=0)
tk.Label(frame, text='To').grid(row=6, column=1)
to_ent14 = tk.Entry(frame,width=15)
to_ent14.grid(row=7, column=1)
tk.Label(frame, text='From').grid(row=8, column=0)
from_ent15 = tk.Entry(frame,width=5)
from_ent15.grid(row=9, column=0)
tk.Label(frame, text='To').grid(row=8, column=1)
to_ent15 = tk.Entry(frame,width=15)
to_ent15.grid(row=9, column=1)
### Separator ###
sep11 = ttk.Separator(frame, orient="vertical")
sep12 = ttk.Separator(frame, orient="vertical")
sep13 = ttk.Separator(frame, orient="vertical")
sep14 = ttk.Separator(frame, orient="vertical")
sep15 = ttk.Separator(frame, orient="vertical")
sep16 = ttk.Separator(frame, orient="vertical")
sep17 = ttk.Separator(frame, orient="vertical")
sep18 = ttk.Separator(frame, orient="vertical")
sep19 = ttk.Separator(frame, orient="vertical")
sep110 = ttk.Separator(frame, orient="vertical")
sep11.grid(column=2, row=0, sticky="ns",)
sep12.grid(column=2, row=1, sticky="ns")
sep13.grid(column=2, row=2, sticky="ns")
sep14.grid(column=2, row=3, sticky="ns")
sep15.grid(column=2, row=4, sticky="ns")
sep16.grid(column=2, row=5, sticky="ns")
sep17.grid(column=2, row=6, sticky="ns")
sep18.grid(column=2, row=7, sticky="ns")
sep19.grid(column=2, row=8, sticky="ns")
sep110.grid(column=2, row=9, sticky="ns")
sty = ttk.Style(frame)
sty.configure("TSeparator", background="red")

### 2 st set ###
tk.Label(frame, text='From').grid(row=0, column=3)
from_ent21 = tk.Entry(frame,width=5)
from_ent21.grid(row=1, column=3)
tk.Label(frame, text='To').grid(row=0, column=4)
to_ent21 = tk.Entry(frame,width=15)
to_ent21.grid(row=1, column=4)
tk.Label(frame, text='From').grid(row=2, column=3)
from_ent22 = tk.Entry(frame,width=5)
from_ent22.grid(row=3, column=3)
tk.Label(frame, text='To').grid(row=2, column=4)
to_ent22 = tk.Entry(frame,width=15)
to_ent22.grid(row=3, column=4)
tk.Label(frame, text='From').grid(row=4, column=3)
from_ent23 = tk.Entry(frame,width=5)
from_ent23.grid(row=5, column=3)
tk.Label(frame, text='To').grid(row=4, column=4)
to_ent23 = tk.Entry(frame,width=15)
to_ent23.grid(row=5, column=4)
tk.Label(frame, text='From').grid(row=6, column=3)
from_ent24 = tk.Entry(frame,width=5)
from_ent24.grid(row=7, column=3)
tk.Label(frame, text='To').grid(row=6, column=4)
to_ent24 = tk.Entry(frame,width=15)
to_ent24.grid(row=7, column=4)
tk.Label(frame, text='From').grid(row=8, column=3)
from_ent25 = tk.Entry(frame,width=5)
from_ent25.grid(row=9, column=3)
tk.Label(frame, text='To').grid(row=8, column=4)
to_ent25 = tk.Entry(frame,width=15)
to_ent25.grid(row=9, column=4)
### Separator ###
sep21 = ttk.Separator(frame, orient="vertical")
sep22 = ttk.Separator(frame, orient="vertical")
sep23 = ttk.Separator(frame, orient="vertical")
sep24 = ttk.Separator(frame, orient="vertical")
sep25 = ttk.Separator(frame, orient="vertical")
sep26 = ttk.Separator(frame, orient="vertical")
sep27 = ttk.Separator(frame, orient="vertical")
sep28 = ttk.Separator(frame, orient="vertical")
sep29 = ttk.Separator(frame, orient="vertical")
sep210 = ttk.Separator(frame, orient="vertical")
sep21.grid(column=5, row=0, sticky="ns",)
sep22.grid(column=5, row=1, sticky="ns")
sep23.grid(column=5, row=2, sticky="ns")
sep24.grid(column=5, row=3, sticky="ns")
sep25.grid(column=5, row=4, sticky="ns")
sep26.grid(column=5, row=5, sticky="ns")
sep27.grid(column=5, row=6, sticky="ns")
sep28.grid(column=5, row=7, sticky="ns")
sep29.grid(column=5, row=8, sticky="ns")
sep210.grid(column=5, row=9, sticky="ns")
sty = ttk.Style(frame)
sty.configure("TSeparator", background="red")

### 3 st set ###
tk.Label(frame, text='From').grid(row=0, column=6)
from_ent31 = tk.Entry(frame,width=5)
from_ent31.grid(row=1, column=6)
tk.Label(frame, text='To').grid(row=0, column=7)
to_ent31 = tk.Entry(frame,width=15)
to_ent31.grid(row=1, column=7)
tk.Label(frame, text='From').grid(row=2, column=6)
from_ent32 = tk.Entry(frame,width=5)
from_ent32.grid(row=3, column=6)
tk.Label(frame, text='To').grid(row=2, column=7)
to_ent32 = tk.Entry(frame,width=15)
to_ent32.grid(row=3, column=7)
tk.Label(frame, text='From').grid(row=4, column=6)
from_ent33 = tk.Entry(frame,width=5)
from_ent33.grid(row=5, column=6)
tk.Label(frame, text='To').grid(row=4, column=7)
to_ent33 = tk.Entry(frame,width=15)
to_ent33.grid(row=5, column=7)
tk.Label(frame, text='From').grid(row=6, column=6)
from_ent34 = tk.Entry(frame,width=5)
from_ent34.grid(row=7, column=6)
tk.Label(frame, text='To').grid(row=6, column=7)
to_ent34 = tk.Entry(frame,width=15)
to_ent34.grid(row=7, column=7)
tk.Label(frame, text='From').grid(row=8, column=6)
from_ent35 = tk.Entry(frame,width=5)
from_ent35.grid(row=9, column=6)
tk.Label(frame, text='To').grid(row=8, column=7)
to_ent35 = tk.Entry(frame,width=15)
to_ent35.grid(row=9, column=7)
### Separator ###
sep31 = ttk.Separator(frame, orient="vertical")
sep32 = ttk.Separator(frame, orient="vertical")
sep33 = ttk.Separator(frame, orient="vertical")
sep34 = ttk.Separator(frame, orient="vertical")
sep35 = ttk.Separator(frame, orient="vertical")
sep36 = ttk.Separator(frame, orient="vertical")
sep37 = ttk.Separator(frame, orient="vertical")
sep38 = ttk.Separator(frame, orient="vertical")
sep39 = ttk.Separator(frame, orient="vertical")
sep310 = ttk.Separator(frame, orient="vertical")
sep31.grid(column=8, row=0, sticky="ns",)
sep32.grid(column=8, row=1, sticky="ns")
sep33.grid(column=8, row=2, sticky="ns")
sep34.grid(column=8, row=3, sticky="ns")
sep35.grid(column=8, row=4, sticky="ns")
sep36.grid(column=8, row=5, sticky="ns")
sep37.grid(column=8, row=6, sticky="ns")
sep38.grid(column=8, row=7, sticky="ns")
sep39.grid(column=8, row=8, sticky="ns")
sep310.grid(column=8, row=9, sticky="ns")
sty = ttk.Style(frame)
sty.configure("TSeparator", background="red")

### 4 st set ###
tk.Label(frame, text='From').grid(row=0, column=9)
from_ent41 = tk.Entry(frame,width=5)
from_ent41.grid(row=1, column=9)
tk.Label(frame, text='To').grid(row=0, column=10)
to_ent41 = tk.Entry(frame,width=15)
to_ent41.grid(row=1, column=10)
tk.Label(frame, text='From').grid(row=2, column=9)
from_ent42 = tk.Entry(frame,width=5)
from_ent42.grid(row=3, column=9)
tk.Label(frame, text='To').grid(row=2, column=10)
to_ent42 = tk.Entry(frame,width=15)
to_ent42.grid(row=3, column=10)
tk.Label(frame, text='From').grid(row=4, column=9)
from_ent43 = tk.Entry(frame,width=5)
from_ent43.grid(row=5, column=9)
tk.Label(frame, text='To').grid(row=4, column=10)
to_ent43 = tk.Entry(frame,width=15)
to_ent43.grid(row=5, column=10)
tk.Label(frame, text='From').grid(row=6, column=9)
from_ent44 = tk.Entry(frame,width=5)
from_ent44.grid(row=7, column=9)
tk.Label(frame, text='To').grid(row=6, column=10)
to_ent44 = tk.Entry(frame,width=15)
to_ent44.grid(row=7, column=10)
tk.Label(frame, text='From').grid(row=8, column=9)
from_ent45 = tk.Entry(frame,width=5)
from_ent45.grid(row=9, column=9)
tk.Label(frame, text='To').grid(row=8, column=10)
to_ent45 = tk.Entry(frame,width=15)
to_ent45.grid(row=9, column=10)
### Separator ###
sep41 = ttk.Separator(frame, orient="vertical")
sep42 = ttk.Separator(frame, orient="vertical")
sep43 = ttk.Separator(frame, orient="vertical")
sep44 = ttk.Separator(frame, orient="vertical")
sep45 = ttk.Separator(frame, orient="vertical")
sep46 = ttk.Separator(frame, orient="vertical")
sep47 = ttk.Separator(frame, orient="vertical")
sep48 = ttk.Separator(frame, orient="vertical")
sep49 = ttk.Separator(frame, orient="vertical")
sep410 = ttk.Separator(frame, orient="vertical")
sep41.grid(column=11, row=0, sticky="ns",)
sep42.grid(column=11, row=1, sticky="ns")
sep43.grid(column=11, row=2, sticky="ns")
sep44.grid(column=11, row=3, sticky="ns")
sep45.grid(column=11, row=4, sticky="ns")
sep46.grid(column=11, row=5, sticky="ns")
sep47.grid(column=11, row=6, sticky="ns")
sep48.grid(column=11, row=7, sticky="ns")
sep49.grid(column=11, row=8, sticky="ns")
sep410.grid(column=11, row=9, sticky="ns")
sty = ttk.Style(frame)
sty.configure("TSeparator", background="red")

### 5 st set ###
tk.Label(frame, text='From').grid(row=0, column=12)
from_ent51 = tk.Entry(frame,width=5)
from_ent51.grid(row=1, column=12)
tk.Label(frame, text='To').grid(row=0, column=13)
to_ent51 = tk.Entry(frame,width=15)
to_ent51.grid(row=1, column=13)
tk.Label(frame, text='From').grid(row=2, column=12)
from_ent52 = tk.Entry(frame,width=5)
from_ent52.grid(row=3, column=12)
tk.Label(frame, text='To').grid(row=2, column=13)
to_ent52 = tk.Entry(frame,width=15)
to_ent52.grid(row=3, column=13)
tk.Label(frame, text='From').grid(row=4, column=12)
from_ent53 = tk.Entry(frame,width=5)
from_ent53.grid(row=5, column=12)
tk.Label(frame, text='To').grid(row=4, column=13)
to_ent53 = tk.Entry(frame,width=15)
to_ent53.grid(row=5, column=13)
tk.Label(frame, text='From').grid(row=6, column=12)
from_ent54 = tk.Entry(frame,width=5)
from_ent54.grid(row=7, column=12)
tk.Label(frame, text='To').grid(row=6, column=13)
to_ent54 = tk.Entry(frame,width=15)
to_ent54.grid(row=7, column=13)
tk.Label(frame, text='From').grid(row=8, column=12)
from_ent55 = tk.Entry(frame,width=5)
from_ent55.grid(row=9, column=12)
tk.Label(frame, text='To').grid(row=8, column=13)
to_ent55 = tk.Entry(frame,width=15)
to_ent55.grid(row=9, column=13)
################################################

################################################
result.set('Welcome!!!, Press Esc to leave')
textlabel =  tk.Label(mGui,textvariable = result,font=('',14))
textlabel.pack()
################################################


################################################
### getting the result from click and return ###
################################################
btn_text = tk.StringVar()
#mGui.bind('<Return>', saving)
mbutton = tk.Button(mGui,height=2, width=20, textvariable=btn_text,font=('',15))
mbutton.bind('<Button-1>', saving)
btn_text.set("save")
mbutton.pack()

mGui.bind('<Escape>', begining)
btn_text2 = tk.StringVar()
btn_text2.set("go")
mbutton2 = tk.Button(mGui,height=2, width=20, textvariable=btn_text2,font=('',12))
mbutton2.bind('<Button-1>', go)
#btn_text2.set("running")
mbutton2.pack()

#######################
### Running Tkinter ###
#######################
mGui.mainloop()
