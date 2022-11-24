import sqlite3
con = sqlite3.connect("../db.sqlite3")
cur = con.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

for table in cur:
    print(table)

con.commit()
con.close()