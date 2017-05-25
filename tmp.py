import Tkinter
#import Theme
#import Info
import ttk

Tk = Tkinter.Tk()
message = 'Not pressed.'

#Sets window Options
#Tk.wm_title(ttk.Title)
Tk.resizable(width='FALSE', height='FALSE')
Tk.wm_geometry("%dx%d%+d%+d" % (720, 480, 0, 0))


#Method run by item button
def press():
    Instruction.configure(text='Button Pressed')
    Tk.update()
    # message = 'Button Pressed'
    while True:
        answer = raw_input('y/n?')
        if answer == 'y':
            break
    Instruction.configure(text='Not pressed')
    #

#item button
item = Tkinter.Button(Tk, command=press).pack()

#label
Instruction = Tkinter.Label(Tk, text=message, font='size, 20')
Instruction.pack()

#Background
#Tk.configure(background=Theme.GUI_bg)
Tk.mainloop()