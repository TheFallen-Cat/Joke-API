import sqlite3
import random

conn = sqlite3.connect("jokes.db", check_same_thread=False)

cursor = conn.cursor()


def random_joke():
    choice = random.randrange(1, 38269)
    joke = cursor.execute(f"""SELECT * FROM jokes WHERE id=={choice}""")

    elements = [j for j in joke]
    return elements


def with_id(id: int):
    joke = cursor.execute(f"""SELECT * FROM jokes WHERE id=={id}""")

    elements = [j for j in joke]
    return elements


conn.commit()
