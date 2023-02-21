#  Copyright (c) 2023.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator
import time
import keyboard
# from pynput import keyboard
import Importall
import pyaudio, speech_recognition as sr
import wave, sys
import pyttsx3
import stmtEmail
import vosk
from vosk import Model, KaldiRecognizer
import pyttsx3
# import sphinxbase
import pocketsphinx
# import whisper
import torch
import os
import subprocess
from ffmpeg import *
import playsound
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import time
from stmtEmail import openmailandsend
import bankSelector
import stmtCompile
import fileDel

break_program = True
def on_press(key):
    global break_program
    print(key)
    if key == keyboard.press('f1') and break_program:
        print('f1 pressed')
        break_program = False

    if key == keyboard.press('enter'):
        print('Enter pressed')
        break_program = True
def lisMic():
    p = pyaudio.PyAudio()
    r = sr.Recognizer()
    engine = pyttsx3.init()


    hello = ['hello*','hi*', 'wassup', 'hey', 'good day', 'good * ']
    attendance = ['attendan*', 'attendance software', 'realsoft*', 'real soft*']
    # print("len(hello) : " + str(len(hello)))
    def quitDriver():
        pass
        # Importall.driver.quit()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        # engine.say("Recording initiated. Please say something ")
        print("Please say something after the beep ")
        # time.sleep(0.5)
        beep = AudioSegment.from_wav('sound-on.wav')
        play(beep)
        engine.runAndWait()
        audio = r.listen(source)
        # recout = r.record(source)
        try:
            output = r.recognize_google(audio)
            play(beep)
            print("You have said : \n" + output)

            output = output.lower()
            output = str(output)

            if output == "bank folder" or output == "bank statement folder":
                engine.say("Opening Bank Statement Folder")
                engine.runAndWait()
                subprocess.Popen(r'explorer /start,"C:\Users\Acer\Desktop\BANK STATEMENT\CURRENT\"')
                # quitDriver()

            elif output == "work folder":
                engine.say("Opening Work Folder")
                engine.runAndWait()
                subprocess.Popen(r'explorer /start,"E:\WORK\"')
                # quitDriver()

            elif output == "bank selector":
                engine.say(" Opening -- bank selector app")
                engine.runAndWait()
                bankSelector.bankselectAppMain()

            elif output == "statement compile" or output == 'compile statement':
                engine.say(" Running -- Statement Compile Module")
                engine.runAndWait()
                stmtCompile.compileStmt()

            elif output == "send statement" or output == 'email statement':
                engine.say(" Sending Statement ")
                engine.runAndWait()
                stmtEmail.openmailandsend()

            elif any(output in i for i in ['file del', 'delete file?' , 'delete statement',
                                           'delete bank statement', 'delete bank statement file', 'file delete']):
                engine.say(" Deleting Files !!!")
                engine.runAndWait()
                try:
                    fileDel.DeleteFiles()
                except:
                    pass
                quitDriver()

            elif any(output in i for i in hello):
                # print(f'{output} is present in hello list')
                engine.say("Hello there.... How are you?  I hope you are doing well")
                engine.runAndWait()
                quitDriver()

            elif any(output in i for i in attendance):
                # print(f'{output} is present in hello list')
                engine.say("OPENING: REALSOFT ATTENDANCE APPLICATION")
                engine.runAndWait()
                subprocess.Popen(['C:\Program Files (x86)\\realtime_biometrics\Realsoft11.6\Realsoft11.6-old.exe'])
                quitDriver()


            else:
                pass
                # quitDriver()



        except Exception as e:
            print(str(e))

def runlisMic():
    while keyboard.is_pressed(59) == False:
        # time.sleep(1)
        lisMic()
        if keyboard.is_pressed(59):
            print('Esc pressed')
            break
    # print('press enter to initiate')
    # while keyboard.is_pressed('f1'):
    #     time.sleep(1)
    #     lisMic()
    #     # if keyboard.KEY_DOWN('f1'):
    #     #     print('F1 pressed')
    #     #     break

if __name__ == "__main__":
    runlisMic()