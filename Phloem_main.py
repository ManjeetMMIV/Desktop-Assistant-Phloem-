import pyttsx3
import speech_recognition 
import datetime
import pyautogui
import os
import speedtest
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)  # intensity

# Password
from INTRO import play_gif
play_gif        
for i in range(3):
    a = input("Enter password to access Phloem Desktop Assistant :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("Welcome!! :) Please Speak [WAKE UP]to LOAD me UP")
        break
    elif (i == 2 and a != pw):
        exit()
    elif (a != pw):
        print("Try Again")

def speak(audio):  # speak function
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 140  # so that it doesn't listen to whispers or other noise
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime")
                    break 
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is {new_pw}")
                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
                elif "click" in query:
                    pyautogui.press("super")    
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("Smile")
                    pyautogui.press("enter")
                elif "open" in query:  # EASY METHOD
                    query = query.replace("open", "")
                    query = query.replace("phloem", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 
                elif "game" in query:
                    from game import game_play
                    game_play()
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
                    download_net = wifi.download() / 1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is", download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")      
                elif "fun" in query or "doctor strange" in query:
                    time.sleep(3)
                    # Use pyautogui to navigate and open a terminal window
                    pyautogui.hotkey('win', 'r')  # Open the Run dialog
                    time.sleep(1)
                    pyautogui.write('cmd')  # Type cmd for Command Prompt
                    pyautogui.press('enter')  # Press Enter to open it
                    time.sleep(1)

                    
                    # Adjust the path as per your desktop username
                    pyautogui.write(r'cd "C:\\Users\\Manjeet Singh\\OneDrive\\Desktop\\drstrange"')  # Write the command to change directory
                    pyautogui.press('enter')  # Press Enter to execute

                    # Now run the main.py file
                    pyautogui.write('python main.py')  # Write the command to run main.py
                    pyautogui.press('enter')

                
                # Conversations hi hello wale basic questios ke liye
                elif "hello" in query or"what are you doing" in query or "what r u doing"in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("That's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "how r u" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("You are welcome, sir")              
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted")
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)    

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query or "video" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep, sir")  
                    exit()
                # Little bit real usage of file handling :)
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = rememberMessage.replace("phloem", "")
                    speak("You told me " + rememberMessage)
                    remember = open("remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt", "r")
                    speak("You told me " + remember.read())
                elif "whatsapp" in query or "Whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()    
                elif "shutdown the system" in query:
                    speak("Shutting down...")
                    os.system("shutdown /s /t 1")
                    break



                