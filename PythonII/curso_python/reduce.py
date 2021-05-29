
from functools import reduce

my_list=[2,2,2,2,2]
all_multipled=reduce(lambda a,b:a*b,my_list)

                    #en la primera iteración a es el primer elemento de la lista y b el segundo elemento
                    # en las otras iteraciones a pasa a ser el que lleva el acumulado de la multiplicación

print(all_multipled)

