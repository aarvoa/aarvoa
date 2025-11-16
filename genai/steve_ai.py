import speech_recognition as sr
from speech_recognition.recognizers import google
listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        # print(type(voice))
        command = listener.recognize_vosk(audio_data=voice,language="en")
        print(command)
except Exception as e:
    print(e)

# import speech_recognition as sr
# from speech_recognition.recognizers import google
# # Initialize recognizer class (for recognizing the speech)
# r = sr.Recognizer()
#
# # Reading Microphone as source
# # listening the speech and store in audio_text variable
# with sr.Microphone() as source:
#     print("Talk")
#     audio_text = r.listen(source)
#     print("Time over, thanks")
#     # recoginze_() method will throw a request
#     # error if the API is unreachable,
#     # hence using exception handling
#
#     try:
#         # using google speech recognition
#
#         print("Text: " + google.recognize_legacy(audio_data=audio_text,recognizer=r))
#     except:
#         print("Sorry, I did not get that")