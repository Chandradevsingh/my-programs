import pyttsx3, speech_recognition as sr, webbrowser, datetime, pyjokes,

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print('Recognizing...')
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print('Not Understanding...')


speech_to_text()

