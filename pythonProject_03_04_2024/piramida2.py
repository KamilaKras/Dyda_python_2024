try:
    wysokosc = int(input("Podaj wysokość piramidy: "))

    #Sprawdzam, czy wyskosc jest większa niż 0
    if wysokosc <= 0:
        print("Podana wartość nie pozwala na stworzenie piramidy. Podaj liczbę większą niż 0.")
    else:
        # Rosnąca połowa piramidy
        for i in range(1, wysokosc + 1):
            print('#' * i)
        # Malejąca połowa piramidy
        for i in range(wysokosc - 1, 0, -1):
            print('#' * i)

except ValueError:
    # podana inna wartość niż liczba całkowita
    print("Podana wartość nie jest liczbą całkowitą. Proszę podać poprawną liczbę całkowitą.")
