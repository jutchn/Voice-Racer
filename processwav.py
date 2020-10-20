import soundfile as sf

def duration(wav):
    f = sf.SoundFile(wav)
    return len(f) / f.samplerate

#print(duration('microphone-results.wav'))