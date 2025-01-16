# Generazione dati casuali
import random
import pandas as pd

# Funzione per generare dati casuali
def generate_random_data(num_users):
    first_names = ["Mario", "Luca", "Giulia", "Sara", "Alessandro"]
    last_names = ["Rossi", "Bianchi", "Verdi", "Ferrari", "Esposito"]
    domains = ["example.com", "email.com", "test.org"]

    data = []
    for _ in range(num_users):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"
        phone = f"+39 {random.randint(300, 399)}-{random.randint(1000000, 9999999)}"
        data.append({
            "Nome": first_name,
            "Cognome": last_name,
            "Email": email,
            "Telefono": phone
        })
    return data

# Genera i dati per 10 utenti
users_data = generate_random_data(10)

# Crea un file Excel
file_name = "dati_utenti.xlsx"
df = pd.DataFrame(users_data)
df.to_excel(file_name, index=False)
print(f"File Excel creato: {file_name}")