#  Copyright (c) 2022.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator

import time
import yaml
import Importall
import pyautogui
# from WebsiteLoginAutomation import *
from Importall import *
from selenium.webdriver.common.keys import Keys
import datetime


def idbihcMain():
    start_time = datetime.datetime.now()

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  + In case of any changes and/or discrepancies please contact administrator +
    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    engine = Importall.engine

    with open('loginDetails.yml', 'r') as file:
        conf = yaml.safe_load(file)
        myUserId = conf['idbihc']['useridM']
        myPassword = conf['idbihc']['passwordM']


    engine.say("LOGGING IN I.D.B.I. CORPORATE BANK SITE")
    engine.runAndWait()
    CAPS = Importall.CAPSLOCK_STATE()


    def logfile():
        today = datetime.datetime.now()
        today = today.strftime('%d-%b-%Y')
        end_time = datetime.datetime.now()
        timetaken = end_time - start_time
        timetaken = str(timetaken)
        print(timetaken)
        line = ['IDBI HC', '\n\t start time :'+ str(start_time),'\n\t end time :'+str(end_time),'\n\t time taken : '+ str(timetaken)]
        line = str(','.join(line))
        with open(f'LOG\\logFileTest {today}.txt', 'a') as f:
            f.writelines(str(line))
            # f.write(''.join(line))
            f.write('\n\n')
        # print(line)


    def login(Url, usernameId, username, captchaclickId, loginButton, passwordId, password, submit_buttonId):
        # driver.get(Url)
        driver.get(url=Url)
        # driver.find_element('id',usernameClick).click()
        driver.find_element('id', usernameId).send_keys(username)
        # root.mainloop()
        driver.find_element('id', captchaclickId).click()
        time.sleep(6)
        try:
            driver.find_element('id', loginButton).click()
        except:
            pass
        time.sleep(0.5)
        # driver.find_element('xpath', '//*[@id="AuthenticationFG.TARGET_CHECKBOX"]').click()
        driver.find_element('xpath','/html/body/form/div/div/div[3]/div[4]/div/p[3]/span[1]/span[1]').click()
        driver.find_element('id', passwordId).send_keys(password)
        time.sleep(1)
        driver.find_element('id', submit_buttonId).click()



    url = 'https://corp.idbibank.co.in/corp/AuthenticationController?FORMSGROUP_ID' \
            '__=AuthenticationFG&__START_TRAN_FLAG__=Y&__FG_BUTTONS__=LOAD&ACTION.LOAD=' \
            'Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=IBKL'

    # login(url, 'AuthenticationFG.USER_PRINCIPAL', myUserId, 'AuthenticationFG.VERIFICATION_CODE',
    #       'STU_VALIDATE_CREDENTIALS'
    #       , 'AuthenticationFG.ACCESS_CODE', myPassword, 'VALIDATE_STU_CREDENTIALS1')

    # newtabscript("idbihc")

    login(url,'AuthenticationFG.USER_PRINCIPAL',myUserId,
          'AuthenticationFG.VERIFICATION_CODE','STU_VALIDATE_CREDENTIALS','AuthenticationFG.ACCESS_CODE',myPassword,'VALIDATE_STU_CREDENTIALS1')

    if ((CAPS) & 0xffff) == 0:
        pyautogui.press('capslock')
    time.sleep(1)
    try:
        if (driver.find_element('id', 'headerouter').is_displayed() == True):
            engine.say("I.D.B.I. HEALTH-CARE LOGIN SUCCESSFULL")
            engine.runAndWait()
            print("Login Successful")
            side_panel = '//a[@id="menu-button"]'
            driver.find_element('xpath', side_panel).click()
            time.sleep(1)
            # try:
            #     driver.get('https://corp.idbibank.co.in/corp/Finacle;jsessionid='
            #            '0000y38-TCVhg0cDRc1KuwD0VWL:1dclnsgeo?bwayparam=SEgPj1ZgsXpO0scYJ7eYV8wxbbS'
            #            'tnlCKfJmTFEy%2FLpclBbR2h4L%2Fwy1DJ1l%2FEtLXw6AqW0HcaOIGJnCXfjFRvQEllGearVMI7q18bR'
            #            'yLXXlMVVuEomi0LZGxsP8tzj5D%0D%0AxAyPWf1YfuDhQDVb6Lha3tjpQRbncXgvvKxbMwdS1ekY6%2B5iwLNtCc'
            #            'AiR4r55e0GHiKdytInTVRFgqVNLIxfiRPOQdELGTh5VTBBSyCukTc%3D')
            #
            # except Exception:
            #     pass
        else:
            print('Login Failed due to some error')
    except:
        pass

    def saveSetting(tabname):
        newtabscript(tabname)
        driver.get('about:preferences')
        driver.find_element('xpath', '//*[@id="alwaysAsk"]').click()
        driver.find_element('xpath', '//*[@id="chooseFolder"]').click()

    # saveSetting("tab2")
    logfile()

if __name__ == "__main__":
    idbihcMain()