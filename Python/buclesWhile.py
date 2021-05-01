def run():
    LIMITE=1000000 # se escribe en mayuscula para que signifique constante
    contador=0
    potencia_2=2**contador
    
    while potencia_2 < LIMITE:
        print("2 elevado a "+str(contador)+ " es igual a: "+str(potencia_2)) # str es para volver string un valor numérico
        contador+=1
        potencia_2=2**contador


if __name__=="__main__":
    run()