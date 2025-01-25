import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from openai import OpenAI

r=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiprocess(commond):
        client = OpenAI(api_key="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")
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant named jarvis."},
            {
                "role": "user",
                "content": commond
            }
        ]
    )

        return (completion.choices[0].message.content)


def processcommond(c):
    if "open google" in c.lower():
        webbrowser.open('https://google.com')
    elif "open instagram" in c.lower():
        webbrowser.open('https://instagram.com')
    elif "open youtube" in c.lower():
        webbrowser.open('https://youtube.com')
    elif "open chrome" in c.lower():
        webbrowser.open('https://googlechrome.com')
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "open chat" in c.lower():
        webbrowser.open('https://chatgpt.com')
    elif "open linkedin" in c.lower():
        webbrowser.open('https://linkedin.com')
    else:
        #let openai handel request
        output=aiprocess(c)
        speak(output)
        pass
        
    

if __name__=="__main__":
    speak('Waking up sir.....')
    # listen for the word jarvis
    while True:
        r = sr.Recognizer()
    
        print('recognizing...')
        try:
            with sr.Microphone() as source:
             print("Listening")
             audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes sir")
                #listen for commond
                with sr.Microphone() as source:
                    print("Jarvis active")
                    audio = r.listen(source)
                    commond=r.recognize_google(audio)

                    processcommond(commond)



        except Exception as e:
            print("Error; {0}".format(e))
