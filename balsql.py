import sqlite3

# Připojení k databázi (nebo vytvoření nové databáze, pokud ještě neexistuje)
conn = sqlite3.connect("moje_databaze.db")

# Vytvoření kurzoru pro provádění SQL příkazů
cursor = conn.cursor()

# Vytvoření tabulky
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")

# Vložení dat do tabulky
cursor.execute("""
INSERT INTO users (id, name, email)
VALUES
    (1, 'Jan Novák', 'jan.novak@seznam.cz'),
    (2, 'Petr Novák', 'petr.novak@seznam.cz'),
    (3, 'Marie Svobodová', 'marie.svobodova@seznam.cz')
""")

# Potvrzení změn v databázi
conn.commit()

# Dotaz na data v tabulce
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Vypsání výsledků
for row in rows:
    print(row)

# Uzavření kurzoru a připojení k databázi
cursor.close()
conn.close()