#  Copyright (c) 2022.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator
import datetime
import time
# import iciciStmt
# import idbisaify
import yaml
import Importall
import pyautogui
import subprocess
import os
# from WebsiteLoginAutomation import *
from Importall import *
from selenium.webdriver.common.keys import Keys
import iciciStmt
import idbiAsian
from idbiAsian import asianMain
import idbihc, idbisaify

try:
    Importall.driver.minimize_window()
except Exception as e:
    print(e)

def compileStmt():

    date_now = datetime.datetime.now()
    date_now = date_now.strftime('%d')
    time_now = datetime.datetime.now()
    time_now = time_now.strftime('%H')
    # print('datenow : ' + date_now + '\ntimenow : '+ time_now)

    in_morning_till = 11

    stmtpath = "C:\\Users\\Acer\\Desktop\\BANK STATEMENT\\CURRENT"
    try:
        def saveSetting(path):
            Importall.downloadLoc(path)
    except:
        pass
    saveSetting(stmtpath)
    engine = Importall.engine
    engine.say("A.A.I. LoginBot Initiated")
    engine.runAndWait()
    try:
        Importall.driver.minimize_window()
    except Exception as e:
        print(e)
    # otp = sendotpAuth("BANK STATEMENT COMPLIE".title())
    # authenticate = input("Please Enter OTP to proceed: \n")

    # if authenticate == otp:
    iciciStmt.main()
    # idbisaify.asnlog == True
    # idbisaify.saveset == False
    newtabscript("tabcorpidbi")
    idbihc.idbihcMain()

    time.sleep(0.6)
    newtabscript("tabidbinet")
    idbisaify.idbisaifyMain()

    try:
        time_now = int(time_now)
        time.sleep(0.6)
        if (date_now == "31" and time_now <= in_morning_till):
            newtabscript('tabAsian30')
            idbiAsian.asianMain()

        elif (date_now == "30" and time_now <= in_morning_till):
            newtabscript('tabAsian30')
            idbiAsian.asianMain()

        else:
            pass
    except Exception as e:
        print("RAISED EXCEPTION : "+e)

if __name__ == "__main__":
    compileStmt()
