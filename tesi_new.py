# Generazione ed estrazione dati casuali

import random
import faker
import openpyxl
import sqlite3

# Funzione per generare i dati casuali che serviranno per essere inseriti su excel
def genera_dati():
    fake = faker.Faker()
    utenti = []

    # Genera 10 utenti casuali
    for _ in range(10):
        nome = fake.first_name()
        cognome = fake.last_name()
        email = fake.email()
        telefono = fake.phone_number()
        utenti.append((nome, cognome, email, telefono))

    return utenti

# Funzione per scrivere i dati in un file Excel
def scrivi_excel(utenti):
    # Crea un nuovo file Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Dati Utenti"

    # Aggiungi intestazioni al file Excel
    sheet.append(["Nome", "Cognome", "Email", "Numero di Telefono"])

    # Inserisci i dati degli utenti nel file Excel
    for utente in utenti:
        sheet.append(utente)

    # Salva il file Excel
    workbook.save("dati_utenti.xlsx")
    print("Dati salvati in dati_utenti.xlsx")

# Funzione per scrivere i dati in una tabella SQL
def scrivi_sql(utenti):
    # Connessione al database SQLite
    conn = sqlite3.connect('dati_utenti.db')
    cur = conn.cursor()

    # Crea la tabella SQL per memorizzare i dati
    cur.execute('''
    CREATE TABLE IF NOT EXISTS utenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cognome TEXT,
        email TEXT,
        telefono TEXT
    )
    ''')

    # Inserisci i dati nella tabella
    cur.executemany('''
    INSERT INTO utenti (nome, cognome, email, telefono)
    VALUES (?, ?, ?, ?)
    ''', utenti)

    # Salvataggio e chiusura della connessione
    conn.commit()
    conn.close()
    print("Dati salvati nel database dati_utenti.db")

# Funzione principale che esegue tutto il processo
def main():
    # Generazione dei dati casuali
    utenti = genera_dati()

    # Scrittura dei dati nel file Excel
    scrivi_excel(utenti)

    # Scrittura dei dati nella tabella SQL
    scrivi_sql(utenti)

# Esecuzione del processo
if __name__ == "__main__":
    main()