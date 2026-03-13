print("Pet Store")
pets = ["Dog", "Cat", "Rabbit"]

messages = {
    "Dog": "dog,Give high protein food",
    "Cat": "cat,Give high protein food",
    "Rabbit": "rabbit,Give high fiber food"
}
print("Select your pet: ")

for i, pet in enumerate(pets, start=1):
    print(f"{i}. {pet}")


petselected = int(input("Enter yout pet number: "))

print(f"{messages[pets[petselected - 1]]}")


