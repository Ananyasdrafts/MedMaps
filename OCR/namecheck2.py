import sqlite3
import editdistance

def check_drug_name(name: str):
    conn = sqlite3.connect('drug_names.db')
    c = conn.cursor()

    min_distance = len(name) // 2 + 1
    min_name = None

    for row in c.execute('''SELECT name FROM drug_names'''):
        drug_name = row[0]
        distance = editdistance.eval(name, drug_name)
        if distance <= min_distance:
            min_distance = distance
            min_name = drug_name

    if min_name is None:
        return name
    else:
        return min_name