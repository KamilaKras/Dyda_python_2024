def create_chart(a, c):
    b = int(round((a + c) / 2, 0))
    top_bar = "+" + "-" * a + "+"

    mid_bar = "+" + "-" * b + "+"
    bot_bar = "+" + "-" * c + "+"
    vertical_bar = "|"
    space = " "

    max_width = max(a, b, c) + 2  # dodanie 2 dla "+"

    #elementy wykresu
    chart_lines = [
        space * (max_width - 1) + vertical_bar,
        space * (max_width - a - 2) + top_bar + space * (max_width - a - 2),
        space * (max_width - a - 2) + vertical_bar + space * a + vertical_bar,
        space * (max_width - a - 2) + top_bar + space * (max_width - a - 2),
        space * (max_width - 1) + vertical_bar,
        space * (max_width - b - 2) + mid_bar + space * (max_width - b - 2),
        space * (max_width - b - 2) + vertical_bar + space * b + vertical_bar,
        space * (max_width - b - 2) + mid_bar + space * (max_width - b - 2),
        space * (max_width - 1) + vertical_bar,
        space * (max_width - c - 2) + bot_bar + space * (max_width - c - 2),
        space * (max_width - c - 2) + vertical_bar + space * c + vertical_bar,
        space * (max_width - c - 2) + bot_bar + space * (max_width - c - 2),
        space * (max_width - 1) + vertical_bar
    ]

    return "\n".join(chart_lines)

try:
    a = int(input("Enter the length of the top bar (a): "))
    c = int(input("Enter the length of the bottom bar (c): "))

    if a == c:
        print(f"Wysokości pierwszego i trzeciego słupka nie mogą być takie same")
    elif c <= 0 or c >= 20:
        print(f"Wysokość trzeciego słupka powinna być większa od 0 i niemniejsza od 20")
    elif a <= 0 or a >= 20:
        print(f"Wysokość pierwszego słupka powinna być większa od 0 i niemniejsza od 20")
    else:
        chart_output = create_chart(a, c)
        print(chart_output)

except ValueError:
    print(f"Podane wartości nie spełniają warunków. Proszę upewnić "
          f"się, że podane wartości to liczby.")