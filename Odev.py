import math

#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

#boy = float(input("Lutfen boyunuzu giriniz : "))
#kilo = int(input ("Lutfen kilonuzu giriniz :"))
#vki=kilo/(boy*boy)
#print("vücut kitle indeksiniz:",vki)

def vucutKitleIndeksi(b , w):
    vki = w/(b*b)
    return vki
def vkiDurumu(vki):
    if vki < 18.5:
        return "Ideal Kilonuzun Altindasiniz"
    elif 18.5 <= vki < 25:
        return "Normal"
    elif 25 <= vki < 30:
        return "Fazla Kilolu"
    else:
        return"Obez"           
boy = float(input("Lutfen boyunuzu giriniz : "))
kilo = float(input ("Lutfen kilonuzu giriniz :"))       
vki = vucutKitleIndeksi(boy , kilo)
print("Vucut Kitle Indeksi" , vki)
print("Durumunuz" , vkiDurumu(vki))

#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
#maas = 50000
#zamOrani = 10
#zamliMaas = maas + (maas * zamOrani / 100)
#print("Zamlı maaşınız:", zamliMaas)

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
#sayi1 = int(input ("Lutfen birinci sayiyi giriniz :"))
#sayi2 = int(input ("Lutfen ikinci sayiyi giriniz :"))
#sayi3 = int(input ("Lutfen ucuncu sayiyi giriniz :"))
#
#if(sayi1>sayi2 and sayi1>sayi3):
#    print("En buyuk sayi:",sayi1)
#elif(sayi2>sayi1 and sayi2>sayi3):
#    print("En buyuk sayi:",sayi2)
#elif(sayi3>sayi1 and sayi3>sayi2):
#    print("En buyuk sayi:",sayi3)
#else:
#    print("Ayni sayilari girdiniz , lutfen tekrar deneyiniz.")

#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
#yaricap = int(input("Dairenin yarıçapını girin: "))
#alan = math.pi * yaricap ** 2

#cevre = 2 * 3.14 * yaricap
#print("Dairenin alanı:", alan)
#print("Dairenin çevresi:", cevre)


#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
#sayi = int(input ("Lutfen bir sayi giriniz :"))
#def is_palindrome(number):
#    reverse_number = int(str(number)[::-1])
#    return number == reverse_number
#
#if is_palindrome(sayi):
#    print("Girdiginiz sayi palindromdur.")
#else:
#    print("Girdiginiz sayi palindrom degildir.")

