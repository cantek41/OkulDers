import sqlite3 as sql

veriTabani=sql.connect("database.sqlite")

cr=veriTabani.cursor()


cr.execute("""CREATE Table if not Exists Ogrenciler(ad,Soyad,Sinif,Numara) """)


cr.execute("""INSERT Into Ogrenciler values("Ali","Can",11,299)""")


veriTabani.commit()


cr.execute("""SELECT ad from Ogrenciler""")


veriler = cr.fetchall()

print(veriler)

