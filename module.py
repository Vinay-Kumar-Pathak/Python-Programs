import pyjokes
jokes= pyjokes.get_joke()
print(jokes)

import random
x= random.randint(1,100)
print(x)


import pyttsx3

sound=pyttsx3.init()
sound.say("VINAY you are best")
sound.runAndWait()