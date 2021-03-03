from gtts import gTTS
import speech_recognition as sr
import os
import playsound
from datetime import datetime
import webbrowser
import time

keeprunning = True

WAKING = "HEY GOOGLE"
def chec(cond, tex):
    if cond in tex:
        return True
    else:
        return False

def speak(text):
    speaker = gTTS(text = text, lang = "en")
    speaker.save("Voice.mp3")
    playsound.playsound("voice.mp3")
    os.remove("Voice.mp3")
def cleanify(text, wtremove, wtremove2=""):
    try:
        text = text.replace(wtremove, " ")
    except:
        if not wtremove2 == "":
            text = text.replace(wtremove2, " ")
    return text

#Main controlling part here(Oof!)
def Control(comnd):
    if chec("SEARCH", comnd) or chec("GOOGLE", comnd):
        comnd = cleanify(comnd, "SEARCH", "GOOGLE")
        webbrowser.open(f"https://google.com/search?q={comnd.lower()}")

    elif chec("WHO ARE YOU", comnd):
        speak("I am your virtual assistant, google")
        keepcontrol()

    elif chec("TIME", comnd):
        t = datetime.now()
        t = time.strptime(t.strftime("%H:%S"), "%H:%M")
        tt = time.strftime( "%I:%M %p", t )
        speak(f"The current time is {tt}")
    elif chec("NOTE", comnd) or chec("REMEMBER", comnd) or chec("JOT", comnd):
        try:
            text = comnd.replace("NOTE")
        except:
            try:
                text = text.replace("REMEMBER")
            except:
                text = text.replace("JOT")
        try:
            with open("This_File_Name_Is_Very_Big_Because_I_dont_Want_to_overwrite_anyother_files_so_forgive_me_plz.txt", "rt") as file:
                previous = file.read()
        except:
            with open("This_File_Name_Is_Very_Big_Because_I_dont_want_to_overwrite_any_other_files_so_forgive_me_plz.txt", "wt") as file:
                ttw = f"""
                    •{text.lower()}
                """
                file.write(previous + ttw)
                previous = ""

        with open("Notes.txt", "wt") as file:
            ttw = previous + "  •" + text

            file.write(ttw)
        speak("Got it! I noted it down")

    elif chec("OPEN", comnd):
        speak("Which website do you want to open?")
        web = listen()
        print(web)
        if web == "":
            web = listen()
        else:
            if "https://" in web:

                webbrowser.open(web.lower())
            else:
                web = "https://" + web
                webbrowser.open(web.lower())
        keepcontrol()
        
#Main controlling part ends

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        listen = r.listen(source)
        try:
            text = r.recognize_google(listen)
            return text.upper()
        except Exception as e:
            if not e == "":
                return ""
                keepcontrol()
            else:
                speak("Sorry we couldnt catch that, please try again")
                keepcontrol()

def keepcontrol():
    while keeprunning:
        text = listen()
        if not text == None:
            if text.count(WAKING) == 1:
                speak("I am listening..")
                text = listen()
                if not text == None and not text == "":
                    Control(text)
                else:
                    speak("Sorry i did not get that. Try again in a few seconds")
                    keepcontrol()
            elif chec("QUIT", text):
                exit()
            elif chec("", text):
                keepcontrol()
            else:
                speak("Sorry we didnt get that right. Please try again.")
                        
                
        
speak("I am booting up...")
keepcontrol()
