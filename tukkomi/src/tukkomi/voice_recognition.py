import speech_recognition as sr

def speech_rec():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("---------------------------------------------------------------")
        print("-- RECORDING...")
        audio = r.listen(source)
    try:
        # Google Web Speech APIで音声認識
        text = r.recognize_google(audio, language="ja-JP")
    except sr.UnknownValueError:
        #print("Error:Google Web Speech APIは音声を認識できませんでした")
        return "***"
    except sr.RequestError as e:
        #print("Error:GoogleWeb Speech APIに音声認識を要求できませんでした;"
        #    " {0}".format(e))
        return "***"
    else:
        return text

def main():
    while True:
        question = speech_rec()
        if(question != "***"):
            print(question)


if __name__ == '__main__':
    print("-- VOICE RECOGNITION --")
    main()






