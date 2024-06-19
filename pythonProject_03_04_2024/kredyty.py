kwota = input("Podaj kwotę kredytu: ")
lata = input("Podaj liczbę lat dla kredytu: ")
procent = input("Podaj procent w skali roku dla kredytu: ")
typ = input("Podaj typ raty kredytu (malejące lub stałe): ")

try:
    int_kwota = int(kwota)
    int_miesiace = int(lata)*12
    int_procent = int(procent)/100

    print(f"Wprowadzone przez Ciebie informacje o kredycie: kredyt na kwotę {int_kwota} złotych na {int_lata} lat. "
      f"Kredyt ma raty {typ} a jego oprocentowanie wynosi {procent}%")

    #obliczanie kredytu ze stalyimi stopami
    if typ == "stale":
        q=1+int_procent/12
        rata: float = int_kwota*(q**int_miesiace)*((q-1)/q**int_miesiace -1)
        return rata
    elif typ == "malejace":
        #liczenie
        return typ

    #pokazanie wyników

#całkowitym koszcie kredytu (sumie odsetek ze wszystkich rat),
# a następnie wyświetlić Informacje o poszczególnych ratach zawierające następujące dane:
#numer kolejny raty
#część kapitałowa raty
#część odsetkowa raty
#wysokość raty
#kapitał pozostały do spłaty po opłaceniu raty.

except ValueError:
    print("Dla wprowadzonych wartości niemożliwe jest wygenerowanie listy rat. Proszę podać poprawne dane")
    #(informując, która z wprowadzonych wartości jest problematyczna)


