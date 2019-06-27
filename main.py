import pyttsx3 as pyt
import speech_recognition as sr
import smtplib
import credentials
import pandas as pd
import serial_test as st
import apiai
import json
import wikipedia

def say(output):
    engine = pyt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 140)
    engine.say(output)
    engine.runAndWait()
    
