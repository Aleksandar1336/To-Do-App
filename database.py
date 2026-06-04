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

    print(f"{'ID':<5} {'Note'}")
    print("-" * 40)

    if not items:
        print("No notes found.")
        return

    for item in items:
        print(f"{item[0]:<5} {item[1]}")

    conn.commit()

    conn.close()


def add_one(name):
    conn = sqlite3.connect("todoapp.db")
    c = conn.cursor()

    c.execute("INSERT INTO todolist VALUES (?)", ([name]))

    conn.commit()

    conn.close()


def delete_one(id):
    conn = sqlite3.connect("todoapp.db")
    c = conn.cursor()

    c.execute("DELETE from todolist WHERE rowid = (?)", (id,))

    conn.commit()

    conn.close()


def delete_all():
    conn = sqlite3.connect("todoapp.db")
    c = conn.cursor()

    c.execute("DELETE FROM todolist")

    conn.commit()

    conn.close()
