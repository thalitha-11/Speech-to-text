import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source2:
    print("Silence pls... calibrating the background noise")
    r.adjust_for_ambient_noise(source2, duration=2)
    print("Calibrated... now speak!")

    audio2 = r.listen(source2)

    try:
        MyText = r.recognize_google(audio2)
        MyText = MyText.lower()

        print("Did you say...\n" + MyText)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Amazon service; {0}".format(e))