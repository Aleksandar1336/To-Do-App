import sqlite3

conn = sqlite3.connect("todoapp.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS todolist (
            name text NOT NULL
        );""")

conn.commit()

conn.close()


def show_all():
    conn = sqlite3.connect("todoapp.db")
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM todolist")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()

    conn.close()


def add_one(name):
    conn = sqlite3.connect("todoapp.db")
    c = conn.cursor()

    c.execute("INSERT INTO todolist VALUES (?)", ([name]))

    conn.commit()

    conn.close()
