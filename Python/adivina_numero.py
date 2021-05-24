
import random


def run():
    aleatorio=random.randint(1,100)
    elegido=int(input('Elige un número del 1 al 100: '))

    while elegido!=aleatorio:
        if elegido < aleatorio:
            print("Busca un número mas grande")
        else:
            print ("Busca un número más pequeño")

        elegido=int(input('Elige otro número: '))
    print("Ganaste")

if __name__=='__main__':
    run()

