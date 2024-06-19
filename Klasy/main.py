from klasy import *

# Przykładowe użycie:
# Tworzenie studentów
student1 = Student("Jan", "Kowalski", "123456", [5, 4, 3])
student2 = Student("Anna", "Nowak", "123457", [4, 4, 5])
student3 = Student("Piotr", "Zieliński", "123456", [3, 3, 3])


# Tworzenie grupy i dodawanie studentów
grupa = Grupa()
grupa.dodaj_studenta(student1)
grupa.dodaj_studenta(student2)
grupa.dodaj_studenta(student3)

# Średnia ocen w grupie
print("Średnia ocen w grupie:", grupa.srednia_ocen())

# Eksport danych do CSV
grupa.eksportuj_dane_do_csv('studenci.csv')

# Studenci z wyższą średnią niż 3.5
print("Studenci z wyższą średnią niż 3.5:", [student.opis() for student in grupa.studenci_z_wyzsza_srednia(3.5)])

# Tworzenie przedmiotów
przedmiot1 = Przedmiot("Matematyka", "MAT101", "Dr. Kowalski", 5)
przedmiot2 = Przedmiot("Fizyka", "PHY101", "Dr. Nowak", 6)
przedmiot3 = Przedmiot("Chemia", "CHE101", "Dr. Kowalski", 4)

# Tworzenie planu zajęć i dodawanie przedmiotów
plan_zajec = PlanZajec()
plan_zajec.dodaj_przedmiot(przedmiot1)
plan_zajec.dodaj_przedmiot(przedmiot2)
plan_zajec.dodaj_przedmiot(przedmiot3)

# Przedmioty prowadzone przez Dr. Kowalskiego
print("Przedmioty prowadzone przez Dr. Kowalskiego:",
      [przedmiot.opis() for przedmiot in plan_zajec.przedmioty_po_prowadzacym("Dr. Kowalski")])

# Suma ECTS dla przedmiotów studenta
kody_przedmiotow_studenta = ["MAT101", "CHE101"]
print("Suma ECTS dla studenta:", plan_zajec.suma_ects_studenta(kody_przedmiotow_studenta))
