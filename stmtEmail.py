#  Copyright (c) 2022.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator

import time
import yaml
import os
import glob
try:
    import Importall
except:
    pass
import pyautogui
import webbrowser as wb
import subprocess
import pyttsx3
import tkinter
from tkinter import messagebox
import tkmessagebox
import smtplib, ssl
import random, math
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# try:
#     Importall.driver.quit()
# except:
#     pass
#
try:
    Importall.driver.minimize_window()
except Exception as e:
    print(e)
    pass

engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')  # getting details of current speaking rate
# print(rate)  # printing current voice rate
engine.setProperty('rate', 200)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty('volume', 0.8)  # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female


def CAPSLOCK_STATE():
    import ctypes
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)

path = 'C:\\Users\\Acer\\Desktop\\BANK STATEMENT\\CURRENT\\'
path = path.replace('/',"\\")

yahoourl = 'https://mail.yahoo.com/d/compose/'
mailto = 'juzer@saifygroup.com; online@saifygroup.com; ' \
            'info@saifygroup.com; saifygroup.acc@gmail.com; murtaza@saifygroup.com; '

def stmt():
    engine.say("-----Opening BANK STATEMENT FOLDER-----")
    engine.runAndWait()
    subprocess.Popen(r'explorer /start,"C:\Users\Acer\Desktop\BANK STATEMENT\CURRENT\"')


pyautogui.press('capslock')


def openmailandsend():

    # yahoourl = 'https://mail.yahoo.com/d/compose/'
    # mailto = 'juzer@saifygroup.com; online@saifygroup.com; ' \
    #          'info@saifygroup.com; saifygroup.acc@gmail.com; murtaza@saifygroup.com; '

    engine.say("Opening : Yahoo E-MAIL")
    engine.runAndWait()

    wb.open_new(yahoourl)
    time.sleep(3)
    CAPS = CAPSLOCK_STATE()
    if ((CAPS) & 0xffff) != 0:
        pyautogui.press('capslock')
    time.sleep(3.5)
    print(pyautogui.position())
    pyautogui.moveTo([386, 374])
    pyautogui.click()
    time.sleep(2.5)
    pyautogui.write(mailto)
    time.sleep(0.3)
    pyautogui.press('Tab')
    pyautogui.write('BANK STATEMENT'.upper())
    time.sleep(1)
    pyautogui.press(['Tab', 'Tab'])
    pyautogui.write('please find attachment'.title())
    pyautogui.press('capslock')
    stmt()
    time.sleep(0.4)
    messagebox.showinfo(title="SUCCESS !!!", message="DONE !!!!")
    print("Mail Sent Successfully!!!")


def mailMain():
    yahoo_smtp = 'smtp.mail.yahoo.com'
    server = smtplib.SMTP(yahoo_smtp, 587)
    # Create a secure SSL context
    context = ssl.create_default_context()
    # gmail_smtp = 'smtp.gmail.com'
    server.starttls()  # context=context
    print("Connection Established !!")


    pwdofgmail = str('fhlrausxukdzixus')
    yahoo_pwd = str('hjtalymnbyecdpfh')
    yahoo_mail = str('aliasger341@yahoo.com')
    mail_gmail = str("aliasger1481@gmail.com")
    serverport = 'verify@serverport.online'

    login_add = yahoo_mail
    login_pwd = yahoo_pwd
    sender_add = yahoo_mail
    # reciever_add = ['juzer@saifygroup.com', 'online@saifygroup.com', 'info@saifygroup.com', 'saifygroup.acc@gmail.com', 'murtaza@saifygroup.com']
    reciever_add = [yahoo_mail]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = 'BANK STATEMENT'
    msg["To"] = ", ".join(reciever_add)


    text = """
    PFA
    
    
    """
    html = """\
        <html>
        <head>
            <style>
                mark {
                background-color: yellow;
                color: black;
                font-weight: bold;
                }
            </style>
        </head>
        <body>
            
            <p style = "font-size: 16px; color: black; font-weight: bold; padding: 13px;">
            <b><span style="background-color: yellow;">   PFA   </span></b>
            </p><br><br>
        </body>
        </html>
    """
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    msg.attach(part1)
    msg.attach(part2)

    #Attaching files
    try:
        os.chdir(path)

        attachmentfiles = ['ICICI SAIFY.xls', 'ICICI SAIFY_NEW.xls', 'ICICI SAIFY_OLD.xls', 'ICICI SHC.xls', 'IDBI SAIFY.xls', 'IDBI SHC.pdf',
                           'IDBI SAIFY.pdf', 'IDBI SHC.xls']

        attachment_path = path + ",".split(attachmentfiles)
        labeltext = ''

        # for file in os.listdir(path):
        #     if file.endswith(".pdf"):
        #         attachedfile = MIMEApplication(file, _subtype="pdf")
        #         # attachedfile.set_payload(file.read())
        #         attachedfile.add_header('content-disposition', 'attachment', filename= f'{file}')
        #         msg.attach(attachedfile)
        #         print(attachedfile)
        #
        #     if file.endswith(".xls"):
        #         attachedfile = MIMEApplication(file, _subtype="xls")
        #         # attachedfile.set_payload(file.read())
        #         attachedfile.add_header('content-disposition', 'attachment', filename= f'{file}')
        #         msg.attach(attachedfile)
        #         print(attachedfile)
        #
        #     if file.endswith(".xlsx"):
        #         attachedfile = MIMEApplication(file, _subtype="xlsx")
        #         # attachedfile.set_payload(file.read())
        #         attachedfile.add_header('content-disposition', 'attachment', filename= f'{file}')
        #         msg.attach(attachedfile)
        #         print(attachedfile)

                # with open(file, encoding = 'utf-8', errors = 'replace') as opened:
                #     openedfile = opened.read()
                #     print(openedfile)
                #     attachedfile = MIMEApplication(openedfile, _subtype="pdf")
                #     attachedfile.add_header('content-disposition', 'attachment', filename= openedfile)
                #     msg.attach(attachedfile)
        for file_path in attachment_path:
            ctype, encoding = mimetypes.guess_type(file_path)
            with open(file_path, 'rb') as f:
                attachedfile = MIMEApplication(f , _subtype="pdf")
                attachedfile.add_header('content-disposition', 'attachment', filename= f)
                msg.attach(attachedfile)
                print(attachedfile)


    except OSError:
        for file in os.listdir(path):
            if file == '':
                labeltext += " No file Found of PDF and/or Excel Type \n"


    msg = msg.as_string()

    finalmsg = msg
    server.login(login_add, login_pwd)
    server.sendmail(from_addr=sender_add,
                to_addrs=reciever_add,
                msg=finalmsg)

def mailBot():
    with open('loginDetails.yml', 'r') as file:
        conf = yaml.safe_load(file)
        myUserId = conf['yahoo']['userid']
        myPassword = conf['yahoo']['password']

    driver = Importall.driver
    driver.maximize_window()
    driver.get('https://login.yahoo.com/?.src=ym&pspid=159600001&activity=mail-direct&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%2Fcompose%2F')
    print(driver.current_url)
    driver.find_element('id','login-username').send_keys(myUserId)
    time.sleep(0.5)
    driver.find_element('xpath','//input[@type="submit"]').click()
    # pass

# mailMain()
if __name__ == "__main__":
    openmailandsend()
    # mailBot()


