# Get the libs you need
import warnings
import pyttsx3
import speech_recognition as sr
import playsound
import os 
from gtts import gTTS
import datetime
import calendar
import wikipedia
import webbrowser
import random
import winshell
import subprocess
import pyjokes
from PIL import ImageGrab

# Ignore warnigns
warnings.filterwarnings("ignore")

# Init
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. 0 for male, 1 for female. Change as you wish.

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        recog.adjust_for_ambient_noise(source, duration=1)
        audio = recog.listen(source)

    data = ' '

    try:
        data=recog.recognize_google(audio)
        print("You said: ", data)

    except sr.UnknownValueError:
        print("Assistant could not understand you.")
    
    except sr.RequestError as ex:
        print("Request error from Google Speach Rocognition: ", ex)

    return data


def respnse(text):
    print(text)

    tts = gTTS(text=text, lang="en")

    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)

    os.remove(audio)


def call(text):
    action_call = "jarvis" # The wake word

    text = text.lower()

    if action_call in text:
        return True
    
    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return f'Today is {week_now}, {months[month_now - 1]} the {ordinals[day_now - 1]}.'



def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == 'who' and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + "" + list_wiki[i + 3]
        
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, 'w') as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def take_screenshot():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    save_path = os.path.join(r"[YOUR SCREENSHOT DIRECTORY]", f"screenshot_{timestamp}.png") # ------------------------------------------------------- PUT YOUR SCREENSHOT DIRECTORY IN THERE ---------------------------------------
    
    screenshot = ImageGrab.grab()
    screenshot.save(save_path)
    screenshot.show()

while True:
    try:

        text = rec_audio()
        speak = ' '

        if call(text):

    

            if "date" in text:
                get_today = today_date()
                talk(get_today)

            elif "time" in text:
                now = datetime.datetime.now()

                meridien = ''
                if now.hour >= 12:
                    meridien = "PM"
                    hour = now.hour - 12

                else:
                    meridien = "AM"
                    hour = now.hour
                
                
                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                talk(f"It is {str(hour)}:{str(minute)} {meridien}.")
            
            elif "wikipedia" in text.lower():
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=3)
                    talk(wiki)
                    print("\n", wiki, "\n")
            
            elif "who are you" in text:
                bio_message = """Hello, I am Jarvis, your personal computer assistant. I am here to make your life easier and simpler. I have various abilities such as solving math problems to opening aplications on your computer."""
                talk(bio_message)              

            elif "your name" in text:
                talk("My name is Jarvis.")

            elif "who am i" in text.lower():
                talk("You are the user. Probably a human.")  

            elif "why do you exist" in text.lower():
                talk("It is a secret.")

            elif "how are you" in text:
                talk("I am fine How are you?")

            elif "open" in text.lower():
                if "browser" in text.lower():
                    talk("Opening browser")
                    os.startfile(
                        r"C:\Users\COSMI\AppData\Local\Programs\Opera GX\launcher.exe"
                    )
                elif "notepad" in text.lower():
                    talk("Opening notepad.")
                    os.startfile(
                        r"c:\\windows\\system32\\notepad.exe"
                    )
                elif "vs code" in text.lower() or "visual studio" in text.lower():
                    talk("Opening Visual Studio Code.")
                    os.startfile(
                        r"C:\Users\[YOUR USERNAME]\AppData\Local\Programs\Microsoft VS Code\Code.exe" ------------------------------------------------------------ PUT YUOR USERNAME ------------------------------------------------------------
                    )
                elif "youtube" in text.lower():
                    talk("Opening Youtube")
                    webbrowser.open("https://www.youtube.com")
                elif "stackoverflow" in text.lower():
                    talk("Opening stackoverflow")
                    webbrowser.open("https://stackoverflow.com/")
                elif "roblox" in text.lower():
                    talk("Opening Roblox")
                    webbrowser.open("https://roblox.com/home")
                else:
                    talk("Website or application not found.")

            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open("https://www.youtube.com/results?search_query=", search)
                talk("Searching for ", search, " on youtube.")

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open("https://www.google.com/search?q=", search)
                talk("Searching for ", search, " on google.")

            elif "play music" in text.lower() or "play songs" in text.lower():
                talk("Opening your music library.")
                music_dir = r"C:\Users\COSMI\Music"
                songs = os.listdir(music_dir)
                random_song = os.path.join(music_dir, random.choice(songs))
                playsound.playsound(random_song)

            elif "empty recycle bin" in text.lower() or "clear recycle bin" in text.lower():
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                talk("Rycycle bin emptied")

            elif "note" in text.lower():
                talk("What would you like me to write?")
                note_text = rec_audio()
                note(note_text)
                talk("I have taken a note.")
            
            elif "joke" in text.lower():
                joke = pyjokes.get_joke()
                talk(joke)

            elif "take a screenshot" in text.lower():
                talk("Taking screenshot")
                take_screenshot()
            
            elif "show me my screenshots" in text.lower():
                talk("Here are your screenshots")
                path_to_open = r"[PUT YOUR SCREENSHOTS DIRECTORY]" ------------------------------------------- PUT YOUR SCREENSHOTS DIRECTORY IN THERE ------------------------------------------------------------
                subprocess.Popen(["explorer", path_to_open])
            
            elif "stop" in text.lower():
                talk("Jarvis deactivated")
                break
            
            respnse(speak)

    except:
        continue
