def perulangan():
    print("")
    import random
    a = 0
    jumlah = int(input("masukan jumlah N:"))

    print("")
                 
    for x in range(0,jumlah):
        i = random.uniform(0.0,0.5)
        a += 1
        print("data ke-",a,"=>",i)

    jawab = "ya"
    hitung = 0
    while jawab == "ya":
        hitung == 1
        jawab = input("apakah anda ingin mengulai program ini dari awal ? (ya/tidak) jawab:")
        if jawab == "ya":
            return perulangan()
        elif jawab =="tidak":
            break
    print("total perulangan: ",hitung)
perulangan()
