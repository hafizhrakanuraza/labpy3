def perulangan():
    
    print(" ")
    
    max=0
    while True:
        a=int(input("masukan bilangan :"))
        if max < a:
            max = a
        if a==0:
            print(" ")
            print ("bilangan terbesar : ",max)
            print(" ")
            jawab = "ya"
            while jawab == "ya":
                jawab = input("apakah anda ingin mengulai program ini ? (ya/tidak) ")
                if jawab == "ya" :
                    return perulangan()
                elif jawab == "tidak" :
                    break
                print(" ")
                
perulangan()
