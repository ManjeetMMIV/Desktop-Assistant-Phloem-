import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def game_play():
    speak("Let's play STONE, PAPER, SCISSORS!!")
    print("LET'S PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0

    # Define possible recognized words for each choice
    stones_synonyms = ["stones", "stone", "stun", "stuns","store"]
    paper_synonyms = ["paper", "piper", "pay per", "peper", "pepper"]
    scissors_synonyms = ["scissors", "scissor", "caesar", "cisors", "seizer", "sizer"]

    while i < 5:
        choose = ("stones", "paper", "scissors")  # Tuple
        com_choose = random.choice(choose)
        print("Choose yours")
        query = takeCommand().lower()

        # Check if query matches any of the synonyms for stones
        if query in stones_synonyms:
            if com_choose == "stones":
                speak("STONES")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif com_choose == "paper":
                speak("PAPER")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("SCISSORS")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        # Check if query matches any of the synonyms for paper
        elif query in paper_synonyms:
            if com_choose == "stones":
                speak("STONES")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif com_choose == "paper":
                speak("PAPER")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("SCISSORS")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        # Check if query matches any of the synonyms for scissors
        elif query in scissors_synonyms:
            if com_choose == "stones":
                speak("STONES")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif com_choose == "paper":
                speak("PAPER")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("SCISSORS")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                
        # If the word doesn't match, print what was heard
        else:
            speak("Invalid choice, please say stones, paper, or scissors.")
            print(f"Unrecognized word: {query}")  # Debugging: print the word it heard
        i += 1

    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")
    if Me_score > Com_score:
        speak("Congratulations, You won!!")
    elif Me_score == Com_score:
        speak("MATCH TIED")
    else:
        speak("I Won")

# Example function call to play the game
#game_play()





