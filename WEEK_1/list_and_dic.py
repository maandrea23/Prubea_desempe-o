# 1. Agregar y eliminar elementos de una lista
list = ["manzana", "pera", "naranja", "uva", "fresa"]
list.append("kiwi")
print(list)
list.insert(1, "melon")
print(list)
list.remove("uva")
print(list)
list.pop()
print(list)

# 2. Ordenar y contar elementos en una lista
numeros = [4, 2, 7, 2, 9, 1, 2]
numeros.sort()
print(f"Lista usando sort: {numeros}")
numeros.reverse()
print(numeros)
numeros.count(2)
print(numeros.count(2))
numeros.index(7)
print(numeros.index(7))

# 3. Copiar y extender listas
a = [1, 2, 3]
b = [4, 5, 6]