import sqlite3 as sql

veriTabani=sql.connect("database.sqlite")

cr=veriTabani.cursor()


cr.execute("""SELECT * from Ogrenciler Where Numara=9 """)



for eleman in cr.fetchall():
	print(eleman)

