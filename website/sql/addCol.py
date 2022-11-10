import sqlite3
con = sqlite3.connect("../db.sqlite3")
cur = con.cursor()

cur.execute("ALTER TABLE math_app_ucebnice ADD obrazek VARCHAR;")

con.commit()
con.close()