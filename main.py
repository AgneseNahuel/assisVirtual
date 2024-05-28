import speech_recognition as sr
import pyttsx3
import pywhatkit

name = 'gordo'
engine =pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id) #Elijo la voz

def talk(text):
    engine.say(text)
    engine.runAndWait()

def main():
    reconocer = sr.Recognizer()

    try:
        with sr.Microphone() as mic:
            print("Por favor, hable ahora...")
            reconocer.adjust_for_ambient_noise(mic)
            voz = reconocer.listen(mic)
            print("Procesando...")

            # Intenta reconocer la voz usando Google Web Speech API
            try:
                texto = reconocer.recognize_google(voz, language="es-ES")
                texto = texto.lower()
                if name in texto:
                    texto = texto.replace(name, '')
                    talk(texto)
            except sr.UnknownValueError:
                print("No se pudo entender el audio")
            except sr.RequestError as e:
                print(f"No se pudo solicitar los resultados del servicio de reconocimiento; {e}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return texto

def run():
    texto = main()
    if 'reproduce' in texto:
        music = texto.replace('reproduce', '')
        talk('reproduciendo' + music)
        pywhatkit.playonyt(music)

run()
