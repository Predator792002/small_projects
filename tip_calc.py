print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
no_of_people = int(input("How many people to split the bill?\n"))
split_pay = (total + total * (tip / 100)) / no_of_people
print(f"Each person should pay: ${split_pay :.2f}")