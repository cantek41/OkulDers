import sqlite3 as sql

vt=sql.connect("db.sqlite")

vt.execute("""CREATE TABLE kullanicilar(Ad,Soyad,Sifre)""")

vt.commit()
