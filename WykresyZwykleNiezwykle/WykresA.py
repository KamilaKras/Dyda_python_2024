wysokosc_pierwsza = input("Podaj wysokość pierwszego słupka: ")
wysokosc_trzecia = input("Podaj wysokość trzeciego słupka: ")

def liczWysokoscB(wysokoscA, wysokoscC):
    wysokoscB = int(round((wysokoscA+wysokoscC)/2, 0))
    return wysokoscB
def rysujWykres(wysokoscA, wysokoscB, wysokoscC):
    # Function to draw a horizontal line of the given width
    def horizontal_line(width):
        return '+' + '-' * width + '+'

    # Function to draw a vertical line
    def vertical_line(width):
        # The vertical line should be in the center of the "step"
        padding = ' ' * ((max_width - 2) // 2)
        return padding + '|' + padding

    # The maximum width of the diagram is determined by the top bar
    max_width = wysokoscA + 2

    # Start with the top horizontal line
    diagram_lines = [horizontal_line(wysokoscA).center(max_width)]

    # Calculate the widths of the middle and bottom horizontal lines
    step_decrease = (wysokoscA - wysokoscC) // 2
    middle_width = wysokoscA - step_decrease
    bottom_width = middle_width - step_decrease

    # Draw the diagram with vertical lines in between the horizontal lines
    diagram_lines.append(vertical_line(max_width))
    diagram_lines.append(horizontal_line(middle_width).center(max_width))
    diagram_lines.append(vertical_line(max_width))
    diagram_lines.append(horizontal_line(bottom_width).center(max_width))

    # Return the joined diagram lines
    return '\n'.join(diagram_lines)


try:
    int_wysokosc_pierwsza = int(wysokosc_pierwsza)
    int_wysokosc_trzecia = int(wysokosc_trzecia)

    int_wysokosc_druga = liczWysokoscB(int_wysokosc_pierwsza, int_wysokosc_trzecia)

    if int_wysokosc_trzecia == int_wysokosc_pierwsza:
        print(f"Wysokość pierwszego i trzeciego słupka nie mogą być takie same")
    elif int_wysokosc_trzecia <= 0 or int_wysokosc_trzecia >= 20:
        print(f"Wysokość pierwszego i trzeciego słupka nie mogą być takie same")
    elif int_wysokosc_pierwsza <= 0 or int_wysokosc_pierwsza >= 20:
        print(f"Wysokość każdego słupka musi być większa od 0 i mniejsza od 20")

    else:
        print(f"Wysokości słupków: a = {int_wysokosc_pierwsza}, b = {int_wysokosc_druga}, c = {wysokosc_trzecia}")
        print("Wykres: ")
        print(rysujWykres(int_wysokosc_pierwsza, int_wysokosc_druga, int_wysokosc_trzecia))


except ValueError:
    print("Podane wartości nie spełniają warunków. Proszę upewnić się, że podane wartości to liczby.")
