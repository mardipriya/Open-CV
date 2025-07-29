import speech_recognition as sr

rec = sr.Recognizer()
with sr.Microphone () as source:
    print('Spake Anything...')
    audio = rec.listen(source)
    try:
        text = rec.recognize_google(audio)
        print(text)
    except Exception as e:
        print(e)
