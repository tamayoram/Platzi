def divisor(num):

        if num < 0:
            raise ValueError("Debe ser positvo")
        divisors =[i for i in range(1, num + 1) if num % i == 0]
        return divisors
   
               


def run():
    
        num = input(f'Ingresa un número: ')
        assert num.isnumeric(),"Debes ingresar un número"     
        print(divisor(int(num)))
        print("termino mi programa")
    
    
if __name__ =='__main__':
    run()