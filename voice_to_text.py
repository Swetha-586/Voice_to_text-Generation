import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

def record_text():
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source, duration=0.2)

        # Listen for the user's input
        audio = r.listen(source)

        try:
            # Recognize the speech
            text = r.recognize_google(audio)
            print(f"You said: {text}")

            # If the command is "stop", break the loop
            if "stop" in text.lower():
                print("Stopping listening.")
                return "stop"  # Use this to break the loop

            return text

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

# Example usage
while True:
    text = record_text()
    if text == "stop":
        break  # Exit the loop if "stop" is said
