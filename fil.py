import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty('rate',125)
    engine.runAndWait()


with open(' The Hunger Games.txt','r') as f:
    while True:
        curr_lin = f.readline()
        speak(curr_lin)

# engine = pyttsx3.init()
# engine.say('hello world well come again')
# engine.setProperty('rate',150)
# engine.setProperty('voice','english-us')
# engine.runAndWait()




        
 
    
        