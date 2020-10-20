#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 21:52:56 2020

@author: trabdlkarim
"""
from PyQt5 import QtCore

import speech_recognition as speech
import gtts
from gtts import gTTS
import random, string
import os
import tempfile
from pydub import AudioSegment
from pydub.playback import play
import threading


def gen_rand_string(length=16):
    fname = "".join(random.choice(string.ascii_uppercase +
                                  string.ascii_lowercase +
                                  string.digits) for _ in range(length))
    return fname


class VoceRecognizer(speech.Recognizer):
    pass


class VoceSynthesizer(gTTS):
    pass

class AssistantSignals(QtCore.QObject):
    welcome = QtCore.pyqtSignal()
    openNewTab = QtCore.pyqtSignal()
    openNewWindow = QtCore.pyqtSignal()
    closeCurrentTab = QtCore.pyqtSignal()
    closeCurrentWindow = QtCore.pyqtSignal()
    reload = QtCore.pyqtSignal()
    back = QtCore.pyqtSignal()
    forward = QtCore.pyqtSignal()
    homepage = QtCore.pyqtSignal()
    bye  = QtCore.pyqtSignal()
    search = QtCore.pyqtSignal(str)




class VoceAssistant(QtCore.QObject):
    def __init__(self,name="Voce",age=None,gender=None,lang=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.lang = lang
        self.recognizer = VoceRecognizer()
        self.tmp_fname = os.path.join(tempfile.gettempdir(),"voce-" + gen_rand_string() +".mp3")
        self.signals = AssistantSignals()
        self.stop_event = threading.Event()
        self.isRunning = False

    def welcome(self):
        text = "Hello, welcome to Voce Browser. My name is Voce, your browser assistant. How can I help you?"
        self.speak(text)

    def listen(self):
        with speech.Microphone() as mic:
            text_data = ""
            voice_data  = self.recognizer.listen(mic,5,5)
            try:
                text_data = self.recognizer.recognize_google(voice_data)
            except speech.UnknownValueError:
                pass
            except speech.RequestError:
                self.speak("Sorry, the service is down")

            return text_data.lower()

    def speak(self,text):
        try:
            tts = gTTS(text=text,lang='en')
            tts.save(self.tmp_fname)
            song = AudioSegment.from_mp3(self.tmp_fname)
            play(song)
        except gtts.tts.gTTSError:
            print("Voce Failed to connect")

    def check_voice_cmd(self,cmds,voice_cmd):
        for cmd in cmds:
            if cmd in voice_cmd:
                return True
        return False

    def do_greet(self,name=None):
       greetings = "Hello, how can I help you"
       if name:
           greetings += name
       self.speak(greetings)

    def do_introduce_yourself(self):
        reply = "My name is " + self.name
        self.speak(reply)

    def do_search(self,cmd):
        kwords = cmd.split()
        if len(kwords)>1:
            kwords = kwords[1:]
            query = ""
            for w in kwords:
                query += w
            self.speak("Searching "+query+" on the web for you.")
            self.signals.search.emit(query)
        else :
            self.speak("What do you want me to search ?")

    def do_open_new_tab(self):
        self.speak("Opening new tab for you")
        self.signals.openNewTab.emit()

    def do_close_tab(self):
        self.speak("Okay, closing current tab")
        self.signals.closeCurrentTab.emit()


    def do_open_new_window(self):
        self.speak("Opening new window for you")
        self.signals.openNewWindow.emit()

    def do_close_window(self):
        self.speak("Okay, closing  current window")
        self.signals.closeCurrentWindow.emit()

    def do_exit_browser(self):
        self.speak("Okay, exiting")
        self.signals.bye.emit()


    def do_goback(self):
       self.speak("Opening new tab for you")
       self.signals.back.emit()

    def do_goforward(self):
        self.speak("Going back to previous web page")
        self.signals.forward.emit()

    def do_reload_page(self):
        self.speak("Wait a second reloading current web page")
        self.signals.reload.emit()

    def do_gohome(self):
         self.speak("Going back to homepage")
         self.signals.homepage.emit()

    def run_forever(self):
        self.welcome()
        while not self.stop_event.is_set():
            voice_cmd = self.listen()
            if voice_cmd:
                if self.check_voice_cmd(["Voce","voice","assistant"],voice_cmd):
                    self.speak("Yes, I am listening to you. Tell me what to do.")

                elif self.check_voice_cmd(["Thank you","Thanks"],voice_cmd):
                    self.speak("You are welcome")

                elif self.check_voice_cmd(["Search","Lookup","Look for"],voice_cmd):
                    self.do_search(voice_cmd)

                elif self.check_voice_cmd(["open tab","open new tab"],voice_cmd):
                    self.do_open_new_tab()

                elif self.check_voice_cmd(["open window","open new window"],voice_cmd):
                    self.do_open_new_window()

                elif self.check_voice_cmd(["close window","close current window"],voice_cmd):
                    self.do_close_window()

                elif self.check_voice_cmd(["close tab","close current tab"],voice_cmd):
                    self.do_close_tab()

                elif self.check_voice_cmd(["go back","previous page"],voice_cmd):
                    self.do_goback()

                elif self.check_voice_cmd(["go forward","next page"],voice_cmd):
                    self.do_goforward()

                elif self.check_voice_cmd(["go home","homepage"],voice_cmd):
                    self.do_gohome()

                elif self.check_voice_cmd(["reload page","reload current page","refresh page"],voice_cmd):
                    self.do_reload_page()

                elif self.check_voice_cmd(["exit","quit"],voice_cmd):
                    self.do_exit_browser()
                else:
                    self.speak("Sorry, I did not get that. Please repeat again!")



class AssistantRunnable(QtCore.QRunnable):
    def __init__(self,target,*args,**kwargs):
        super(AssistantRunnable,self).__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args,**self.kwargs)

    def start(self):
        QtCore.QThreadPool.globalInstance().start(self)