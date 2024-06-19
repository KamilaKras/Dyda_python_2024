import pylab

def draw_plot():
    #Pytania do użytkownika
    a = float(input(f"Proszę podać współczynnik a: "))
    b = float(input(f"Proszę podać współczynnik b: "))
    x_poczatek = int(input(f"Proszę podać początek zakresu dla osi x: "))
    x_koniec = int(input(f"Proszę podać koniec zakresu dla osi x: "))
    y_poczatek = int(input(f"Proszę podać początek zakresu dla osi y: "))
    y_koniec = int(input(f"Proszę podać koniec zakresu dla osi y: "))
    tytul = input(f"Proszę podać tytuł swojego wykresu: ")
    siatka = input(f"Proszę określić czy na wykresie ma być widoczna siatka? (Odpowiedź tak lub nie)").lower()

    #Zakres dla x
    x=range(x_poczatek, x_koniec+1)
    #Równanie funkcji
    y = [a * xi + b for xi in x]

    pylab.plot(x,y)
    pylab.title(tytul)

    #siata na tak czy na nie
    if siatka == "tak":
        pylab.grid(True)
    else:
        pylab.grid(False)
    pylab.ylim(y_poczatek, y_koniec)
    pylab.show()

try:
    draw_plot()
except ValueError:
    "Coś poszło nie tak, prosimy o sprawdzenie poprawności podanych wartości"