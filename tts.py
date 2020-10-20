from gtts import gTTS 

def tts(input, output):
    language = 'en'
    input_string = ' '.join(input)
    output_string = ' '.join(output)

    input_aud = gTTS(text=input_string, lang=language, slow=False) 
    output_aud = gTTS(text=output_string, lang=language, slow=False) 

    input_aud.save("")
    output_aud.save("")