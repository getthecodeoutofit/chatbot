import os
import datetime
# from googlesearch import search
import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import webbrowser
import myapi

i=1
def getmycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        global i
        if i == 1:
            print("Please wait. Calibrating microphone...")   
            i +=1
        r.energy_threshold = 300
        # r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 1.4
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
    if "google" in  command.lower() or "browser" in command.lower() and "search" in command:
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
        assistant_speaks("opening.. visual studio code")
        os.system("code .")

    elif "terminal" in command.lower():
        assistant_speaks("opening terminal")
        os.system("gnome-terminal")

    elif "java application" in command.lower():
        assistant_speaks("opening intelli j idea")
        os.system("gnome-terminal -- bash -c \"/home/ravi/Idea/bin/idea.sh\"")

    elif "college" in command.lower() or "erp" in command.lower():
        assistant_speaks("Opening college website: ")
        webbrowser.open("https://student.gehu.ac.in")    

def create(command):
    if "named" in command:
        check = "named"
    elif "name" in command:
        check = "name"
    res = command.split(check,1)
    name  = res[1]
    if "file" in command or "text" in command:
        assistant_speaks("creating text file named "+ name)
        os.system(f"touch {name}.txt")
    elif "folder" in command:
        assistant_speaks("Creating a directory..")
        os.system(f"mkdir {name}")

def remove(command):
    if "named" in command:
        check = "named"
    elif "name" in command:
        check = "name"
    res = command.split(check,1)
    name  = res[1]
    if "file" in command or "text" in command:
        assistant_speaks("removing text file named "+ name)
        os.system(f"rm -rf {name}.txt")
    elif "folder" in command:
        assistant_speaks("removing a directory..")
        os.system(f"rmdir {name}")



def greet():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        assistant_speaks(f"GOOD MORNING")
    elif hour > 12 and hour < 17:
        assistant_speaks(f"GOOD AFTERNOON")
    else:
        assistant_speaks(f"GOOD EVENING")

def telltime():
    # second = datetime.datetime.now().second
    minute = datetime.datetime.now().minute
    hour  = datetime.datetime.now().hour
    assistant_speaks(f"The time is {hour} .... {minute}")

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
number = 1
if __name__ == "__main__":
    while True:
        query = getmycommand()
        if "open" in query.lower() or "play" in query or "search" in query:
            browsercommand(query)
        
        elif "time" in query.lower():
            telltime()

        elif "hello" in query.lower() and "program" in query.lower():
            print("sending request please wait....")
            a = myapi.AI(query + "give the consize answer")
            print(a)
            assistant_speaks(a)

        elif "take" in query.lower():
            assistant_speaks("Taking screenshot")
            os.system(f"xfce4-screenshooter -f -s /home/ravi/chatbot/{number}.png")
            number += 1    

        elif "your name" in query.lower():
            assistant_speaks("I dont have any name yet: ")

        elif "create" in query.lower():
            create(query)

        elif "remove" in query.lower():
            remove(query)

        elif "introduce yourself" in query.lower():
            intro = ('''I'm your friendly voice assistant,ready to assist you with your tasks. What would you like me to do for you?''')
            assistant_speaks(intro)

        elif "what" in query.lower() and "can" in query and "you" in query:
            assistant_speaks('''I can answer your questions play music,create or delete files or folder and much more. I'm getting regular updates.''')

        elif "hello" in query.lower() or "whatsup" in  query.lower():
            assistant_speaks("Hello there! How can i help you: ")
        
        elif "shutdown" in  query.lower():
            assistant_speaks("okay")
            os.system("sudo shutdown -h now")
            
        
        else:
            othercommand(query)