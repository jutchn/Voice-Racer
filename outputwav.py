import speech_recognition as sr
import os

def google_wav(recognizer, wav):
    if isinstance(wav, str) == False or os.path.isfile(wav) == False:
        raise TypeError("invalid input")
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    

    r = recognizer
    src = sr.AudioFile(wav)
    
    with src as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.record(source)

    text = r.recognize_google(audio)
    text = text.lower()
    output = list(text.split(" "))

    #print(output)
    #print(len(output))
    return output

#r = sr.Recognizer()
#print(google_wav(r, "harvard1m.wav"))