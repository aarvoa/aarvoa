import speech_recognition as sr
import pyttsx3
import json
from speech_recognition.recognizers import google
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            # print(type(voice))
            full_command = listener.recognize_vosk(audio_data=voice,language="en")
            full_command = full_command.lower()
            command = json.loads(full_command)['text']

            if 'steve' in command:
                command =  command.replace('alexa', '')
                print(command)
            else:
                print("Steve not detected")

    except Exception as e:
        print(e)
    return command

def run_steve():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print('playing')


run_steve()