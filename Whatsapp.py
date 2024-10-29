import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Take voice command function
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

# Function to send WhatsApp message instantly
def sendMessage():
    speak("Who do you want to message?\n")
    person_choice = int(input("Person 1 - 1 \nPerson 2 - 2 \n"))
    
    if person_choice == 1:
        phone_number = "enter the phone number"
    elif person_choice == 2:
        phone_number = "enter another phone number"
    else:
        speak("Invalid choice")
        return
    
    speak("What's the message?")
    message = str(input("Enter the message: \n"))

    try:
        # Inform the user that the message is being sent
        speak("Sending your message...")
        
        # Send the message instantly using pywhatkit with an 8-second delay
        pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=8)
        
        # Confirm the message is sent
        speak("Message sent successfully!")
        print(f"Message to {phone_number} sent successfully!")
    except Exception as e:
        speak("Something went wrong. Please try again.")
        print(f"Error: {e}")

# Call the sendMessage function to run the process
#sendMessage()




        