try:
    a = int(input("Enter a number: "))
    print(a/0)
except ZeroDivisionError:
    print("cannot divide by zero")
finally: 
    print("This code always executes") 