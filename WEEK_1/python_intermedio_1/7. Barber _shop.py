print ("Barber shop")

hour = int (input("Enter the time you arrive, between 0 to 23: "))

match hour:
    case hour if 6 <= hour <= 11:
        print("morning")
    case hour if 12 <= hour <= 17:
        print ("afternoon")
    case hour if 18 <= hour <= 22:
        print ("night")
    case _: 
        print("out of the time")