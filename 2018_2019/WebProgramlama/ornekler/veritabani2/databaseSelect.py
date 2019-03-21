import sqlite3 as sql

k_adi=input("lütfen kullanıcı adını giriniz")

sifre=input("lütfen sifreyi giriniz")


vt=sql.connect("db.sqlite")


c=vt.cursor()

c.execute("select * from kullanicilar where Ad='"+k_adi+"' and Sifre='"+sifre+"'")

sonuc=c.fetchall()
print(sonuc)
