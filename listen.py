import os
import datetime
from googlesearch import search
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import webbrowser
from youtubesearchpython import ChannelsSearch
import myapi
i=1
def getmycommand():

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        global i
        if i == 1:
            print("Please wait. Calibrating microphone...")   
            i +=1
        # listen for 5 seconds and calculate the ambient noise energy level  
        r.energy_threshold = 600
        r.pause_threshold = 1
        print("listening.....")
        audio = r.listen(source)
        print("Recognizing....")

        try:
            query = r.recognize_google(audio,language="en-in")
            print(f"{query}")
            return query
        except Exception as e:
            return "error"


def assistant_speaks(output):
    mytext = "hello"
    myobj = gTTS(text=output, lang="en",tld = 'ca' ,slow=False)
    myobj.save(mytext + ".mp3")
    playsound.playsound(mytext+".mp3", True)
    os.remove(mytext+".mp3")


def browsercommand(command):
    if "google" in  command.lower() or "browser" in command.lower() or "search" in command:
        if "search" in  command:
            word = "search"
            res = command.split(word, 1)
            splitString = res[1]
            assistant_speaks("Searching " + splitString)
            newstr = ""
            for char in splitString:
                if char == " ":
                    newstr += "+"
                else:
                    newstr += char
            webbrowser.open_new_tab(f"https://www.google.com/search?client=firefox-b-lm&q={newstr}")
        else :
            assistant_speaks("opening google")
            webbrowser.open_new_tab("https://www.google.com")

    elif "youtube" in command.lower():
        if "search" in command:
            word = "search"
            res = command.split(word, 1)
            splitString = res[1]
            assistant_speaks("Searching " + splitString)
            newstr = ""
            for char in splitString:
                if char == " ":
                    newstr += "+"
                else:
                    newstr += char
            webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={newstr}")
        else:
            assistant_speaks("opening youtube")
            webbrowser.open_new_tab("https://www.youtube.com")

    elif "python application" in command.lower():
        assistant_speaks("opening pycharm")
        os.system("gnome-terminal -- bash -c \"/home/ravi/pycharm-2023.2.3/bin/pycharm.sh\"")

    elif "code" in command.lower():
        assistant_speaks("opening.. visual code")
        os.system("code .")

    elif "terminal" in command.lower():
        assistant_speaks("opening terminal")
        os.system("gnome-terminal")


def greet():
    hour = datetime.datetime.now().hour
    user = "Ravi"
    if hour >= 0 and hour < 12:
        assistant_speaks(f"GOOD MORNING")
    elif hour > 12 and hour < 17:
        assistant_speaks(f"GOOD AFTERNOON")
    else:
        assistant_speaks(f"GOOD EVENING")


def othercommand(command):
    if "search" in command.lower():
        browsercommand(command)

    elif "close" in command or "stop" in command:
        assistant_speaks("okayy")
        os.system("kill -9 $(pgrep bash)")
    elif "update" in command:
        assistant_speaks("updating the system...")
        os.system("gnome-terminal -- bash -c \"sudo apt update\"")
        assistant_speaks("you will require to enter the password")


greet()
lang = "en"
if __name__ == "__main__":
    while True:
        if lang == "en":

            query = getmycommand()

            if "open" in query.lower() or "play" in query or "search" in query:
                browsercommand(query)
            elif "your name" in query.lower():
                assistant_speaks("I dont have any name yet: ")


            elif "introduce yourself" in query.lower():
                intro = ('''I'm your friendly voice assistant,ready to assist you with your tasks.. What would you like me to do for you?''')
                assistant_speaks(intro)

            elif "what" in query and "can" in query and "you" in query:
                assistant_speaks('''I can answer your questions set alarms play music and much more. I'm always learning new things, so please don't hesitate to ask me anything.
                I'm here to help you with all your needs, big or small.''')

            elif "change language" in query:
                lang = "hi"

            elif "hello" in query.lower() or "whatsup" in  query:
                assistant_speaks("Hello there, How can i help you: ")
            
            elif "shutdown" in  query.lower():

                assistant_speaks("Are your sure: ")
                b = input("yes/no: ")
                if b == "yes":
                    os.system("sudo shutdown -h now")
                else:
                    pass
            elif "what" in query or "can" in query or "tell" in query or "which" in query:
                a = myapi.AI(query)
                assistant_speaks(a)

            else:
                othercommand(query)

