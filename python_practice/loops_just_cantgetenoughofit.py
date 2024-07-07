target = int(input("Enter Number between 0 and 1000: ")) # Number between 0 and 1000
# Your code here 👇
sum = 0
for number in range(1, target + 1):
    print(f" {number} + {number}")
    if number % 2 == 0:
        sum += number
print(sum)