import sqlite3 as sql

veriTabani=sql.connect("database.sqlite")

cr=veriTabani.cursor()


cr.execute("""INSERT Into Ogrenciler values("Bero","Zero",01,9)""")


veriTabani.commit()


