#  Copyright (c) 2022.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator

import time
import yaml
import Importall
try:
    Importall.driver.minimize_window()
except Exception as e:
    print(e)
    pass
import pyautogui
# from WebsiteLoginAutomation import *
from Importall import *
import datetime
import tkinter

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  + In case of any changes and/or discrepancies please contact administrator +
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def icici():
    start_time = datetime.datetime.now()
    engine = Importall.engine
    # try:
    #     driver.minimize_window()
    # except:
    #     pass
    engine.say("LOGG-ING IN  I C I C I BANK SITE")
    engine.runAndWait()

    with open('loginDetails.yml', 'r') as file:
        conf = yaml.safe_load(file)
        saifynewUserId = conf['icici']['saifynew']['userid']
        saifynewPass = conf['icici']['saifynew']['password']

        saifyUserId = conf['icici']['saify']['userid']
        saifyPass = conf['icici']['saify']['password']

        hcUserId = conf['icici']['hc']['userid']
        hcPass = conf['icici']['hc']['password']

    CAPS = Importall.CAPSLOCK_STATE()

    def showStmt():
        driver.find_element('xpath','/html/body/form/div[3]/div[1]/div[4]/ul/li[3]/a/div/span[3]').click()
        driver.find_element('xpath','/html/body/form/div[3]/div[1]/div[4]/ul/li[3]/div/ul/li[17]/h4/u').click()
        if (driver.find_element('xpath','/html/body/form/div[3]/div[1]/div[4]/ul/li[3]/div/ul/li[18]/a').is_displayed() == True):
            driver.find_element('xpath','/html/body/form/div[3]/div[1]/div[4]/ul/li[3]/div/ul/li[18]/a').click()


    def login(Url, usernameId, username, passwordId, password, submit_buttonId):
        # driver.get(Url)
        # pyautogui.keyDown('ctrl')
        # pyautogui.press('n')
        # pyautogui.keyUp('ctrl')
        driver.get(Url)
        # driver.find_element('id',usernameClick).click()
        driver.find_element('id', usernameId).send_keys(username)
        driver.find_element('id', passwordId).send_keys(password)
        driver.find_element('id', submit_buttonId).click()
        # showStmt()
        time.sleep(0.3)


    if ((CAPS) & 0xffff) == 0:
        pyautogui.press('capslock')

    url = 'https://cibnext.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__' \
          '=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=' \
          '1&BANK_ID=ICI&ITM=nli_corp_primer_login_btn_desk'
    try:
        login(url, 'login-step1-userid', saifynewUserId, 'AuthenticationFG.ACCESS_CODE', saifynewPass, 'VALIDATE_CREDENTIALS1')
    except:
        pass

    newtabscript("tabtwo")
    try:
        login(url, 'login-step1-userid', saifyUserId, 'AuthenticationFG.ACCESS_CODE', saifyPass, 'VALIDATE_CREDENTIALS1')
    except:
        pass

    newtabscript("tabthree")
    try:
        login(url, 'login-step1-userid', hcUserId, 'AuthenticationFG.ACCESS_CODE', hcPass, 'VALIDATE_CREDENTIALS1')
    except:
        pass
    try:
        if (driver.find_element('xpath',
                                '/html/body/form/div[5]/div/div[3]/div[1]/div/div[3]/div[1]/'
                                'div/div[2]/div/div/div[1]/div/div[1]/div/div/div').is_displayed() == True):
            engine.say("I-C-I-C-I  NET---BANKING Login Successfull")
            engine.runAndWait()
            print('Login Successfull !!')
        else:
            print('Some error might have occured while execution !!')

    except:
        pass
    stmtpath = "C:\\Users\\Acer\\Desktop\\BANK STATEMENT\\CURRENT"
    def saveSetting(path):
        Importall.downloadLoc(path)


    saveSetting(stmtpath)
    a = pyautogui.position()
    print(a)

    def logfile():
        today = datetime.datetime.now()
        today = today.strftime('%d-%b-%Y')
        end_time = datetime.datetime.now()
        timetaken = end_time - start_time
        timetaken = str(timetaken)
        print(timetaken)
        line = ['ICICI', '\t start time :' + str(start_time), '\n\t end time :' + str(end_time),
                '\n\t time taken : ' + str(timetaken)]
        line = str(','.join(line))
        with open(f'LOG\\logFileTest {today}.txt', 'a') as f:
            f.writelines(str(line))
            # f.write(''.join(line))
            f.write('\n\n')
        # print(line)

    logfile()
    # engine.say(a)
    # engine.runAndWait()

def main():
    otp =  Importall.sendotpAuth('ICICI Bank Site')
    # authenticate = input("Please Enter OTP to proceed \n")
    engine.say("Please enter OTP below to proceed")
    engine.runAndWait()
    authenticate = input("Please Enter OTP to proceed \n")

    if authenticate == otp:
        try:
            driver.maximize_window()
        except:
            pass
        icici()
    else:
        print("Error!!!\n Authentication Failed\n")

if __name__ == "__main__":
        main()
# if __name__ == "__main__":
#     icici()