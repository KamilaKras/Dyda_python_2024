import csv
# Zadanie 1: Utworzenie klasy Przedmiot
class Przedmiot:
    def __init__(self, nazwa, kod_przedmiotu, prowadzacy, ects):
        self.nazwa = nazwa
        self.kod_przedmiotu = kod_przedmiotu
        self.prowadzacy = prowadzacy
        self.ects = ects

    def opis(self):
        return f"Przedmiot: {self.nazwa}, Kod: {self.kod_przedmiotu}, Prowadzący: {self.prowadzacy}, ECTS: {self.ects}"




# Zadanie 2: Kolekcja studentów
class Student:
    def __init__(self, imie, nazwisko, numer_indeksu, oceny=None):
        if oceny is None:
            oceny = []
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = oceny

    def opis(self):
        return f"Student: {self.imie} {self.nazwisko}, Numer indeksu: {self.numer_indeksu}"


class Grupa:
    def __init__(self):
        self.studenci = []

    def dodaj_studenta(self, student):
        self.studenci.append(student)

    def studenci_z_numerem_indeksu(self, numer_indeksu):
        return [student for student in self.studenci if student.numer_indeksu == numer_indeksu]

    # Zadanie 3: Średnia ocen studentów
    def srednia_ocen(self):
        wszystkie_oceny = [ocena for student in self.studenci for ocena in student.oceny]
        if wszystkie_oceny:
            return sum(wszystkie_oceny) / len(wszystkie_oceny)
        return 0

    # Zadanie 4: Eksport danych
    def eksportuj_dane_do_csv(self, nazwa_pliku):
        with open(nazwa_pliku, 'w', newline='') as csvfile:
            fieldnames = ['imie', 'nazwisko', 'numer_indeksu']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for student in self.studenci:
                writer.writerow(
                    {'imie': student.imie, 'nazwisko': student.nazwisko, 'numer_indeksu': student.numer_indeksu})

    # Zadanie 5: Studenci z określoną średnią
    def studenci_z_wyzsza_srednia(self, wartosc):
        return [student for student in self.studenci if sum(student.oceny) / len(student.oceny) > wartosc if
                student.oceny]


# Zadanie 6: Wyszukiwanie przedmiotów po prowadzącym
class PlanZajec:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def przedmioty_po_prowadzacym(self, prowadzacy):
        return [przedmiot for przedmiot in self.przedmioty if przedmiot.prowadzacy == prowadzacy]

    # Zadanie 7: ECTS dla przedmiotów studenta
    def suma_ects_studenta(self, kody_przedmiotow):
        return sum(przedmiot.ects for przedmiot in self.przedmioty if przedmiot.kod_przedmiotu in kody_przedmiotow)
