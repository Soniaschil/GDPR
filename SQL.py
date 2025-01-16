# Estrazione dati casuali
import pandas as pd
import sqlite3

# Leggi il file Excel
file_name = "dati_utenti.xlsx"
df = pd.read_excel(file_name)

# Connessione al database SQLite
db_name = "dati_utenti.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Creazione della tabella SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS Utenti (
    Nome TEXT,
    Cognome TEXT,
    Email TEXT,
    Telefono TEXT
)
""")

# Inserisci i dati nella tabella SQL
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO Utenti (Nome, Cognome, Email, Telefono)
    VALUES (?, ?, ?, ?)
    """, (row['Nome'], row['Cognome'], row['Email'], row['Telefono']))

conn.commit()
print(f"Dati inseriti nel database: {db_name}")

# Chiudi la connessione
conn.close()