try:
    wysokosc = int(input("Podaj liczbe: "))
    if wysokosc > 0:
        for y in range(wysokosc):
            for x in range(wysokosc - y - 1):
                print(" ", end="")
            for x in range(2 * y + 1):
               print("#", end="")
            print()

    else:
        print("Podana wartość nie pozwala na stworzenie piramidy")

except ValueError:
    print("Podana wartość nie pozwala na stworzenie piramidy")