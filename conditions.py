ortalamaNot = input("Lutfen ortalamanizi giriniz : ")
ortalamaNot = int(ortalamaNot)

if ortalamaNot > 80:
    print("Bravo")
elif ortalamaNot > 50:    
    print("Eh iste")
    if ortalamaNot < 40:
        print("Kotu")
    elif ortalamaNot > 40:
        print("Iyi")    
else:
    print("Terlik Geliyor")
