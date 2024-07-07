# ticket_price = 100
# total_price = 0
# passenger_count = 0

# while passenger_count < 5:
#     age = int(input(f"Enter the age of passenger {passenger_count + 1}: "))

#     if age < 3:
#         print("Ticket is free for children under 3 years old.")
#         # Skip further processing for this passenger
#         passenger_count += 1
#         continue

#     total_price += ticket_price

#     passenger_count += 1

# print(f"\nThe total price for the tickets is: ${total_price}")


total_price = 0
passenger_count = 0
while True:  # Use a loop that continues indefinitely
    age = int(input("Enter passenger's age (or -1 to finish): "))

    if age < 0:  # Break the loop if age is negative
        break

    if age <= 3:
        print("Ticket is free for children under 3.")
        continue  # Proceed to the next passenger without adding to the price

    total_price += 100
    passenger_count += 1

    if passenger_count == 5:  # Break the loop after 5 passengers
        break

print("Total price for the tickets: $", total_price)

