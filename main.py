import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello I am Mehooly, your assistant")
engine.say("How can I help you?")
engine.runAndWait()
print("Hello I am Mehuly, your assistant")
print("How can I help you?")

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower();
            # if 'mehuly' in command:
            #   command=command.replace('mehuly','')
            #  print(command)
            print(command)
    except:
        pass
    return command


def run_mehuly():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('>>Playing: ' + song)
        # print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  # '%H:%M' for 24 hour format
        print(time)
        talk('>>Current time is ' + time)
    elif 'search for' in command:
        person = command.replace('search for', '')
        info = wikipedia.summary(person, 3)
        print(">>"+info)
        talk(info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(">>"+info)
        talk(info)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 3)
        print(">>"+info)
        talk(info)
    #elif 'chup lag jaaye' in command:
     #   print("Tell me something new, you disgusting piece of shit")
      #  talk("Tell me something new, you disgusting piece of shit")
    elif 'date' in command:
        print(">>I'd rather die, than dating you")
        talk("I'd rather die, than dating you")
    elif 'boyfriend' in command or 'girlfriend' in command:
        print(">>Come out of your dream world honey")
        talk("Come out of your dream world, honey")
    elif 'inspire me' in command or 'i feel so weak' in command or ' i am not good enough' in command:
        print(">>YOU ARE STRONG. YOU ARE LOVELY. YOU ARE BEAUTIFUL. LET NO ONE DEFINE YOUR HOPES AND LIFE. FIGHT BACK AND MAKE IT WORTH IT")
        print(">>DO WHAT MAKES YOU HAPPY. FLY. AND NEVER LOOK BACK. DO WHAT YOU NEED TO, TO BE HAPPY.")
        talk("YOU ARE STRONG. YOU ARE LOVELY. YOU ARE BEAUTIFUL. LET NO ONE DEFINE YOUR HOPES AND LIFE. FIGHT BACK AND MAKE it WORTH it")
        talk("DO WHAT MAKES YOU HAPPY. FLY. AND NEVER LOOK BACK. DO WHAT YOU NEED TO, TO BE HAPPY.")
    elif 'joke' in command:
        j = pyjokes.get_joke()
        print(j)
        talk(j)
    elif 'how are you'in command or 'whats up' in command:
        print(">>I was doing great, before you asked for my assistance. Now i think I have a headache.")
        talk("I was doing great, before you asked for my assistance. Now i think I have a headache.")
    else:
        print(">>Sorry, my engine couldn't get you. Kindly say it again in simpler words")
        talk("Sorry, my engine couldn't get you. Kindly say it again in simpler words")


while True:
    run_mehuly()
