#  Copyright (c) 2022.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator

import pyttsx3
import webbrowser
from selenium import webdriver
from selenium import *
from selenium_firefox import *
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_binary import *
from selenium.webdriver.firefox.options import Options
import datetime
import smtplib, ssl
import random, math
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup

binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\\firefox.exe")
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.startup.homepage","http://www.duckduckgo.com")
fp.set_preference('javascript.enabled',True)
fp.set_preference('browser.urlbar.openintab',True)
# fp.set_preference('browser.link.open_external',2)
fp.set_preference('browser.link.open_newwindow',3)
fp.set_preference("browser.download.useDownloadDir",False)
fp.set_preference("pref.downloads.disable_button.edit_actions",False)
fp.set_preference("browser.download.always_ask_before_handling_new_types",True)
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.useDownloadDir",False)
fp.set_preference("browser.download.dir", "C:\\Users\\Acer\\Desktop\\BANK STATEMENT\\CURRENT")
fp.set_preference("browser.download.lastDir", "C:\\Users\\Acer\\Desktop\\BANK STATEMENT\\CURRENT")
# 0 means to download to the desktop, 1 means to download to the default "Downloads" directory, 2 means to use the directory
def downloadLoc(location):
    if location != "":
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.dir", location)
        fp.set_preference("browser.download.lastDir", location)
    else:
        fp.set_preference("browser.download.folderList", 1)

opts = Options()
opts.profile = fp
# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True

driver = webdriver.Firefox(firefox_binary=binary, executable_path='geckodriver.exe', firefox_profile=fp)
# driver = webdriver.Firefox(firefox_binary=binary, executable_path='geckodriver.exe', firefox_profile=fp, capabilities=firefox_capabilities)
# durl = driver.command_executor._url
# session_id = driver.session_id
# driver = webdriver.Remote(command_executor=durl,desired_capabilities={})
# driver.session_id = session_id

# initiating py text to speech tts
engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')  # getting details of current speaking rate

engine.setProperty('rate', 217)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)

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


def newtabscript(TabName):
    driver.execute_script(f"window.open('about:blank','{TabName}');")
    # It is switching to second tab now
    driver.switch_to.window(f"{TabName}")

def logfile(name,start_time):
    today = datetime.datetime.now()
    today = today.strftime('%d-%b-%Y')
    end_time = datetime.datetime.now()
    timetaken = end_time - start_time
    timetaken = str(timetaken)
    print(timetaken)
    line = [name, '\n\t start time :'+ str(start_time),'\n\t end time :'+str(end_time),'\n\t time taken : '+ str(timetaken)]
    line = str(','.join(line))
    with open(f'LOG\\logFileTest {today}.txt', 'a') as f:
        f.writelines(str(line))
        # f.write(''.join(line))
        f.write('\n\n')


yahoo_smtp = 'smtp.mail.yahoo.com'
server = smtplib.SMTP(yahoo_smtp, 587)
# Create a secure SSL context
context = ssl.create_default_context()
# gmail_smtp = 'smtp.gmail.com'
server.starttls()  # context=context


def sendotpAuth(otpfor):
    # otpfor = str(otpfor).upper()
    pwdofgmail = str('fhlrausxukdzixus')
    yahoo_pwd = str('hjtalymnbyecdpfh')
    yahoo_mail = str('aliasger341@yahoo.com')
    mail_gmail = str("aliasger1481@gmail.com")
    serverport = 'verify@serverport.online'

    login_add = yahoo_mail
    login_pwd = yahoo_pwd
    sender_add = serverport
    reciever_add = [yahoo_mail ]#, ' juzer@saifygroup.com']

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f'OTP for {otpfor}'
    msg["To"] = ", ".join(reciever_add)

    otp = ''
    String = '1234567890'
    length = len(String)
    for i in range(6):
        otp += String[math.floor(random.random() * length)]
        # return otp

    text = f"""\
        Your OTP for {otpfor} is : \n\t {otp}
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
            <p>Your <b>OTP for """ + otpfor + """</b> is : \n\t</p>
            <p style = "font-size: 16px; color: black; font-weight: bold; padding: 13px;">
            <b><span style="background-color: yellow;">   """ + otp + """   </span></b>
            </p>
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


    # msg = msg.as_string()

    finalmsg = msg
    server.login(login_add, login_pwd)
    server.sendmail(from_addr=sender_add,
                    to_addrs=reciever_add,
                    msg=finalmsg.as_string())
    print("OTP sent successfully !!! ")
    return otp