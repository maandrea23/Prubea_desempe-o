print("GYM")

age = int (input("Enter your age:  "))
if age < 13:
    print ("Cannot enter to the gym")
elif 13 <= age <= 17:
    print ("Gain Access, Junior class")
elif 18 <= age <= 59:
    print ("Gain Access, General class")
else:
    print ("Gain Access, Senior class")