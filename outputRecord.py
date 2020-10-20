import speech_recognition as sr


def google_record(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    r = recognizer
    mic = microphone

    with mic as source:
        print("recording...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("recording finished")

    try:
        response["transcription"] = r.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
    
    if(response["transcription"] != None):
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
        output = list(response["transcription"].split(" "))
        return output
    return response["error"]
    

#r = sr.Recognizer()
#mic = sr.Microphone()
#output = google_record(r,mic)
#print(output)
#print(len(output))