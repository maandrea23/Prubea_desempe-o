print (" parking ")
hours = int (input("How many hours did you stay ?: "))
if hours < 2:
    print("You should pay $ 5.000")
elif hours >= 2:
    total = 5000 + (hours - 1) * 3000
    print("You should pay $", total)