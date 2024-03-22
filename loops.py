#solid prensipleri
#for
#start:i'nin baslangic degeri (default 0)
#stop:i'nin bitis degeri
#step:i'nin artis degeri (default 1)

#for i in range(10):
#    print(i)
#
##kullanicinin girdigi sayilar arasinda en buyugu bulan kod
#    biggestValue = 0
#for i in range(3):
#    sayi = int(input(f"{i}.sayi giriniz: "))
##    sayi = abs(sayi)#mutlak deger
#    if sayi > biggestValue:
#        biggestValue = sayi
#
#print(f"En buyuk sayi:, {biggestValue}")
#
#
#numbers = []
#for i in range(3):
#    numbers.append(int(input(f"{i+1}.sayi giriniz: ")))
#    print(numbers)
#    numbers.sort(reverse=True)#ters cevirme
#print(numbers)
#print(max(numbers))
#
#index = int(input("Sayilar arasinda en buyuk kacinci elemani istiyorsun ? :"))
#print(numbers[index-1])

students = ["Ahmet", "Hakan" , "Kabe" , "Ercan" , "Tuba"]
for i in range(len(students)):
    if i>2:
        break #ilgili dongunun o an da kirilmasini saglar
    print(f"{i+1}. ogrenci: {students[i]}line")

for student in students:
    if student == "Ercan":
        continue
    print(f"{student}")


#while
i = 0
while i < 10:
    print(i)
    i = +1



