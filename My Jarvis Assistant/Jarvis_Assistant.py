import pyttsx3 
import pywhatkit
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os 
import smtplib
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from pyautogui import click
from googletrans import Translator
from pywikihow import WikiHow,search_wikihow
from pytube import YouTube
from pyautogui import hotkey
import pyperclip
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    engine.setProperty('voice', voices[0].id)
    speak('Jarvis is Starting Sir')
    engine.setProperty('voice', voices[1].id)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("How could i help you sir.")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,7)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e) 
    
        #speak('sorry sir Say that again please... ')   
        print("Say that again please...")  
        return "None"
    return query


def DownloadYoutubeVideo():

    speak('sure sir')
    
    sleep(1)

    click(x=718, y=68)

    hotkey('ctrl','c')

    value = pyperclip.paste()

    press_and_release('esc')
    press_and_release('esc')

    Link = str(value)

    speak('download process started sir')

    def DownloadVideo(link):
    
     url = YouTube(link)

     video = url.streams.get_highest_resolution(  )

     speak('download process Done sir')

     video.download('D:\\Jarvis Video\\')

    DownloadVideo(Link)

    speak('Sir I have downloaded this video')
    speak('You can check this video in E drive')

    os.startfile('D:\\Jarvis Video\\')


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        ### Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('sure sir')

        elif 'download this youtube video' in query:
            DownloadYoutubeVideo()

        elif 'download this video' in query:

            DownloadYoutubeVideo()

        elif 'open google' in query:

            speak('sure sir')
            webbrowser.open("google.com")

############### Controlling Browser and Window  #########################

        elif 'open new tab' in query:

            speak('sure sir')
            press_and_release('ctrl + t')

        elif 'open lock' in query:
            speak("ok sir")
            press_and_release('space bar')

        elif 'up volume' in query:
            press_and_release('up')

        elif 'half volume' in query:
            press_and_release('up')

        elif 'down volume' in query:
            press_and_release('down')

        elif 'volume up' in query:
            press_and_release('up')

        elif 'volume half' in query:
            press_and_release('up')

        elif 'volume down' in query:
            press_and_release('down')
        
        elif 'open download' in query:

            speak('sure sir')
            press_and_release('ctrl + j')

        elif 'open incognito tab' in query:

            speak('sure sir')
            press_and_release('ctrl + shift + n')

        elif 'close tab' in query:

            speak('sure sir')
            press_and_release('ctrl + w')

        elif 'closed tab' in query:

            speak('sure sir')

            press_and_release('ctrl + w')

         
        elif 'close this video' in query:

            speak('sure sir')

            press_and_release('alt + f4')

        elif 'close this window' in query:

            speak('sure sir')

            press_and_release('alt + f4')

        elif 'close window' in query:

            speak('sure sir')

            press_and_release('alt + f4')

        elif 'minimize this video' in query:

            speak('sure sir')

            press_and_release('esc')
            click(x=1768, y=11)

        elif 'minimize this window' in query:

            speak('sure sir')

            press_and_release('esc')
            click(x=1768, y=11)

        elif 'minimize it' in query:

            speak('sure sir')

            press_and_release('esc')
            click(x=1768, y=11)

        elif 'minimise this video' in query:

            speak('sure sir')

            press_and_release('esc')
            click(x=1768, y=11)

        elif 'minimise this window' in query:

            speak('sure sir')

            press_and_release('esc')
            click(x=1768, y=11)

        elif 'minimise it' in query:

            speak('sure sir')

            press_and_release('esc')
            click(x=1768, y=11)


        elif 'close it' in query:

            speak('sure sir')

            press_and_release('alt + f4')
            
        
       
        elif 'search on youtube' in query:
            speak('What to search sir')
            lis = takeCommand()
            content = "https://www.youtube.com/results?search_query=" + lis
            speak('sure sir.')
            webbrowser.open(content)
            pywhatkit.playonyt(lis)
            sleep(3)
            press_and_release('f')


############# Switching Window   ##############################

# More complex to make my jarvis hear and understand.due to audio quality and depends upon the way of speaking words.

        elif 'switch tab' in query:
            speak('sure sir.')
            speak("Which tab sir")
            tab = takeCommand()
            
           
            if 'one' in tab:
               
               press_and_release('ctrl + 1')

            elif 'second' in tab:
               
               press_and_release('ctrl + 2')

            if 'third' in tab:
               
               press_and_release('ctrl + 3')

            if 'fourth' in tab:
               
               press_and_release('ctrl + 4')

        elif 'which tab' in query:     ## sometime my jarvis hears "which" instead of "switch". because it is only trained on voice cmd.
            speak('sure sir.')
            speak("Which tab sir")
            tab = takeCommand()
            
            Tab = tab

            if '1' in Tab:
               
               press_and_release('ctrl + 1')

            elif '2' in Tab:
               
               press_and_release('ctrl + 2')

            elif '3' in Tab:
               
               press_and_release('ctrl + 3')

            elif '4' in Tab:
               
               press_and_release('ctrl + 4')

        elif 'open histroy' in query:
            speak('sure sir.')
            press_and_release('ctrl + h')

        elif 'open new window' in query:
            speak('sure sir.')
            press_and_release('ctrl + n')

        elif 'open stackoverflow' in query:
            speak('sure sir.')
            webbrowser.open("stackoverflow.com")

##############################  For playing Video ###############################

        elif 'pause' in query:
            press_and_release('space bar')

        elif 'pos' in query:
            press_and_release('space bar')

        elif 'pose' in query:
            press_and_release('space bar')

        elif 'resume' in query:
            press_and_release('space bar')

        elif 'continue' in query:
            press_and_release('space bar')


        elif 'full screen' in query:
            press_and_release('f')

        elif 'out full screen' in query:
            press_and_release('f')

        elif 'skip' in query:
            press_and_release('l')

        elif 'mute' in query:
            press_and_release('m')

        elif 'mute video' in query:
            press_and_release('m')

        elif 'mute this video' in query:
            press_and_release('m')

        elif 'unmute' in query:
            press_and_release('m')

        elif 'unmute video' in query:
            press_and_release('m')

        elif 'unmute this video' in query:
            press_and_release('m')

        elif 'back' in query:
            press_and_release('j')

        elif 'shutdown pc' in query:
            speak("ok sir now you is ready to shutdown")
            hotkey('win','x')
            press_and_release('u')
            press_and_release('u')
            press_and_release('u')
        
## sometime my jarvis hears "bright,right" instead of "write". because it is only trained on voice cmd and depended on Audio Quality
        elif 'right' in query:
            speak('sure sir.')
            speak('What do you want to write sir')
            word = takeCommand()
            write(word)
            press_and_release('enter')

        elif 'bright' in query:
            speak('sure sir.')
            speak('What do you want to write sir')
            word = takeCommand()
            write(word)
            press_and_release('enter')

        elif 'write' in query:
            speak('sure sir.')
            speak('What do you want to write sir')
            word = takeCommand()
            write(word)
            press_and_release('enter')

        elif 'open Spider-Man movie' in query:
            speak('sure sir.')
            codePath = "E:\\Movie\\Marvel\\Spider-Man"
            os.startfile(codePath)

        elif 'search on google' in query:
            speak('ok sir.')
            webbrowser.open("https://www.google.com/")
            speak('What do you want to write sir')
            word = takeCommand()
            click(x=857, y=456)
            write(word)
            press_and_release('enter')

        elif 'open trading view' in query:
            speak('sure sir.')
            webbrowser.open("https://in.tradingview.com/chart/kcATBtdR/?symbol=NSE%3ABANKNIFTY")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'open tradingview' in query:
            speak('sure sir.')
            webbrowser.open("https://in.tradingview.com/chart/kcATBtdR/?symbol=NSE%3ABANKNIFTY")

#################################### Controlling Music Player of PC #########################

        elif 'play music' in query:
            speak('sure sir.')
            music_dir = 'F:\\Lofi Music\\Mymusic'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'pause music' in query:
            speak('sure sir.')
            press_and_release('f10')

        elif 'play next music' in query:
            speak('sure sir.')
            press_and_release('f11')

        elif 'continue music' in query:
            speak('sure sir.')
            press_and_release('f10')

        elif 'play previous music' in query:
            speak('sure sir.')
            press_and_release('f9')
########################################################################

        elif 'the time' in query:
            speak('sure sir.')
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak('sure sir.')
            codePath = "C:\Program Files\Microsoft VS Code\code.exe"
            os.startfile(codePath)

## sometime my jarvis hears "buy,by" instead of "bye". because it is only trained on voice cmd and depended on Audio Quality


        elif 'bye jarvis' in query:
            os.startfile("F:\\Jarvis Backup\\wakepu.pyw")
            exit()

        elif 'buy jarvis' in query:
            os.startfile("F:\\Jarvis Backup\\wakepu.pyw")
            exit()

        elif 'by jarvis' in query:

            os.startfile("F:\\Jarvis Backup\\wakepu.pyw")
            exit()

        elif 'exit jarvis' in query:
            speak("ok thank you sir")
            exit()

        

        