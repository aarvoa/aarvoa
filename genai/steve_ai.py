import json

import pyttsx3
import speech_recognition as sr
from streamui import ask_gemini




#reusable code
def talk(text):
    #this is a function/ it takes one argument called text
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    del(engine)

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source: #with is my manager who will take care of my resource which is my mic
            print("listening...")
            voice = listener.listen(source=source,phrase_time_limit=10)
            # print(type(voice))
            full_command = listener.recognize_vosk(audio_data=voice,language="en")
            full_command = full_command.lower()
            command = json.loads(full_command)['text']
            if 'steve' in command:
                command =  command.replace('steve', '')
                return command
            if 'exit' in command:
                print("Tschuss...")
                talk("Good Bye")
                exit(0)
            return "Steve Not Found"
    except Exception as e:
        print(e)
        exit(0)



def run_steve():
    while True:
        command = take_command()
        if command=="Steve Not Found":
            print("Call me Steve...")
        else:
            print("You :" + command)
            ans="Today is a beautiful day"
            # ans = ask_gemini(q=command)


            print("Steve :"+ans)
            talk(ans)
run_steve()