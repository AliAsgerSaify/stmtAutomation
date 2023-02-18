#  Copyright (c) 2022.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator

import time
import yaml
import Importall
import pyautogui
import tkinter
from tkinter import messagebox
# from WebsiteLoginAutomation import *
from Importall import *
import datetime

def asianMain():
    start_time = datetime.datetime.now()
    try:
        driver.maximize_window()
    except:
        pass
    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  + In case of any changes and/or discrepancies please contact administrator +
    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # root = tkinter.Tk()
    # root.wm_attributes("-topmost", 1)
    # root.withdraw()

    engine = Importall.engine
    engine.say("lOGG-ING IN I.D.B.I. BANK SITE")
    engine.runAndWait()

    with open('loginDetails.yml', 'r') as file:
        conf = yaml.safe_load(file)
        asianid = conf['idbiasian']['userid']
        asianpwd = conf['idbiasian']['password']


    CAPS = Importall.CAPSLOCK_STATE()


    def login(Url, usernameId, username, captchaclickId, loginButton, passwordId, password, submit_buttonId):
        # driver.get(Url)
        # pyautogui.keyDown('ctrl')
        # pyautogui.press('n')
        # pyautogui.keyUp('ctrl')
        time.sleep(1)

        driver.get(Url)
        # driver.find_element('id',usernameClick).click()
        driver.find_element('id', usernameId).send_keys(username)
        driver.find_element('id', captchaclickId).click()
        time.sleep(6)
        try:
            driver.find_element('id', loginButton).click()
        except:
            pass
        time.sleep(0.5)
        # driver.find_element('id','AuthenticationFG.TARGET_CHECKBOX').click()
        # mouse.drag(0,0,-635.53,100.98,False)
        # pyautogui.moveTo([251,513])
        # # ULTRAWIDE MONITOR COORDINATES: (x=199, y=412)
        # #mouse.click('left')
        # pyautogui.click()
        driver.find_element('xpath',
                            '/html/body/form/div/div/div[3]/div[3]/div[1]/div[1]/div[1]/div/p[1]/span/span[1]').click()
        driver.find_element('id', passwordId).send_keys(password)
        time.sleep(1)
        driver.find_element('id', submit_buttonId).click()

        # idbisaify

    # newtabscript("idbiasian")
    url = 'https://inet.idbibank.co.in/ret/AuthenticationController?FORMSGROUP_' \
               'ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&__FG_BUTTONS__=LOAD&ACTION.' \
               'LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=IBKL'

    if ((CAPS) & 0xffff) == 0:
        pyautogui.press('capslock')


    login(url, 'AuthenticationFG.USER_PRINCIPAL', asianid, 'AuthenticationFG.VERIFICATION_CODE',
          'STU_VALIDATE_CREDENTIALS'
          , 'AuthenticationFG.ACCESS_CODE', asianpwd, 'VALIDATE_STU_CREDENTIALS1')

    time.sleep(2)
    try:
        if (driver.find_element('xpath', '//*[@id="RetailUserDashboardUX5_WAC85__1"]').is_displayed() == True):
            engine.say("I.D.B.I. ASIAN LOGIN SUCCESSFULL")
            engine.runAndWait()
            print("Login Successful")
            # time.sleep(0.5)
            driver.find_element('id', 'RetailUserDashboardUX5_WAC85__1:VIEW_TRANSACTION_HISTORY_PAGEJUMP[0]0').click()
        else:
            print('Login Failed due to some error')

    except:
        pass

    time.sleep(1)
    a = pyautogui.position()
    print(a)


    def logfile():
        today = datetime.datetime.now()
        today = today.strftime('%d-%b-%Y')
        end_time = datetime.datetime.now()
        timetaken = end_time - start_time
        timetaken = str(timetaken)
        print(timetaken)
        line = ['IDBI ASIAN', '\t start time :'+ str(start_time),'\n\t end time :'+str(end_time),'\n\t time taken : '+ str(timetaken)]
        line = str(','.join(line))
        with open(f'LOG\\logFileTest {today}.txt', 'a') as f:
            f.writelines(str(line))
            # f.write(''.join(line))
            f.write('\n\n')
        # print(line)


    logfile()

    def saveSetting(tabname):
        newtabscript(tabname)
        driver.get('about:preferences')
        driver.find_element('xpath', '//*[@id="alwaysAsk"]').click()
        driver.find_element('xpath', '//*[@id="chooseFolder"]').click()

if __name__ == "__main__":
    asianMain()