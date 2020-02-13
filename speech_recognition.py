import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone(chunk_size=4096) as source:
        print("Speak Anything :")
        r.adjust_for_ambient_noise(source ,duration=0.5)
        audio = r.listen(source)
        print ("convert ...")
        try:
            outF = open("myOutFile.txt", "a")
            outF.write(" "+r.recognize_google(audio ,language= "ar-PS").encode('utf-8'))
            outF.write("\n")
            print(" you said " + r.recognize_google(audio ,language= "ar-PS").encode('utf-8'))
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio")
