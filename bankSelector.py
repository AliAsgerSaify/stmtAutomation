#  Copyright (c) 2022.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator
# try:
#     a = input("Do you want to execute fileDel module? [Y/N]")
#     a = a.lower()
#     if  a == 'y' or a == 'yes':
#         import fileDel
#         fileDel
#         #print('Files Deleted')
#     else:
#         print('Files not Deleted')
#         pass
# except:
#     pass
import importlib
import time
import yaml
import Importall
import pyautogui
import subprocess
import os
Importall.driver.minimize_window()
from Importall import *
from Importall import CAPSLOCK_STATE
from selenium.webdriver.common.keys import Keys
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser as wb
import pyttsx3
# from __main__ import *
import datetime
import stmtCompile
import idbiAsian, iciciStmt
import idbisaify
from idbisaify import idbisaifyMain
from idbihc import idbihcMain
import stmtEmail

driver = Importall.driver
engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 200)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
engine.setProperty('volume', 0.8)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def bankselectAppMain():
    # formation of tkinter box
    root = Tk()
    # width and heigth of box
    Tk_Width = 750
    Tk_Height = 230
    # center alignment of the box
    x_Left = int(root.winfo_screenwidth() / 2 - Tk_Width / 2)
    y_Top = int(root.winfo_screenheight() / 2 - Tk_Height / 2)
    root.geometry("{}x{}+{}+{}".format(Tk_Width, Tk_Height, x_Left, y_Top))
    #restrict root from resizing on both x and y axis
    root.resizable(False,False)
    bg_col = "#44d7a8"
    fg = "#0000b5"    #0000b5
    root.config(background=bg_col)

    # Use the root.attributes('-alpha',0.5) to set the transparency for the root; WHERE 1 = OPAQUE AND 0 = TRANSPARENT.
    # root.attributes('-alpha',0.5)

    # box's title
    root.title("Bank Selector")
    root.withdraw()
    root.deiconify()
    root.attributes('-topmost', 1)

    CAPS = Importall.CAPSLOCK_STATE()


    root.deiconify()

    def newtaburl():
        try:
            if driver.current_url == "about:blank":
                driver.get("https://duckduckgo.com/")
        except:
            pass
    newtaburl()
    def winmax():
        try:
            driver.maximize_window()
        except:
            pass

    def isBrowserAlive(driver):
        try:
            # driver.current_url
            driver.current_url == "about:blank"
            driver.current_url == None
            # or driver.title
            driver.title == None
            return True

        except:
            return False

    stmtpath = "C:\\Users\\Acer\\Desktop\\BANK STATEMENT\\CURRENT"
    try:
        def saveSetting(path):
            Importall.downloadLoc(path)

    except:
        pass

    def idbisaify():
        msg = messagebox.askyesno("Download Settings", "Do you want to set download folder to CURRENT ?")
        root.iconify()
        winmax()
        if msg == True:
            saveSetting(stmtpath)
        else:
            pass
        if isBrowserAlive(driver) == True:
            newtabscript("tabidbisaify")
        else:
            # newtabscript("saifycondfalse")
            driver.get("https://duckduckgo.com/")
            pass
        try:
            idbisaifyMain()
        except Exception as e:
            pass
            # print('IDBI SAIFY ERROR: '+str(e))
            # os.system("idbisaify.py")
            # idbisaifyMain()

        root.deiconify()
        # root.destroy()

    def idbihc():
        msg = messagebox.askyesno("Download Settings", "Do you want to open and set download settings ?")
        root.iconify()
        winmax()
        if msg == True:
            saveSetting(stmtpath)
        else:
            pass
        if isBrowserAlive(driver) == True:
            newtabscript("tabidbihc")
        else:
            pass
        try:
            idbihcMain()
        except Exception as e:
            pass
            # print('IDBI HC ERROR: ' + str(e))
            # idbihcMain()
            pass
        root.deiconify()
        # root.destroy()

    def idbiasian():
        msg = messagebox.askyesno("Download Settings", "Do you want to open and set download settings ?")
        root.iconify()
        winmax()
        if msg == True:
            saveSetting(stmtpath)
        else:
            pass
        if isBrowserAlive(driver) == True:
            newtabscript("tabidbiasian")
        else:
            pass
        try:
            idbiAsian.asianMain()
        except Exception as e:
            pass
            # print("IDBI ASIAN ERROR: " + str(e))
            # idbiAsian.asianMain()
            pass
        root.deiconify()
        # root.destroy()

    def icici():
        root.iconify()
        winmax()
        if isBrowserAlive(driver) == True:
            newtabscript("tabicici")
        else:
            pass
        try:
            iciciStmt.main()

        except Exception as e:
            # print("ICICI STMT ERROR: " + str(e))
            pass
            # iciciStmt.main()
        root.deiconify()
        # root.destroy()

    def compile():
        root.iconify()
        winmax()
        if isBrowserAlive(driver) == True:
            newtabscript("tabNEW4C")
        else:
            pass
        try:
            stmtCompile.compileStmt()
        except Exception as e:
            # print("StmtCompile Error: " + str(e))
            # stmtCompile.stmtCompile()
            pass
        newtabscript("preferences")
        driver.get("about:preferences")
        # driver.find_element('xpath','/html/html:body/stack/hbox/vbox[2]/vbox/vbox/groupbox[10]/richlistbox/richlistitem[7]').click()
        # driver.find_element('xpath','/html/html:body/stack/hbox/vbox[2]/vbox/vbox/groupbox[10]/richlistbox/richlistitem[7]/hbox[2]/label').click()
        root.deiconify()
        # root.destroy()

    def stmtemail():
        root.iconify()
        # time.sleep(4)
        try:
            stmtEmail.openmailandsend()

        except:
            pass
            # stmtEmail.openmailandsend()


        root.deiconify()
        # root.destroy()


    def sbi():
        sbi_start_time = datetime.datetime.now()
        root.iconify()
        if ((CAPS) & 0xffff) == 0:
            pyautogui.press('capslock')
        # driver.quit()
        url = 'https://corp.onlinesbi.com/corpuser/login.htm'
        engine.say("Opening : s.b.I. bank site")
        engine.runAndWait()
        wb.open(url)
        root.deiconify()
        logfile('SBI ',sbi_start_time)
        # exit()

    def exit():
        root.destroy()
        # print(driver.title)
        if driver.current_url == "" or driver.current_url == "https://duckduckgo.com/" or driver.title == 'DuckDuckGo — Privacy, simplified.' or \
                driver.current_url == "about:blank" or driver.current_url == None:
            driver.quit()
        elif driver.current_url == 'https://duckduckgo.com/':
            driver.quit()
        # engine.stop()

    button_frame_row1 = Frame(root,background=bg_col)
    button_frame_row1.pack(pady=30,padx=10)

    button_frame_row2 = Frame(root,background=bg_col)
    button_frame_row2.pack(pady=10,padx=10)


    #Buttons in Row 1
    btnidbisaify = ttk.Button(button_frame_row1, text="IDBI SAIFY", padding=20, command=lambda:idbisaify(), cursor="hand2")
    btnidbisaify.grid(row=0, column=0, padx=20)

    btnidbihc = ttk.Button(button_frame_row1, text="IDBI HC", padding=20, command=lambda:idbihc(), cursor="hand2")
    btnidbihc.grid(row=0, column=2, padx=20)

    btnidbiasn = ttk.Button(button_frame_row1, text="IDBI ASIAN", padding=20, command=lambda:idbiasian(), cursor="hand2")
    btnidbiasn.grid(row=0, column=3, padx=20)

    btnicici = ttk.Button(button_frame_row1, text="ICICI", padding=20, command=lambda:icici(), cursor="hand2")
    btnicici.grid(row=0, column=4, padx=20)

    #Buttons in Row 2
    btncompile = ttk.Button(button_frame_row2, text="STMT COMPILE", padding=20, command=lambda:compile(), cursor="hand2")
    btncompile.grid(row=1, column=1, padx=20)

    btnsbi = ttk.Button(button_frame_row2, text="SBI", padding=20, command=lambda:sbi(), cursor="hand2")
    btnsbi.grid(row=1, column=2, padx=20)

    btnemail = ttk.Button(button_frame_row2, text="EMAIL STMT", padding=20, command=lambda:stmtemail(), cursor="hand2")
    btnemail.grid(row=1, column=3, padx=20)

    btnexit = ttk.Button(button_frame_row2, text="EXIT", padding=20, command=lambda:exit(), cursor="hand2")
    btnexit.grid(row=1, column=4, padx=20)


    # TO CHANGE THE ICON OF ROOT USE:
    root.iconbitmap(resource_path('./assets/icon/login.ico'))

    try:
        root.deiconify()
    except Exception as e:
        print(str(e))
    root.mainloop()
    # root.destroy()

if __name__ == "__main__":
    bankselectAppMain()