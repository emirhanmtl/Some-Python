print("- - - Hesap Makinesi - - -")

print("Yapmak istediğiniz işlemi seçiniz :")
print("1 : Toplama")
print("2 : Çıkarma")
print("3 : Çarpma")
print("4 : Bölme")

islem = input("İşlemi giriniz :")
a = int(input("Birinci sayıyı giriniz :"))
b = int(input("İkinci sayıyı giriniz :"))

if islem == "1":
    print("Girdiğiniz sayıların toplamı = ", a + b)

elif islem == "2":
    print("Girdiğiniz sayıların farkı = ", a - b)

elif islem == "3":
    print("Girdiğiniz sayıların çarpımı = ", a * b)

elif islem == "4":
    print("Girdiğiniz sayıların bölümü = ", a / b)

else:
    print("Hatalı işlem girdiniz!")
