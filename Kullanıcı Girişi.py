print("""
************************
Kullanıcı Giriş Programı
************************
""")

sys_kullanıcı_adı = "Emirhan"

sys_parola = "123456"

giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı adı: ")
    parola = input("Parola: ")
    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı adı hatalı.")
        giriş_hakkı -= 1
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola hatalı.")
        giriş_hakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı adı ve Parola hatalı.")
        giriş_hakkı -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı...")
        break
    if (giriş_hakkı == 0):
        print("Giriş hakkınız bitti...")
        break