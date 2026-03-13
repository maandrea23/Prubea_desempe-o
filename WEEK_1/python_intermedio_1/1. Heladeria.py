print("-"*36)
print("Ice Cream Shop")

vainilla = 0
chocolate = 0
strawberry = 0

for i in range(5):
    print("Vainilla")
    print("Chocolate")
    print("Strawberry")
    sabor = input("What ice cream do you want?: ")
    if sabor.lower() == "vainilla":
        vainilla += 1
    elif sabor.lower() == "chocolate":
        chocolate += 1
    elif sabor.lower() == "strawberry":
        strawberry += 1
    else:
        print("Sabor no disponible")
    
    if vainilla > chocolate and vainilla > strawberry:
     print("El sabor mas pedido es Vainilla")
    elif chocolate > vainilla and chocolate > strawberry:
        print("El sabor mas pedido es Chocolate")
    elif strawberry > vainilla and strawberry > chocolate:
        print("El sabor mas pedido es Strawberry")

print("vainilla:", vainilla)
print("chocolate:", chocolate)
print("strawberry:", strawberry)
