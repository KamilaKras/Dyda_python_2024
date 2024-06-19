from typing import NamedTuple

class ChartData(NamedTuple):
  a: int
  b: int
  c: int

space = " "
gapBetweenSeq = "+-+"
markedTwoGaps = "--"
empty = "   "
betweenLines = "| |"


def draw_line(data: ChartData, line: int):
    # no need to subtract 1 since line starts at 0
    if line == 0:
        print(markedTwoGaps + (gapBetweenSeq + markedTwoGaps) * 3)
    else:
        line_buffer = space

        for bar in data:
            if line < bar:
                line_buffer += betweenLines
            elif line == bar:
                line_buffer += gapBetweenSeq
            else:
                line_buffer += empty

            line_buffer += space

        line_buffer += space
        print(line_buffer)


def draw_chart(data: ChartData):
    total_offset = max(data)

    print()
    print(f"a = {data.a}, b = {data.b}, (c = {data.c})")

    for line in range(total_offset + 1):
        draw_line(data, line)

def input_measurments():
    a = int(input("Enter the length of the first bar (a): "))
    b = int(input("Enter the length of the second bar (b): "))

    if a == b:
        print(f"Wysokości pierwszego i drugiego słupka nie mogą być takie same")
    elif b < 0 or b >= 9:
        print(f"Wysokość drugiego słupka powinna być większa lub równa 0 i niemniejsza od 9")
    elif a < 0 or a >= 9:
        print(f"Wysokość pierwszego słupka powinna być większa lub równa 0 i niemniejsza od 9")
    else:
        c = abs(a - b)
        return ChartData(a, b, c)

try:
    data = input_measurments()
    draw_chart(data)


except ValueError:
    print(f"Podane wartości nie spełniają warunków. Proszę upewnić "
          f"się, że podane wartości to liczby.")