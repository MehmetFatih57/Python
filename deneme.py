def odev2():

  hak = 3

  while hak > 0:
    # Kullanıcıdan sayı girmesini isteyin.
    sayi = int(input("Lütfen bir sayı giriniz: "))

    # Sayı negatifse hak sayısını azaltın.
    if sayi < 0:
      hak -= 1

      # Hak sayısı 0'a eşitse bloke mesajını yazdırın.
      if hak == 0:
        print("Geçersiz bir sayı girdiginiz icin hakkiniz kalmamistir.")
        break
      else:
        print("Kalan hakkınız:", hak)
    else:
      # Kullanıcıdan gelen sayıyı kontrol edin.
      toplam = 0
      for i in range(1, sayi):
        if sayi % i == 0:
          toplam += i

      # Sayı mükemmel sayı ise "mükemmel sayıdır" mesajını yazdırın.
      if toplam == sayi:
        print(sayi, "mükemmel sayıdır.")
        break

      # Sayı mükemmel sayı değilse "mükemmel sayı değildir" mesajını yazdırın.
      else:
        print(sayi, "mükemmel sayı değildir.")
        break

  # Hakkı biten kullanıcıya tekrar denemek isteyip istemediğini sor.
  if hak == 0:
    devam = input("Tekrar denemek ister misiniz? (q): ")
    if devam == "q":
      odev2()

# Fonksiyonu çağır
odev2()