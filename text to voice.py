import gtts
from playsound import playsound

text = input("what do you want me read for you :")
t1 = gtts.gTTS(text)

# save the audio file
t1.save("welcome.mp3")

# play the audio file
playsound("welcome.mp3")

