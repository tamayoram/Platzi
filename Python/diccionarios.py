def run():
    miDiccionario={
        'llave1':1,
        'llave2':2,
        'llave3':3,
        'llave4':4

    }

    print(miDiccionario)

    # print(miDiccionario['llave1'])
    # print(miDiccionario['llave2'])
    # print(miDiccionario['llave3'])
    # print(miDiccionario['llave4'])

    for llave in miDiccionario.keys(): # para ver el nombre de las llaves del diccionario
        print(llave)

    for llave in miDiccionario.values(): # para ver los valores de las llaves del diccionario
        print(llave)

    for llave in miDiccionario.items(): # para ver tanto la llave como su valor
        print(llave)

    for llave,valor in miDiccionario.items(): # para ver el nombre de las llaves del diccionario
        print("La "+llave+" tiene el número "+str(valor))

if __name__=='__main__':
    run()

