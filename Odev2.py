#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
fibonacciSeri = [1, 1]  # İlk iki elemanı 1'e eşit olan Fibonacci serisi

while len(fibonacciSeri) < 20:  # En az 20 elemanlı bir Fibonacci serisi oluşturmak için döngü
    yeni_eleman = fibonacciSeri[-1] + fibonacciSeri[-2]  # Fibonacci serisindeki son iki elemanın toplamı
    fibonacciSeri.append(yeni_eleman)  # Yeni Fibonacci sayısını listeye ekle

print("En az 20 elemanli Fibonacci serisi: " , fibonacciSeri)  

def soru1():
    fibonacci_serisi = [1, 1]  # İlk iki elemanı 1'e eşit olan Fibonacci serisi
    while len(fibonacci_serisi) < 20:
        yeni_eleman = fibonacci_serisi[-1] + fibonacci_serisi[-2]  # Son iki elemanın toplamı
        fibonacci_serisi.append(yeni_eleman)  # Yeni elemanı serinin sonuna ekle
    print(fibonacci_serisi)
soru1()

#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
def odev2():
    sayi = int(input("Lutfen bir sayi giriniz: "))
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    if toplam == sayi:
        print(sayi, "mukemmel sayidir.")
    else:
        print(sayi, "mukemmel sayi degildir.")
odev2()

##3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
def odev3():
    sayi1 = int(input("Lutfen bir sayi giriniz: "))
    sayi2 = int(input("Lutfen bir sayi daha giriniz: "))
    ebob = 1
    ekok = 1
    for i in range(1, min(sayi1, sayi2) + 1):
        if sayi1 % i == 0 and sayi2 % i == 0:
            ebob = i  # EBOB değeri güncellenir
    ekok = (sayi1 * sayi2) //ebob
    print("Ebob:", ebob)
    print("Ekok:", ekok)
odev3()    

#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
def odev4():
    sayi = int(input("Lutfen bir sayi giriniz: "))
    asal = True
    for i in range(2, sayi):
        if sayi % i == 0:
            asal = False
            break
    if asal:
        print(sayi, "asal sayidir.")
    else:
        print(sayi, "asal sayi degildir.")
odev4()

#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız.
def cevap5():
    def asal_carpanlar(sayi):
        asal_carpanlar_listesi = []
        carpan = 2

        while sayi > 1:
            if sayi % carpan == 0:
                if carpan not in asal_carpanlar_listesi:
                    asal_carpanlar_listesi.append(carpan)
                sayi //= carpan
            else:
                carpan += 1
        return asal_carpanlar_listesi

    # Kullanıcıdan bir sayı al
    sayi = int(input("Bir sayı girin: "))

    # Asal çarpanları bul
    asal_carpanlar_listesi = asal_carpanlar(sayi)

    # Asal çarpanları yazdır
    print(f"{sayi} sayısının asal çarpanları:", asal_carpanlar_listesi)

#Fonksiyonu çağıralım
cevap5()