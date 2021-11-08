import pyttsx3
engine = pyttsx3.init()
newVoiceRate = 120
engine.setProperty('rate',newVoiceRate)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


for x in range(4):
    pyttsx3.speak("Hey Welcome to this world  ")
    
    engine.runAndWait()
engine.stop()
