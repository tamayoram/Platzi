nombre=input("Cuál es tu nombre?: ")

nombre=nombre.upper() # todas las letras en mayusculas
print(nombre)

nombre=nombre.capitalize() # la primera letra en mayuscula
print(nombre)

nombre=nombre.strip() # Elimina espacios innecesarios al inicio o al final de la palabra
print(nombre)

nombre=nombre.lower() # Todas las letras en minuscula
print(nombre)

nombre=nombre.replace("o","h") # Reemplazar letras
print(nombre)

print(nombre[0]) # Retorna el primer caracter del nombre
print(nombre[1]) # Retorna el segundo caracter del nombre

print(len(nombre)) # Cantidad de caracteres

