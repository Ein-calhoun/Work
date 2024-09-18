# Ask the user for their age
age = int(input("Enter your age: "))

freeage = 3
kidage = 12
adultage = 64
seniorage = 65
freeprice = 0
kidprice = 10
adultprice = 20
seniorprice = 12
studentprice = 15


if age <= freeage:
    price = freeprice
elif age >= freeage and age <= kidage:
    price = kidprice
elif age > kidage and age <= adultage:
    price = adultprice
else:   
    price = seniorprice
if price > studentprice:
    student = input("are you a student ")
    if student == "y":
        price = studentprice

print(f"The ticket price is ${price}.")
