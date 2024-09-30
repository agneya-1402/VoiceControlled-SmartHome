import speech_recognition as sr
import pyttsx3
import serial
import time

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set up the serial connection to Arduino
arduino = serial.Serial('/dev/cu.usbmodem1101', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return ""

def send_command(command):
    arduino.write(command.encode())
    time.sleep(0.1)
    response = arduino.readline().decode().strip()
    print(f"Arduino response: {response}")

def main():
    speak("Welcome to your voice-controlled smart home.")
    
    while True:
        command = listen()
        
        if "light on" in command:
            send_command("LED_ON")
            speak("Light turned on.")
        elif "light off" in command:
            send_command("LED_OFF")
            speak("Light turned off.")
        elif "fan on" in command:
            send_command("MOTOR_ON")
            speak("Fan turned on.")
        elif "fan off" in command:
            send_command("MOTOR_OFF")
            speak("Fan turned off.")
        elif "door open" in command:
            send_command("SERVO_LEFT")
            speak("Door Opened")
        elif "door close" in command:
            send_command("SERVO_RIGHT")
            speak("Door Closed")
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()