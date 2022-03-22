from gtts import gTTS


def text_to_speech(fname="", final_text=""):
    tts = gTTS(final_text)
    tts.save(fname+".mp3")

    return(fname+".mp3")
