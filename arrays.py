sayilar = [100 , 200 , 300 , "Merhaba" , True]

print(sayilar)
print(sayilar[0])
print(sayilar[1])

sayilar.append(200)#sona ekler
print(sayilar)
sayilar.remove(200)#degere gore siler
print(sayilar)
sayilar.pop(2)#indexe gore siler
print(sayilar)
sayilar.insert(0,100)
print(sayilar)
sayilar.extend([100,200,300])#listeye ekler
print(sayilar)
sayilar.clear()#listeyi temizler
print(sayilar)