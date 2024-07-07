import pyttsx3  # Import the text-to-speech library

engine = pyttsx3.init()  # Initialize the text-to-speech engine

while True:
    text2speak = input("Welcome to text2speech (or 'quit' to exit): ")

    if text2speak.lower() == "quit":
        engine.say("'Bye bye friend'")
        break  # Exit the loop if the user enters 'quit'

    engine.say(text2speak)  # Set the text to be spoken
    engine.runAndWait()