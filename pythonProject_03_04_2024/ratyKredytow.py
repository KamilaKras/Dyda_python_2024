def sprawdzanie_danych(kwota, lata, procent, typ_raty):
    if kwota <= 0:
        return False, "Kwota kredytu musi być większa od 0. Proszę spróbować ponownie"
    if lata <= 0:
        return False, "Liczba lat musi być większa od 0. Proszę spróbować ponownie"
    if procent <= 0:
        return False, "Procent w skali roku musi być większy od 0. Proszę spróbować ponownie"
    if typ_raty not in ["malejące", "stałe"]:
        return False, "Nieprawidłowy typ raty. Wybierz 'malejące' lub 'stałe'. Proszę spróbować ponownie"
    return True, ""


def oblicz_rate_malejaca(kwota, lata, procent):
    miesiace = lata * 12
    czesc_kapitalowa = kwota / miesiace
    pozostala_kwota = kwota
    # będę uzupełniać pętlą
    raty = []

    for miesiac in range(1, miesiace + 1):
        czesc_odsetkowa = pozostala_kwota * (procent / 100) / 12
        rata = czesc_kapitalowa + czesc_odsetkowa
        pozostala_kwota -= czesc_kapitalowa

        raty.append((miesiac, czesc_kapitalowa, czesc_odsetkowa, rata, pozostala_kwota))

    odsetki_calkowite = sum(r[2] for r in raty)
    return odsetki_calkowite, raty


def oblicz_rate_stala(kwota, lata, procent):
    miesiace = lata * 12
    miesieczna_stopa_procentowa = procent / 100 / 12
    rata_stala = kwota * (miesieczna_stopa_procentowa / (1 - (1 + miesieczna_stopa_procentowa) ** (-miesiace)))
    pozostala_kwota = kwota
    # będę uzupełniać pętlą
    raty = []

    for miesiac in range(1, miesiace + 1):
        czesc_odsetkowa = pozostala_kwota * miesieczna_stopa_procentowa
        czesc_kapitalowa = rata_stala - czesc_odsetkowa
        pozostala_kwota -= czesc_kapitalowa

        raty.append((miesiac, czesc_kapitalowa, czesc_odsetkowa, rata_stala, pozostala_kwota))

    odsetki_calkowite = sum(r[2] for r in raty)
    return odsetki_calkowite, raty


def main():
    print("Kalkulator kredytowy")
    kwota = float(input("Podaj kwotę kredytu: "))
    lata = int(input("Podaj liczbę lat: "))
    procent = float(input("Podaj procent w skali roku: "))
    typ_raty = input("Podaj typ raty (malejące/stałe): ")

    is_valid, error_message = sprawdzanie_danych(kwota, lata, procent, typ_raty)
    if not is_valid:
        print(f"Błąd: {error_message}")
        return

    if typ_raty == "malejące":
        odsetki_calkowite, raty = oblicz_rate_malejaca(kwota, lata, procent)
    else:
        odsetki_calkowite, raty = oblicz_rate_stala(kwota, lata, procent)

    print(f"\nCałkowity koszt kredytu (suma odsetek): {odsetki_calkowite:.2f}")
    print("Numer raty | Część kapitałowa | Część odsetkowa | Wysokość raty | Kapitał pozostały")
    for rata in raty:
        print(f"{rata[0]} | {rata[1]:.2f} | {rata[2]:.2f} | {rata[3]:.2f} | {rata[4]:.2f}")

try:
    main()

except ValueError:
    print("Wprowadzone są niepoprawne. Proszę spróbować ponownie")
