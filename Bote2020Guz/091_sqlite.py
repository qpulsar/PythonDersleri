import sqlite3

print(sqlite3.version)

baglanti = sqlite3.connect("veritabani.db")
if baglanti:
    print("bağlantı başarılı")
else:
    print("Bağlantı kurulamadı")

vt = baglanti.cursor()
vt.execute("""
create table if not exists covid(
id integer primary key autoincrement, 
isim text, 
yas int)
""")

vt.execute("insert into covid (isim, yas) values('Süheyla',17)")
baglanti.commit()

kayitlar = vt.execute("select * from covid")
print(kayitlar.fetchall())

baglanti.commit()

baglanti.close()
