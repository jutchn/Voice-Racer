import speech_recognition as sr
import inputFormat as iF
import outputRecord as oR
import outputwav as ow
import accuracy as acc
import processwav as pw

sampleText = "The birch canoe slid on the smooth planks.\
Glue the sheet to the dark blue background.\
It's easy to tell the depth of a well.\
These days a chicken leg is a rare dish.\
Rice is often served in round bowls.\
The juice of lemons makes fine punch.\
The box was thrown beside the parked truck.\
The hogs were fed chopped corn and garbage.\
Four hours of steady work faced us.\
Large size in stockings is hard to sell."


input = iF.readTextInput(sampleText)
numWords = len(input)

r = sr.Recognizer()
mic = sr.Microphone()

output = oR.google_record(r,mic)
#process wav file - microphone-results.wav

#output = ow.google_wav(r, 'harvard1m.wav')

outputwav = 'microphone-results.wav'

#pw.trim(outputwav)

duration_sec = pw.duration(outputwav)

duration_min = duration_sec/60
wpm = numWords/duration_min
wps = numWords/duration_sec

print(acc.levenshtein_accuracy(input, output,False))
print(wpm)

