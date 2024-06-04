data = input("What are you looking for car/bike: ")

if data == 'bike':
    bike = input("Which company bike are you looking for : ")
    if bike == 'honda':
        print('splender \n activa \n shine \n unicorn \n navi')
        model = input("select any one bike to see detail : ")
        if model == "splender":
            print("""actual-price:120000\ndiscount-price:100000
                   \n cc: 110\n manufacturer : Honda Pune""")
        elif model == "activa":
            print('''actual-price:150000\n discount-price:120000
                   \n cc:110\n manufacturer:Honda''')

elif data == 'car':
    car = input("Which company car are you looking for : ")
    if car == 'tata':
        print("""indica\n nano \n safari \n harrier \n nexon""")
        model = input("select any one car to see detail : ")
        if model == 'indica':
            print("Indica")












        


            
