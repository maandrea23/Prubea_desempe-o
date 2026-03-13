print("CoffeShop")


print("1. Coffe: $ 4.000")
print("2. Tea: $ 3.500")
print("3. Juice: $ 5.000")

drink = int (input("Enter the drink number: "))
quantity = int (input("How many drinks do you want?: "))


if drink == 1 and quantity > 0:
    total = 4000 * quantity
    print("You have to pay: $", total)
elif drink == 2 and quantity > 0:
    total = 3500 * quantity
    print("You have to pay: $", total)
elif drink == 3 and quantity > 0:      
    total = 5000 * quantity
    print("You have to pay: $", total)
else:
    print("Invalid option or invalid quantity")