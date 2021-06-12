def divisor(num):
    try:
        if num < 0:
            raise ValueError("Debe ser positvo")
        divisors =[i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        
        

def run():
    try: 
        num = int(input(f'Ingresa un número: '))      
        print(divisor(num))
        print("termino mi programa")
    except ValueError:
        print("Debe ser un número")
    
if __name__ =='__main__':
    run()