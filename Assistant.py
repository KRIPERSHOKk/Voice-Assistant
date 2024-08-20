import os
import speech_recognition as sr
import Voice
import Ai

recognizer = sr.Recognizer()

Ai.main('Ты голосовой ассистент, который должен отвечать на вопросы людей. Твое имя - Морковь. Твой создатель никита калашников.')

def speak(text):
    print(text)
    Voice.say(text)


def listen():
   with sr.Microphone() as source:
       print("Слушаю...")
       recognizer.adjust_for_ambient_noise(source)
       audio = recognizer.listen(source)

   try:
       print("Распознавание...")
       query = recognizer.recognize_google(audio, language='ru-RU')
       print(f"Вы сказали: {query}")
       return query
   except sr.UnknownValueError:
       return ""
   except sr.RequestError as e:
       speak(f"Ошибка сервиса распознавания речи; {e}")
       return ""

def main():
    while True:
        query = listen().lower()
        if query != "":
            if 'выход' in query:
                speak("До свидания!")
                break
            elif 'открой браузер' in query:
                os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
            else:
                speak(Ai.main(query))
        else:
            pass

if __name__ == "__main__":
   main()