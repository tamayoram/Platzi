# for contador in range(1000): # range te permite crear un vector con números desde el 0 hasta el 999
#     print(contador)

# for contador in range(1,1001): # range te permite crear un vector con números desde el 1 hasta el 1000
#     print(contador)

# for i in range(10): # tabla del 11
#     print(i*11)

### Recorriendo un string con la sentencia for

def run():
    # nombre=input("Escribe tu nombre: ")
    # for letra in nombre:
    #     print(letra)

    frase=input("Escribe una frase: ")
    for caracter in frase:
        print(caracter.upper())


if __name__=="__main__":
    run()