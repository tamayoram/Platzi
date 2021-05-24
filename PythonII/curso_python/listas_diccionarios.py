def run():
    
    my_list=[1,"Hello",True,4.5]
    
    my_dic={
        "First Name":"Camilo",
        "Last Name":"Tamayo"
    }

    super_list=[

        {"First Name":"Camilo", "Last Name":"Tamayo" },
        {"First Name":"Pablo", "Last Name":"Alvarez" },
        {"First Name":"Daniel", "Last Name":"Castrillo" }

    ]

    super_dic={

        "natural nums":[1,2,3,4,5],
        "integer nums":[-1,0,1,2],
        "floating nums":[1.1,2.5,3.5]
    }

    for key,value in super_dic.items():
        print(key,"-",value)

    for element in super_list:
        for key, value in element.items():
            print(key,"-",value)

if __name__=='__main__':
    run()
    