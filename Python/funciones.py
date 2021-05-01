# def imprimirMensaje():
#     print("Estoy aprendiendo a usar funciones!")

# imprimirMensaje()
# imprimirMensaje()
# imprimirMensaje()

def conversacion(mensaje):
    print("Hola")
    print("Cómo estas?")
    print(mensaje)
    print ("Chao")


opcion=input("Elige una opción (1,2,3): ")

if opcion=="1":
    conversacion("Elegista la opción 1")
elif opcion=="2":
    conversacion("Elegista la opción 2")
elif opcion=="3":
    conversacion("Elegista la opción 3")
else:
    print("Elige una opción correcta")

