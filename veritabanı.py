# CREATE TABLE
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():

    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()

def veri_ekle():

    cursor.execute("Insert into kitaplık Values ('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):

    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def verileri_al():

    cursor.execute("Select * from kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri")
    for i in liste:
        print(i)

def verileri_al2():

    cursor.execute("Select İsim,Yazar from kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri")
    for i in liste:
        print(i)

def verileri_al3(yayınevi):

    cursor.execute("Select * from kitaplık where Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri")
    for i in liste:
        print(i)

verileri_al3("Everest")
con.close()

#Verileri güncellemek için kod = {Update kitaplık set Yayınevi = 'Everest' where Yayınevi = 'Doğan Kitap'} ||Yayınevi Doğan Kitap olanları Everest olarak değiştirir.

#Verileri silmek için kod = {Delete from kitaplık where Yazar = 'Ahmet Ümit' || Yazar özelliği 'Ahmet Ümit' olan kitapları tablodan siler.
