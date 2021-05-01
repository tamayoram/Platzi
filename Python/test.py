# numero1=input("Escribe un número: ")
# numero1=int(numero1)

# print(numero1)

# numero2=input("Escribe un número: ")
# numero2=int(numero2)
# print (numero2)

# print(numero1+numero2)

# es_estudiante=True
# trabaja=False
# print(es_estudiante and trabaja)
# print(es_estudiante or trabaja)

# menu="""
# Bienvenido al conversor de monedas 😉

# 1- Pesos colombianos
# 2- Pesos argentinos
# 3- Pesos mexicanos

# Elige una opción:  """

# opcion=input(menu)

# if opcion=="1":
    
#     pesos=input("Ingresa la cantidad de pesos que tienes: ")
#     pesos=float(pesos)
#     valor_dolar=3875
#     dolares=pesos/valor_dolar
#     dolares=round(dolares,2)
#     dolares=str(dolares)
#     print("La cantidad de dolares que tienes es "+dolares)
    
# elif opcion=="2":

#     pesos=input("Ingresa la cantidad de pesos que tienes: ")
#     pesos=float(pesos)
#     valor_dolar=65
#     dolares=pesos/valor_dolar
#     dolares=round(dolares,2)
#     dolares=str(dolares)
#     print("La cantidad de dolares que tienes es "+dolares)
    
# elif opcion =="3":
    
#     pesos=input("Ingresa la cantidad de pesos que tienes: ")
#     pesos=float(pesos)
#     valor_dolar=24
#     dolares=pesos/valor_dolar
#     dolares=round(dolares,2)
#     dolares=str(dolares)
#     print("La cantidad de dolares que tienes es "+dolares)

# else:
#     print("Ingresa una opción correcta")


def cambioMoneda(valorDolar):

    pesos=input("Ingresa la cantidad de pesos que tienes: ")
    pesos=float(pesos)
    valor_dolar=valorDolar
    dolares=pesos/valor_dolar
    dolares=round(dolares,2)
    dolares=str(dolares)
    print("La cantidad de dolares que tienes es "+dolares)


menu="""
Bienvenido al conversor de monedas 😉

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción:  """

opcion=input(menu)

if opcion=="1":
    cambioMoneda(3875)
    
elif opcion=="2":
    cambioMoneda(65)
    
elif opcion =="3":
    cambioMoneda(24)

else:
    print("Ingresa una opción correcta")








