import speech_recognition as sr

while True:
    r=sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    print(type(sr.Microphone.list_microphone_names()))
    print(sr.Microphone.list_working_microphones())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold()
        print("say anything : ")
        audio= r.listen(source)
        try:
            text = r.recognize_google_cloud(source)
            print(text)
        except:
            print("sorry, could not recognise")

