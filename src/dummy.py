import time
from furhat_controller import FurhatController

furhat = FurhatController()

def speak_1():
    while True:
        furhat.say_text(text="Hello, my name is Furhat.")
        time.sleep(2)
        
def speak_2():
    while True:
        furhat.say_url(url="https://www2.cs.uic.edu/~i101/SoundFiles/gettysburg10.wav", lipsync=True)
        time.sleep(2)    