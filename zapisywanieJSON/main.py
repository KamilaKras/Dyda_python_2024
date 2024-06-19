import json
import os

# Ścieżka do pliku z danymi klientów
FILE_PATH = os.path.join(os.path.dirname(__file__), 'clients.json')


# Funkcja do wczytywania danych klientów z pliku
def load_clients():
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Plik JSON jest pusty lub uszkodzony. Tworzenie nowego pliku.")
            return {}
    return {}


# Funkcja do zapisywania danych klientów do pliku
def save_clients(clients):
    with open(FILE_PATH, 'w') as file:
        json.dump(clients, file, indent=4)


# Funkcja do dodawania nowego klienta lub aktualizacji istniejącego
def add_or_update_client(clients):
    client_id = input("Podaj ID klienta: ")
    name = input("Podaj imię klienta: ")
    surname = input("Podaj nazwisko klienta: ")
    email = input("Podaj email klienta: ")
    phone = input("Podaj telefon klienta: ")

    clients[client_id] = {
        'name': name,
        'surname': surname,
        'email': email,
        'phone': phone
    }
    print(f"Klient {name} {surname} został dodany/zaktualizowany.")


# Główna funkcja programu
def main():
    clients = load_clients()
    while True:
        print("\n1. Dodaj/Zaktualizuj klienta")
        print("2. Wyświetl wszystkich klientów")
        print("3. Zakończ program")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            add_or_update_client(clients)
        elif choice == '2':
            for client_id, client_data in clients.items():
                print(
                    f"ID: {client_id}, Imię: {client_data['name']}, Nazwisko: {client_data['surname']}, Email: {client_data['email']}, Telefon: {client_data['phone']}")
        elif choice == '3':
            save_clients(clients)
            print("Dane zostały zapisane. Kończę program.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == '__main__':
    main()
