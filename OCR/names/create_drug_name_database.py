import sqlite3
import csv

def create_drug_name_database():
    conn = sqlite3.connect('names.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS drug_names(name TEXT)''')

    with open('drug_names.csv', 'r') as f:
        data = list(csv.reader(f))
        for row in data:
            c.execute('''INSERT INTO drug_names VALUES(?)''', (row[0],))

    conn.commit()
    conn.close()

create_drug_name_database()