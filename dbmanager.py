import sqlite3
import random

conn = sqlite3.connect("jokes.db", check_same_thread=False)

cursor = conn.cursor()


data = cursor.execute("SELECT * FROM jokes")


def random_joke():
    choice = random.randrange(1, 100)
    joke = cursor.execute(f"""SELECT * FROM jokes WHERE id=={choice}""")

    elements = [j for j in joke]
    return elements


conn.commit()
