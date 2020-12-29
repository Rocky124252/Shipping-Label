import sqlite3
import random
conn = sqlite3.connect('barcodes.db')
c = conn.cursor()


def init():
    try:
        c.execute("""CREATE TABLE Barcodes (
                    barcode text
                    )""")
    except sqlite3.OperationalError as e:
        pass

def contains(num):
    c.execute("SELECT * FROM Barcodes WHERE barcode=?", (num,))
    if len(c.fetchall()) == 0:
        return False
    else:
        return True

def insert(num):
    if(contains(num)):
        pass
    else:
        c.execute("INSERT INTO Barcodes VALUES (?)", (num,))

def clear():
    c.execute("DELETE FROM Barcodes")


def stop():
    conn.close()

def generateBarCode(length):
    return int(''.join([str(random.randint(0,10)) for _ in range(length)]))