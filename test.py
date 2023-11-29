import speech_recognition as s
from gtts import gTTS
def assist():
    r = s.Recognizer()

    with s.Microphone as source:
        r.energy_threshold = 300
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio,language="en-in")
            return query
        except Exception as e:
            return "error"

def take(command):
    name = "hello"

    sobj = gTTS(text = command,lang= "ca",slow = False)
    