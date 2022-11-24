import sqlite3
con = sqlite3.connect("../db.sqlite3")
cur = con.cursor()

cur.execute("SELECT * FROM math_app_reseni;")

for row in cur:
    print(row)

con.commit()
con.close()