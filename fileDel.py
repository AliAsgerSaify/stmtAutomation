#  Copyright (c) 2022.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator
import os
import glob
import sys
import tkinter as tk
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
import datetime
import time
from send2trash import send2trash
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno
from tkinter.messagebox import askyesnocancel

fg = "#000"
bg_col= "#fecd45"
def initTk():
    root = Tk()
    root.title("Success !!!")
    # width and heigth of box
    Tk_Width= 350
    Tk_Height = 160
    # center alignment of the box
    x_Left = int(root.winfo_screenwidth() / 2 - Tk_Width / 2)
    y_Top = int(root.winfo_screenheight() / 2 - Tk_Height / 2)
    root.geometry("{}x{}+{}+{}".format(Tk_Width, Tk_Height, x_Left, y_Top))
    # root.eval('tk::PlaceWindow . center')
    # fg = "#000"
    # bg_col = "#fecd45"
    global fg, bg_col
    root.resizable(False,False)
    # more bg colors : #a0aecd
    root.config(bg=bg_col)
    root.withdraw()
    root.iconbitmap(resource_path('./assets/icon/bin.ico'))
    return root
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def DeleteFiles():
    # root = Tk()
    # root.title("Success !!!")
    # # width and heigth of box
    # Tk_Width= 350
    # Tk_Height = 160
    # # center alignment of the box
    # x_Left = int(root.winfo_screenwidth() / 2 - Tk_Width / 2)
    # y_Top = int(root.winfo_screenheight() / 2 - Tk_Height / 2)
    # root.geometry("{}x{}+{}+{}".format(Tk_Width, Tk_Height, x_Left, y_Top))
    # # root.eval('tk::PlaceWindow . center')
    # bg_col= "#fecd45"
    # root.resizable(False,False)
    # # more bg colors : #a0aecd
    # fg = "#000"
    # root.config(bg=bg_col)
    # root.withdraw()
    # root.iconbitmap(resource_path('./assets/icon/bin.ico'))
    root = initTk()
    # fg = "#000"
    # bg_col = "#fecd45"
    def end():
        root.destroy()

    try:
        path = ''
        # cnfm_box = askyesno('Confirm', 'To continue with default location press Yes otherwise press no')
        cnfm_box = askyesnocancel('Confirm', 'To continue with default location press Yes otherwise press no')

        if cnfm_box == 1:
            path = r'C:\Users\Acer\Desktop\BANK STATEMENT\CURRENT'
            print(cnfm_box.__index__())

        elif cnfm_box == 0:
            print(cnfm_box.__index__())
            ask_path = tkinter.filedialog.askdirectory()
            path = fr'{ask_path}'

        else:
            # print(cnfm_box.__index__())
            exit()
            pass
    except Exception as e:
        if path == '' or None:
            print('Specified File Location not found')
        else:
            print('Error: ' + str(e))
    # path = askopenfilename()
    path = path.replace('/',"\\")
    print(path)
    #path = r'E:\WORK\EWAYBILL'

    try:
        os.chdir(path)

        dateToday = datetime.datetime.today()
        # Both the variables would contain time
        # elapsed since EPOCH in float
        ti_c = os.path.getctime(path)
        ti_m = os.path.getmtime(path)

        # Converting the time in seconds to a timestamp
        c_ti = time.ctime(ti_c)
        m_ti = time.ctime(ti_m)

        labeltext = ''

        for file in os.listdir(path):
            if file.endswith('.xlsx') or file.endswith('.xls'):
                print(file)
                send2trash(file)
                labeltext += " All Excel Files Deleted \n"

            elif file.endswith('.pdf'):
                print(file)
                send2trash(file)
                labeltext += " All PDF Files Deleted \n"

    except OSError:
        for file in os.listdir(path):
            if file == '':
                labeltext += " No file Found of PDF and/or Excel Type \n"


    print(labeltext)



    label = ttk.Label(root, text="All Files Deleted Successfully", padding=20,  font=("Cascadia Code", 12), foreground= fg,
                    background= bg_col)
    label.pack(pady=12)


    button_frame = Frame(root, background=bg_col)
    button_frame.pack(pady=5,padx=5)

    button_main = ttk.Button(button_frame,text="OK", padding=15, command=end)
    button_main.focus()
    button_main.grid(row=0, column=0, padx=30)


    root.deiconify()
    root.mainloop()

if __name__ == "__main__":
    DeleteFiles()