import sqlite3

print(sqlite3.version)

baglanti = sqlite3.connect("veritabani.db")
if baglanti:
    print("Bağlantı başarılı")
else:
    print("Bağlantı başarısız")

db = baglanti.cursor()
db.execute("""
create table if not exists bilgi(
id integer primary key autoincrement,
isim text,
kilo int)
""")

db.execute("""
insert into bilgi (isim, kilo) values ('Ayşe',55)
""")
baglanti.commit()

oku = db.execute("select * from bilgi")
print(oku.fetchall())
baglanti.close()
