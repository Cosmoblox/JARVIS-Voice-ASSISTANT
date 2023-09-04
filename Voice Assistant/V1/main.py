import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime 
import wikipedia
import os
import pyautogui

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def listen_for_wake_word():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recorded_audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recorded_audio, language='en-US')
        return text.lower()
    except Exception as ex:
        print(ex)
        return ""

def speak(message):
    engine.say(message)
    engine.runAndWait()

def main():
    while True: 
        wake_word = "jarvis"
        detected_text = listen_for_wake_word()
        if detected_text.startswith(wake_word):
            speak("Jarvis activated.")
            while True:
                user_input = listen_for_command()
                if user_input:
                    print(f"You said: {user_input}")

                browser_key_words = ["open browser", "open chrome", "open opera"]
                mail_key_words = ["open mail", 'mail', 'gmail', 'email', 'inbox']
                greeting_key_words = ["hello", "good morning", "good evning", "good night", "hey", "hi"]
                
                # Process the remaining words for commands
                if any(keyword in user_input for keyword in browser_key_words):
                    print("Opened Browser")
                    speak("Opened Browser")
                    webbrowser.open('https://google.com/')

                elif "wikipedia" in user_input:
                    speak("Searching wikipedia...")
                    user_input = user_input.replace("wikipedia", "")
                    results = wikipedia.summary(user_input,sentences =5)
                    speak("According to wikipedia")
                    try:
                        print("\n", results, "\n")
                        speak(results)
                    except Exception as e:
                        speak("Could not find a page on wikipedia for requested topic.")
                        return

                elif any(keyword in user_input for keyword in mail_key_words):
                    speak("Here is your email inbox.")
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

                elif any(keyword in user_input for keyword in greeting_key_words):
                    hour = int(datetime.datetime.now().hour)
                    if hour>= 0 and hour<12:
                        speak("Good Morning !")
                    elif hour>= 12 and hour<18:
                        speak("Good Afternoon !") 
                    else:
                        speak("Good Evening !") 
            
                
                elif 'open youtube' in user_input:
                    speak("Here you go to Youtube\n")
                    webbrowser.open("https://www.youtube.com/")

                elif 'open notepad' in user_input:
                    speak('opening notepad for you.......')
                    path = ("c:\\windows\\system32\\notepad.exe")
                    os.startfile(path)
                elif 'close notepad' in user_input:
                    speak('closing notepad wait.....')
                    os.system('c:\\windows\\system32\\taskkill.exe /F /IM notepad.exe')
                
                elif "type" in user_input:
                    user_input = user_input.replace("type","")
                    speak("Typing..")
                    pyautogui.typewrite(user_input, interval=0.1)

                elif 'time' in user_input:
                    current_time = datetime.datetime.now().strftime("%I:%M %p")
                    print(f"It's {current_time}")
                    speak(f"It's {current_time}")


                elif "stop" in user_input:
                    print("Jarvis deactivated")
                    speak("Jarvis deactivated.")
                    return

def listen_for_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recorded_audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recorded_audio, language='en-US')
        return text.lower()
    except Exception as ex:
        print(ex)
        return ""

if __name__ == "__main__":
    main()
