#Koşullu İfadeler (if-else)
#Soru: Kullanıcıdan bir sayı alarak, bu sayının çift mi tek mi olduğunu ekrana yazdıran bir Python programı yazın. Eğer sayı negatifse, ekrana "Negatif sayı girdiniz!" mesajı versin.


def sayiKontrol():
    sayi = int(input(f"bir sayı girin : "))

    if sayi < 0:
        print("girdiğiniz {sayi} sayısı negatif ;)")
    elif sayi % 2 ==0:
        print(f"{sayi} sayısı bir çift sayıdır :)")
    else:
        print(f"{sayi} sayısı bir tek sayıdır :( ")

sayiKontrol()
