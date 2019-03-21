import sqlite3 as sql

vt=sql.connect("db.sqlite")

vt.execute("""INSERT Into kullanicilar values("Salih","Kaya","1234")""")
