#definition: Tanimlama

def ortalamaHesaplama():
    vize = 67
    final = 86
    ortalama = (vize * 0.4) + (final * 0.6)
    print(ortalama)

def ortalamaHesaplama2():
    vize = 67
    final = 86
    ortalama = (vize * 0.4) + (final * 0.6)
    return ortalama

ortalamaHesaplama()
print(ortalamaHesaplama2())

def ortalamaHesaplama3(vize:float , final:float):
    return = (vize * 0.4) + (final * 0.6)
exam1 = int(input("Lutfen vize notunuzu giriniz : "))
exam2 = int(input("Lutfen final notunuzu giriniz : "))
    print(ortalamaHesaplama3(exam1,exam2))
