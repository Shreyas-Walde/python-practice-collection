import os
if __name__ == '__main__':
    print("Hey There,Welcome to t")
    while True: 
        text2speak = input("Welcome to text2speech (or 'quit' to exit): ")
        if text2speak.lower() == "quit":
            os.system("say 'bye bye friend'")
            break
    command = f"say {text2speak}"
    os.system(command)



