def palindromo(palabra):
 palabra=palabra.strip()
 palabra=palabra.replace(" ","")
 palabra=palabra.lower()
 palabraInvertida=palabra[::-1]
 if palabra==palabraInvertida:
     return True
 else:
     return False


def run(): # Función estandar para correr el programa
    palabra=input("Escribe una palabra: ")
    esPalindromo= palindromo(palabra)
    
    if esPalindromo==True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__=="__main__": #Punto de entrada estandar, es decir Python empieza a correr todo el código hacia abajo
    run()

