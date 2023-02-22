#  Copyright (c) 2023.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator
import Importall
import time
import yaml
from selenium.webdriver.common.keys import Keys
import datetime
import pyautogui

engine = Importall.engine
driver = Importall.driver
def jsClick(btn):
    driver.execute_script("arguments[0].click();", btn)
def linkedinMain():


    with open('loginDetails.yml', 'r') as file:
        conf = yaml.safe_load(file)
        myUserId = conf['linkedin']['userid']
        myPassword = conf['linkedin']['password']

    CAPS = Importall.CAPSLOCK_STATE()

    try:
        driver.maximize_window()
    except:
        pass

    driver.get('https://www.linkedin.com/')
    time.sleep(2)
    driver.find_element('xpath', '//input[@id="session_key"]').send_keys(myUserId)
    time.sleep(1)
    driver.find_element('xpath', '//input[@id="session_password"]').send_keys(myPassword)
    time.sleep(2)
    submit_btn = driver.find_element('xpath', '//button[@type="submit"]').click()

    if ((CAPS) & 0xffff) == 0:
        pyautogui.press('capslock')
    time.sleep(1)

    driver.get('https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=71z')
    time.sleep(2.5)
    # msg_btn = driver.find_element('xpath','//button[@id="ember"]').click()
    all_btns = driver.find_elements('tag name', 'button')
    msg_buttons = [btn for btn in all_btns if btn.text == 'Message']
    msg_buttons[0].click()
    time.sleep(1)
    paragraphs = driver.find_elements('tag name', 'p')
    # paragraphs[-5].send_keys('aaaaa')
    time.sleep(0.2)
    print(paragraphs[-5].text)
    driver.execute_script("alert('Success !!');")

if __name__ == "__main__":
    linkedinMain()