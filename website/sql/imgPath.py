import sqlite3
con = sqlite3.connect("../db.sqlite3")
cur = con.cursor()

"""for row in cur.execute("PRAGMA table_info(math_app_ucebnice);"):
    print(row)"""

cur.execute("UPDATE math_app_ucebnice SET obrazek = '/static/img/book.png' WHERE id = 5;")

con.commit()
con.close()