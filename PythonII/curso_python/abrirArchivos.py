def read():
    numbers=[]
    with open("./archivos/numbers.txt","r",encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names=["Facundo","Miguel","Antonio","Pablo"]

    with open("./archivos/names.txt","w",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')
    
    # si se deja la "w" se sobreescribe, si lo que se quiere es ir agregando cada cambio se debe pone "a"




def run():
    write()

if __name__=='__main__':
    run()

