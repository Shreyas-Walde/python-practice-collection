try:
    a = int(input("Enter a number: "))
    print(a*3)
except Exception as e: 
    print("An error occured", e)