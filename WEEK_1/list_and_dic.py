print("-"*36)

print("1. Agregar y eliminar elementos de una lista") 

list = ["manzana", "pera", "naranja", "uva", "fresa"]
list.append("kiwi")
print(list)
list.insert(1, "melon")
print(list)
list.remove("uva")
print(list)
list.pop()
print(list)

print("-"*36)
print("-"*36)

print("2. Ordenar y contar elementos en una lista")

numeros = [4, 2, 7, 2, 9, 1, 2]
numeros.sort()
print(f"Lista usando sort: {numeros}")
numeros.reverse()
print(numeros)
numeros.count(2)
print(numeros.count(2))
numeros.index(7)
print(numeros.index(7))

print("-"*36)
print("-"*36)

print("3. Copiar y extender listas")

a = [1, 2, 3]
b = [4, 5, 6]
c = a.copy()
print(c)
c.extend(b)
print(c)

print("-"*36)
print("-"*36)

print("4. Vaciar una lista")

student = ["Andrea", "Camila", "Maria", "Luis"]
print(student)
student.clear()
print(student)

print("-"*36)
print("-"*36)

print("5. Crear y consultar un diccionario")

persona = {
    "nombre": "Andrea",
    "edad": 25,
    "ciudad": "Barranquilla"
}
print(persona["nombre"])

persona.get("edad")
print(persona.get("edad"))

persona.get("telefono","No se encontró el teléfono")
print(persona.get("telefono","No se encontró el teléfono"))     

print("-"*36)
print("-"*36)

print("6. Agregar, actualizar y eliminar claves en un diccionario")

persona = {
    "nombre": "Andrea",
    "edad": 25,
    "ciudad": "Barranquilla",
    "profesion": "Ingeniera"
}
persona["edad"] = 26
print(persona)
ciudad = persona.pop("ciudad")
print("La ciudad que fue eliminado es: ",ciudad)
print(persona)

print("-"*36)
print("-"*36)

print("7. Recorrer claves, valores y elementos")

productos = {
    "pan": 1500,
    "leche": 3200,
    "huevos": 9000
}
print(productos.keys())
print(productos.values())
print(productos.items())

print("-"*36)
print("-"*36)

print("# 8. Unir diccionarios y actualizar datos")
d1 = {"a": 1, "b": 2}
d2 = {"b": 5, "c": 3}

d1.update(d2)
print(d1)

print("-"*36)
print("-"*36)

print("9. Eliminar el último par clave-valor")

cabello = {
    "peinilla": 1500,
    "shampoo": 3200,
    "acondicionador": 9000
}
delete = cabello.popitem()
print("se elimino:", delete)
print(cabello)

print("-"*36)
print("-"*36)

print("10. Combinar listas y diccionarios")
estudiantes = [
    {"nombre": "Luis", "nota": 4.5},
    {"nombre": "Marta", "nota": 3.8},
    {"nombre": "Carlos", "nota": 4.2}
]
for i in range(len(estudiantes)):
        print(f"Nombre: {estudiantes[i]['nombre']}, Nota: {estudiantes[i]['nota']}")
        average = estudiantes[i]['nota']
        if average >= 4.0:
            print("El estudiante aprobó")
        else: 
             print("El estudiante reprobó")
        average = average + estudiantes[i]['nota']
print("El promedio de la clase es: ", average/len(estudiantes))

