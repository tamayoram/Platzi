from math import sqrt

def run():
    
    # my_dict={i: i**3 for i in range(1,101) if i%3 !=0}
    # print(my_dict)

    # {key:value for value in iterable if condición}

    my_dict2={i:sqrt(i) for i in range(1,1001)}
    print(my_dict2)

if __name__=="__main__":
    run()