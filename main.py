print('Merhaba Tobeto Test Ekibi')#Anasayfa
print('Merhaba Tobeto Test Ekibi')#Profil
print('Merhaba Tobeto Test Ekibi')#About
print('Merhaba Tobeto Test Ekibi')#Contact

#degiskenler
#String => metinsel ifade
text = 'Merhaba Tobeto Test Uyesi'
print(text)
#print(type(text))

#int , integer => tamsayı
studentCount = 45
studentCount2 = '45'
print(studentCount + 5)

isVerified = True
print(isVerified)

number = 20
print(number + 20)
print(number - 5)
print(number * 5)
print(number / 5)
print(number % 3)

print(number == 20)#True
print(number == 25)#False

print(number != 20)#False
print(number != 25)#True

print(number > 20)#False
print(number >= 20)#True

print(number < 20)#False
print(number <= 20)#True

#String interpolation => metin birlestirme
hello = 'Merhaba'
userName = 'Fatih'
totalText = hello + ' ' + userName
print(totalText)

totalText = "{message} Sayin {name}".format(message = "Selamlar" , name = userName)
print(totalText)

totalText = f"Hosgeldiniz {userName}"
print(totalText)










