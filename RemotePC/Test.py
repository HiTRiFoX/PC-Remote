import speech_recognition as sr
import pyttsx3 as tts
import datetime as dt
import webbrowser as wb
import neuralintents

# wb.open("URL")

# Settings
r = sr.Recognizer()
r.energy_threshold = 20000                                                                            # The input volume

speaker = tts.init()
speaker.setProperty('rate', 170)


def say_time():
    hour = dt.datetime.now().hour
    if 5 <= hour <= 11:
        return "Good Morning"
    elif 12 <= hour <= 14:
        return "Good Noon"
    elif 15 <= hour <= 19:
        return "Good Afternoon"
    elif hour >= 20 or hour <= 4:
        return "Good Night"


def say_name():
    return "Reuven"


def help(saytime="", sayname=""):
    speaker.say(f"{saytime} {sayname}, How can I help you?")
    speaker.runAndWait()


def listening():
    with sr.Microphone() as mic:
        print("How can I help you?")
        audio = r.listen(mic)

        try:
            return r.recognize_google(audio)
        except:
            print("What did you say?..")


assistant = GenericAs

help(say_time(), say_name())


with sr.Microphone() as m:
    print('What you want? ')
    audio = r.listen(m)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except:
        print("What did you say?..")

